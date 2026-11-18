#!/usr/bin/env python3
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Release archive gate: extracts a tarball, runs its installer in a throwaway HOME and
# verifies every pack lands plus KDE activation, so a release can never ship an archive
# that cannot install or activate.
# Usage: tools/dev/check_release_archive.py [tarball]   (defaults to the newest dist/*.tar.xz)

import configparser
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "tools" / "icons"))

try:
    from icon_palette import cursors_meta, theme_name
except ImportError:
    sys.exit("cannot import tools/icons/icon_palette.py")

DIST_ROOT = REPO_ROOT / "dist"


def newest_archive() -> Path:
    # Fall back to the most recent tarball so the gate needs no arguments.
    archives = sorted(DIST_ROOT.glob("*.tar.xz"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not archives:
        sys.exit(f"no release archive in {DIST_ROOT}; run tools/icons/package.sh first")
    return archives[0]


def extract(archive: Path, target: Path) -> Path:
    # Unpack the archive and return its single top-level directory.
    with tarfile.open(archive) as tar:
        tar.extractall(target, filter="data")
    roots = [p for p in target.iterdir() if p.is_dir()]
    if len(roots) != 1:
        sys.exit(f"{archive.name}: expected one top-level directory, found {len(roots)}")
    return roots[0]


def expected_packs() -> list[str]:
    # Pack names the archive must carry, taken from the palette instead of hardcoded here.
    return [theme_name("dark"), theme_name("light"), cursors_meta()["tech_name"]]


def check_payload(root: Path, errors: list[str]) -> None:
    # The archive must expose the layout install.sh resolves paths against.
    required = ["install.sh", "README.md", "palette/icons.json", "LICENSES/GPL-3.0.txt",
                "LICENSES/CC-BY-SA-4.0.txt", "LICENSES/UPSTREAM-ATTRIBUTION.md"]
    for entry in required:
        if not (root / entry).exists():
            errors.append(f"payload missing {entry}")
    for pack in expected_packs():
        kind = "cursors" if pack == cursors_meta()["tech_name"] else "icons"
        path = root / "src" / kind / pack
        if not (path / "index.theme").is_file():
            errors.append(f"payload missing src/{kind}/{pack}/index.theme")


def run_installer(root: Path, workdir: Path, errors: list[str]) -> None:
    # Install into a scratch HOME so the gate never touches the real ~/.icons.
    home = workdir / "home"
    home.mkdir()
    env = dict(os.environ, HOME=str(home))
    result = subprocess.run(
        ["sh", str(root / "install.sh"), "--no-activate"],
        env=env, capture_output=True, text=True,
    )
    if result.returncode != 0:
        errors.append(f"install.sh exited {result.returncode}: {(result.stderr or result.stdout).strip()}")
        return
    icons = home / ".icons"
    for pack in expected_packs():
        if not (icons / pack / "index.theme").is_file():
            errors.append(f"installer did not lay down {pack}/index.theme")


def ini_key(path: Path, group: str, key: str) -> str | None:
    # Read one key from an ini-style file (KDE or GTK), tolerating missing files.
    if not path.is_file():
        return None
    parser = configparser.ConfigParser(interpolation=None, strict=False)
    parser.optionxform = str  # keep key case so Theme/ColorScheme match exactly
    try:
        parser.read(path, encoding="utf-8")
    except configparser.Error:
        return None
    return parser.get(group, key, fallback=None)


def run_activation(root: Path, scratch: Path, args: list[str], errors: list[str]) -> None:
    # Activate inside an isolated XDG environment so no session or real config is touched.
    scratch.mkdir(parents=True, exist_ok=True)
    (scratch / ".config").mkdir(parents=True, exist_ok=True)
    (scratch / "xdg").mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, HOME=str(scratch), XDG_CONFIG_HOME=str(scratch / ".config"),
               XDG_CONFIG_DIRS=str(scratch / "xdg"), DBUS_SESSION_BUS_ADDRESS="")
    result = subprocess.run(
        ["sh", str(root / "install.sh"), *args],
        env=env, capture_output=True, text=True,
    )
    if result.returncode != 0:
        errors.append(f"install.sh {' '.join(args)} exited {result.returncode}: {(result.stderr or result.stdout).strip()}")


def check_kde_activation(root: Path, workdir: Path, errors: list[str]) -> None:
    # Activation must reach KDE's config files when kwriteconfig6 is available.
    if shutil.which("kwriteconfig6") is None:
        print("SKIP  KDE activation (kwriteconfig6 not installed)")
        return
    dark, light = theme_name("dark"), theme_name("light")
    cursors = cursors_meta()["tech_name"]
    kde = workdir / "kde"

    # (a) explicit --dark writes both keys and rewrites the seeded GTK settings.ini.
    home_a = kde / "dark-explicit"
    seed_gtk(home_a)
    run_activation(root, home_a, ["--dark"], errors)
    if ini_key(home_a / ".config" / "kdeglobals", "Icons", "Theme") != dark:
        errors.append("kdeglobals [Icons] Theme not set to the dark pack")
    if ini_key(home_a / ".config" / "kcminputrc", "Mouse", "cursorTheme") != cursors:
        errors.append("kcminputrc [Mouse] cursorTheme not set to the cursor pack")
    for gtk in ("gtk-3.0", "gtk-4.0"):
        if ini_key(home_a / ".config" / gtk / "settings.ini", "Settings", "gtk-icon-theme-name") != dark:
            errors.append(f"{gtk}/settings.ini not rewritten to the dark pack")

    # (b) auto-detect: BreezeDark selects dark, no kdeglobals at all leans light.
    home_dark = kde / "auto-dark"
    seed_kde_scheme(home_dark, "BreezeDark")
    run_activation(root, home_dark, ["--icons-only"], errors)
    if ini_key(home_dark / ".config" / "kdeglobals", "Icons", "Theme") != dark:
        errors.append("BreezeDark colour scheme did not auto-select the dark icon pack")
    if (home_dark / ".config" / "kcminputrc").exists():
        errors.append("--icons-only unexpectedly wrote kcminputrc")
    home_light = kde / "auto-light"
    run_activation(root, home_light, ["--icons-only"], errors)
    if ini_key(home_light / ".config" / "kdeglobals", "Icons", "Theme") != light:
        errors.append("missing colour scheme did not fall back to the light icon pack")


def seed_gtk(home: Path) -> None:
    # Plant GTK settings.ini files so the installer's sync has something to rewrite.
    for gtk in ("gtk-3.0", "gtk-4.0"):
        ini = home / ".config" / gtk / "settings.ini"
        ini.parent.mkdir(parents=True, exist_ok=True)
        ini.write_text("[Settings]\ngtk-icon-theme-name=Adwaita\n", encoding="utf-8")


def seed_kde_scheme(home: Path, scheme: str) -> None:
    # Plant a kdeglobals colour scheme for the auto-detect path.
    ini = home / ".config" / "kdeglobals"
    ini.parent.mkdir(parents=True, exist_ok=True)
    ini.write_text(f"[General]\nColorScheme={scheme}\n", encoding="utf-8")


def main() -> int:
    # Check one archive end to end and report a compact verdict.
    archive = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else newest_archive()
    errors: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        root = extract(archive, workdir / "x")
        check_payload(root, errors)
        if not errors:
            run_installer(root, workdir, errors)
        if not errors:
            check_kde_activation(root, workdir, errors)
    for line in errors:
        print(f"FAIL  {line}")
    if errors:
        print(f"\n{len(errors)} release archive failure(s) in {archive.name}")
        return 1
    print(f"PASS  {archive.name} installs {', '.join(expected_packs())} into a clean HOME")
    return 0


if __name__ == "__main__":
    sys.exit(main())

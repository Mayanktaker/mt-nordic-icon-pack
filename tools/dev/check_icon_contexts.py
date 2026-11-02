#!/usr/bin/env python3
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Icon context gate: catches lookup-order shadowing and dangling aliases in each icon theme.
# Run after generate_icons.py; exits non-zero on errors.
# Usage: tools/dev/check_icon_contexts.py [--variant dark|light|all]

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "tools" / "icons"))

try:
    from icon_palette import PALETTES, REPO_ROOT as PALETTE_ROOT, theme_name
except ImportError:
    sys.exit("cannot import tools/icons/icon_palette.py")

ICONS_ROOT = PALETTE_ROOT / "src" / "icons"
COLOR_CONTEXTS = ("apps", "devices", "places", "mimetypes", "categories")
SYMBOLIC_ONLY_CONTEXTS = ("status", "actions", "ui")


def directory_order(theme_dir: Path) -> list[str]:
    # Parse the resolution order declared in index.theme.
    for line in (theme_dir / "index.theme").read_text().splitlines():
        if line.startswith("Directories="):
            return [d.strip() for d in line.split("=", 1)[1].split(",") if d.strip()]
    return []


def icon_names(directory: Path) -> set[str]:
    # Collect icon stems (svg/png, files and symlinks) in one directory.
    return {p.stem for p in directory.iterdir() if p.suffix in (".svg", ".png")}


def check_shadowing(theme_dir: Path, order: list[str]) -> list[str]:
    # A color-named icon (no -symbolic suffix) living in a symbolic scalable dir listed
    # before a color dir hides the color art for that name.
    problems = []
    per_dir = {}
    for ctx in COLOR_CONTEXTS + SYMBOLIC_ONLY_CONTEXTS:
        d = theme_dir / "scalable" / ctx
        per_dir[f"scalable/{ctx}"] = icon_names(d) if d.is_dir() else set()
    rank = {d: i for i, d in enumerate(order)}
    for sym_ctx in SYMBOLIC_ONLY_CONTEXTS:
        sym_dir = f"scalable/{sym_ctx}"
        for color_ctx in COLOR_CONTEXTS:
            color_dir = f"scalable/{color_ctx}"
            if sym_dir not in rank or color_dir not in rank or rank[sym_dir] > rank[color_dir]:
                continue
            shared = per_dir[sym_dir] & per_dir[color_dir]
            for name in sorted(shared):
                if name.endswith("-symbolic"):
                    continue  # symbolic names have no color art to shadow
                color_file = theme_dir / color_dir / f"{name}.svg"
                if color_file.is_file() and "currentColor" in color_file.read_text(errors="ignore"):
                    continue  # same symbolic glyph in both places, nothing hidden
                problems.append(f"shadowing: {name} resolves to {sym_dir} before {color_dir}")
    return problems


def check_aliases(theme_dir: Path) -> list[str]:
    # Every symlink must resolve to a real file inside the theme.
    problems = []
    for link in theme_dir.rglob("*"):
        if link.is_symlink() and not link.exists():
            problems.append(f"dangling alias: {link.relative_to(theme_dir)} -> {link.readlink()}")
    return problems


def check_variant(variant: str) -> tuple[int, int]:
    # Run both gates for one variant; returns (errors, warnings).
    theme_dir = ICONS_ROOT / theme_name(variant)
    if not theme_dir.is_dir():
        print(f"FAIL [{variant}] theme directory missing ({theme_dir}); run generate_icons.py --variant {variant}")
        return 1, 0
    errors = check_shadowing(theme_dir, directory_order(theme_dir))
    warnings = check_aliases(theme_dir)
    for line in errors:
        print(f"FAIL [{variant}] {line}")
    for line in warnings:
        print(f"WARN [{variant}] {line}")
    if not errors:
        print(f"PASS [{variant}] {theme_dir.name}: {len(warnings)} warning(s)")
    return len(errors), len(warnings)


def main() -> int:
    # Check every requested variant and report a compact summary.
    parser = argparse.ArgumentParser(description="Icon context gate for the icon suites.")
    parser.add_argument("--variant", choices=("dark", "light", "all"), default="all")
    args = parser.parse_args()
    variants = list(PALETTES) if args.variant == "all" else [args.variant]
    errors = warnings = 0
    for variant in variants:
        variant_errors, variant_warnings = check_variant(variant)
        errors += variant_errors
        warnings += variant_warnings
    if errors:
        print(f"\n{errors} error(s), {warnings} warning(s)")
        return 1
    print(f"\nIcon context gate passed ({warnings} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())

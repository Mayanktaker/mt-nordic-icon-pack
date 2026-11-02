#!/usr/bin/env python3
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Copies a curated set of icons from both generated suites into docs/gallery/.
# so a README or page can switch between Polar Night and Snow Storm artwork.
# Usage: tools/dev/build_icon_gallery.py

import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "tools" / "icons"))

try:
    from icon_palette import PALETTES, theme_name
except ImportError:
    sys.exit("cannot import tools/icons/icon_palette.py")

ICONS_ROOT = REPO_ROOT / "src" / "icons"
GALLERY_ROOT = REPO_ROOT / "docs" / "gallery"

# (context, icon name, gallery slug, caption) — a representative slice, not the full 4k set.
CURATED = (
    ("places", "folder", "folder", "Folder"),
    ("places", "folder-home", "folder-home", "Home"),
    ("places", "folder-documents", "folder-documents", "Documents"),
    ("places", "folder-download", "folder-download", "Downloads"),
    ("places", "user-trash", "user-trash", "Trash"),
    ("apps", "org.gnome.Nautilus", "nautilus", "Files"),
    ("apps", "utilities-terminal", "terminal", "Console"),
    ("apps", "preferences-system", "settings", "Settings"),
    ("devices", "drive-harddisk", "drive-harddisk", "Internal Drive"),
    ("mimetypes", "application-pdf", "application-pdf", "PDF Document"),
    ("apps", "firefox", "firefox", "Firefox"),
    ("apps", "code", "code", "VS Code"),
    ("apps", "blender", "blender", "Blender"),
    ("apps", "gimp", "gimp", "GIMP"),
    ("apps", "inkscape", "inkscape", "Inkscape"),
    ("apps", "krita", "krita", "Krita"),
    ("apps", "spotify", "spotify", "Spotify"),
    ("apps", "discord", "discord", "Discord"),
)


def copy_variant(variant: str) -> int:
    # Copy the curated slice out of one generated pack into its gallery folder.
    pack = ICONS_ROOT / theme_name(variant)
    if not pack.is_dir():
        print(f"missing {pack}; run tools/icons/generate_icons.py --variant {variant}", file=sys.stderr)
        return 0
    target = GALLERY_ROOT / variant
    target.mkdir(parents=True, exist_ok=True)
    written = 0
    for context, name, slug, _caption in CURATED:
        source = pack / "scalable" / context / f"{name}.svg"
        if not source.is_file():
            print(f"  ! missing {variant} icon {context}/{name}.svg", file=sys.stderr)
            continue
        shutil.copyfile(source, target / f"{slug}.svg")
        written += 1
    return written


def main() -> int:
    # Refresh both gallery variants and report what shipped.
    total = 0
    for variant in PALETTES:
        written = copy_variant(variant)
        print(f"{variant}: {written}/{len(CURATED)} icons -> {(GALLERY_ROOT / variant).relative_to(REPO_ROOT)}")
        total += written
    if total != len(CURATED) * len(PALETTES):
        print("gallery incomplete; check missing icons above", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

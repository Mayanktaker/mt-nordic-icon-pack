#!/usr/bin/env python3
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Renders contact sheets for an icon variant so light/dark artwork can be eyeballed.
# Usage: tools/icons/preview_sheet.py [--variant dark|light] [--out DIR]

import argparse
import sys
from pathlib import Path

import cairo
import gi

gi.require_version("Rsvg", "2.0")
from gi.repository import Rsvg

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

try:
    from icon_palette import meta, output_dir, set_variant, theme_name, variant as active_variant
except ImportError:
    from tools.icons.icon_palette import (
        meta,
        output_dir,
        set_variant,
        theme_name,
        variant as active_variant,
    )

# Sheet layout: 80px cells, icon drawn at 64px with 8px padding.
CELL = 88
ICON = 64
PAD = 12
COLUMNS = 12

# librsvg 2.60 deprecated render_cairo; a fixed 64-unit viewport keeps the sheet framing.
VIEWPORT = Rsvg.Rectangle()
VIEWPORT.x, VIEWPORT.y, VIEWPORT.width, VIEWPORT.height = 0, 0, 64, 64

# Categories previewed per sheet plus the backdrop each variant is judged on.
SHEETS = ("places", "apps", "devices", "mimetypes", "status")


def sheet_background(variant: str) -> tuple[float, float, float]:
    # Preview backdrop mimics the desktop surface the suite is used on.
    return (0.98, 0.99, 1.0) if variant == "light" else (0.055, 0.078, 0.114)


def collect(theme_dir: Path, context: str) -> list[Path]:
    # SVGs of one context; symlinked glyphs count once and alias duplicates are skipped.
    folder = theme_dir / "scalable" / context
    if not folder.is_dir():
        return []
    seen = set()
    icons = []
    for path in sorted(folder.iterdir()):
        if path.suffix != ".svg":
            continue
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        icons.append(path)
    return icons


def draw_sheet(variant: str, theme_dir: Path, context: str, out_path: Path) -> int:
    # Render one context into a grid PNG; returns the number of icons drawn.
    icons = collect(theme_dir, context)
    if not icons:
        return 0
    rows = (len(icons) + COLUMNS - 1) // COLUMNS
    width, height = COLUMNS * CELL + PAD * 2, rows * CELL + PAD * 2
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(*sheet_background(variant))
    ctx.paint()

    for index, icon_path in enumerate(icons):
        col, row = index % COLUMNS, index // COLUMNS
        x = PAD + col * CELL + (CELL - ICON) / 2
        y = PAD + row * CELL + (CELL - ICON) / 2
        try:
            handle = Rsvg.Handle.new_from_data(icon_path.read_bytes())
        except Exception:
            continue
        ctx.save()
        ctx.translate(x, y)
        ctx.scale(ICON / 64.0, ICON / 64.0)
        handle.render_document(ctx, VIEWPORT)
        ctx.restore()

    out_path.parent.mkdir(parents=True, exist_ok=True)
    surface.write_to_png(str(out_path))
    return len(icons)


def main() -> int:
    # Build every preview sheet for the requested variant.
    parser = argparse.ArgumentParser(description="Render icon contact sheets for a variant.")
    parser.add_argument("--variant", choices=("dark", "light"), default=active_variant())
    parser.add_argument("--out", default=None, help="Output directory (default build/preview/<variant>)")
    args = parser.parse_args()

    set_variant(args.variant)
    theme_dir = output_dir()
    if not theme_dir.is_dir():
        print(f"No icon suite at {theme_dir}; run generate_icons.py --variant {args.variant}", file=sys.stderr)
        return 1

    out_dir = Path(args.out) if args.out else REPO_ROOT / "build" / "preview" / args.variant
    total = 0
    for context in SHEETS:
        target = out_dir / f"{context}.png"
        drawn = draw_sheet(args.variant, theme_dir, context, target)
        if drawn:
            print(f"{theme_name()} {context}: {drawn} icons -> {target}")
            total += drawn
    print(f"{meta()['name']}: {total} preview icons rendered")
    return 0


if __name__ == "__main__":
    sys.exit(main())

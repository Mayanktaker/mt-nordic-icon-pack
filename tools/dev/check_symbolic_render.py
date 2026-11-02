#!/usr/bin/env python3
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Symbolic artwork gate: a -symbolic glyph must follow the theme ink, never bake in black or white.
# Renders each unique glyph with an injected foreground colour and fails on fixed or blank output.
# Usage: tools/dev/check_symbolic_render.py

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

import cairo
import gi

gi.require_version("Rsvg", "2.0")
from gi.repository import Rsvg

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "tools" / "icons"))

try:
    from icon_palette import PALETTES, theme_name
except ImportError:
    sys.exit("cannot import tools/icons/icon_palette.py")

ICONS_ROOT = REPO_ROOT / "src" / "icons"

# The foreground GTK hands a symbolic glyph, and the colour it must come back as.
THEME_INK = "#ECEFF4"
INK_RGB = (236, 239, 244)
SAMPLE_SIZE = 48
MIN_ALPHA = 16
TOLERANCE = 24
# Extremes that mean the artwork ignored the injected ink and baked in its own colour.
DARK_CEILING = 70
LIGHT_FLOOR = 245
MAX_REPORTED = 20


def intrinsic_size(svg_text: str) -> tuple[float, float]:
    # Coordinate-system size, so a glyph is fitted instead of clipped by its own canvas.
    viewbox = re.search(r'viewBox="([^"]+)"', svg_text)
    if viewbox:
        parts = [float(value) for value in viewbox.group(1).replace(",", " ").split()]
        if len(parts) == 4 and parts[2] > 0 and parts[3] > 0:
            return parts[2], parts[3]
    width = re.search(r'\bwidth="([\d.]+)"', svg_text)
    height = re.search(r'\bheight="([\d.]+)"', svg_text)
    return (float(width.group(1)) if width else 16.0, float(height.group(1)) if height else 16.0)


def ink_histogram(svg_text: str) -> Counter:
    # Pixel count per unpremultiplied colour when the glyph is told the ink is THEME_INK.
    # The root tag may span lines, so match the element instead of a single-line literal.
    text = re.sub(r"<svg\b", f'<svg color="{THEME_INK}"', svg_text, count=1, flags=re.IGNORECASE)
    width, height = intrinsic_size(text)
    handle = Rsvg.Handle.new_from_data(text.encode("utf-8"))
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, SAMPLE_SIZE, SAMPLE_SIZE)
    ctx = cairo.Context(surface)
    ctx.scale(SAMPLE_SIZE / width, SAMPLE_SIZE / height)
    # librsvg 2.60 deprecated render_cairo; the viewport is the glyph's own coordinate space.
    viewport = Rsvg.Rectangle()
    viewport.x, viewport.y, viewport.width, viewport.height = 0, 0, width, height
    handle.render_document(ctx, viewport)

    buffer = surface.get_data()
    stride = surface.get_stride()
    counts: Counter = Counter()
    for y in range(SAMPLE_SIZE):
        row = y * stride
        for x in range(SAMPLE_SIZE):
            b, g, r, a = buffer[row + x * 4 : row + x * 4 + 4]
            if a > MIN_ALPHA:
                # Cairo ARGB32 is premultiplied; recover the true colour before comparing.
                counts[(r * 255 // a, g * 255 // a, b * 255 // a)] += 1
    return counts


def classify(svg_text: str) -> str:
    # ok, blank, fixed-dark, fixed-light or accent, judged by the colour the glyph mostly paints.
    # A handful of stray antialiasing pixels must not fail a glyph that renders correctly.
    counts = ink_histogram(svg_text)
    if not counts:
        return "blank"
    main = counts.most_common(1)[0][0]
    if all(abs(main[i] - INK_RGB[i]) <= TOLERANCE for i in range(3)):
        return "ok"
    if max(main) < DARK_CEILING:
        return "fixed-dark"
    if min(main) > LIGHT_FLOOR:
        return "fixed-light"
    return "accent"


def main() -> int:
    # Check every unique symbolic glyph across both suites.
    failures = []
    accents = []
    seen = set()
    checked = 0
    for variant in PALETTES:
        theme_dir = ICONS_ROOT / theme_name(variant)
        if not theme_dir.is_dir():
            failures.append(f"theme directory missing: {theme_dir}")
            continue
        for svg in sorted(theme_dir.rglob("*-symbolic*.svg")):
            if svg.is_symlink():
                continue
            digest = hashlib.sha256(svg.read_bytes()).hexdigest()
            if digest in seen:
                continue
            seen.add(digest)
            checked += 1
            name = str(svg.relative_to(theme_dir))
            try:
                result = classify(svg.read_text(errors="ignore"))
            except Exception as exc:  # noqa: BLE001 - an unreadable glyph is a gate failure
                failures.append(f"render failed: {name} ({exc})")
                continue
            if result in ("fixed-dark", "fixed-light", "blank"):
                failures.append(f"{result}: {name}")
            elif result == "accent":
                accents.append(name)

    for line in failures[:MAX_REPORTED]:
        print(f"FAIL  {line}")
    if len(failures) > MAX_REPORTED:
        print(f"FAIL  ... and {len(failures) - MAX_REPORTED} more")
    if accents:
        print(f"note  {len(accents)} glyph(s) paint a deliberate colour, allowed: {accents[:3]}")
    if failures:
        print(f"\n{len(failures)} symbolic glyph(s) do not follow the theme ink")
        return 1
    print(f"PASS  {checked} unique symbolic glyphs follow the theme ink in both variants")
    return 0


if __name__ == "__main__":
    sys.exit(main())

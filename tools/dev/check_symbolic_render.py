#!/usr/bin/env python3
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Symbolic artwork gate: a -symbolic glyph must follow the theme ink, never bake in black or white.
# Mode A simulates KDE's KIconLoader (scheme classes drive the ink); Mode B simulates a plain
# third-party renderer (only the baked fallbacks). Also proves the sanitiser injection is idempotent.
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
    from icon_palette import PALETTES, palette, theme_name
    from generate_icons import sanitize_symbolic
except ImportError:
    sys.exit("cannot import tools/icons/icon_palette.py or tools/icons/generate_icons.py")

ICONS_ROOT = REPO_ROOT / "src" / "icons"

# Mode A drives the scheme classes with an ink far from both palette inks, so a pass proves the
# classes — not the baked fallbacks — chose the colour, the way KIconLoader recolours glyphs.
SCHEME_TEST_INK = "#FF00AA"
SCHEME_TEST_RGB = (255, 0, 170)
SAMPLE_SIZE = 48
MIN_ALPHA = 16
TOLERANCE = 24
# Extremes that mean the artwork ignored the expected ink and baked in its own colour.
DARK_CEILING = 70
LIGHT_FLOOR = 245
MAX_REPORTED = 20

# Paint declarations that carry no colour of their own and must not be flagged.
NEUTRAL_PAINTS = {"", "none", "currentcolor", "inherit", "transparent", "context-fill", "context-stroke"}

# `-inkscape-stroke`, `stop-color` and friends are metadata, not painted geometry.
PAINT_ATTRIBUTE = re.compile(r'(?<![-\w])(fill|stroke)\s*=\s*"([^"]*)"', re.IGNORECASE)
PAINT_DECLARATION = re.compile(r'(?<![-\w])(fill|stroke)\s*:\s*([^;"]+)', re.IGNORECASE)

# Glyphs that deliberately paint a colour instead of inheriting the theme ink, with the values
# they are allowed to keep. A colour picker showing a swatch is the only sanctioned case.
COLOUR_ALLOWLIST = {"color-pick": {"#50dbb5"}}

# One case per syntax upstream has shipped; fragments, since the KIconLoader pass adds scheme metadata.
SANITISER_CASES = (
    ('fill="black"', 'fill="currentColor"'),
    ('fill="white"', 'fill="currentColor"'),
    ('stroke="rgb(0,0,0)"', 'stroke="currentColor"'),
    ('stroke="url(&quot;#gpa:foreground&quot;) rgb(0,0,0)"', 'stroke="currentColor"'),
    ('fill="foreground"', 'fill="currentColor"'),
    ('fill="#D9D9D9"', 'fill="currentColor"'),
    ('style="fill:#ffffff;fill-opacity:1"', 'style="fill:currentColor;fill-opacity:1"'),
    ('color="#363636"', ""),
    ('fill="none"', 'fill="none"'),
    ('fill="currentColor"', 'fill="currentColor"'),
    ('fill="#88C0D0"', 'fill="#88C0D0"'),
)

# The sanitiser's injected scheme block, in any attribute order, for the Mode A strip.
SCHEME_BLOCK = re.compile(
    r"<style[^>]*\bid\s*=\s*[\"']current-color-scheme[\"'][^>]*>.*?</style\s*>",
    re.IGNORECASE | re.DOTALL,
)
# A colour declaration inside a style attribute; the lookbehind keeps out `border-color` and friends.
COLOR_DECLARATION = re.compile(r"(?<![-\w])color\s*:[^;\"]*", re.IGNORECASE)
# The root tag and an element tag with its attribute blob (quoted values may span lines).
ROOT_TAG = re.compile(r"<svg\b[^>]*>", re.IGNORECASE)
STYLE_ATTRIBUTE = re.compile(r'(\bstyle\s*=\s*")([^"]*)(")', re.IGNORECASE)
ELEMENT_TAG = re.compile(r"<([a-zA-Z][\w:-]*)((?:\"[^\"]*\"|'[^']*'|[^>\"'])*)>")
# A currentColor paint as an attribute value or a style declaration on the element itself.
CURRENT_COLOR_PAINT = re.compile(r'(?<![-\w])(fill|stroke)\s*[=:]\s*["\']?\s*currentColor\b', re.IGNORECASE)
CLASS_ATTRIBUTE = re.compile(r'\bclass\s*=\s*"([^"]*)"', re.IGNORECASE)
SCHEME_CLASS = re.compile(r"\bColorScheme-[A-Za-z-]+\b")


def hex_rgb(value: str) -> tuple[int, int, int]:
    # #RRGGBB text as the RGB triple the pixel buffer carries.
    return (int(value[1:3], 16), int(value[3:5], 16), int(value[5:7], 16))


def variant_ink(variant: str) -> str:
    # The variant's own ink, the same value the sanitiser baked into the emitted glyph.
    return palette(variant)["color"]["icon"]["ink"]


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


def render_histogram(svg_text: str) -> Counter:
    # Pixel count per unpremultiplied colour when the text is rendered exactly as given.
    width, height = intrinsic_size(svg_text)
    handle = Rsvg.Handle.new_from_data(svg_text.encode("utf-8"))
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


def unclassed_current_colors(svg_text: str) -> int:
    # Elements painted in currentColor whose class attribute lacks a ColorScheme-* entry.
    offenders = 0
    for match in ELEMENT_TAG.finditer(svg_text):
        attrs = match.group(2)
        if not CURRENT_COLOR_PAINT.search(attrs):
            continue
        class_attr = CLASS_ATTRIBUTE.search(attrs)
        if not class_attr or not SCHEME_CLASS.search(class_attr.group(1)):
            offenders += 1
    return offenders


def kicon_loader_sim(svg_text: str, test_ink: str) -> str:
    # Strip the sanitiser's baked fallbacks and drive the scheme classes with the test ink,
    # the stylesheet-only behaviour of KDE's KIconLoader.
    stripped = SCHEME_BLOCK.sub("", svg_text)

    def strip_root_style(match: "re.Match") -> str:
        # Remove only the fallback colour declaration, leaving any other root style intact.
        style = STYLE_ATTRIBUTE.search(match.group(0))
        if not style or not COLOR_DECLARATION.search(style.group(2)):
            return match.group(0)
        cleaned = COLOR_DECLARATION.sub("", style.group(2))
        return match.group(0).replace(style.group(0), f"{style.group(1)}{cleaned}{style.group(3)}", 1)

    stripped = ROOT_TAG.sub(strip_root_style, stripped, count=1)
    rules = "".join(f".{name} {{ color:{test_ink}; }}" for name in sorted(set(SCHEME_CLASS.findall(stripped))))
    return ROOT_TAG.sub(lambda match: f'{match.group(0)}<style type="text/css">{rules}</style>', stripped, count=1)


def judge(counts: Counter, expected_rgb: tuple[int, int, int]) -> str:
    # ok, blank, fixed-dark, fixed-light or accent, judged against the expected ink.
    # A handful of stray antialiasing pixels must not fail a glyph that renders correctly.
    if not counts:
        return "blank"
    main = counts.most_common(1)[0][0]
    if all(abs(main[i] - expected_rgb[i]) <= TOLERANCE for i in range(3)):
        return "ok"
    if max(main) < DARK_CEILING:
        return "fixed-dark"
    if min(main) > LIGHT_FLOOR:
        return "fixed-light"
    return "accent"


def fixed_paints(svg_text: str, stem: str) -> set[str]:
    # Every paint that hard-codes a colour instead of following the theme ink.
    allowed = COLOUR_ALLOWLIST.get(stem, set())
    found = set()
    for _name, value in PAINT_ATTRIBUTE.findall(svg_text) + PAINT_DECLARATION.findall(svg_text):
        paint = value.strip().lower()
        if paint in NEUTRAL_PAINTS or paint.startswith("url(") or paint in allowed:
            continue
        found.add(paint)
    return found


def symbolic_glyphs(theme_dir: Path) -> list[Path]:
    # Every symbolic glyph, following the dedupe symlinks so each real file is checked once.
    glyphs = []
    seen = set()
    for svg in sorted(theme_dir.rglob("*.svg")):
        if "-symbolic" not in svg.stem and "symbolic" not in svg.relative_to(theme_dir).parts[0]:
            continue
        target = svg.resolve()
        if target in seen:
            continue
        seen.add(target)
        glyphs.append(svg)
    return glyphs


def check_idempotency(sample: Path) -> str | None:
    # Re-sanitising an emitted glyph must keep exactly one scheme block and change nothing.
    text = sample.resolve().read_text(errors="ignore")
    once = sanitize_symbolic(text)
    occurrences = once.count("current-color-scheme")
    if occurrences != 1:
        return f"expected exactly one current-color-scheme occurrence, found {occurrences}"
    if sanitize_symbolic(once) != once:
        return "a second sanitiser pass changed the glyph"
    return None


def check_sanitiser(failures: list[str]) -> None:
    # Pin the sanitiser's syntax coverage and idempotency, which the render check cannot isolate.
    try:
        from generate_icons import sanitize_symbolic
    except ImportError as exc:
        failures.append(f"sanitiser: cannot import sanitize_symbolic ({exc})")
        return
    for source, expected in SANITISER_CASES:
        actual = sanitize_symbolic(source)
        if expected and expected not in actual:
            failures.append(f"sanitiser: {source!r} -> {actual!r}, expected {expected!r}")
        elif not expected and source in actual:
            failures.append(f"sanitiser: {source!r} survived as {actual!r}")
        elif sanitize_symbolic(actual) != actual:
            failures.append(f"sanitiser: {source!r} is not idempotent")


def main() -> int:
    # Check every unique symbolic glyph across both suites in both render modes.
    failures = []
    accents = []
    seen = set()
    checked = 0
    idempotency_error = None
    for variant in PALETTES:
        theme_dir = ICONS_ROOT / theme_name(variant)
        if not theme_dir.is_dir():
            failures.append(f"theme directory missing: {theme_dir}")
            continue
        ink_rgb = hex_rgb(variant_ink(variant))
        for svg in symbolic_glyphs(theme_dir):
            digest = hashlib.sha256(svg.read_bytes()).hexdigest()
            if digest in seen:
                continue
            seen.add(digest)
            checked += 1
            name = str(svg.relative_to(theme_dir))
            if idempotency_error is None:
                idempotency_error = check_idempotency(svg)
            text = svg.read_text(errors="ignore")
            offenders = unclassed_current_colors(text)
            if offenders:
                failures.append(f"unclassed currentColor x{offenders}: {name}")
            for mode, rendered, expected in (
                ("kicon", kicon_loader_sim(text, SCHEME_TEST_INK), SCHEME_TEST_RGB),
                ("baked", text, ink_rgb),
            ):
                try:
                    verdict = judge(render_histogram(rendered), expected)
                except Exception as exc:  # noqa: BLE001 - an unreadable glyph is a gate failure
                    failures.append(f"{mode} render failed: {name} ({exc})")
                    continue
                if verdict == "blank" or verdict.startswith("fixed-"):
                    failures.append(f"{mode}-{verdict}: {name}")
                elif verdict == "accent":
                    if svg.stem in COLOUR_ALLOWLIST:
                        accents.append(name)
                    else:
                        failures.append(f"accent: {name}")
            for paint in sorted(fixed_paints(text, svg.stem)):
                failures.append(f"fixed-paint {paint}: {name}")

    check_sanitiser(failures)
    if idempotency_error:
        failures.append(f"idempotency: {idempotency_error}")
    for line in failures[:MAX_REPORTED]:
        print(f"FAIL  {line}")
    if len(failures) > MAX_REPORTED:
        print(f"FAIL  ... and {len(failures) - MAX_REPORTED} more")
    if accents:
        print(f"note  {len(accents)} glyph(s) paint a deliberate colour, allowed: {sorted(set(accents))[:3]}")
    if failures:
        print(f"\n{len(failures)} symbolic glyph(s) are not KIconLoader-recolorable")
        return 1
    print(f"PASS  {checked} unique symbolic glyphs: classed, third-party-safe and idempotent in both variants")
    return 0


if __name__ == "__main__":
    sys.exit(main())

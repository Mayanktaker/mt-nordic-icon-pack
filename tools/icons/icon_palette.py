# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Variant-aware icon palette for the standalone icon pack.
# Single source of truth: palette/icons.json (dark and light variants + cursor colours).

import json
import os
import re
from functools import lru_cache
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PALETTE_FILE = REPO_ROOT / "palette" / "icons.json"

# Selects the variant for this process; set before importing artwork modules.
VARIANT_ENV = "MT_ICON_VARIANT"
DEFAULT_VARIANT = "dark"

# Variants available for generation, in build order.
PALETTES = ("dark", "light")

# Matches a 6-digit hex literal but never the prefix of a longer (8-digit) colour.
HEX_PATTERN = re.compile(r"#[0-9a-fA-F]{6}(?![0-9a-fA-F])")

# Literal artwork hexes (dark artwork) -> light equivalents, applied before token fill.
# Only hand-drawn artwork literals are listed; palette-resolved colours are untouched.
LIGHT_HEX_MAP = {
    "#040609": "#B8C4D4",  # deep shadow flood -> soft daylight shadow
    "#090d14": "#FFFFFF",  # darkest panel / ink-on-accent -> paper
    "#0a1018": "#FFFFFF",
    "#0e141d": "#E9EEF5",  # base panel -> light sunken surface
    "#141d28": "#E2E8F1",
    "#151d2a": "#F1F5FA",  # tile
    "#182332": "#EDF2F8",
    "#1a2434": "#EDF2F8",  # raised
    "#202d40": "#F5F8FC",
    "#223145": "#F7FAFD",
    "#243346": "#DFE6EF",
    "#25344a": "#B9C6D6",  # border
    "#2a3a52": "#CBD6E4",
    "#2b3c52": "#B9C6D6",
    "#2c3f57": "#B0BFD1",
    "#2e415a": "#FBFCFE",
    "#354a68": "#D5DEEA",
    "#3e5a3a": "#B7CBB4",
    "#405878": "#7E8FA6",  # crisp perimeter border
    "#435c7e": "#7E8FA6",
    "#486490": "#7E8FA6",
    "#5a7a54": "#8FA98B",
    "#eceff4": "#2E3440",  # snow ink -> polar ink
    "#d8dee9": "#4C566A",
    "#88c0d0": "#4C719C",  # frost accent
    "#a3d4e2": "#5E81AC",
    "#81a1c1": "#5E81AC",  # glacier accent
    "#00d2ff": "#0079A8",  # cyber accent, darkened for daylight legibility
    "#5e81ac": "#4C719C",
    "#8fbcbb": "#3E7C7A",  # aurora
    "#e5737f": "#BF616A",
    "#e5b580": "#B4803F",
    "#e5a855": "#B4791F",
    "#ebcb8b": "#B9892F",
    "#bf616a": "#BF616A",
    "#a3be8c": "#5B7A45",
    "#b48ead": "#8B5F86",
    "#d08770": "#B0664F",
}


def set_variant(value: str) -> str:
    # Validate and export the icon variant for this process.
    if value not in PALETTES:
        raise SystemExit(f"unknown icon variant '{value}'; expected one of {list(PALETTES)}")
    os.environ[VARIANT_ENV] = value
    return value


def variant() -> str:
    # Active icon variant, defaulting to the dark suite.
    return os.environ.get(VARIANT_ENV, DEFAULT_VARIANT)


@lru_cache(maxsize=None)
def palette_file() -> dict:
    # Whole palette/icons.json document (meta, variants, cursors).
    return json.loads(PALETTE_FILE.read_text())


def palette(variant_name: str | None = None) -> dict:
    # One variant section: tech_name, name, inherits and its colour tree.
    name = variant_name or variant()
    variants = palette_file()["variants"]
    if name not in variants:
        raise SystemExit(f"palette has no '{name}' variant")
    return variants[name]


def meta() -> dict:
    # Pack metadata (name, version, upstream theme link).
    return palette_file()["meta"]


def cursors_meta() -> dict:
    # Cursor pack name plus the colour tree it borrows from the dark variant.
    cursors = palette_file()["cursors"]
    return {**cursors, "color": palette("dark")["color"]}


def color_tree() -> dict:
    # Colour subtree of the active variant.
    return palette()["color"]


def icon_colors() -> dict:
    # The `color.icon` block of the active variant.
    colors = color_tree().get("icon")
    if not colors:
        raise SystemExit(f"palette for '{variant()}' has no color.icon block")
    return colors


def theme_name(variant_name: str | None = None) -> str:
    # Icon theme directory/name, e.g. MT-Nordic-Light-Icons.
    return palette(variant_name)["tech_name"]


def inherits() -> str:
    # Fallback chain for this variant.
    return palette()["inherits"]


def output_dir(variant_name: str | None = None) -> Path:
    # Generated icon suite location for this variant.
    return REPO_ROOT / "src" / "icons" / theme_name(variant_name)


@lru_cache(maxsize=None)
def svg_context(variant_name: str | None = None) -> dict:
    # Placeholder values substituted into the icon SVG templates for one variant.
    name = variant_name or variant()
    colors = palette(name)["color"]["icon"]
    accent = palette(name)["color"]["accent"]
    return {
        "COLOR_BG_BASE": colors["surface"],
        "COLOR_SURFACE": colors["surface_mid"],
        "COLOR_SURFACE_HOVER": colors["surface_strong"],
        "COLOR_BORDER": colors["border"],
        "COLOR_ACCENT": accent["base"],
        "COLOR_ACCENT_STRONG": accent["strong"],
        "COLOR_PAPER": colors["paper"],
        "COLOR_PAPER_BOTTOM": colors["paper_bottom"],
        "COLOR_PAPER_EDGE": colors["paper_edge"],
        "PAPER_EDGE_WIDTH": str(colors["paper_edge_width"]),
        "COLOR_PAPER_LINE": colors["paper_line"],
        "COLOR_FOLDER_BACK_TOP": colors["folder_back_top"],
        "COLOR_FOLDER_BACK_BOTTOM": colors["folder_back_bottom"],
        "COLOR_FOLDER_BACK_EDGE": colors["folder_back_edge"],
        "COLOR_FOLDER_FLAP_TOP": colors["folder_flap_top"],
        "COLOR_FOLDER_FLAP_MID": colors["folder_flap_mid"],
        "COLOR_FOLDER_FLAP_BOTTOM": colors["folder_flap_bottom"],
        "COLOR_FOLDER_FLAP_EDGE": colors["folder_flap_edge"],
        "COLOR_SPEC_1": colors["specular_1"],
        "COLOR_SPEC_2": colors["specular_2"],
        "COLOR_SPEC_3": colors["specular_3"],
        "COLOR_SHADOW": colors["shadow"],
        "SHADOW_ALPHA": str(colors["shadow_alpha"]),
        "COLOR_TILE_TOP": colors["tile_top"],
        "COLOR_TILE_BOTTOM": colors["tile_bottom"],
        "COLOR_TILE_BORDER": colors["tile_border"],
    }


def remap(text: str) -> str:
    # Recolour hand-drawn dark artwork literals for the light suite (identity for dark).
    if variant() == "dark":
        return text
    return HEX_PATTERN.sub(lambda match: LIGHT_HEX_MAP.get(match.group(0).lower(), match.group(0)), text)


def render(svg_raw: str) -> str:
    # Recolour artwork for the variant, then substitute palette placeholders.
    svg = remap(svg_raw)
    return svg.format(**svg_context()) if "{COLOR_" in svg else svg

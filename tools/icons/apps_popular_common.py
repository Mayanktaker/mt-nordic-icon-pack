# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Shared 64x64 Nordic tile builder for the popular-app icon batches.
# Colors come from the active icon variant palette (dark or light) via icon_palette.

try:
    from icon_palette import icon_colors, color_tree
except ImportError:
    from tools.icons.icon_palette import icon_colors, color_tree

_TOKENS = color_tree()
_ICON = icon_colors()

ACCENT = _TOKENS["accent_flavors"]["cyber"]        # Frost accent used by app tiles
ACCENT2 = _TOKENS["accent"]["base"]                # Glacier secondary
SNOW = _TOKENS["text"]["primary"]                  # Snow paper
GOLD = _TOKENS["status"]["warning"]
RED = _TOKENS["status"]["destructive"]
GREEN = _TOKENS["status"]["success"]
PURPLE = _TOKENS["status"]["petal_decorative"]
ORANGE = _TOKENS["accent_flavors"]["blaze"]
# Placeholders, not literals: these values collide with dark artwork hexes, so they must be
# resolved after the dark->light remap instead of being baked in at import time.
TILE_FILL = "{COLOR_TILE_FILL}"
BORDER = "{COLOR_BORDER_DEFAULT}"
BASE = _TOKENS["bg"]["base"]

# Tile surface is variant-owned so light tiles keep a visible edge on light windows.
TILE_TOP = _ICON["tile_top"]
TILE_BOTTOM = _ICON["tile_bottom"]
TILE_BORDER = _ICON["tile_border"]


def tile(key: str, body: str) -> str:
    # Wrap a glyph body in the standard Nordic rounded app tile.
    return f'''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="bg-{key}" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="{TILE_TOP}"/>
    <stop offset="100%" stop-color="{TILE_BOTTOM}"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#bg-{key})" stroke="{TILE_BORDER}" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="{ACCENT2}" fill-opacity="0.25"/>
{body}
</svg>'''

#!/usr/bin/env python3
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# WCAG contrast gate for the icon palettes: icon ink/tile/accent pairs per variant.
# Run before committing palette or artwork changes.

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PALETTE_FILE = REPO_ROOT / "palette" / "icons.json"


def srgb_to_linear(channel: int) -> float:
    # Convert an 8-bit sRGB channel to linear light.
    c = channel / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(hex_color: str) -> float:
    # WCAG relative luminance of a #RRGGBB color.
    r, g, b = (int(hex_color[i : i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * srgb_to_linear(r) + 0.7152 * srgb_to_linear(g) + 0.0722 * srgb_to_linear(b)


def contrast_ratio(fg: str, bg: str) -> float:
    # WCAG contrast ratio between two #RRGGBB colors.
    l1, l2 = relative_luminance(fg), relative_luminance(bg)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def report(label: str, ratio: float, needed: float, preferred: float, failures: list) -> None:
    # Print one PASS/FAIL line and record failures.
    ok = ratio >= needed
    state = "PASS+" if ratio >= preferred else ("PASS" if ok else "FAIL")
    print(f"{state}  {label}: {ratio:.2f}:1 (min {needed})")
    if not ok:
        failures.append((label, round(ratio, 2)))


def check_variant(variant: str, section: dict, minimums: dict, failures: list) -> None:
    # Validate the icon pairs that decide whether artwork reads on its surface.
    # Tile and shape perimeters are decorative edges, not controls, so they are not gated here.
    icon = section["color"]["icon"]
    accent = section["color"]["accent"]["base"]
    pairs = (
        ("icon.ink", "icon.folder_flap_top", icon["ink"], icon["folder_flap_top"], minimums["body_text"]),
        ("icon.ink_soft", "icon.surface", icon["ink_soft"], icon["surface"], minimums["ui_component"]),
        ("accent.base", "icon.tile_bottom", accent, icon["tile_bottom"], minimums["ui_component"]),
    )
    for fg_label, bg_label, fg, bg, needed in pairs:
        report(f"[{variant}] {fg_label} on {bg_label}", contrast_ratio(fg, bg), needed, minimums["preferred_text"], failures)


def main() -> int:
    # Gate every variant declared in the palette.
    document = json.loads(PALETTE_FILE.read_text())
    minimums = document["wcag_minimums"]
    failures = []
    for variant, section in document["variants"].items():
        check_variant(variant, section, minimums, failures)
    if failures:
        print(f"\nContrast failures: {failures}", file=sys.stderr)
        return 1
    print("\nAll icon pairs meet WCAG minimums.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

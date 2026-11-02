#!/usr/bin/env python3
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Light remap gate: colour tokens that artwork modules bake in before remap() runs must survive
# the dark->light map unchanged, otherwise the light palette value is silently overridden.
# Usage: tools/dev/check_light_remap.py

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ICONS_ROOT = REPO_ROOT / "tools" / "icons"
sys.path.insert(0, str(ICONS_ROOT))

try:
    from icon_palette import LIGHT_HEX_MAP, set_variant, svg_context
except ImportError:
    sys.exit("cannot import tools/icons/icon_palette.py")

HEX = re.compile(r"#[0-9a-fA-F]{6}(?![0-9a-fA-F])")


def baked_tokens() -> dict[str, str]:
    # Light-variant constants the popular-app batches interpolate straight into SVG text.
    set_variant("light")
    import apps_popular_common as common

    tokens = {}
    for name in dir(common):
        value = getattr(common, name)
        if name.isupper() and isinstance(value, str) and HEX.fullmatch(value):
            tokens[name] = value
    return tokens


def remap_once(value: str) -> str:
    # The same single-pass substitution render() applies to raw artwork text.
    return HEX.sub(lambda match: LIGHT_HEX_MAP.get(match.group(0).lower(), match.group(0)), value)


def main() -> int:
    # Fail when a baked token would be rewritten after the light palette resolved it.
    tokens = baked_tokens()
    placeholders = svg_context("light")
    errors = []
    for name, value in sorted(tokens.items()):
        if value.startswith("{COLOR_"):
            # Placeholders are resolved after remap(); they must exist in the render context.
            if value[1:-1] not in placeholders:
                errors.append(f"{name} uses {value} but svg_context() has no such token")
            continue
        if not HEX.fullmatch(value):
            errors.append(f"{name} is {value!r}, expected a #RRGGBB literal or a {{COLOR_*}} token")
            continue
        remapped = remap_once(value)
        if remapped != value:
            errors.append(
                f"{name} is baked as {value} but remap() rewrites it to {remapped}; "
                f"use a {{COLOR_*}} placeholder instead"
            )
    for line in errors:
        print(f"FAIL  {line}")
    if errors:
        print(f"\n{len(errors)} baked light token(s) disagree with LIGHT_HEX_MAP")
        return 1
    print(f"PASS  {len(tokens)} baked light token(s) survive the dark->light remap unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main())

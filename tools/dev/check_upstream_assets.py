#!/usr/bin/env python3
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Vendored asset gate: the committed upstream glyphs must match provenance.json byte for byte,
# so a build is reproducible on any machine and no glyph silently disappears.
# Usage: tools/dev/check_upstream_assets.py

import hashlib
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
UPSTREAM_ROOT = REPO_ROOT / "tools" / "icons" / "upstream"
MANIFEST = UPSTREAM_ROOT / "provenance.json"


def verify_set(name: str, record: dict) -> list[str]:
    # Every recorded icon must exist with its recorded hash, and nothing unrecorded may ship.
    errors = []
    folder = UPSTREAM_ROOT / name
    expected = record.get("icons", {})
    if not folder.is_dir():
        return [f"{name}: vendored directory missing ({folder})"]
    present = {svg.name for svg in folder.glob("*.svg")}
    for filename, digest in expected.items():
        path = folder / filename
        if not path.is_file():
            errors.append(f"{name}: recorded icon missing ({filename})")
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != digest:
            errors.append(f"{name}: {filename} changed since it was vendored")
    for filename in sorted(present - set(expected)):
        errors.append(f"{name}: unrecorded icon ({filename}); re-run the vendoring script")
    if record.get("count") != len(expected):
        errors.append(f"{name}: manifest count {record.get('count')} != {len(expected)} recorded icons")
    if not record.get("license"):
        errors.append(f"{name}: no upstream license recorded")
    if not (folder / "LICENSE").is_file():
        errors.append(f"{name}: missing the per-set LICENSE note")
    for license_file in record.get("license_files", []):
        if not (REPO_ROOT / license_file).is_file():
            errors.append(f"{name}: license text missing ({license_file})")
    if not record.get("license_files"):
        errors.append(f"{name}: no license text recorded")
    return errors


def main() -> int:
    # Validate the manifest and every vendored set.
    if not MANIFEST.is_file():
        print(f"FAIL  no provenance manifest at {MANIFEST}; run tools/dev/vendor_upstream_icons.py --force")
        return 1
    manifest = json.loads(MANIFEST.read_text())
    sets = manifest.get("sets", {})
    if not sets:
        print("FAIL  provenance manifest lists no icon sets")
        return 1
    errors = []
    total = 0
    for name, record in sorted(sets.items()):
        errors.extend(verify_set(name, record))
        total += len(record.get("icons", {}))
    for line in errors:
        print(f"FAIL  {line}")
    if errors:
        print(f"\n{len(errors)} vendored asset problem(s)")
        return 1
    print(f"PASS  {total} vendored upstream glyph(s) across {len(sets)} sets match provenance.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# One-shot snapshot refresh for Tela name parity; snapshots are committed, builds never read Tela.
# Usage:
#   tools/dev/snapshot_tela_names.py --catalog              # refresh tools/icons/catalog_names.json
#   tools/dev/snapshot_tela_names.py /path/to/Tela-circle   # refresh tela_parity_names.json + parity_aliases.py data

import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ICONS_TOOLS = REPO_ROOT / "tools" / "icons"
sys.path.insert(0, str(ICONS_TOOLS))

from parity_aliases import CATALOG_PACK_NAME, classify_parity, map_parity_name, primary_context

ICON_SUFFIXES = (".svg", ".png")
SIZE_DIR_RE = re.compile(r"^(?:\d+x\d+|\d+)$")
RETINA_RE = re.compile(r"@\d+x$")
NON_CONTEXT_DIRS = frozenset({"scalable"})
GENERATED_BY = "tools/dev/snapshot_tela_names.py"
BEGIN_MARK = "# --- BEGIN GENERATED PARITY DATA"
END_MARK = "# --- END GENERATED PARITY DATA"
TELA_SNAPSHOT = ICONS_TOOLS / "tela_parity_names.json"
CATALOG_SNAPSHOT = ICONS_TOOLS / "catalog_names.json"
PARITY_MODULE = ICONS_TOOLS / "parity_aliases.py"
PACK_DIR = REPO_ROOT / "src" / "icons" / CATALOG_PACK_NAME


def context_of(dir_parts: tuple[str, ...]) -> str | None:
    # Deepest non-size directory is the icon context; 'scalable' and @2x suffixes are transparent.
    for part in reversed(dir_parts):
        base = RETINA_RE.sub("", part)
        if base in NON_CONTEXT_DIRS or SIZE_DIR_RE.match(base):
            continue
        return base
    return None


def collect_names(root: Path) -> dict[str, list[str]]:
    # Walk files and symlinks; map every icon stem to its sorted context list.
    names: dict[str, set[str]] = {}
    seen_dirs: set[Path] = set()
    for dirpath, dirnames, filenames in os.walk(root, followlinks=True):
        here = Path(dirpath)
        real = here.resolve()
        if real in seen_dirs:
            dirnames[:] = []
            continue
        seen_dirs.add(real)
        rel_parts = here.relative_to(root).parts
        context = context_of(rel_parts) if rel_parts else None
        for filename in filenames:
            suffix = Path(filename).suffix
            if suffix not in ICON_SUFFIXES:
                continue
            stem = filename[: -len(suffix)]
            names.setdefault(stem, set()).add(context or "root")
    return {name: sorted(contexts) for name, contexts in sorted(names.items())}


def write_snapshot(data: dict, path: Path) -> None:
    # Deterministic, hermetic JSON: sorted keys, no host paths.
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def snapshot_catalog() -> None:
    # Refresh the committed catalog snapshot from the committed pack.
    names = collect_names(PACK_DIR)
    write_snapshot({"pack": PACK_DIR.name, "generated_by": GENERATED_BY, "names": names}, CATALOG_SNAPSHOT)
    print(f"{CATALOG_SNAPSHOT.relative_to(REPO_ROOT)}: {len(names)} names from {PACK_DIR.name}")


def build_parity_tables(tela_names: dict[str, list[str]], catalog: set[str]) -> tuple[dict[str, str], dict[str, str], dict[str, int]]:
    # Recompute aliases, generic contexts, and stats with the pure mapping functions.
    aliases: dict[str, str] = {}
    contexts: dict[str, str] = {}
    stats = {"tela_names": len(tela_names), "already_present": 0, "matched": 0, "generic": 0}
    for name, tela_contexts in tela_names.items():
        primary = primary_context(tela_contexts)
        kind = classify_parity(name, catalog)
        stats["already_present" if kind == "present" else kind] += 1
        if kind == "present":
            continue
        aliases[name] = map_parity_name(name, catalog, primary)
        if kind == "generic":
            contexts[name] = primary
    return aliases, contexts, stats


def render_data_block(aliases: dict[str, str], contexts: dict[str, str], stats: dict[str, int]) -> str:
    # One entry per line keeps the committed mapping reviewable and diff-friendly.
    lines = [f"{BEGIN_MARK} (refresh: python3 tools/dev/snapshot_tela_names.py <tela_theme_dir>) ---"]
    lines.append("PARITY_ALIASES: dict[str, str] = {")
    lines += [f"    {json.dumps(name)}: {json.dumps(target)}," for name, target in sorted(aliases.items())]
    lines += ["", "}", "", "PARITY_CONTEXTS: dict[str, str] = {"]
    lines += [f"    {json.dumps(name)}: {json.dumps(context)}," for name, context in sorted(contexts.items())]
    lines += ["", "}", "", "MATCH_STATS: dict[str, int] = {"]
    lines += [f"    {json.dumps(key)}: {value}," for key, value in sorted(stats.items())]
    lines += ["}", END_MARK + " ---", ""]
    return "\n".join(lines)


def refresh_parity_module(aliases: dict[str, str], contexts: dict[str, str], stats: dict[str, int]) -> None:
    # Replace only the generated block; hand-written logic above the markers stays authoritative.
    lines = PARITY_MODULE.read_text().splitlines()
    begin = next((i for i, line in enumerate(lines) if line.startswith(BEGIN_MARK)), None)
    end = next((i for i, line in enumerate(lines) if line.startswith(END_MARK)), None)
    if begin is None or end is None or end < begin:
        sys.exit(f"generated markers missing in {PARITY_MODULE}")
    PARITY_MODULE.write_text("\n".join(lines[:begin] + render_data_block(aliases, contexts, stats).splitlines() + lines[end + 1 :]))


def snapshot_tela(tela_dir: Path) -> None:
    # Refresh the Tela snapshot and regenerate the committed parity tables from both snapshots.
    if not CATALOG_SNAPSHOT.is_file():
        sys.exit(f"{CATALOG_SNAPSHOT} missing; run with --catalog first")
    tela_names = collect_names(tela_dir)
    write_snapshot({"theme": tela_dir.name, "generated_by": GENERATED_BY, "names": tela_names}, TELA_SNAPSHOT)
    catalog = set(json.loads(CATALOG_SNAPSHOT.read_text())["names"])
    aliases, contexts, stats = build_parity_tables(tela_names, catalog)
    refresh_parity_module(aliases, contexts, stats)
    print(
        f"{TELA_SNAPSHOT.relative_to(REPO_ROOT)}: {stats['tela_names']} names from {tela_dir.name} | "
        f"present {stats['already_present']} | matched {stats['matched']} | generic {stats['generic']}"
    )
    print(f"{PARITY_MODULE.relative_to(REPO_ROOT)}: {len(aliases)} aliases, {len(contexts)} generic contexts")


def main() -> int:
    # Dispatch on --catalog or a Tela theme directory argument.
    args = sys.argv[1:]
    if args == ["--catalog"]:
        snapshot_catalog()
    elif len(args) == 1 and Path(args[0]).is_dir():
        snapshot_tela(Path(args[0]))
    else:
        sys.exit(__doc__.splitlines()[3])
    return 0


if __name__ == "__main__":
    sys.exit(main())

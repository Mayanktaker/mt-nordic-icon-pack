#!/usr/bin/env python3
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Tela name-parity gate: snapshot integrity, deterministic alias mapping, and built artifacts.
# Artifacts: every snapshotted name must resolve in both built suites and no parity link may dangle.
# Run: python3 tools/dev/check_tela_parity.py

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ICONS_TOOLS = REPO_ROOT / "tools" / "icons"
sys.path.insert(0, str(ICONS_TOOLS))
sys.path.insert(0, str(REPO_ROOT / "tools" / "dev"))

try:
    import parity_aliases
    import snapshot_tela_names
    from icon_palette import PALETTES, theme_name
except ImportError as exc:
    sys.exit(f"cannot import parity modules ({exc}); run tools/dev/snapshot_tela_names.py first")

TELA_SNAPSHOT = ICONS_TOOLS / "tela_parity_names.json"
CATALOG_SNAPSHOT = ICONS_TOOLS / "catalog_names.json"
ICONS_ROOT = REPO_ROOT / "src" / "icons"
PACK_DIR = ICONS_ROOT / parity_aliases.CATALOG_PACK_NAME
SNAPSHOT_GENERATOR = "tools/dev/snapshot_tela_names.py"
STAT_KEYS = ("tela_names", "already_present", "matched", "generic")


def load_json(path: Path) -> dict:
    # Parsed JSON or a failing-gate sentinel message.
    if not path.is_file():
        return {"__missing__": f"snapshot missing: {path.relative_to(REPO_ROOT)}"}
    return json.loads(path.read_text())


def check_names_shape(data: dict, source: str) -> list[str]:
    # Snapshot names must be non-empty stems mapped to sorted, non-empty context lists.
    problems = []
    names = data.get("names")
    if not isinstance(names, dict) or not names:
        return [f"{source}: names must be a non-empty object"]
    for name, contexts in names.items():
        if not name or "/" in name or name != name.strip():
            problems.append(f"{source}: bad name entry {name!r}")
        if not isinstance(contexts, list) or not contexts or contexts != sorted(set(contexts)):
            problems.append(f"{source}: contexts for {name!r} must be a sorted non-empty list")
    return problems


def check_shape(data: dict, source: str) -> list[str]:
    # Both snapshots share a strict shape: origin label + generator + name map, no host paths.
    problems = []
    if "__missing__" in data:
        return [data["__missing__"]]
    expected = {"names", "generated_by", "theme"} if "theme" in data else {"names", "generated_by", "pack"}
    if set(data) != expected:
        problems.append(f"{source}: keys must be {sorted(expected)}, got {sorted(data)}")
        return problems
    if data["generated_by"] != SNAPSHOT_GENERATOR:
        problems.append(f"{source}: generated_by must be {SNAPSHOT_GENERATOR}")
    if "/" in data.get("theme", "") or "/" in data.get("pack", ""):
        problems.append(f"{source}: origin label must not contain a path")
    return problems + check_names_shape(data, source)


def check_catalog_fresh(data: dict) -> list[str]:
    # The committed catalog snapshot must equal the live authored pack (parity aliases excluded),
    # so mapping targets stay real while emitted parity names cannot leak into the catalog pool.
    live = set(snapshot_tela_names.collect_names(PACK_DIR))
    live -= set(parity_aliases.PARITY_ALIASES)
    if set(data.get("names", {})) != live:
        stale = set(data.get("names", {})) ^ live
        preview = ", ".join(sorted(stale)[:5])
        return [f"catalog_names.json stale vs {PACK_DIR.name} ({len(stale)} differed, e.g. {preview}); rerun with --catalog"]
    return []


def check_generics_in_catalog(catalog: set[str]) -> list[str]:
    # Every context generic must be a real glyph, or the fallback tail would point at nothing.
    problems = []
    for context, (symbolic, plain) in sorted(parity_aliases.CONTEXT_GENERICS.items()):
        for target in (symbolic, plain):
            if target not in catalog:
                problems.append(f"generic for {context} missing from catalog: {target}")
    return problems


def check_mapping(tela: dict, catalog: set[str]) -> tuple[list[str], dict[str, int]]:
    # Recompute every mapping deterministically and demand equality with the committed tables.
    problems = []
    stats = dict.fromkeys(STAT_KEYS, 0)
    aliases, contexts = parity_aliases.PARITY_ALIASES, parity_aliases.PARITY_CONTEXTS
    tela_names = tela.get("names", {})
    missing = set(tela_names) - catalog
    if set(aliases) != missing:
        extra, absent = sorted(set(aliases) - missing)[:5], sorted(missing - set(aliases))[:5]
        problems.append(f"PARITY_ALIASES keys != missing Tela names (extra e.g. {extra}, absent e.g. {absent})")
    stats["tela_names"] = len(tela_names)
    generics_seen = {}
    for name in sorted(tela_names):
        primary = parity_aliases.primary_context(tela_names[name])
        target = parity_aliases.map_parity_name(name, catalog, primary)
        kind = parity_aliases.classify_parity(name, catalog)
        stats[{"present": "already_present", "matched": "matched", "generic": "generic"}[kind]] += 1
        if target not in catalog:
            problems.append(f"{name}: mapping target not in catalog: {target}")
        if name.endswith("-symbolic") != target.endswith("-symbolic"):
            problems.append(f"{name}: symbolicness not preserved -> {target}")
        if kind == "present":
            if target != name:
                problems.append(f"{name}: already in catalog but mapped to {target}")
            continue
        if aliases.get(name) != target:
            problems.append(f"{name}: committed alias {aliases.get(name)!r} != recomputed {target!r}")
        if kind == "generic":
            generics_seen[name] = primary
    if contexts != generics_seen:
        diff = sorted(set(contexts) ^ set(generics_seen))[:5]
        problems.append(f"PARITY_CONTEXTS != generic-resolved names (diff e.g. {diff})")
    elif any(contexts[n] != generics_seen[n] for n in generics_seen):
        bad = [n for n in generics_seen if contexts[n] != generics_seen[n]][:5]
        problems.append(f"PARITY_CONTEXTS wrong primary context for e.g. {bad}")
    if stats != parity_aliases.MATCH_STATS:
        problems.append(f"MATCH_STATS {parity_aliases.MATCH_STATS} != recomputed {stats}")
    return problems, stats


def mapped_real_file(pack: Path, mapped: str) -> Path | None:
    # First existing SVG of a mapped name (sorted scalable-then-symbolic scan), resolved to a real file.
    for ctx in sorted(parity_aliases.DECLARED_CONTEXTS):
        for tree in ("scalable", "symbolic"):
            candidate = pack / tree / ctx / f"{mapped}.svg"
            if candidate.exists():
                return candidate.resolve()
    return None


def check_parity_link(problems: list[str], pack: Path, variant: str, name: str, expected: Path | None, dest: Path) -> None:
    # A parity destination must exist, resolve inside the theme, and point at the mapped real file.
    where = f"[{variant}] {name} in {dest.parent.name}: "
    if not dest.exists():
        problems.append(f"{where}parity link missing")
        return
    if not dest.is_symlink():
        return  # a real file (only possible if the name joined the catalog)
    resolved = dest.resolve()
    if not resolved.exists():
        problems.append(f"{where}dangling -> {dest.readlink()}")
    elif pack.resolve() not in resolved.parents:
        problems.append(f"{where}escapes the theme -> {dest.readlink()}")
    elif expected is not None and resolved != expected:
        problems.append(f"{where}points at {resolved.name}, expected {expected.name}")


def check_built_artifacts(tela: dict) -> list[str]:
    # Both built suites must resolve every snapshotted name with zero dangling parity links.
    problems: list[str] = []
    names = tela.get("names", {})
    aliases = parity_aliases.PARITY_ALIASES
    for variant in PALETTES:
        pack = ICONS_ROOT / theme_name(variant)
        if not pack.is_dir():
            problems.append(f"[{variant}] suite not built ({pack.name}); run generate_icons.py --variant both")
            continue
        built: set[str] = set()
        for ctx in sorted(parity_aliases.DECLARED_CONTEXTS):
            for tree in ("scalable", "symbolic"):
                ctx_dir = pack / tree / ctx
                if ctx_dir.is_dir():
                    built |= {p.stem for p in ctx_dir.iterdir() if p.suffix == ".svg"}
        unresolved = set(names) - built
        if unresolved:
            preview = sorted(unresolved)[:5]
            problems.append(f"[{variant}] {len(unresolved)} snapshotted names do not resolve, e.g. {preview}")
        links = 0
        expected_cache: dict[str, Path | None] = {}
        for name, mapped in sorted(aliases.items()):
            contexts = parity_aliases.emission_contexts(names.get(name, []))
            if mapped not in expected_cache:
                expected_cache[mapped] = mapped_real_file(pack, mapped)
            expected = expected_cache[mapped]
            for ctx in contexts:
                check_parity_link(problems, pack, variant, name, expected, pack / "scalable" / ctx / f"{name}.svg")
                links += 1
            if name.endswith("-symbolic"):
                for ctx in contexts:
                    mirror = pack / "symbolic" / ctx
                    if mirror.is_dir():
                        check_parity_link(problems, pack, variant, name, expected, mirror / f"{name}.svg")
                        links += 1
        print(f"  [{variant}] {len(built)} built names, {links} parity links checked")
    return problems


def main() -> int:
    # Run every parity check and print the coverage counts.
    problems = []
    tela = load_json(TELA_SNAPSHOT)
    catalog_data = load_json(CATALOG_SNAPSHOT)
    problems += check_shape(tela, "tela_parity_names.json")
    problems += check_shape(catalog_data, "catalog_names.json")
    if problems:
        for line in problems:
            print(f"FAIL {line}")
        return 1
    problems += check_catalog_fresh(catalog_data)
    catalog = set(catalog_data["names"])
    problems += check_generics_in_catalog(catalog)
    mapping_problems, stats = check_mapping(tela, catalog)
    problems += mapping_problems
    problems += check_built_artifacts(tela)
    for line in problems:
        print(f"FAIL {line}")
    if problems:
        print(f"\n{len(problems)} error(s)")
        return 1
    print(
        f"tela names: {stats['tela_names']} | already present: {stats['already_present']} | "
        f"token-matched: {stats['matched']} | context generic: {stats['generic']}"
    )
    print("Tela name-parity gate passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

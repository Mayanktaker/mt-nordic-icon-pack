# AGENTS.md — MT Nordic Icon Pack

© Mayanktaker Computers & Web Development | https://mayanktaker.com

Standalone icon + cursor pack for the MT Nordic desktop suite. Split out of the theme repository
so artwork can be versioned and released independently — **this repo must not read the theme's
`palette/` or build files**.

## Stack & toolchain (verify before assuming; update when versions change)
- Python 3.14 runtime, PyGObject (Rsvg, Gio, Adw), pycairo, `numpy` (cursor rasterisation).
- Output: FreeDesktop/KDE icon themes (`index.theme`, scalable SVG + 32/48/64/128 PNG) and Xcursor themes.
- Repo: git 2.56, `gh` authenticated as `Mayanktaker`, default branch `master`, public.
- Installation policy: user packs go to the user's `~/.icons` ONLY. No sudo, no system dirs.

## Single source of truth
- `palette/icons.json` — every icon and cursor colour, per variant (`dark`, `light`) plus the
  cursor pack. No magic values in generators; add tokens instead.
- The theme repo keeps its own palette; changing a theme colour does **not** flow here by design.

## Commands
- Contrast gate: `python3 tools/dev/check_contrast.py` (icon ink/tile/accent pairs, both variants).
- Build: `python3 tools/icons/generate_icons.py --variant both` (or `--variant dark|light`) → `src/icons/<pack>`.
- Lookup gate: `python3 tools/dev/check_icon_contexts.py` (shadowing + dangling aliases; run after every icon build).
- Preview: `python3 tools/icons/preview_sheet.py --variant light` → contact sheets in `build/preview/<variant>/`.
- Gallery: `python3 tools/dev/build_icon_gallery.py` → `docs/gallery/{dark,light}/`.
- Cursors: `python3 tools/icons/generate_cursors.py` → `src/cursors/<pack>`.
- Package: `tools/icons/package.sh [version]` → `dist/<slug>-v<version>.tar.xz`.
- Release: `tools/release.sh [version]` (gates + both suites + cursors + tarball).
- Install: `./install.sh [--dark|--light|--both] [--no-activate] [--icons-only|--cursors-only]`.

## Layout
- `palette/icons.json` — variant + cursor tokens (metadata, inheritance chains, colours)
- `src/icons/` — generated `MT-Nordic-Blue-Icons` and `MT-Nordic-Light-Icons` (committed artifacts)
- `src/cursors/` — generated `MT-Nordic-Blue-Cursors`
- `tools/icons/` — generators, artwork catalog, `icon_palette.py`, `package.sh`
- `tools/dev/` — contrast gate, lookup gate, gallery builder
- `docs/` — `design.md` (palette rules), `gallery/` (curated preview SVGs)
- `build/`, `dist/` — generated output (gitignored)

## Artwork rules
- One catalog, two variants: `icon_palette.py` maps dark artwork literals to light equivalents
  (`LIGHT_HEX_MAP`) and resolves `{COLOR_*}` placeholders from `color.icon`.
- Symbolic glyphs are `currentColor`; upstream resources are sanitized at extraction time
  (`sanitize_symbolic`) and camera lenses use an evenodd knockout, never a painted background.
- App tiles share one edge weight (`icon.tile_border`, 1.5px); folder edges use their own tokens.
- Dark generation must stay backward-compatible when touching shared artwork.

## Conventions
- Every file starts with the © header line.
- Every function/block gets one ≤1-line comment.
- License: GPL-3.0 (code) + CC BY-SA 4.0 (artwork). Commit at verified milestones, never force-push.

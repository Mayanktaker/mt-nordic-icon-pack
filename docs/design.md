# Icon Design Guide — MT Nordic Icon Pack

© Mayanktaker Computers & Web Development | https://mayanktaker.com

Single source of truth for colours: `palette/icons.json`. Generators read the `color.icon` block per
variant and pass it in as `{COLOR_*}` placeholders. Hand-drawn artwork may still carry literal hexes;
those are the one exception, remapped for the light suite through `LIGHT_HEX_MAP` in
`tools/icons/icon_palette.py`. A literal missing from that map silently keeps its dark value, so map
any new colour when you add it.

Artwork modules (`apps_popular_common.py` and friends) are imported *before* `remap()` runs, so a
colour they interpolate must be a `{COLOR_*}` placeholder: baking a hex whose value is also a dark
artwork literal makes the remap rewrite it and the light palette value is lost
(`tools/dev/check_light_remap.py` guards this).

## Principles
- **One catalog, two variants.** Dark and light suites share every shape; only colour differs, so
  coverage and aliases can never drift between modes.
- **Polar Night (dark).** Slate tiles (`#25344A` → `#0E141D`), snow ink (`#ECEFF4`), frost accents.
- **Snow Storm (light).** Paper-white tiles (`#FFFFFF` → `#DDE5F0`), polar ink (`#2E3440`), and
  accents darkened for daylight (`#00D2FF` → `#0079A8`, `#88C0D0` → `#4C719C`).
- **Edges are a system.** App tiles share one perimeter weight (`tile_border`, 1.5px). Folder
  bodies use their own `folder_*_edge` tokens because their gradients already carry the depth.
- **Contrast is a gate.** `tools/dev/check_contrast.py` must pass before commits.

## Key tokens (dark → light)
| Token | Dark | Light | Use |
|---|---|---|---|
| `icon.surface` | #202D40 | #DEE7F2 | App/device body |
| `icon.border` | #486490 | #7E8FA6 | Shape perimeter (3.08:1 dark) |
| `icon.tile_top` / `tile_bottom` | #25344A / #0E141D | #FFFFFF / #DDE5F0 | App tile gradient |
| `icon.tile_border` | #486490 | #A5B4C7 | App tile edge |
| `icon.folder_flap_top` | #2E415A | #FDFEFF | Folder front plate |
| `icon.folder_back_top` | #243346 | #E3EAF3 | Folder back plate |
| `icon.ink` | #ECEFF4 | #2E3440 | Glyph ink on plates (12.4:1 light) |
| `icon.specular_1..3` | #88C0D0 / #00D2FF / #81A1C1 | #4C719C / #0079A8 / #5E81AC | Folder sheen |

## Symbolic artwork
- Every symbolic glyph renders in `currentColor`; nothing carries a literal colour.
- Upstream GNOME Shell, Adwaita and extension icons ship hardcoded near-blacks (`#241f31`,
  `#363636`, `#dedede`, `#0e141d`); `sanitize_symbolic()` rewrites them at build time from the
  vendored copies in `tools/icons/upstream/` (see `provenance.json` for origin and licence).
- Detail knockouts (camera lenses) are evenodd subpaths, so the ring stays transparent on any surface.

## Storage
- A glyph is written once and referenced from its other contexts by relative symlink, so
  `scalable/status`, `scalable/actions`, `scalable/ui` and the `symbolic/` mirror never hold copies.
- Editor state (`sodipodi:namedview`) is stripped during sanitisation; `<metadata>` and `dc:creator`
  are kept because they carry upstream attribution.

## Fallback chains
- Dark: `Tela-circle,Adwaita,breeze-dark,breeze,hicolor`
- Light: `Tela-circle,Adwaita,breeze,hicolor` (never falls back to a dark pack)

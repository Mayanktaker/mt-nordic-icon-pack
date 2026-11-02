# Upstream attribution

© Mayanktaker Computers & Web Development | https://mayanktaker.com

MT Nordic Icon Pack ships original artwork plus symbols harvested, sanitised and recoloured from
upstream icon sets. Harvested glyphs are vendored under `tools/icons/upstream/` with per-file hashes
in `provenance.json`, so the build never reads the machine it runs on. Original artwork is CC BY-SA
4.0; derived glyphs keep their upstream terms and are redistributed under those terms.

## Icon artwork

| Source | Where it arrives from | Upstream terms |
|---|---|---|
| **GNOME Shell** symbolic icons | vendored in `tools/icons/upstream/gnome-shell/` from `gnome-shell-icons.gresource` | GPL-2.0-or-later |
| **libadwaita / Adwaita** symbolic icons | vendored in `tools/icons/upstream/adwaita/` from libadwaita's `GResource` bundle | LGPL-3.0-or-later; artwork CC BY-SA 3.0 |
| **Blur my Shell** extension icons | vendored in `tools/icons/upstream/blur-my-shell/` | GPL-3.0 |
| **Tiling Shell** extension icons | vendored in `tools/icons/upstream/tiling-shell/` | GPL-3.0 |
| **MT Nordic** curated glyphs | `tools/icons/symbolic_assets.py`, `settings_symbolics.py`, `misc_symbolics.py` | CC BY-SA 4.0 |

Adwaita artwork by Jakub Steiner and the GNOME Design Team; `<dc:title>` / `<dc:creator>` metadata
inside the generated SVGs is preserved where upstream shipped it.

CC BY-SA 3.0 artwork is redistributed into a CC BY-SA 4.0 collection through the one-way
compatibility granted by Creative Commons; the derived files remain available under CC BY-SA 4.0.

## Cursor artwork

`MT-Nordic-Blue-Cursors` is a recolour of **Nordic-cursors** from
[EliverLara/Nordic](https://github.com/EliverLara/Nordic) (`kde/cursors/Nordic-cursors`), which is
**GPL-3.0**. Provenance was verified in two ways: the shipped `index.theme` is byte-identical to
upstream, and the `wait` and `fleur` cursor binaries are byte-identical before recolouring.

Only colour is changed — geometry, hotspots and frame timing are untouched. Because GPL-3.0 is
copyleft, **the cursor pack is distributed under GPL-3.0**, not CC BY-SA 4.0. The source theme is not
committed here; rebuild it by installing Nordic-cursors and running
`python3 tools/icons/generate_cursors.py`.

## Application trademarks

App tile artwork identifies third-party applications. Names and logos are trademarks of their
respective owners and are used only to identify the corresponding software.

## License texts

| File | Covers |
|---|---|
| `LICENSES/GPL-3.0.txt` | build tooling, installers, CI, the cursor pack |
| `LICENSES/CC-BY-SA-4.0.txt` | original icon artwork |
| `LICENSES/GPL-2.0.txt` | vendored GNOME Shell glyphs |
| `LICENSES/LGPL-3.0.txt` | vendored libadwaita glyphs |
| `LICENSES/CC-BY-SA-3.0.txt` | vendored libadwaita artwork |

Each `tools/icons/upstream/<set>/LICENSE` names the exact terms for that set, and
`tools/icons/upstream/provenance.json` records the same per file hash.

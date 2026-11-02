# MT Nordic Icon Pack

© Mayanktaker Computers & Web Development | https://mayanktaker.com

Companion icon and cursor packs for the MT Nordic desktop suite, maintained as a standalone
project so the artwork can be versioned, reviewed and released on its own.

Two full icon suites and one cursor pack ship together:

| Pack | Mode | Notes |
|---|---|---|
| `MT-Nordic-Blue-Icons` | Polar Night (dark) | Snow-on-slate folders, app tiles, devices, MIME documents |
| `MT-Nordic-Light-Icons` | Snow Storm (light) | Paper-white folders, slate edges, daylight-legible accents |
| `MT-Nordic-Blue-Cursors` | both | Nordic pointer set used by either mode |

Coverage: ~370 app icons plus ~400 aliases, 120 MIME types, 26 GNOME Settings panels,
FreeDesktop symbolics and device/media icons, generated from one catalog so both variants never
drift apart.

## Install

```bash
./install.sh                 # copy both icon suites + cursors, activate for the current mode
./install.sh --light         # activate the Snow Storm artwork
./install.sh --dark          # activate the Polar Night artwork
./install.sh --no-activate   # copy files only
./install.sh --cursors-only  # skip the icon suites
```

Everything lands in `~/.icons` only — no root, no system directories. GNOME picks the icon theme
through `org.gnome.desktop.interface icon-theme`; GTK3 `~/.config/gtk-3.0/settings.ini` is kept in
sync so older apps follow along.

Missing icons fall back through `Tela-circle,Adwaita,breeze-dark,breeze,hicolor` (dark) and
`Tela-circle,Adwaita,breeze,hicolor` (light).

## Build from source

Requires Python 3 with PyGObject, pycairo, librsvg **and libadwaita** typelibs, plus numpy for the
cursors. Rebuilding the symbolic set also harvests whatever GNOME Shell / libadwaita resources the
build host provides, so a different host can produce a different glyph set — commit the regenerated
`src/icons/` whenever that happens.

The cursor pack is recoloured from the **Nordic-cursors** theme installed at
`~/.icons/Nordic-cursors`. Without that source the build fails loudly; pass `--reuse-existing` to
keep the committed pack instead (this is what CI does).

```bash
python3 tools/dev/check_contrast.py             # palette legibility gate
python3 tools/dev/check_light_remap.py          # palette vs dark->light remap gate
python3 tools/icons/generate_icons.py --variant both
python3 tools/dev/check_icon_contexts.py        # lookup-order and alias gate
python3 tools/dev/check_symbolic_render.py      # every -symbolic glyph honours the ink
python3 tools/icons/generate_cursors.py
python3 tools/icons/preview_sheet.py --variant light   # contact sheets in build/preview/
```

After packaging, `tools/dev/check_release_archive.py [tarball]` extracts the archive, installs it
into a throwaway `HOME` and fails if any pack does not land.

`tools/release.sh [version]` runs the gates, both suites, the cursors and the archive check, then
writes a `dist/` tarball; pushing a `v*` tag publishes it through GitHub Actions.

## Relationship to the theme

The icon pack does not depend on the MT Nordic Blue theme repository. Colours live in
`palette/icons.json`; the theme keeps its own palette, layout and shell CSS. Switching the desktop
mode does not move icons on its own — run `./install.sh --light` (or the theme's toggle, which swaps
icon themes only when these packs are installed).

- Theme: [Mayanktaker/mt-nordic-blue](https://github.com/Mayanktaker/mt-nordic-blue)

## License

- Code and build tooling: GPL-3.0 (`LICENSES/GPL-3.0.txt`)
- Artwork: CC BY-SA 4.0 (`LICENSES/CC-BY-SA-4.0.txt`)

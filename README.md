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

Coverage: 387 authored app icons plus 475 app-name aliases per suite — GNOME Settings panels
(`org.gnome.Settings*`) and KDE Plasma's `org.kde.*` names (dolphin, konsole, systemsettings and
friends) included — 120 MIME types, 16 KDE `preferences-*` settings names, FreeDesktop
symbolics (folder, edit, document, dialog, media, device and MIME families) and
device/media icons, generated from one catalog so both variants never drift apart.

## Install

```bash
./install.sh                 # copy both icon suites + cursors, activate for the current mode
./install.sh --light         # activate the Snow Storm artwork
./install.sh --dark          # activate the Polar Night artwork
./install.sh --no-activate   # copy files only
./install.sh --cursors-only  # skip the icon suites
```

Everything lands in `~/.icons` only — no root, no system directories. Activation follows the
running desktop, KDE first: Plasma gets `kdeglobals` `[Icons] Theme` and `kcminputrc`
`[Mouse] cursorTheme` through `kwriteconfig6`, while GNOME's `org.gnome.desktop.interface
icon-theme` still receives a best-effort write. GTK3/GTK4 `settings.ini` icon names are kept in
sync either way. Without an explicit `--dark`/`--light` the variant is detected from the desktop:
on KDE a `kdeglobals` colour scheme containing "dark" picks Polar Night, anything else Snow Storm;
without KDE tools the GNOME `color-scheme` decides.

Missing icons fall back through `Tela-circle,Adwaita,breeze-dark,breeze,hicolor` (dark) and
`Tela-circle,Adwaita,breeze,hicolor` (light).

### Verify the activation

```bash
kreadconfig6 --file kdeglobals --group Icons --key Theme        # -> MT-Nordic-Blue-Icons or MT-Nordic-Light-Icons
kreadconfig6 --file kcminputrc --group Mouse --key cursorTheme  # -> MT-Nordic-Blue-Cursors
kiconfinder dolphin                                             # resolves inside ~/.icons/MT-Nordic-*-Icons
kiconfinder org.kde.systemsettings                              # KDE alias resolves
kiconfinder preferences-system                                  # settings tile resolves
```

`kiconfinder` ships with a full Plasma install and reports where the active theme serves a
name, so each lookup above should print a path under `~/.icons/MT-Nordic-*-Icons`. On GNOME the
same spot-check is `gsettings get org.gnome.desktop.interface icon-theme`.

## Build from source

Requires Python 3 with PyGObject, pycairo and librsvg typelibs, plus numpy for the cursors.
Upstream symbolic glyphs are vendored under `tools/icons/upstream/`, so the build is hermetic: the
same commit produces the same suites on any machine. To refresh them against a newer GNOME, run
`python3 tools/dev/vendor_upstream_icons.py --force` on a host with gnome-shell and libadwaita
installed (that script needs the `Adw` typelib; the build itself does not).

The cursor pack is recoloured from the **Nordic-cursors** theme installed at
`~/.icons/Nordic-cursors`. Without that source the build fails loudly; pass `--reuse-existing` to
keep the committed pack instead (this is what CI does).

```bash
python3 tools/dev/check_contrast.py             # palette legibility gate
python3 tools/dev/check_light_remap.py          # palette vs dark->light remap gate
python3 tools/dev/check_upstream_assets.py      # vendored glyphs match provenance.json
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

- Build tooling, installers and CI: GPL-3.0 (`LICENSES/GPL-3.0.txt`)
- Original icon artwork: CC BY-SA 4.0 (`LICENSES/CC-BY-SA-4.0.txt`)
- Cursor pack: GPL-3.0, derived from [EliverLara/Nordic](https://github.com/EliverLara/Nordic)
- Vendored GNOME Shell / libadwaita / extension glyphs: their upstream terms (GPL-2.0+,
  LGPL-3.0, CC BY-SA 3.0, GPL-3.0). Per-set notes live in `tools/icons/upstream/<set>/LICENSE`;
  see `LICENSES/UPSTREAM-ATTRIBUTION.md`.

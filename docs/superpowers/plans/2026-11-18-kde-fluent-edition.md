# KDE-Fluent Edition — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the existing MT-Nordic-Blue/Light suites fully KDE-fluent — KIconLoader-safe symbolics, Tier-1 KDE app tiles, KDE activation in `install.sh` — verified offline by gates and live on the Fedora 45 KDE host.

**Architecture:** One catalog, two variants (unchanged). A post-pass inside `sanitize_symbolic()` makes every emitted symbolic KDE-recolorable; a new artwork module adds KDE app tiles through the existing `tile()` builder; `install.sh` gains a KDE activation branch. No new palette tokens.

**Tech Stack:** Python 3.14 + PyGObject (Rsvg), pycairo; POSIX sh for install/release; librsvg for gates.

**Spec:** `docs/superpowers/specs/2026-11-18-kde-fluent-edition-design.md` (design agreed with Mayank in conversation, 2026-11-18; this plan argues from it).

## Spec (design summary)

- **Intent:** The suites already claim KDE support (`FollowsColorScheme=true`, `breeze` in `Inherits`) but symbolics render black under KIconLoader, KDE apps fall back to Breeze, and activation is gsettings-only.
- **Approach chosen: A (pipeline-first).** Rejected B (vendored Breeze artwork — breaks the Nordic tile system) and C (aliases only — a "KDE version" without Dolphin misses the point).
- **Scope: Tier 1 (~26 KDE apps)** + `preferences-*` aliases; extras can follow as wave 2 without rework.
- **Non-goals:** No separate KDE-branded packs, no store.kde.org packaging, no new palette tokens, no changes to the theme repo.

## Global Constraints

- Every new/modified file starts with the © header (`© Mayanktaker Computers & Web Development | https://mayanktaker.com`); `#!` stays line 1 for executables.
- ≤1-line comment per function/block; no magic values — colours from `palette/icons.json` tokens at runtime.
- Installs go to `~/.icons` only; no sudo, no system dirs.
- Dark generation stays backward-compatible; light artwork via `{COLOR_*}` placeholders or `LIGHT_HEX_MAP`.
- One glyph written once; other contexts are relative symlinks.
- Tests = the repo's gates; run lint/py_compile plus relevant gates after each task.

## Review Focus

1. **Vendored upstream SVGs with existing `<style>` blocks / gpa attributes survive class injection uncorrupted** — Task 1 gate renders every emitted symbolic in both modes; also assert no `<style` id collision (idempotency check).
2. **Full-colour app tiles must NOT be touched by the recolour pass** (KIconLoader stylesheets apply theme-wide) — Task 1 includes a regen-diff check that `scalable/apps` full-colour SVGs are byte-identical before/after.
3. **Light suite fallback ink must be `#2E3440`, not the dark `#ECEFF4`** — Task 1 gate runs on both variants and asserts per-variant ink.
4. **Hosts with both `gsettings` and `kwriteconfig6`** (Fedora KDE + GNOME bits) — activation must prefer the KDE path when KDE tools exist; pinned by Task 4's throwaway-HOME test.
5. **Symlinked contexts never get double-injected** (single real file per glyph) — Task 1 asserts `current-color-scheme` appears exactly once per real file and zero times in symlink targets.

---

### Task 1: KIconLoader-safe symbolics

**Files:**
- Modify: `tools/icons/generate_icons.py` (`sanitize_symbolic`, ~line 1432; class rewrite helpers `rewrite_style_attribute`/`rewrite_paint_attribute`)
- Modify: `tools/dev/check_symbolic_render.py` (dual-mode assertions)
- Modify: `tools/release.sh` (gate description line 31, still step 7)

**Interfaces:**
- Consumes: `icon_palette.icon_colors() -> dict` (key `"ink"`); `sanitize_symbolic(svg_text: str) -> str`.
- Produces: every emitted symbolic SVG carries (a) `class="ColorScheme-Text"` on every `currentColor` paint, (b) a root `style="color:{ink}"` fallback, (c) one `<style id="current-color-scheme" type="text/css">` block defining `.ColorScheme-Text { color:{ink}; }` with `{ink}` resolved at runtime from the active variant (never a source literal — the light-remap gate must stay green).

- [ ] **Step 1: Extend `check_symbolic_render.py` with KDE assertions (fail first)**

  - Mode A (KIconLoader sim): strip the injected root style + style block, inject class rules with a test ink, assert every `currentColor` paint in the source carries a `ColorScheme-*` class (regex source assertion) and renders in the test ink.
  - Mode B (third-party sim): render untouched; assert output matches the variant ink (dark `#ECEFF4`, light `#2E3440`), never pure black.
  - Idempotency: run the injection logic on an already-processed sample; assert exactly one `current-color-scheme` occurrence.

- [ ] **Step 2: Run gate, verify it fails**

  Run: `python3 tools/dev/check_symbolic_render.py`
  Expected: FAIL — missing classes / missing fallback block.

- [ ] **Step 3: Implement the injection in `sanitize_symbolic()`**

  After the existing `currentColor` rewrites: append `ColorScheme-Text` to the `class` of every element whose fill/stroke is `currentColor` and lacks a `ColorScheme-*` class; inject the style block after the root tag and a root `style="color:{ink}"`; short-circuit if `id="current-color-scheme"` already present. Read ink via `icon_colors()["ink"]` at call time (per-variant builds bake their own).

- [ ] **Step 4: Verify gates + no full-colour drift**

  Run: `python3 tools/icons/generate_icons.py --variant both && python3 tools/dev/check_symbolic_render.py && python3 tools/dev/check_light_remap.py && python3 tools/dev/check_icon_contexts.py && git diff --stat src/icons/*/scalable/apps | tail -1`
  Expected: all gates PASS; `scalable/apps` full-colour SVGs unchanged (empty diff).

- [ ] **Step 5: Commit**

  `git add tools/icons/generate_icons.py tools/dev/check_symbolic_render.py tools/release.sh && git commit -m "feat: make every symbolic KIconLoader-recolorable"`

### Task 2: Tier-1 KDE app tiles

**Files:**
- Create: `tools/icons/apps_kde.py` (`KDE_APP_ICONS: dict[str, str]`, `KDE_APP_ALIASES: dict[str, str]`)
- Modify: `tools/icons/generate_icons.py` (import + merges placed AFTER the `POPULAR_APP_*` updates, generate_icons.py:812/883)

**Interfaces:**
- Consumes: `tile(key: str, body: str) -> str` from `apps_popular_common.py`; accent tokens (`ACCENT`, `SNOW`, `GREEN`, `RED`, …) from the same module.
- Produces: 22 NEW canonical names — `dolphin, konsole, yakuake, systemsettings, discover, ark, spectacle, kdeconnect, kcalc, kclock, kfind, filelight, printer-manager, kgpg, skanpage, krfb, krdc, dragonplayer, juk, kmail, kontact, kaddressbook` — plus `KDE_APP_ALIASES` covering desktop ids for ALL 26 Tier-1 names (`org.kde.dolphin → dolphin`, `org.kde.discover → discover`, `org.kde.dragonplayer → dragonplayer`, …). Pre-existing and NOT re-authored: `kate/kwrite/krita/kdenlive/kwalletmanager` (apps_extra / apps_popular_3 / apps_creative) and `gwenview/elisa` (apps_popular_5.py:25/85), `okular/partitionmanager` (apps_popular_6.py:11/178) — the four only gain their missing `org.kde.*` aliases. Merge `APP_ICONS.update(KDE_APP_ICONS)` / `APP_ALIASES.update(KDE_APP_ALIASES)` AFTER the `POPULAR_APP_*` merges (generate_icons.py:812/883) — no keys collide, but the position documents intent.

- [ ] **Step 1: Author the first three tiles** (`dolphin`, `konsole`, `systemsettings`) using `tile()` + `{COLOR_*}` placeholders or imported accent tokens; wire the module into `generate_icons.py`.

- [ ] **Step 2: Build + preview + ARTWORK CHECKPOINT**

  Run: `python3 tools/icons/generate_icons.py --variant both && python3 tools/icons/preview_sheet.py --variant dark && python3 tools/icons/preview_sheet.py --variant light`
  Show Mayank the contact sheets and **wait for approval** before mass-producing the remaining 23.

- [ ] **Step 3: Author the remaining 19 tiles + aliases** following the approved vocabulary; SVG body ≤ ~15 elements each.

- [ ] **Step 4: Verify gates + gallery**

  Run: `python3 tools/icons/generate_icons.py --variant both && python3 tools/dev/check_contrast.py && python3 tools/dev/check_icon_contexts.py && python3 tools/dev/check_symbolic_render.py && python3 tools/dev/build_icon_gallery.py`
  Expected: PASS; 22 new names present in both `src/icons/*/scalable/apps`, all 26 `org.kde.*` aliases resolve.

- [ ] **Step 5: Commit**

  `git add tools/icons/apps_kde.py tools/icons/generate_icons.py src/icons docs/gallery && git commit -m "feat: Tier-1 KDE tiles (22 new) + org.kde.* aliases for 26"`

### Task 3: `preferences-*` settings aliases

**Files:**
- Modify: `tools/icons/misc_symbolics.py` (small currentColor glyph batch + alias map entries)
- Modify: `tools/icons/generate_icons.py` (alias wiring, following the existing `preferences-desktop-theme` precedent in `app_assets.py:771`)

**Interfaces:**
- Produces: `preferences-system-windows`, `preferences-desktop-display`, `preferences-desktop-notifications`, `preferences-desktop-sound`, `preferences-desktop-wallpaper`, `preferences-desktop-cursor`, `preferences-desktop-font`, `preferences-desktop-locale`, `preferences-desktop-user`, `preferences-system-network`, `preferences-system-bluetooth`, `preferences-system-power`, `preferences-system-printer`, `preferences-system-bluetooth` (dedup) — authored as symbolics or aliased to existing glyphs where one fits (reuse > duplicate).

- [ ] **Step 1: Map each name** — alias to an existing symbolic where one fits; author the missing ~6 as 16-grid currentColor SVGs in the `misc_symbolics.py` style.
- [ ] **Step 2: Verify** — `python3 tools/icons/generate_icons.py --variant both && python3 tools/dev/check_icon_contexts.py && python3 tools/dev/check_symbolic_render.py` → PASS, no dangling aliases.
- [ ] **Step 3: Commit** — `git commit -m "feat: cover KDE preferences-* icon names"`

### Task 4: KDE activation in install.sh

**Files:**
- Modify: `install.sh` (`current_variant()` ~line 81; activation block ~lines 111-135; uninstall hint line 96)
- Modify: `tools/dev/check_release_archive.py` (activation assertions in the throwaway-HOME run)

**Interfaces:**
- Produces: `activate_kde(target, cursors)` — uses `kwriteconfig6 --file kdeglobals --group Icons --key Theme` and `--file kcminputrc --group Mouse --key cursorTheme`; detection `command -v kwriteconfig6`; precedence: the KDE path runs FIRST when present, gsettings calls still run best-effort after it (harmless without a GNOME session). The `gtk-3.0`/`gtk-4.0` `settings.ini` sync (install.sh:123-127) is factored into a shared helper BOTH branches call — GTK apps on a KDE host read those files, so skipping them would leave GTK apps on the old theme. `current_variant()` gains a KDE branch: `kreadconfig6 --file kdeglobals --group General --key ColorScheme`, case-insensitive substring — contains `dark` → dark; anything else (`Breeze`, `Breeze Light`, empty, unrecognized) → light, mirroring Plasma's light-leaning default and giving both variants a real path (the GNOME branch keeps its own rule). Uninstall message mentions resetting via KDE System Settings. `--no-activate` and `--cursors-only` semantics preserved.

- [ ] **Step 1: Extend `check_release_archive.py`** — after its throwaway-HOME install, if `kwriteconfig6` exists, run activation in a subprocess with `HOME=<tmp>` AND `XDG_CONFIG_HOME=<tmp>/.config` (kwriteconfig6 honours XDG_CONFIG_HOME) and `DBUS_SESSION_BUS_ADDRESS=` neutralised. Two scenarios: (a) explicit `./install.sh --dark` → assert `<tmp>/.config/kdeglobals` holds `[Icons]` `Theme=MT-Nordic-Blue-Icons`, `kcminputrc` `[Mouse]` `cursorTheme=MT-Nordic-Blue-Cursors`, and a seeded `gtk-3.0/settings.ini` rewritten to the dark pack; (b) auto-detect with a seeded `kdeglobals` `[General] ColorScheme=BreezeDark` → asserts the dark pack, and with no `kdeglobals` at all → asserts the light pack. Skip gracefully (printed SKIP) where KDE tools are absent so CI stays green.
- [ ] **Step 2: Run it, verify FAIL** (no KDE branch yet).
- [ ] **Step 3: Implement the KDE branch** in `install.sh` per Interfaces — factor the `settings.ini` sync into the shared helper first, then add the KDE activation block; keep `set -eu` safety — every kwriteconfig6 call `|| true` guarded exactly like the gsettings ones.
- [ ] **Step 4: Verify** — `python3 tools/dev/check_release_archive.py` → PASS incl. KDE assertions on the Fedora host; `sh -n install.sh` clean.
- [ ] **Step 5: Commit** — `git commit -m "feat: activate icons and cursors on KDE Plasma"`

### Task 5: Docs + release wiring

**Files:**
- Modify: `README.md` (KDE activation/verification section), `AGENTS.md` (commands + artwork rules note), `docs/design.md` (symbolic artwork section: ColorScheme-Text contract)
- Modify: `tools/release.sh` only if gate names/numbering shifted

- [ ] **Step 1: Full local release run** — `tools/release.sh` end-to-end → all 11 gates PASS, tarball produced.
- [ ] **Step 2: Update the three docs** (trigger skill `lolu-docs-sync` rules: behaviour changed ⇒ README + AGENTS + design.md in the same commit).
- [ ] **Step 3: Commit** — `git commit -m "docs: KDE-fluent edition documentation"`

### Task 6: Live verification on the Fedora 45 KDE host

**Evidence path** (claims → evidence, per verification-planning):
- *Lookup claim*: `kiconfinder dolphin`, `kiconfinder folder-symbolic`, `kiconfinder preferences-system-windows` resolve to paths under `~/.icons/MT-Nordic-*` (after `./install.sh --dark` + `kbuildsycoca6`).
- *Activation claim*: `kreadconfig6 --file kdeglobals --group Icons --key Theme` returns the pack; `kcminputrc [Mouse] cursorTheme` likewise.
- *Render claim (the one offline gates can't fully prove)*: with Mayank's consent, `systemctl --user restart plasma-plasmashell` (or re-login) and eyeball the tray/panel/Kickoff — symbolics tinted by the scheme, KDE tiles showing Nordic artwork. **Known limit:** pixel truth on Plasma's compositor is human-verified; offline gates cover everything else.

- [ ] **Step 1:** `./install.sh --dark` on the host; run the three kiconfinder lookups → all resolve to our pack.
- [ ] **Step 2:** Assert the two kreadconfig6 values; ask Mayank before restarting plasmashell; visual confirm.
- [ ] **Step 3:** Roll call — record results in the PR/description; revert activation if Mayank prefers his previous theme.

### Task 7: Tela name-parity snapshot + deterministic mapping (follow-up, Mayank 2026-11-18)

**Context:** Mayank reverted to Tela because icons were missing and asked to "complete the icon pack", choosing **full Tela name parity** over desktop-complete or broken-only. This is NAME coverage: every icon name Tela ships resolves inside our pack; artwork is a token-matched Nordic glyph or a context-appropriate Nordic generic for the tail. Tela inheritance stays as a safety net.

**Files:**
- Create: `tools/dev/snapshot_tela_names.py` (one-shot, refreshable; reads a Tela theme dir given as argv[1])
- Create: `tools/icons/tela_parity_names.json` (committed snapshot: name → sorted Tela contexts)
- Create: `tools/icons/catalog_names.json` (committed snapshot of canonical glyph names from `src/icons/MT-Nordic-Blue-Icons`)
- Create: `tools/icons/parity_aliases.py` (`PARITY_ALIASES`, `PARITY_CONTEXTS`, `MATCH_STATS`, `map_parity_name(name, catalog) -> str`)
- Create: `tools/dev/check_tela_parity.py` (determinism + snapshot integrity gate)

**Interfaces:**
- Snapshot JSON shape: `{"theme": "Tela-circle", "generated_by": "tools/dev/snapshot_tela_names.py", "names": {"<name>": ["apps", "status", ...]}}`; no absolute host paths.
- `map_parity_name(name: str, catalog: set[str]) -> str` — pure: normalize name (lowercase; strip `-symbolic`/`-app`/`-panel`/`-gui`/`-icon`/`-desktop`; split non-alnum; drop stopwords `org,kde,gnome,the,app`); symbolic requests only match symbolic candidates; score = token-overlap count; tie-break = smallest token-count delta, then lexicographic; threshold ≥1; zero-match → context generic: apps→`applications-symbolic`/`application-x-generic`, places→`folder-symbolic`/`folder`, status/actions→`dialog-information-symbolic`/`application-x-generic`, mimetypes→`document-open-symbolic`/`application-x-generic`, devices→`network-symbolic`/`computer` (symbolic / plain as requested).
- Known scale from recon: 15,290 Tela names, 1,290 ours, 14,458 missing; 9,937 have ≥1 token match; ~4,500 need generics; 1,389 `-symbolic` names; 39 Wine `.0` names.

- [ ] **Step 1: TDD gate first** — `check_tela_parity.py` asserts snapshot shape, every name has a deterministic mapping equal to `PARITY_ALIASES`, and match/generic counts equal `MATCH_STATS`; run → FAIL.
- [ ] **Step 2: Implement snapshot scripts + mapping module**; verify: `python3 tools/dev/check_tela_parity.py` PASS with counts printed; commit.
- [ ] **Step 3: Commit** — `git commit -m "feat: Tela name-parity snapshot and deterministic alias map"`

### Task 8: Emit parity aliases + verify + docs (follow-up)

**Files:**
- Modify: `tools/icons/generate_icons.py` (import parity module; `build_parity_aliases()` after app + symbolic builds)
- Modify: `README.md`, `AGENTS.md`, `docs/design.md` (name parity ≠ artwork parity; new gate command)
- Artifacts: ~25-30k SVG symlinks per variant in declared contexts (no PNG aliases — scalable dirs cover all sizes)

**Interfaces:**
- `build_parity_aliases()` creates one relative symlink per (name, context) from `PARITY_CONTEXTS`, normalized to our declared contexts (`apps, actions, status, places, devices, mimetypes, ui, categories`); `-symbolic` names also mirrored into `symbolic/<ctx>`; target = first real (non-symlink) SVG of the mapped name, chosen by sorted-context scan, relative to link location; zero dangling links.
- Gate: `tools/dev/check_tela_parity.py` additionally asserts every snapshotted name resolves in both built variants.

- [ ] **Step 1: Implement emission**, run `python3 tools/icons/generate_icons.py --variant both`, then `python3 tools/dev/check_tela_parity.py`, `python3 tools/dev/check_icon_contexts.py`, `python3 tools/dev/check_symbolic_render.py`, `python3 tools/dev/check_contrast.py` — all PASS.
- [ ] **Step 2: Controller checkpoint** — render a sample of 10 matched + 10 generic mappings for Mayank (no theme activation — he is on Tela and said not to surprise him).
- [ ] **Step 3: Full release run** (`tools/release.sh`), revert PNG churn, commit artifacts + code + docs — `git commit -m "feat: full Tela name parity for both icon suites"`.

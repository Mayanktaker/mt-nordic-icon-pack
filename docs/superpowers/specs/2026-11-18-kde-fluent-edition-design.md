# KDE-Fluent Edition — Design

© Mayanktaker Computers & Web Development | https://mayanktaker.com

Agreed with Mayank, 2026-11-18. The implementation plan that argues from this
design is `docs/superpowers/plans/2026-11-18-kde-fluent-edition.md`.

## Intent and why

The MT Nordic suites already claim KDE support in `index.theme`
(`FollowsColorScheme=true`, `KDE-Extensions=.svg`, `breeze`/`breeze-dark` in
`Inherits`), but four gaps make them GNOME-first in practice:

1. Symbolics are GTK-style `fill="currentColor"` — under KIconLoader the
   unclassed paths can render black-on-dark, the classic third-party-theme bug.
2. KDE app coverage is thin (kate, kwrite, krita, kdenlive, kwalletmanager
   only); Dolphin, Konsole, System Settings and friends fall back to Breeze.
3. `install.sh` activates via gsettings + GTK `settings.ini` only — nothing
   writes `kdeglobals` or `kcminputrc`.
4. No KDE distribution story.

Mayank's desktop is Fedora 45 KDE, so the edition is verified live on Plasma.

## Goals

- Every emitted symbolic survives KIconLoader recoloring AND renders with the
  variant ink in non-KDE renderers (dual mechanism: `ColorScheme-Text` classes
  plus a `current-color-scheme` style block with per-variant fallback ink).
- Tier-1 KDE app tiles (~26 names) in the existing Nordic `tile()` vocabulary,
  plus `org.kde.*` desktop-id aliases and `preferences-*` settings names.
- One-command activation on KDE: icons into `kdeglobals [Icons]`, cursors into
  `kcminputrc [Mouse]`, GTK `settings.ini` kept in sync.
- Offline gates prove everything except Plasma's on-screen tint; a live host
  check covers that.

## Non-goals / anti-goals

- No separate KDE-branded packs (rejected: duplicates the catalog for no gain).
- No vendored Breeze app artwork (rejected: breaks the Nordic tile system and
  one-catalog principle).
- No store.kde.org packaging in this edition (small follow-up later if wanted).
- No new palette tokens; no changes to the theme repository.

## Approaches considered

- **A. Pipeline-first (chosen)** — extend the single-catalog pipeline: a
  `sanitize_symbolic()` post-pass, a new `apps_kde.py` artwork module, a KDE
  branch in `install.sh`, extended gates. Reuses every existing convention.
- **B. Vendored Breeze shortcut (rejected)** — faster but mixes visual
  languages and fights the repo's remap/contrast gates.
- **C. Minimal shim (rejected)** — aliases and activation only; a "KDE version"
  where Dolphin still shows Breeze artwork misses the point.

## Decisions settled in conversation

- Scope is Tier 1 (~26 apps); Tier-2 extras come later as the same module grows.
- `gwenview`/`elisa`/`okular`/`partitionmanager` already exist as Nordic tiles —
  keep them, only add their missing `org.kde.*` aliases.
- KDE colour-scheme detection: `ColorScheme` containing `dark` → dark variant;
  anything else (`Breeze`, empty, unknown) → light, mirroring Plasma's
  light-leaning default.
- Activation precedence: KDE tools first when present, gsettings still
  best-effort, GTK `settings.ini` sync shared by both branches.
- Builder-check findings (variant-detection dead end, pre-existing tiles, GTK
  sync gap, XDG_CONFIG_HOME test pinning) are folded into the plan.

## Left to the builder

Task order, file-level interfaces, gate extensions and verification commands
live in the plan.

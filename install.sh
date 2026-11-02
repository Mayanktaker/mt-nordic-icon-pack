#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Installs the MT Nordic icon packs and cursors into the user's ~/.icons ONLY.
# Usage: ./install.sh [--dark|--light|--both] [--no-activate] [--icons-only|--cursors-only|--uninstall]

set -eu

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
ICONS_DIR="${HOME}/.icons"

# Pack names live in palette/icons.json; read them once so nothing is hardcoded here.
eval "$(python3 -c "
import json, shlex
doc = json.load(open('${REPO_ROOT}/palette/icons.json'))
print('ICONS_DARK=' + shlex.quote(doc['variants']['dark']['tech_name']))
print('ICONS_LIGHT=' + shlex.quote(doc['variants']['light']['tech_name']))
print('CURSORS=' + shlex.quote(doc['cursors']['tech_name']))
print('PACK_NAME=' + shlex.quote(doc['meta']['tech_name']))
" 2>/dev/null)" || {
  echo "cannot read palette/icons.json; run from a full checkout" >&2
  exit 1
}

WANT_ICONS=1
WANT_CURSORS=1
ACTIVATE=1
UNINSTALL=0
VARIANT="auto"

while [ $# -gt 0 ]; do
  case "$1" in
    --dark) VARIANT="dark" ;;
    --light) VARIANT="light" ;;
    --both) VARIANT="both" ;;
    --no-activate) ACTIVATE=0 ;;
    --icons-only) WANT_CURSORS=0 ;;
    --cursors-only) WANT_ICONS=0 ;;
    --uninstall) UNINSTALL=1 ;;
    -h|--help)
      sed -n '2,4p' "$0" | sed 's/^# \{0,1\}//'
      echo "  --dark | --light | --both   activate that icon variant (default: match the desktop)"
      echo "  --no-activate               install files only"
      echo "  --icons-only | --cursors-only"
      echo "  --uninstall                 remove both icon suites and the cursor pack"
      exit 0
      ;;
    *)
      echo "unknown option: $1" >&2
      exit 1
      ;;
  esac
  shift
done

# Reuse the icon cache so newly installed packs appear without a re-login.
refresh_cache() {
  if command -v gtk-update-icon-cache >/dev/null 2>&1; then
    gtk-update-icon-cache -f -t "${ICONS_DIR:?}/$1" >/dev/null 2>&1 || true
  fi
}

# Copy one pack next to its final location, then swap it in, so a failed copy never
# leaves the user without icons.
install_pack() {
  pack="${1:?missing pack name}"
  src="${REPO_ROOT}/src/${2:?missing pack kind}/${pack}"
  if [ ! -d "${src}" ]; then
    echo "  ! missing ${src} (build it first: $3)" >&2
    return 1
  fi
  staging="${ICONS_DIR:?}/.${pack}.tmp"
  rm -rf "${staging}"
  cp -r "${src}" "${staging}"
  rm -rf "${ICONS_DIR:?}/${pack}"
  mv "${staging}" "${ICONS_DIR:?}/${pack}"
  refresh_cache "${pack}"
  echo "  ✓ ${pack}"
}

# Which icon variant the desktop is currently using.
current_variant() {
  case "$(gsettings get org.gnome.desktop.interface color-scheme 2>/dev/null | tr -d "'")" in
    prefer-light|default) echo "light" ;;
    *) echo "dark" ;;
  esac
}

# Removal only deletes packs this repository owns; the active theme is left to the user.
if [ "${UNINSTALL}" -eq 1 ]; then
  for pack in "${ICONS_DARK}" "${ICONS_LIGHT}" "${CURSORS}"; do
    if [ -d "${ICONS_DIR:?}/${pack}" ]; then
      rm -rf "${ICONS_DIR:?}/${pack}"
      echo "  ✗ removed ${pack}"
    fi
  done
  echo "Uninstalled ${PACK_NAME}. Pick another icon theme with gsettings if one is still active."
  exit 0
fi

mkdir -p "${ICONS_DIR}"
echo "Installing ${PACK_NAME} into ${ICONS_DIR}"

if [ "${WANT_ICONS}" -eq 1 ]; then
  install_pack "${ICONS_DARK}" icons "python3 tools/icons/generate_icons.py --variant dark" || exit 1
  install_pack "${ICONS_LIGHT}" icons "python3 tools/icons/generate_icons.py --variant light" || exit 1
fi
if [ "${WANT_CURSORS}" -eq 1 ]; then
  install_pack "${CURSORS}" cursors "python3 tools/icons/generate_cursors.py" || exit 1
fi

# Activation follows the desktop mode unless an explicit variant was requested.
if [ "${ACTIVATE}" -eq 1 ]; then
  if command -v gsettings >/dev/null 2>&1; then
    if [ "${WANT_ICONS}" -eq 1 ]; then
      case "${VARIANT}" in
        dark) target="${ICONS_DARK}" ;;
        light) target="${ICONS_LIGHT}" ;;
        both) target="${ICONS_DARK}" ;;
        *) if [ "$(current_variant)" = "light" ]; then target="${ICONS_LIGHT}"; else target="${ICONS_DARK}"; fi ;;
      esac
      gsettings set org.gnome.desktop.interface icon-theme "${target}" 2>/dev/null || true
      # GTK3/GTK4 read settings.ini before the session bus, so keep their icon name in sync.
      for ini in "${HOME}/.config/gtk-3.0/settings.ini" "${HOME}/.config/gtk-4.0/settings.ini"; do
        if [ -f "${ini}" ] && grep -q "^gtk-icon-theme-name=" "${ini}"; then
          sed -i "s|^gtk-icon-theme-name=.*|gtk-icon-theme-name=${target}|" "${ini}"
        fi
      done
      echo "Activated icon theme: ${target}"
    fi
    if [ "${WANT_CURSORS}" -eq 1 ]; then
      gsettings set org.gnome.desktop.interface cursor-theme "${CURSORS}" 2>/dev/null || true
      echo "Activated cursor theme: ${CURSORS}"
    fi
  fi
fi

echo "Done. Switch icon variants later with: ${ICONS_DARK} / ${ICONS_LIGHT}"

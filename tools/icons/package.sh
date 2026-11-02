#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Packages the icon packs and cursors into a standalone .tar.xz release archive.
# Usage: tools/icons/package.sh [version]  (defaults to palette/icons.json meta.version)

set -eu

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

# Pack names and slug come from the palette so nothing is duplicated in shell.
eval "$(python3 -c "
import json, shlex
doc = json.load(open('${REPO_ROOT}/palette/icons.json'))
print('PACK_NAME=' + shlex.quote(doc['meta']['tech_name']))
print('PACK_SLUG=' + shlex.quote(doc['meta']['tech_name'].lower()))
print('DISPLAY_NAME=' + shlex.quote(doc['meta']['name']))
print('PALETTE_VERSION=' + shlex.quote(doc['meta']['version']))
print('ICONS_DARK=' + shlex.quote(doc['variants']['dark']['tech_name']))
print('ICONS_LIGHT=' + shlex.quote(doc['variants']['light']['tech_name']))
print('CURSORS=' + shlex.quote(doc['cursors']['tech_name']))
")"

VERSION="${1:-${PALETTE_VERSION}}"
DIST_ROOT="${REPO_ROOT}/dist"
STAGE="${DIST_ROOT}/${PACK_SLUG}-v${VERSION}"
TARBALL="${DIST_ROOT}/${PACK_SLUG}-v${VERSION}.tar.xz"

mkdir -p "${DIST_ROOT}"
rm -rf "${STAGE}"
mkdir -p "${STAGE}"

# Ship both icon variants plus the cursor pack; the installer picks what to activate.
for ICON_PACK in "${ICONS_DARK}" "${ICONS_LIGHT}"; do
  if [ -d "${REPO_ROOT}/src/icons/${ICON_PACK}" ]; then
    cp -r "${REPO_ROOT}/src/icons/${ICON_PACK}" "${STAGE}/"
  fi
done
cp -r "${REPO_ROOT}/src/cursors/${CURSORS}" "${STAGE}/"

# Licenses, palette and the same installer users get from the checkout.
mkdir -p "${STAGE}/LICENSES" "${STAGE}/palette"
cp "${REPO_ROOT}/LICENSES/GPL-3.0.txt" "${STAGE}/LICENSES/"
cp "${REPO_ROOT}/LICENSES/CC-BY-SA-4.0.txt" "${STAGE}/LICENSES/"
cp "${REPO_ROOT}/palette/icons.json" "${STAGE}/palette/icons.json"
cp "${REPO_ROOT}/install.sh" "${STAGE}/install.sh"
chmod +x "${STAGE}/install.sh"

# Bundle README so the archive explains itself without the repository.
{
  echo "# ${PACK_NAME} ${VERSION}"
  echo
  echo "© Mayanktaker Computers & Web Development | https://mayanktaker.com"
  echo
  echo "Companion icon and cursor pack for the MT Nordic desktop suite."
  echo
  echo "## Install"
  echo
  echo '```bash'
  echo "./install.sh              # install and activate for the current desktop mode"
  echo "./install.sh --light      # install and activate the Snow Storm artwork"
  echo "./install.sh --no-activate # copy files only"
  echo '```'
  echo
  echo "Packs: \`${ICONS_DARK}\`, \`${ICONS_LIGHT}\`, \`${CURSORS}\`."
} > "${STAGE}/README.md"

rm -f "${TARBALL}"
tar -C "${DIST_ROOT}" -cJf "${TARBALL}" "$(basename "${STAGE}")"
rm -rf "${STAGE}"

echo "Icon pack ready: ${TARBALL}"

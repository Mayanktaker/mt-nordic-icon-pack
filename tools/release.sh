#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Release builder: gates, rebuilds both icon variants, regenerates cursors and packages a tarball.
# Usage: tools/release.sh [version]

set -eu

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "${REPO_ROOT}"

VERSION="${1:-}"

echo "1/11 contrast gate"
python3 tools/dev/check_contrast.py

echo "2/11 light remap gate"
python3 tools/dev/check_light_remap.py

echo "3/11 cursor build guard"
python3 tools/dev/check_cursor_build.py

echo "4/11 vendored asset gate"
python3 tools/dev/check_upstream_assets.py

echo "5/11 icon suites (dark + light)"
python3 tools/icons/generate_icons.py --variant both

echo "6/11 icon lookup gate"
python3 tools/dev/check_icon_contexts.py

echo "7/11 Tela name-parity gate"
python3 tools/dev/check_tela_parity.py

echo "8/11 symbolic render gate (KIconLoader + third-party)"
python3 tools/dev/check_symbolic_render.py

echo "9/11 cursors"
python3 tools/icons/generate_cursors.py

echo "10/11 packaging"
if [ -n "${VERSION}" ]; then
  sh tools/icons/package.sh "${VERSION}"
  TARBALL="dist/mt-nordic-icon-pack-v${VERSION}.tar.xz"
else
  sh tools/icons/package.sh
  TARBALL=""
fi

echo "11/11 release archive gate"
python3 tools/dev/check_release_archive.py ${TARBALL}

echo "Done. Attach the tarball in dist/ to the GitHub release."

#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Release builder: gates, rebuilds both icon variants, regenerates cursors and packages a tarball.
# Usage: tools/release.sh [version]

set -eu

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "${REPO_ROOT}"

VERSION="${1:-}"

echo "1/7 contrast gate"
python3 tools/dev/check_contrast.py

echo "2/7 cursor build guard"
python3 tools/dev/check_cursor_build.py

echo "3/7 icon suites (dark + light)"
python3 tools/icons/generate_icons.py --variant both

echo "4/7 icon lookup gate"
python3 tools/dev/check_icon_contexts.py

echo "5/7 symbolic render gate"
python3 tools/dev/check_symbolic_render.py

echo "6/7 cursors"
python3 tools/icons/generate_cursors.py

echo "7/7 packaging"
if [ -n "${VERSION}" ]; then
  sh tools/icons/package.sh "${VERSION}"
else
  sh tools/icons/package.sh
fi

echo "Done. Attach the tarball in dist/ to the GitHub release."

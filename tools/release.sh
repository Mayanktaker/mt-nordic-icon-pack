#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Release builder: gates, rebuilds both icon variants, regenerates cursors and packages a tarball.
# Usage: tools/release.sh [version]

set -eu

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "${REPO_ROOT}"

VERSION="${1:-}"

echo "1/5 contrast gate"
python3 tools/dev/check_contrast.py

echo "2/5 icon suites (dark + light)"
python3 tools/icons/generate_icons.py --variant both

echo "3/5 icon lookup gate"
python3 tools/dev/check_icon_contexts.py

echo "4/5 cursors"
python3 tools/icons/generate_cursors.py

echo "5/5 packaging"
if [ -n "${VERSION}" ]; then
  sh tools/icons/package.sh "${VERSION}"
else
  sh tools/icons/package.sh
fi

echo "Done. Attach the tarball in dist/ to the GitHub release."

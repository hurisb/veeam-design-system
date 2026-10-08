#!/bin/sh
# Packages skill/ as dist/veeam-design-system.zip for Claude.ai → Settings → Skills → Upload.
# The zip holds one folder, veeam-design-system/, with SKILL.md at its root.
set -e
cd "$(dirname "$0")/.."
python3 scripts/build-tokens.py >/dev/null
rm -rf dist/tmp && mkdir -p dist/tmp/veeam-design-system
cp -R skill/. dist/tmp/veeam-design-system/
find dist/tmp -name .DS_Store -delete
rm -f dist/veeam-design-system.zip
(cd dist/tmp && zip -qr ../veeam-design-system.zip veeam-design-system)
rm -rf dist/tmp
echo "dist/veeam-design-system.zip ($(du -h dist/veeam-design-system.zip | cut -f1))"

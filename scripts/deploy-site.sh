#!/bin/sh
# The site deploys automatically: every push to main triggers Vercel, which runs
# scripts/build-site.sh and serves _site/ (see vercel.json). Nothing to run by hand.
#
# Manual fallback (only if the Git integration is off):
#   ./scripts/build-site.sh && cd _site && npx vercel deploy --prod --scope huri-1938s-projects
set -e
cd "$(dirname "$0")/.."
./scripts/build-site.sh
echo "Push to main to deploy: git push origin main"

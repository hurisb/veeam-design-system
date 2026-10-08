#!/bin/sh
# Publishes the example pages to Vercel.
# Only what the pages need is uploaded: examples/, css/, tokens/, fonts/, skill/assets/logos/.
# The source PDF, the skill zip, docs and scripts are never deployed.
# Usage: ./scripts/deploy-site.sh   (needs `npx vercel login` once)
#        VERCEL_SCOPE=saltbox-mgmt ./scripts/deploy-site.sh   to deploy under a team
set -e
cd "$(dirname "$0")/.."
python3 scripts/build-tokens.py >/dev/null
rm -rf _site && mkdir -p _site/skill/assets
cp -R examples css tokens fonts _site/
cp -R skill/assets/logos _site/skill/assets/
find _site -name .DS_Store -delete
cat > _site/index.html <<'HTML'
<!doctype html><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url=examples/"><title>Veeam Design System</title><a href="examples/">Examples</a>
HTML
printf 'User-agent: *\nDisallow: /\n' > _site/robots.txt
cat > _site/vercel.json <<'JSON'
{
  "cleanUrls": false,
  "headers": [{ "source": "/(.*)", "headers": [{ "key": "X-Robots-Tag", "value": "noindex, nofollow" }] }]
}
JSON
SCOPE="${VERCEL_SCOPE:-huri-1938s-projects}"
cd _site
npx --yes vercel@latest link --yes --scope "$SCOPE" --project saltbox-veeam-design-system >/dev/null
rm -f .env.local                       # vercel link pulls an OIDC token here; never upload it
printf '.env*\n.vercel\n' > .vercelignore
npx --yes vercel@latest deploy --prod --yes --scope "$SCOPE" < /dev/null

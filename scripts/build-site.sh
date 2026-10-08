#!/bin/sh
# Assembles the public examples site in _site/ — ONLY what the pages need:
# examples/, css/, tokens/, fonts/, skill/assets/logos/.
# Never the source PDF (resources/), the skill zip (dist/), docs, references or scripts.
# Vercel runs this on every push (see vercel.json); you can also run it locally.
set -e
cd "$(dirname "$0")/.."
rm -rf _site && mkdir -p _site/skill/assets
cp -R examples css tokens fonts _site/
cp -R skill/assets/logos _site/skill/assets/
find _site -name .DS_Store -delete
cat > _site/index.html <<'HTML'
<!doctype html><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url=examples/"><title>Veeam Design System</title><a href="examples/">Examples</a>
HTML
printf 'User-agent: *\nDisallow: /\n' > _site/robots.txt
echo "_site ready: $(find _site -type f | wc -l | tr -d ' ') files"

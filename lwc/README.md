# Veeam Lightning Web Components

Ready-to-use **Lightning Web Components** built on the Veeam design system. Pull
a bundle from here, drop it into your Salesforce project, and it inherits the
Veeam brand automatically — no hardcoded colors, fonts, spacing or radius.

Built and tested for **B2B / D2C Commerce on LWR (Experience Builder)**. The
markup/JS is plain LWC, so the same bundles also run on Experience Cloud and
App/Home pages (each exposed component lists its targets in its `*.js-meta.xml`).

## Component catalog

| Component | Folder | What it is | Experience Builder |
|---|---|---|---|
| **Shop by Product** | [`veeamShopByProduct/`](veeamShopByProduct/) | Product-category section: cards with count badge, modern featured icon, title, description and azure link CTA, on the S1 grid | Yes — "Veeam — Shop by Product" |
| Product Icon | [`veeamProductIcon/`](veeamProductIcon/) | Helper: renders one Untitled UI line icon by name (`shield-tick`, `grid-01`, `download-cloud-02`, `safe`) | No (internal) |

Each bundle is a standard LWC: `.html`, `.js`, `.css`, `.js-meta.xml`.

## Prerequisite — load the design tokens + fonts globally (REQUIRED)

LWC uses **shadow DOM**, so the global `css/veeam.css` classes do **not** reach
inside a component — but **CSS custom properties do**. Every component here is
styled only with tokens (`var(--text-primary)`, `var(--spacing-3xl)`,
`var(--color-primary)`…), so those variables and the ES Build fonts must exist
at the page / `:root` level. Without them a component renders unstyled.

Do this once per site, following
[`../skill/references/commerce-cloud.md`](../skill/references/commerce-cloud.md)
→ **§3 (B2B/D2C Commerce on LWR)**:

1. Upload [`../fonts/`](../fonts/) (zipped) as a static resource `veeam_fonts`.
2. **Settings → Advanced → Edit Head Markup** — link the fonts:
   ```html
   <link rel="stylesheet" href="{basePath}/sfsites/c/resource/veeam_fonts/fonts.css">
   ```
3. **Theme → Edit CSS** — paste the contents of
   [`../tokens/veeam-tokens.css`](../tokens/veeam-tokens.css) (it defines every
   `--token` on `:root`, light + dark).
4. **Theme → Fonts** — headings `ES Build Bauhaus`, body `ES Build Neutral`.

(Outside Commerce, the same holds: load `veeam-tokens.css` + `fonts.css` on the
page before the component.)

## Pull & deploy

**Just the components** (sparse checkout):
```bash
git clone --no-checkout https://github.com/hurisb/veeam-design-system.git
cd veeam-design-system
git sparse-checkout init --cone
git sparse-checkout set lwc tokens fonts
git checkout
```

**Into your DX project:** copy the component folder(s) you need into
`force-app/main/default/lwc/`, then:
```bash
sf project deploy start -d force-app/main/default/lwc
```
`veeamShopByProduct` depends on `veeamProductIcon`, so deploy both.

## Use it

**Experience Builder:** drag **"Veeam — Shop by Product"** onto a page. The
header text and the view-all link are editable in the property panel. To change
the cards, paste a JSON array into **Categories (JSON)**; otherwise the four
Veeam defaults are used.

**In markup:**
```html
<c-veeam-shop-by-product></c-veeam-shop-by-product>

<c-veeam-shop-by-product
    heading="Shop by product"
    view-all-url="/products"
    categories-json={myCategoriesJson}>
</c-veeam-shop-by-product>
```

**Customize the cards** — edit `DEFAULT_CATEGORIES` in `veeamShopByProduct.js`,
pass `categories-json`, or replace the `categories` getter with your own source
(Apex / wire / CMS). Each item:
```json
{
  "id": "data-platform",
  "count": "4 editions",
  "title": "Veeam Data Platform",
  "description": "Compare Essentials, Foundation, Advanced and Premium…",
  "cta": "Compare editions",
  "url": "/compare-editions",
  "icon": "shield-tick"
}
```

## Contributing a new component

1. Add a folder `lwc/<yourComponent>/` with the four bundle files.
2. **Token-only styling** — no raw hex, px spacing or radius; use `var(--token)`.
   Remember the shadow-DOM rule: global `.vds-*` classes won't reach inside, so
   port what you need using tokens.
3. Name custom tags `c-veeam-*`; expose to Experience Builder via targets +
   `targetConfigs` only when it's page-droppable.
4. Add a row to the catalog table above.

## Notes

- **A rebrand is a token change** — keep components free of literal values.
- **Icons** are inlined Untitled UI PRO line icons (a licensed set). Inlining in
  a product component is normal use; do not add the raw `.svg` library files.
- **Accessibility:** each card is a single link; decorative glyphs are
  `aria-hidden`. Give `url`s real destinations and descriptive link labels.

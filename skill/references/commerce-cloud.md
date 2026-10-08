# Using the Veeam tokens on Salesforce Commerce Cloud

The tokens are generated in five formats so the same values work on every Salesforce storefront
stack and on plain websites. Pick the row that matches your project.

| Stack | Use | Files |
|---|---|---|
| **B2C Commerce — SFRA** (ISML, Bootstrap 4, SCSS) | SCSS variables + Bootstrap overrides | `tokens/_veeam-tokens.scss`, `fonts/` |
| **B2C Commerce — Composable Storefront / PWA Kit** (React, Chakra UI) | Chakra theme | `tokens/pwa-kit-theme.js`, `fonts/` |
| **B2B / D2C Commerce on LWR** (Experience Builder) | CSS custom properties + `--dxp` styling hooks | `tokens/veeam-tokens.css`, `fonts/` |
| **Any website** (static, Next.js, Astro, WordPress…) | CSS variables + base classes, or Tailwind | `tokens/veeam-tokens.css`, `css/veeam.css`, `tokens/tailwind.preset.js` |
| **Figma / Tokens Studio / Style Dictionary** | DTCG JSON | `tokens/tokens.json` |

All of them come from `scripts/build-tokens.py` — change a value there, run
`python3 scripts/build-tokens.py`, and every format updates.

---

## 1. SFRA (B2C Commerce Storefront Reference Architecture)

1. Create (or reuse) a brand cartridge, e.g. `app_veeam`, ahead of `app_storefront_base` in the
   cartridge path.
2. Copy files:
   ```
   app_veeam/cartridge/client/default/scss/_veeam-tokens.scss   ← tokens/_veeam-tokens.scss
   app_veeam/cartridge/static/default/fonts/                    ← fonts/es-build*/ + fonts/fonts.css
   ```
3. In `app_veeam/cartridge/client/default/scss/global.scss`, import the tokens **before**
   Bootstrap so the overrides apply:
   ```scss
   @import "veeam-tokens";
   @import "~base/global";        // storefront base, which imports Bootstrap
   ```
4. Load the fonts once in `htmlHead.isml`:
   ```html
   <link rel="stylesheet" href="${URLUtils.staticURL('/fonts/fonts.css')}" />
   ```
5. What the overrides do: `$primary` → Electric Azure, `$secondary` → Viridis,
   `$headings-font-family` → ES Build Bauhaus, `$font-family-base` → ES Build Neutral,
   `$btn-border-radius` → 6px, button padding 12/24 (sm 8/20), and the **S1 grid**:
   `$grid-gutter-width` 32px (16px under 768px via an included media query), breakpoints
   `sm 768 / md 1024 / lg 1280 / xl 1440`, container 1280px.
6. Bootstrap `.btn-primary` / `.btn-outline-primary` now match Veeam primary / secondary. Add
   `text-transform: uppercase; letter-spacing: .02em; min-width: 190px` to `.btn` in your
   cartridge (or port `.vds-btn` from `css/veeam.css`).

> SFRA's own breakpoints differ from S1's (`md 769 / lg 992 / xl 1200`). Changing
> `$grid-breakpoints` affects every `col-md-*` in base templates — review PLP/PDP/checkout
> templates after switching, or keep SFRA breakpoints and only set `$container-max-widths`.

## 2. Composable Storefront (PWA Kit)

1. Copy `tokens/pwa-kit-theme.js` to `app/theme/veeam-theme.js` and the fonts to
   `app/static/fonts/`.
2. In `app/theme/index.js`:
   ```js
   import {extendTheme} from '@chakra-ui/react'
   import veeamTheme from './veeam-theme'
   export default extendTheme(veeamTheme)
   ```
3. Load `fonts.css` in `app/components/_app/index.jsx` (Helmet `<link>`) or import it.
4. `<Button>` defaults to Veeam primary (solid azure, uppercase, 6px radius);
   `variant="outline"` = secondary, `variant="ghost"` = tertiary. Headings use Bauhaus.
5. Semantic colors (`text-primary`, `bg-brand-solid`…) are available as CSS variables if you
   also load `tokens/veeam-tokens.css`; inside Chakra prefer the ramps (`brand.600`, `green.500`,
   `gray.900`).

## 3. B2B / D2C Commerce on LWR (Experience Builder)

1. Upload `fonts/` (zipped) as a **static resource** named `veeam_fonts`.
2. In **Settings → Advanced → Edit Head Markup**, add the fonts and tokens:
   ```html
   <link rel="stylesheet" href="{basePath}/sfsites/c/resource/veeam_fonts/fonts.css">
   ```
   (or paste the contents of `tokens/veeam-tokens.css` into **Theme → Edit CSS**).
3. Map the tokens to the site's global styling hooks in **Theme → Edit CSS**:
   ```css
   :root {
     --dxp-g-root: var(--bg-primary);                 /* page background */
     --dxp-g-root-contrast: var(--text-primary);      /* default text */
     --dxp-g-brand: var(--color-primary);             /* #3700FF — buttons, links */
     --dxp-g-brand-contrast: var(--color-white);
     --dxp-g-brand-1: var(--color-primary-hover);     /* #283E8E — hover */
     --dxp-g-accent: var(--color-secondary);          /* #00D15F */
     --dxp-g-accent-contrast: var(--color-gray-800);  /* ink on green, never white */
     --dxp-g-neutral: var(--color-gray-200);
     --dxp-g-success: var(--color-success);
     --dxp-g-warning: var(--color-warning);
     --dxp-g-destructive: var(--color-error);
   }
   ```
   Then set fonts in **Theme → Fonts**: headings `ES Build Bauhaus`, body `ES Build Neutral`,
   button radius 6px. Hook names can differ between releases — confirm them in your org's
   Theme panel before relying on one.
4. In custom LWCs, use the tokens directly (`color: var(--text-secondary)`), never hex.

## 4. Any website

```html
<link rel="stylesheet" href="fonts/fonts.css">
<link rel="stylesheet" href="tokens/veeam-tokens.css">
<link rel="stylesheet" href="css/veeam.css">   <!-- optional: type classes, buttons, grid, cards -->
```

Tailwind (v3): `presets: [require('./tokens/tailwind.preset.js')]`, then
`font-display`, `text-display-lg`, `bg-primary`, `hover:bg-primary-hover`, `text-sem-text-tertiary`,
`rounded-button`, `max-w-container`, `bg-gradient-brand`.

---

## Storefront patterns (see `examples/storefront/`)

| Pattern | Veeam treatment |
|---|---|
| Header | White, 72px, clean logo ~112px wide, search field, cart with azure count badge |
| Category hero | `gradient-brand-light` wash + Bounce Mark, H1 `Display lg`, `Text lg` intro |
| Refinements | Uppercase `Text sm/Semibold` group titles, `border-secondary` rule, azure checkboxes |
| Product tile | 12px radius, `border-secondary` → `border-brand` on hover, Bauhaus name, Navy price |
| PDP buy box | Option chips (selected = `bg-brand-primary` + `border-brand`), qty stepper, full-width primary + secondary CTA |
| Badges | success (green) = "Best seller/Protected", warning = "Early access", error = "Backup failed" |
| Toast | `bg-primary-solid`, Mint check icon |
| Footer | Gradient blue 3 (`#1D1E3F`) with light text |

Rules for commerce
- **One primary (azure) CTA per view** — "Add to cart" on PDP, "Checkout" in cart.
- Prices in Bauhaus SemiBold, Navy (`text-brand-primary`); unit/terms in `Text xs` below.
- Never green buttons on light pages; green belongs to imagery, gradients and "good" states.
- Status needs text + icon, not color alone.
- Images: 16:10 tiles, 4:3 PDP hero, product art on gradient grounds rather than flat white.

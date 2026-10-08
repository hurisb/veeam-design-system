---
name: "veeam-design-system"
description: "The Veeam design system (built on Saltbox's S1 system): ES Build Bauhaus for headings and ES Build Neutral for body, Electric Azure primary / Viridis green secondary colors, the blue-green brand gradient, the Veeam logo and Bounce Mark, S1 spacing/radius tokens, the Veeam 12-column grid, buttons and components. Use whenever building, reviewing or specifying Veeam websites, landing pages, Salesforce Commerce Cloud storefronts (SFRA, PWA Kit, B2B/D2C LWR), banners, documents or decks, or when asked about Veeam tokens, colors, fonts, logo, gradients, icons or components."
---

# Veeam Design System

The single source of truth for building **Veeam** websites and **Salesforce Commerce Cloud**
storefronts at Saltbox. It is a copy of the **S1 design system** — same token architecture,
spacing system, type-scale naming, semantic color names and component inventory — re-valued
with Veeam's brand from the *Veeam Inflection Design System Guidelines* (Interim Styleguide
Toolkit, version 052226, in `resources/`).

**Naming:** the client is **Veeam**. The visual style is the **Veeam + Securiti AI** transitional
system. It's **Securiti** — never "Security". Confirm the latest approved style and any messaging
with Veeam.CreativeTeam.Managers@veeam.com before publishing.

## The 30-second version

| | Value | Token |
|---|---|---|
| **Primary color** | Electric Azure `#3700FF` (hover `#283E8E`) | `--color-primary`, `bg-brand-solid` |
| **Secondary color** | Viridis `#00D15F` (hover `#009277`) | `--color-secondary`, `bg-secondary-brand-solid` |
| Tertiary / accent / highlight | Sky `#57E0FF` · Casia `#8E71F4` · Sol `#FFD839` | `--color-tertiary`, `--color-accent`, `--color-highlight` |
| Dark text | Navy Blue `#0E0D72` (brand) · `#1D1F2A` (default ink) | `text-brand-primary`, `text-primary` |
| Status | success `#00D15F` · warning `#FE8A25` · error (Ignis) `#ED2B3D` | `--color-success/-warning/-error` |
| Brand gradient | White → `#00FF5E` → `#008EE7` → `#283E8E` → `#1D1E3F` | `--gradient-brand` |
| **Headings font** | **ES Build Bauhaus** (SemiBold) | `--font-family-display` |
| **Body font** | **ES Build Neutral** | `--font-family-body` |
| PowerPoint headings | ES Build (never Bauhaus in PPT) | `--font-family-brand` |
| Spacing | S1 scale, 4px base; vertical rhythm 8/16/24/32/48/64/80/120 | `--spacing-*`, `--vspace-*` |
| Grid | 12 col ≥ 1024 · 6 col ≥ 768 · 2 col below; 30px gutter; 1260px container | `--grid-gutter`, `--container-max-width` |
| Buttons | 6px radius, UPPERCASE, 12/24 padding (sm 8/20), min 190 (sm 166) | `.vds-btn` |

## How this skill is organized

| Section | File | Covers |
|---|---|---|
| Tokens | `references/tokens.md` | Brand palette (hex/RGB/CMYK/Pantone), ramps 25–950, gradients, spacing, radius, type scale, grid, banner sizes |
| Color variables | `references/color-variables.md` | Brand aliases + S1 semantic tokens (text/border/fg/bg) with Veeam light **and** dark values, button tokens per surface, contrast flags |
| Typography | `references/typography.md` | ES Build Bauhaus / Neutral / ES Build, fallbacks & language fonts, scale, weights, rules, messaging |
| Logo | `references/logo.md` | Primary/clean/mono logos, favicon, app icon, Bounce Mark, usage |
| Brand elements | `references/brand-elements.md` | Key visual (gradient, Bounce Mark, Wave), green balance, imagery, illustration, motion & plates, checklist |
| Icons | `references/icons.md` | UI icons (Untitled UI line, from S1) vs. Veeam marketing icons (144px grid, 12px line, gradient) |
| Commerce Cloud | `references/commerce-cloud.md` | SFRA, PWA Kit, B2B/D2C LWR, Tailwind setup + storefront patterns |
| Form elements | `references/form-elements.md` | S1 inventory re-valued: inputs, selects, checkboxes, toggles, date pickers… |
| Navigation | `references/navigation.md` | **Veeam button spec** + S1 nav: header, tabs, breadcrumbs, pagination… |
| Data display | `references/data-display.md` | S1 inventory re-valued: tables, cards, badges, alerts, charts… |

**Code:** `tokens/veeam-tokens.css` (variables), `css/veeam.css` (base + `.vds-*` components),
`fonts/fonts.css`, `tokens/*` for SCSS/Tailwind/Chakra/JSON. **Examples:** `examples/`.

## Core principles

- **Token-first.** No raw hex, px spacing or radius in product code — use the named token.
- **Semantic over literal.** `text-secondary`, `bg-brand-solid`, `border-error` — not
  `gray-700` or `#3700FF`. Same names as S1, so S1 habits and components transfer as-is.
- **Azure acts, green brands.** Electric Azure is for actions (buttons, links, focus, selection)
  on light surfaces. Viridis green carries the brand — logo, gradient, imagery, green headlines,
  "good" states — and should fill **30–40%** of a marketing layout. On dark surfaces the CTA
  turns green with dark ink.
- **Every key visual = brand gradient + (Wave through Bounce Mark | Wave | wireframe texture).**
- **Readable over the gradient.** White beneath the logo; blurred white plates under text.
- **Color is contextual:** blue/purple neutral, green good, red/orange problem. Ignis red is
  never decorative.
- **Light first.** Veeam's web guidance prefers a light color scheme; dark (PRISM navy) is
  opt-in with `data-theme="dark"`.
- **Reuse before you build.** Check the component references and `css/veeam.css` first.

## Logo (summary — details in `references/logo.md`)

`veeam-logo-primary.svg` (with Bounce Mark) at ≥ 200px wide; `veeam-logo-clean.svg` under 200px
(headers); `veeam-logo-mono-white.svg` on black/dark/photo; `veeam-logo-mono-black.svg` for
one-color. Never retype, recolor, stretch or add effects. Keep it legible — white under it on
the gradient, or the inverted logo.

## Status

- **From the PDF:** palettes, logo files (vector-extracted), fonts (all three ES Build sets,
  woff2 + woff), type sizes, button spec and states, grid, vertical spacing, banner sizes, plate
  radius/stroke, icon grid, illustration and key-visual rules.
- **Inherited from S1:** spacing and radius scales, semantic token names/roles, component
  inventory, UI icon set (Untitled UI line), accessibility rules.
- **Derived (flagged in `tokens.md`):** intermediate ramp steps, dark-theme neutrals, line heights
  for Display 120/100/60, sampled PRISM gradient stops.
- **Open questions for Veeam Creative:** H2 size (PDF prints "55/52"; we use 44/52); whether a
  UI icon set exists beyond the marketing set; exact Wave artwork files (not in the PDF).
- **Out of scope for now:** Wave artwork, Securiti/partner lockups, PowerPoint template
  (use Veeam's — links on PDF p.90), shadows/elevation beyond the examples.

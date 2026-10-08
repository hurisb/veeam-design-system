---
name: veeam-design-system
description: >
  The Veeam design system (built on Saltbox's S1 system): ES Build Bauhaus for
  headings and ES Build Neutral for body, Electric Azure #3700FF primary and
  Viridis #00D15F secondary colors, the blue-green brand gradient, the Veeam
  logo and Bounce Mark, the S1 spacing, radius and grid, system colors
  (success/warning/error/info), text grays, buttons and components, with
  ready-to-use CSS, fonts and logo files. Use this skill
  whenever building, reviewing or specifying anything for Veeam — websites,
  landing pages, banners, Salesforce Commerce Cloud storefronts (SFRA, PWA Kit,
  B2B/D2C LWR), components, prototypes, PRDs, documents or decks. Also use when
  someone asks "what's the Veeam color/font/token for X" or wants a design
  checked against the Veeam brand, even if they don't say "design system".
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
| Spacing & radius | **Identical to S1** (4px base: 2…160px; radius 2…24px + full); buttons `radius-sm` 6px | `--spacing-*`, `--radius-*` |
| Grid | **Identical to S1:** 12 col / 32px gutter / 32px margin ≥ 1024 (container 1280) · 6 col / 32 / 32 ≥ 768 · 4 col / 16 / 16 on mobile | `--grid-gutter`, `--grid-columns`, `--container-padding` |
| System colors | success green · warning orange · error red · info blue — each with fill, border, icon, text, solid | `bg-success-primary`, `border-warning`, `fg-error-primary`, `text-info-primary`… |
| Text grays | headings `text-primary` #1D1F2A · labels `text-secondary` #3B4049 · **body `text-tertiary` #505861** · captions `text-quaternary` #6E737B | `--text-*` |
| Buttons | 6px radius, UPPERCASE, 12/24 padding (sm 8/20), min 190 (sm 166) | `.vds-btn` |

## How this skill is organized

| Section | File | Covers |
|---|---|---|
| Tokens | `references/tokens.md` | Brand palette (hex/RGB/CMYK/Pantone), ramps 25–950, gradients, spacing, radius, type scale, grid, banner sizes |
| Color variables | `references/color-variables.md` | Brand aliases, S1 semantic tokens with Veeam light **and** dark values, **system colors (success/warning/error/info) with UX rules**, **text grays with contrast**, button tokens per surface |
| Typography | `references/typography.md` | ES Build Bauhaus / Neutral / ES Build, fallbacks & language fonts, scale, weights, rules, messaging |
| Logo | `references/logo.md` | Primary/clean/mono logos, favicon, app icon, Bounce Mark, usage |
| Brand elements | `references/brand-elements.md` | Key visual (gradient, Bounce Mark, Wave), green balance, imagery, illustration, motion & plates, checklist |
| Icons | `references/icons.md` | UI icons (Untitled UI line, from S1) vs. Veeam marketing icons (144px grid, 12px line, gradient) |
| Commerce Cloud | `references/commerce-cloud.md` | SFRA, PWA Kit, B2B/D2C LWR, Tailwind setup + storefront patterns |
| Form elements | `references/form-elements.md` | S1 inventory re-valued: inputs, selects, checkboxes, toggles, date pickers… |
| Navigation | `references/navigation.md` | **Veeam button spec** + S1 nav: header, tabs, breadcrumbs, pagination… |
| Data display | `references/data-display.md` | S1 inventory re-valued: tables, cards, badges, alerts, charts… |

**Code:** see *Building with this skill* below — the tokens, CSS, fonts and logos are bundled in
`assets/`. The GitHub repo (hurisb/veeam-design-system) adds working example pages.

## Building with this skill — bundled files

Everything needed to build on-brand is inside this skill. Paths are relative to the skill folder.

| Need | File |
|---|---|
| All tokens as CSS variables (light + `data-theme="dark"`) | `assets/tokens/veeam-tokens.css` |
| Base styles + components (`.vds-btn`, `.vds-card`, `.vds-input`, `.vds-grid`, `.display-xl`, `.vds-eyebrow`…) | `assets/css/veeam.css` |
| ES Build / Neutral / Bauhaus web fonts + `@font-face` | `assets/fonts/fonts.css` (+ woff2/woff) |
| SFRA SCSS + Bootstrap overrides | `assets/tokens/_veeam-tokens.scss` |
| PWA Kit (Chakra) theme | `assets/tokens/pwa-kit-theme.js` |
| Tailwind preset | `assets/tokens/tailwind.preset.js` |
| Figma / Tokens Studio JSON | `assets/tokens/tokens.json` |
| Logos, favicon, app icon, Bounce Mark | `assets/logos/` |

**Recipe for any HTML page, prototype or artifact**
1. Copy `assets/fonts/` next to the page and link `fonts/fonts.css`. If files can't sit next to
   the page (e.g. a single-file artifact), embed the woff2 files as base64 `@font-face` sources,
   or fall back to Source Sans 3 from Google Fonts and say so.
2. Inline or link `assets/tokens/veeam-tokens.css`, then `assets/css/veeam.css`.
3. Use the `.vds-*` classes and `var(--token)` values — never raw hex, px spacing or radius.
4. Use the logo files from `assets/logos/` (inline the SVG for single-file outputs).
5. Check the result against the rules below and the checklist in `references/brand-elements.md`.

For a Commerce Cloud project, follow `references/commerce-cloud.md` for the stack in use.

> Path note: the reference files use repo paths (`tokens/…`, `css/…`, `fonts/…`). Inside this
> skill the same files are at `assets/tokens/…`, `assets/css/…`, `assets/fonts/…`.

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
- **Inherited from S1 (kept identical, even where the PDF differs):** spacing and radius scales,
  the grid (12/6/4 columns, 32/16px gutters, 1280 container), semantic token names/roles, component
  inventory, UI icon set (Untitled UI line), accessibility rules.
- **Derived (flagged in `tokens.md`):** intermediate ramp steps, dark-theme neutrals, line heights
  for Display 120/100/60, sampled PRISM gradient stops.
- **Open questions for Veeam Creative:** H2 size (PDF prints "55/52"; we use 44/52); whether a
  UI icon set exists beyond the marketing set; exact Wave artwork files (not in the PDF).
- **Out of scope for now:** Wave artwork, Securiti/partner lockups, PowerPoint template
  (use Veeam's — links on PDF p.90), shadows/elevation beyond the examples.

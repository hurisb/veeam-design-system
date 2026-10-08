# Veeam Design System

**Design tokens, fonts, logos, CSS and examples for building Veeam websites and Salesforce
Commerce Cloud storefronts — built on Saltbox's S1 design system.**

This repo turns the *Veeam Inflection Design System Guidelines* PDF into something the whole team
can build with: color, type, spacing and grid **tokens** in every format we use (CSS, SCSS for
SFRA, Chakra for PWA Kit, Tailwind, JSON for Figma), the **ES Build** web fonts, the **logo
files**, ready-made **button/form/card styles**, working **example pages**, and a **Claude
Skill** so anyone can ask "what's our primary button style?" and get the Veeam answer.

> **Private & confidential.** The ES Build fonts are licensed to Veeam and the source PDF is
> marked *Confidential*. Don't make this repo public, don't post the fonts on a public CDN, and
> don't share outside Saltbox and the Veeam project team.

---

## Contents

1. [Start here — pick your role](#1-start-here--pick-your-role)
2. [What's in the repo](#2-whats-in-the-repo)
3. [The system at a glance](#3-the-system-at-a-glance) — colors · fonts · spacing · grid · buttons
4. [Use it in code](#4-use-it-in-code) — any website · SFRA · PWA Kit · B2B/D2C LWR · Tailwind · Figma
5. [See the examples](#5-see-the-examples)
6. [Use it with Claude](#6-use-it-with-claude)
7. [Brand rules you can't skip](#7-brand-rules-you-cant-skip)
8. [How it relates to S1](#8-how-it-relates-to-s1)
9. [Changing a token](#9-changing-a-token)
10. [Open questions & status](#10-open-questions--status)

---

## 1. Start here — pick your role

| I am a… | Do this |
|---|---|
| **Front-end / SFCC developer** | Read [§3](#3-the-system-at-a-glance), then the section for your stack in [§4](#4-use-it-in-code). Copy `tokens/` + `fonts/`, never hard-code a hex. |
| **Designer** | Import `tokens/tokens.json` into Tokens Studio ([§4.6](#46-figma--tokens-studio)), install the fonts from `fonts/`, and open `examples/foundations/` to see every token rendered. |
| **QA / reviewer** | Use the rules in [§7](#7-brand-rules-you-cant-skip) and the contrast table in `skill/references/color-variables.md`. Ask Claude to review a screenshot ([§6](#6-use-it-with-claude)). |
| **PM / sales / leadership** | Skim [§3](#3-the-system-at-a-glance) and [§7](#7-brand-rules-you-cant-skip); open the example pages. Ask Claude questions in plain language. |
| **Anyone who just wants the Claude Skill** | Download [`dist/veeam-design-system.zip`](dist/veeam-design-system.zip) and upload it in Claude → Settings → Skills ([§6](#6-use-it-with-claude)). |
| **New to GitHub or Claude Skills** | Follow the step-by-step [docs/GETTING-STARTED.md](docs/GETTING-STARTED.md). |

Get the files: **`< > Code` → Download ZIP** (you must be signed in and invited), or

```bash
git clone https://github.com/hurisb/veeam-design-system.git
```

---

## 2. What's in the repo

```
veeam-design-system/
├── README.md                    ← you are here
├── docs/GETTING-STARTED.md      ← non-technical setup guide + example prompts
├── tokens/                      ← GENERATED — every token, five formats
│   ├── veeam-tokens.css         ← CSS custom properties (light + opt-in dark)
│   ├── _veeam-tokens.scss       ← SCSS variables + Bootstrap 4 overrides (SFRA)
│   ├── pwa-kit-theme.js         ← Chakra UI theme (Composable Storefront / PWA Kit)
│   ├── tailwind.preset.js       ← Tailwind v3 preset
│   └── tokens.json              ← W3C design tokens (Tokens Studio, Style Dictionary)
├── css/veeam.css                ← base styles + .vds-* components (type, buttons, grid, forms, cards, badges, plates)
├── fonts/                       ← ES Build, ES Build Neutral, ES Build Bauhaus (woff2 + woff) + fonts.css
├── scripts/build-tokens.py      ← SINGLE SOURCE OF TRUTH — edit values here, then run it
├── examples/
│   ├── foundations/             ← every token rendered: colors, ramps, gradients, type, buttons, spacing, grid, logo
│   ├── landing-page/            ← marketing page: gradient hero, Bounce Mark, cards, dark section, banner
│   └── storefront/              ← Commerce Cloud PLP (index.html) + PDP (product.html)
├── dist/veeam-design-system.zip ← THE CLAUDE SKILL, ready to upload (built by scripts/package-skill.sh)
├── skill/                       ← the Claude Skill source (also the full written spec)
│   ├── SKILL.md
│   ├── references/              ← tokens, color-variables, typography, logo, brand-elements, icons,
│   │                              commerce-cloud, form-elements, navigation, data-display
│   └── assets/                  ← bundled copies: tokens, css, fonts, logos (synced by the build script)
└── resources/
    └── Veeam Inflection Design System Guidelines.pdf   ← the source (v052226, confidential)
```

---

## 3. The system at a glance

### Colors

| Role | Color | Hex | CSS token |
|---|---|---|---|
| **Primary** — buttons, links, focus, selected | Electric Azure | `#3700FF` | `--color-primary` |
| Primary hover / focus / active | Gradient blue 2 | `#283E8E` | `--color-primary-hover` |
| **Secondary** — brand presence, logo, dark-theme CTA | Viridis | `#00D15F` | `--color-secondary` |
| Secondary hover | — | `#009277` | `--color-secondary-hover` |
| Tertiary — complement in illustration/diagrams | Sky | `#57E0FF` | `--color-tertiary` |
| Accent | Casia | `#8E71F4` | `--color-accent` |
| Highlight (fills only) | Sol | `#FFD839` | `--color-highlight` |
| Brand dark text | Navy Blue | `#0E0D72` | `--color-text-dark` |
| Default text ink | — | `#1D1F2A` | `--text-primary` |
| Success / Warning / Error | Viridis / Suma / Ignis | `#00D15F` / `#FE8A25` / `#ED2B3D` | `--color-success` … |
| Dark-theme background | PRISM dark | `#0F172C` | `--color-surface-dark` |

**Brand gradient** (`--gradient-brand`): White → `#00FF5E` → `#008EE7` → `#283E8E` → `#1D1E3F`.
Plus 13 more gradients (hero text, PRISM tab/negative/dark, icon, presentation) — see
`skill/references/tokens.md`.

In UI code use the **semantic tokens** — same names as S1: `--text-primary`, `--text-tertiary`,
`--border-secondary`, `--bg-brand-solid`, `--fg-success-primary`… Every one has a light and a
dark value. Full table: [`skill/references/color-variables.md`](skill/references/color-variables.md).

### Fonts

| Use | Font | CSS |
|---|---|---|
| **Headings & display** — H1–H4, hero, prices, metrics | **ES Build Bauhaus** (SemiBold) | `font-family: var(--font-family-display)` |
| **Subheads, body, all UI** — paragraphs, labels, buttons, nav, forms | **ES Build Neutral** | `font-family: var(--font-family-body)` |
| **PowerPoint / Office** headings & subheads | **ES Build** (standard) | `var(--font-family-brand)` |
| Fallbacks | Source Sans Pro (Google Fonts) · Tahoma (Office) · Arial (partner requests) | built into the stacks |

Why: Bauhaus removes the *ears and spurs* — clean, sophisticated headlines. Neutral keeps them —
more legible at small sizes. **Bauhaus is never used in PowerPoint.**

Type scale (S1 naming, Veeam sizes):

| Style | Size/line | Veeam name | | Style | Size/line | Veeam name |
|---|---|---|---|---|---|---|
| `display-3xl` | 120/128 | Display 120 | | `text-2xl` | 24/28 | Text 24 · Eyebrow |
| `display-2xl` | 100/108 | Display 100 | | `text-xl` | 20/24 | Text 20 |
| `display-xl` | 60/68 | Display 60 | | `text-lg` | 18/24 | Body 18 (marketing default) |
| `display-lg` | 50/60 | **H1** | | `text-md` | 16/24 | Paragraph 16 (UI default) |
| `display-md` | 44/52 | **H2** | | `text-sm` | 14/20 | Caption |
| `display-sm` | 36/44 | **H3** | | `text-xs` | 12/18 | Legal (S1) |
| `display-xs` | 28/36 | H4 | | | | |

Details, fallbacks for Japanese/Chinese/Thai/Korean, and rules:
[`skill/references/typography.md`](skill/references/typography.md).

### Spacing, radius, grid

Spacing, radius and grid are **identical to S1** — on purpose, so every Saltbox project shares
one layout system (where the Veeam PDF says otherwise, S1 wins).

- **Spacing:** 4px base — `--spacing-xs` 4 · `md` 8 · `lg` 12 · `xl` 16 · `2xl` 20 · `3xl` 24 ·
  `4xl` 32 · `6xl` 48 · `7xl` 64 · `8xl` 80 · `9xl` 96 · `10xl` 128. Sections: 80 (96 for heroes,
  48 on mobile).
- **Radius:** S1 scale (2 → 24, full). Buttons use `--radius-sm` (6px). Veeam adds only
  `--radius-plate` (60px) for message plates.
- **Grid:**

| | Columns | Gutter | Side margin | Container |
|---|---|---|---|---|
| Desktop ≥ 1024px | 12 | 32px | 32px | max 1280px (1216 content) |
| Tablet 768–1023px | 6 | 32px | 32px | fluid |
| Mobile < 768px | 4 | 16px | 16px | fluid |

`.vds-container` + `.vds-grid` apply this automatically (`--grid-columns`, `--grid-gutter`,
`--container-padding` switch at each breakpoint).

### System colors & text grays

| Status | Use for | Fill · Border · Icon · Text |
|---|---|---|
| **Success** (green) | Done, valid, protected, online | `bg-success-primary` · `border-success` · `fg-success-primary` · `text-success-primary` |
| **Warning** (orange) | Needs attention soon, user can continue | `bg-warning-primary` · `border-warning` · `fg-warning-primary` · `text-warning-primary` |
| **Error** (red) | Failed, invalid, blocked, destructive | `bg-error-primary` · `border-error` · `fg-error-primary` · `text-error-primary` |
| **Info** (blue) | Neutral system messages and tips | `bg-info-primary` · `border-info` · `fg-info-primary` · `text-info-primary` |

Always pair a status color with an icon and words; tell the user how to fix errors. Ready-made:
`.vds-alert--success|warning|error`, `.vds-badge--*`, `.vds-field-msg--*`, `.vds-dot--*`.

| Text tone | Token | Hex | Contrast on white | Use |
|---|---|---|---|---|
| Strongest | `--text-primary` | `#1D1F2A` | 16.4:1 | Headings, values, prices |
| Strong | `--text-secondary` | `#3B4049` | 10.4:1 | Labels, subheadings, nav |
| **Body** | `--text-tertiary` | `#505861` | 7.2:1 | **Paragraphs**, descriptions |
| Subtle | `--text-quaternary` | `#6E737B` | 4.8:1 | Captions, timestamps |
| Disabled | `--text-disabled` | `#ADACAF` | 2.3:1 | Disabled controls only |

Full guidance (UX rules, every token, light/dark values, contrast tables):
[`skill/references/color-variables.md`](skill/references/color-variables.md) §5–6.

### Buttons

| | Large | Small |
|---|---|---|
| Padding | 12 / 24 | 8 / 20 |
| Min width | 190px | 166px |
| Label | 16/24 SemiBold UPPERCASE | 14/20 SemiBold UPPERCASE |
| Radius | 6px | 6px |

| Surface | Primary | Secondary | Tertiary |
|---|---|---|---|
| Light | `#3700FF` → hover `#283E8E` | azure outline → `#283E8E` fill | azure text + → , hover `#EEF4F6` |
| Grey Mineral | white → hover `#232323` | white outline → white fill | white text |
| Dark | `#00D15F` + dark ink → `#009277` | green outline → `#009277` fill | green text |

```html
<a class="vds-btn" href="#">Request a demo</a>
<a class="vds-btn vds-btn--secondary" href="#">Watch video</a>
<a class="vds-btn vds-btn--tertiary" href="#">Read more →</a>
<section data-surface="dark"> …buttons turn green automatically… </section>
```

---

## 4. Use it in code

### 4.1 Any website (HTML, Next.js, Astro, WordPress…)

```html
<link rel="stylesheet" href="fonts/fonts.css">          <!-- ES Build ×3 -->
<link rel="stylesheet" href="tokens/veeam-tokens.css">  <!-- all tokens -->
<link rel="stylesheet" href="css/veeam.css">            <!-- optional: base + .vds-* components -->
```

```css
.promo {
  background: var(--gradient-brand);
  padding: var(--spacing-8xl) var(--container-padding);
  border-radius: var(--radius-2xl);
}
.promo h2 { font: var(--font-weight-semibold) var(--font-size-display-md)/var(--line-height-display-md) var(--font-family-display); }
.promo p  { color: var(--text-tertiary); font-size: var(--font-size-text-lg); }
```

Dark theme is opt-in: `<html data-theme="dark">` (or `class="theme-dark"` on a section).

### 4.2 Salesforce B2C Commerce — SFRA

Copy `tokens/_veeam-tokens.scss` into your brand cartridge's `client/default/scss/`, import it
**before** the base global styles, and copy `fonts/` to `static/default/fonts/`. Bootstrap's
`$primary`, `$secondary`, fonts, button radius/padding, breakpoints and container are overridden
for you. Step by step: [`skill/references/commerce-cloud.md` §1](skill/references/commerce-cloud.md#1-sfra-b2c-commerce-storefront-reference-architecture).

### 4.3 Composable Storefront — PWA Kit

```js
// app/theme/index.js
import {extendTheme} from '@chakra-ui/react'
import veeamTheme from './veeam-theme'   // ← tokens/pwa-kit-theme.js
export default extendTheme(veeamTheme)
```

`<Button>` = Veeam primary, `variant="outline"` = secondary, `variant="ghost"` = tertiary.

### 4.4 B2B / D2C Commerce on LWR (Experience Builder)

Upload `fonts/` as a static resource, load `fonts.css` + the tokens in Head Markup, and map the
tokens onto the `--dxp-g-*` styling hooks — snippet in
[`commerce-cloud.md` §3](skill/references/commerce-cloud.md#3-b2b--d2c-commerce-on-lwr-experience-builder).

### 4.5 Tailwind CSS (v3)

```js
// tailwind.config.js
module.exports = { presets: [require('./tokens/tailwind.preset.js')], content: ['./src/**/*.{html,js,jsx,tsx}'] }
```

```html
<h1 class="font-display text-display-lg text-brand-900">Data protection</h1>
<a class="bg-primary hover:bg-primary-hover text-white rounded-button px-3xl py-lg uppercase font-semibold">Buy now</a>
```

(Also load `tokens/veeam-tokens.css` for the semantic `sem-*` colors.)

### 4.6 Figma / Tokens Studio

Import `tokens/tokens.json` (W3C DTCG format) in Tokens Studio → it creates the ramps, palette,
brand aliases, semantic light/dark sets, typography, spacing and radius. Install the fonts from
`fonts/` (convert from woff2 if your OS needs `.otf`, or request desktop files from Veeam
Creative).

---

## 5. See the examples

The example pages load the real tokens and fonts. Fonts need a local web server (browsers block
fonts from `file://`):

```bash
python3 -m http.server 8000
```

Then open:

| Page | URL | Shows |
|---|---|---|
| Foundations | http://localhost:8000/examples/foundations/ | Every color, ramp, gradient, type style, button state, spacing step, the grid and logos |
| Landing page | http://localhost:8000/examples/landing-page/ | Gradient hero with Bounce Mark, gradient headline word, green-rule cards, PRISM dark section, banner, footer |
| Storefront PLP | http://localhost:8000/examples/storefront/ | Commerce Cloud product listing: header with search & cart, category hero, refinements, product tiles, pagination |
| Storefront PDP | http://localhost:8000/examples/storefront/product.html | Product detail: gallery, option chips, quantity, buy box, tabs, spec table, toast |

All example content (products, prices, SKUs, stats) is placeholder.

---

## 6. Use it with Claude

The **Veeam Design System Skill** works like the S1 skill: install it once and Claude answers
Veeam questions with the real values and builds pages and components with the right tokens,
fonts and logos (they're bundled inside the skill).

**Download the skill:** [`dist/veeam-design-system.zip`](dist/veeam-design-system.zip) (also on the
[Releases page](https://github.com/hurisb/veeam-design-system/releases/latest)).

| Where you use Claude | Install |
|---|---|
| **Claude.ai or the desktop app** | **Settings → Customize → Skills → Upload skill** → pick `veeam-design-system.zip` → toggle it **on**. Don't unzip it. |
| **Claude Code** | `unzip dist/veeam-design-system.zip -d ~/.claude/skills/` (or `cp -R skill ~/.claude/skills/veeam-design-system`) |
| **Whole team at once** (Team/Enterprise plan) | An org owner/admin uploads the same zip in the organization admin settings (Skills section) and shares it org-wide. |
| **No install** | Attach `skill/SKILL.md` + `skill/references/*` to a chat or a Claude Project. |

Try: *"What font do we use for H2 on Veeam pages?"* · *"Build a Veeam PDP buy box in SFRA ISML
using our tokens."* · *"Review this banner against the Veeam rules"* (attach a screenshot).
If you also have the S1 skill, say **"for Veeam"** so Claude picks the right one.
More prompts in [docs/GETTING-STARTED.md](docs/GETTING-STARTED.md).

To rebuild the zip after changing anything: `./scripts/package-skill.sh`.

---

## 7. Brand rules you can't skip

1. **Azure acts, green brands.** Buttons/links are Electric Azure on light pages. Green is the
   logo, gradient, imagery, headlines and "good" states — and stays **30–40%** of a marketing
   layout (never under 30%).
2. **Every key visual** = brand gradient + (Wave through the Bounce Mark · Wave only ·
   wireframe texture).
3. **Logo legibility:** white under the logo on the gradient, or use the inverted logo. Primary
   logo ≥ 200px wide; clean logo below that. Never retype or recolor it.
4. **Text over gradients** gets a blurred white plate or a contrasting background.
5. **Never white text on Viridis** (2.0:1) — use dark ink `#232323`. Green body text uses
   `--text-secondary-brand` `#007F49`.
6. **Gradient headline words** only for *Securiti* or *Agent Commander*.
7. It's **Securiti**, not "Security".
8. **Color is contextual:** blue/purple neutral · green good · red/orange problem. Ignis red
   never decorative, never in illustrations.
9. **One primary CTA per view.**
10. **Messaging** ("The Data & AI Trust Company", "Command your Data and AI Agents",
    "Detect AI. Protect AI. Undo AI.") must be confirmed with Veeam Creative before use.

Questions on brand: **Veeam.CreativeTeam.Managers@veeam.com**.

---

## 8. How it relates to S1

This is a copy of the [S1 design system](https://github.com/hurisb/s1-design-system), re-valued
for Veeam:

| Kept from S1 (unchanged) | Changed for Veeam |
|---|---|
| Token architecture: primitives → semantic (`text-*`, `border-*`, `fg-*`, `bg-*`) → components | All color values (azure primary, green secondary, Veeam neutrals, PRISM dark theme) |
| Semantic token names and roles | Fonts: Space Grotesk/Inter → ES Build Bauhaus/ES Build Neutral |
| Spacing scale (2–160px) and radius scale | Type sizes (Display 120/100/60, H1 50, H2 44, H3 36…) |
| Type-scale naming (`Display xl`, `Text md`…) and weight rules | Type sizes, button spec, status/info colors |
| Component inventory (forms, navigation, data display) | Button spec, gradients, plates, logo, brand elements |
| Grid (12/6/4 columns, 32/16px gutters, 1280 container) | Added: brand aliases, button tokens per surface, `radius-plate`, info ramp |
| Accessibility and UI icon rules (Untitled UI line) | |

If you know S1, you already know where everything is.

---

## 9. Changing a token

1. Edit the value in **`scripts/build-tokens.py`** (all values live there).
2. Run `python3 scripts/build-tokens.py` — regenerates `tokens/*`, `fonts/fonts.css` and
   `skill/references/color-variables.md`.
3. Open `examples/foundations/` to check it.
4. Update the prose in `skill/references/*.md` if the meaning changed.
5. Commit with a message naming what changed, e.g. `tokens: darken warning-700 for contrast`.

Never edit files in `tokens/` by hand — they're overwritten on the next build.

---

## 10. Open questions & status

**Extracted from the PDF:** palettes (hex/RGB/CMYK/Pantone), logo (vector), fonts, type sizes,
button spec, grid, vertical spacing, banner sizes, plates, icon grid, illustration and key-visual
rules, best practices.

**Derived by us (flagged in `tokens.md`):** intermediate ramp steps, dark-theme neutrals, line
heights for Display 120/100/60, sampled PRISM gradient stops.

**To confirm with Veeam Creative:**
- H2 is printed as **"55/52"** — we use **44/52**.
- Is there a UI icon set? (We use Untitled UI line from S1 for UI; Veeam's set is marketing-only.)
- Wave artwork and full key-visual source files (links on PDF p.90).

Maintainer: Huri (Saltbox). Built on the S1 design system.

# Design Tokens — raw values

The primitive/raw layer of the Veeam design system. It follows the **S1 structure** (same ramp
steps, same spacing and radius scale, same naming) with **Veeam values** from the *Veeam
Inflection Design System Guidelines* PDF (Interim Styleguide Toolkit, version 052226 —
`resources/` in this repo).

- For *which* color to use where (`text-primary`, `bg-brand-solid`…), see
  [`color-variables.md`](color-variables.md). For type styles, see [`typography.md`](typography.md).
- Every value here is defined once in `scripts/build-tokens.py` and generated into
  `tokens/veeam-tokens.css`, `tokens/tokens.json`, `tokens/_veeam-tokens.scss`,
  `tokens/tailwind.preset.js` and `tokens/pwa-kit-theme.js`.
- **Bold** hex = printed in the PDF. Plain hex = derived to complete a ramp.

---

## 1. Brand palette (from the PDF)

| Name | Hex | RGB | CMYK | Pantone | Role |
|---|---|---|---|---|---|
| Viridis | **#00D15F** | 0 209 95 | 71 0 84 0 | 2420 C | Signature Veeam green — logo plate, brand presence |
| Viridis 20% | **#40DB87** | 50 219 135 | 54 0 65 0 | 2268 C | Bounce Mark inside the logo |
| Mint | **#32F26F** | 50 242 111 | 54 0 65 0 | — | Bright green, icon gradient end |
| Sky | **#57E0FF** | 87 224 255 | 55 0 0 0 | — | Complement to Viridis in illustration |
| Electric Azure | **#3700FF** | 55 0 255 | 92 97 0 0 | — | **Primary CTA** on the web |
| Casia | **#8E71F4** | 142 113 244 | 49 55 0 0 | — | Supplementary accent |
| Sol | **#FFD839** | 255 216 57 | 0 4 88 0 | — | Highlight (fills only) |
| Suma | **#FE8A25** | 254 138 37 | 0 50 100 0 | — | Warning |
| Ignis (system red) | **#ED2B3D** | — | — | — | Alerts & watch-outs only |
| Navy Blue (Dark Text) | **#0E0D72** | 14 13 114 | 100 86 23 6 | — | Brand dark text |
| White | **#FFFFFF** | 255 255 255 | 4 5 8 0 | — | Gradient start, space under the logo |
| Gradient green | **#00FF5E** | 0 255 94 | 65 0 71 0 | — | Brand gradient stop |
| Gradient blue 1 | **#008EE7** | 0 142 231 | 93 52 0 0 | — | Brand gradient stop, icon gradient start |
| Gradient blue 2 | **#283E8E** | 40 62 142 | 96 73 0 15 | — | Brand gradient stop, **CTA hover** |
| Gradient blue 3 | **#1D1E3F** | 29 30 64 | 96 76 0 20 | — | Brand gradient end, dark sections |
| Black | **#000000** | 0 0 0 | 60 50 50 100 | Black spot | Monochrome logo |

Presentation (PowerPoint) palette, PDF p.58: main **#00D15F #4AFF9C #8E71F4 #1CA8DD #002060
#3700FF #FF6900 #FFD839 #97D700**; neutrals **#1D1F2A #505861 #8F8B90 #DBDEE1 #F2F3F2**;
negative **#ED2B3D**. Web palette, PDF p.39: green **#02613F #007F49 #009277 #00D15F #E1F4EC**
(`#32F26F` and `#9CFFA3` are *not part of PRISM*); blue **#002833 #283E8E #3700FF #57E0FF
#E3EEFE #EEF4F6**; supplementary **#8E71F4 #CECBB8**; system **#ED2B3D #FE8A25 #FFD839
#FCF8EB**; neutral **#000000 #232323 #505861 #ADACAF #F0F0F0 #F9F9F9 #FFFFFF**.

> **Mind the color space:** RGB/hex for screens, CMYK for print. Print never looks as vivid.

CSS: `--color-viridis`, `--color-electric-azure`, `--color-sky`… (kebab-case of the name).

---

## 2. Primitive ramps (25 → 950)

Same 12 steps as S1, so every S1 semantic token resolves to the same step.

| Step | `brand` (Electric Azure) | `green` (Viridis) = `success` | `gray` (light) | `gray-dark` (PRISM) | `error` | `warning` | `info` |
|---|---|---|---|---|---|---|---|
| 25 | `#f5f8fe` | `#f2fdf6` | `#fcfcfc` | `#fafafb` | `#fffafa` | **`#fcf8eb`** | `#f5fbff` |
| 50 | **`#e3eefe`** | **`#e1f4ec`** | **`#f9f9f9`** | `#f5f6f8` | `#fef2f3` | `#fff4ea` | `#e8f5fd` |
| 100 | `#ccd9fe` | `#c6f7da` | **`#f0f0f0`** | `#eceef3` | `#fde3e5` | `#ffe6cf` | `#cfeafb` |
| 200 | `#a9b6ff` | **`#9cffa3`** | **`#dbdee1`** | `#e1e4ec` | `#fbc7cc` | `#ffcd9f` | `#a3d6f6` |
| 300 | `#8a8dff` | **`#4aff9c`** | `#c3c6cb` | `#c8ccd8` | `#f69aa3` | `#feb06a` | `#6cbdf0` |
| 400 | `#6b5cff` | **`#32f26f`** | **`#adacaf`** | `#959cb0` | `#f15f6d` | `#fe9c45` | `#33a3eb` |
| 500 | `#4d2eff` | **`#00d15f`** | `#6e737b` | `#7d859c` | **`#ed2b3d`** | **`#fe8a25`** | **`#008ee7`** |
| 600 | **`#3700ff`** | **`#009277`** | **`#505861`** | `#5a637d` | `#d01a2c` | **`#ff6900`** | `#0077c4` |
| 700 | **`#283e8e`** | **`#007f49`** | `#3b4049` | `#34405e` | `#ad1524` | `#c2510a` | `#005f9e` |
| 800 | **`#1d1e3f`** | **`#02613f`** | **`#232323`** | `#1e2a47` | `#8c1520` | `#9f3f0a` | `#014b7c` |
| 900 | **`#0e0d72`** | `#014a30` | **`#1d1f2a`** | `#162036` | `#74161f` | `#80350c` | `#023d65` |
| 950 | `#0a0a45` | `#002e1e` | `#121318` | **`#0f172c`** | `#400a0f` | `#451905` | `#022640` |

Notes
- `brand` is the **primary** ramp. Like S1's navy→purple ramp, it changes hue at the dark end:
  `brand-700` is Gradient blue 2 (the PDF's CTA hover) and `brand-900` is Navy Blue.
- `green` is the **secondary** ramp and doubles as `success` ("green is good", PDF p.52).
- `info` is anchored on Gradient blue 1 **`#008EE7`** (500) — blue means neutral/system information.
  `warning-25` is the PDF's system cream **`#FCF8EB`**. How to use the four status colors:
  [`color-variables.md`](color-variables.md), section 5.
- `gray-dark` is navy-tinted so dark mode sits on the PRISM dark background (`#0F172C`, sampled
  from the PDF's dark-theme swatch).
- CSS: `--color-brand-600`, `--color-green-500`, `--color-gray-dark-950`…

---

## 3. Brand aliases

Plain-language aliases for marketing and site code — `--color-primary`, `--color-secondary`,
`--color-tertiary`, `--color-accent`, `--color-highlight`, `--color-text-dark`,
`--color-success`, `--color-warning`, `--color-error`. Full table with roles in
[`color-variables.md`](color-variables.md), section 0.

---

## 4. Gradients

| Token | Value | Use |
|---|---|---|
| `gradient-brand` | 135°: `#FFFFFF` 0 → `#00FF5E` 22% → `#008EE7` 52% → `#283E8E` 78% → `#1D1E3F` 100% | **Signature key visual.** Every design needs it. |
| `gradient-brand-radial` | same stops, radial from top-left | Radial version; white corner sits beneath the logo |
| `gradient-brand-light` | `#FFFFFF` → `#E1F4EC` → `#9CFFA3` → `#00D15F` | Light green wash behind dark text |
| `gradient-hero-text` | 90°: `#00D15F` → `#1976A6` → `#3700FF` | PRISM *Hero font* — gradient headline words |
| `gradient-tab-active` | `#15839A` → `#3700FF` | PRISM *Tab: Active* |
| `gradient-negative` | `#E23E57` → `#A0273A` | PRISM *Negative stats* |
| `gradient-dark-bg` | 180°: `#0C1427` → `#1E3C6F` | PRISM *dark theme background* |
| `gradient-icon` | `#008EE7` → `#32F26F` | Marketing icons (Gradient blue 1 → Mint) |
| `gradient-green-cyan` · `-casia-azure` · `-cyan-ocean` | `#00D15F→#1CA8DD` · `#8E71F4→#3700FF` · `#1CA8DD→#0058FF` | Presentation gradients, light BG |
| `gradient-mint-cyan` · `gradient-alert-dark` | `#4AFF9C→#1CA8DD` · `#FFD839→#FE8A25` | Presentation gradients for dark BG |
| `gradient-alert` | `#FF6900` → `#FE8A25` | Negative gradient, light BG |

PRISM gradients (hero text, tab, negative, dark bg) are shown as swatches in the PDF without
stop values; the stops above were sampled from the PDF artwork.

---

## 5. Spacing scale — identical to S1

Base unit 4px, with 2px sub-steps. Use these for padding, gaps, margins **and** vertical space
between sections — there are no Veeam-specific spacing values.

| Token | px | | Token | px |
|---|---|---|---|---|
| spacing-none | 0 | | spacing-3xl | 24 |
| spacing-xxs | 2 | | spacing-4xl | 32 |
| spacing-xs | 4 | | spacing-5xl | 40 |
| spacing-sm | 6 | | spacing-6xl | 48 |
| spacing-md | 8 | | spacing-7xl | 64 |
| spacing-lg | 12 | | spacing-8xl | 80 |
| spacing-xl | 16 | | spacing-9xl | 96 |
| spacing-2xl | 20 | | spacing-10xl | 128 |
| | | | spacing-11xl | 160 |

**Section spacing:** `spacing-8xl` (80) between page sections, `spacing-9xl` (96) for hero and
feature sections, `spacing-6xl` (48) on mobile. Inside sections, stack blocks with
`spacing-xl` / `spacing-3xl` / `spacing-4xl` / `spacing-6xl`.

> The Veeam PDF's "vertical spacing rules" (8 · 16 · 24 · 32 · 48 · 64 · 80 · 120) are all S1
> steps except 120 — use `spacing-9xl` (96) or `spacing-10xl` (128) instead.

---

## 6. Radius scale — S1 + one Veeam token

| Token | px | | Token | px |
|---|---|---|---|---|
| radius-none | 0 | | radius-xl | 12 |
| radius-xxs | 2 | | radius-2xl | 16 |
| radius-xs | 4 | | radius-3xl | 20 |
| radius-sm | 6 | | radius-4xl | 24 |
| radius-md | 8 | | radius-full | 9999 |
| radius-lg | 10 | | **radius-plate** *(Veeam, plates only)* | **60** |

Buttons use `radius-sm` (6px) — the PDF's 6px button corner is already an S1 step.
Strokes: `stroke-plate` 8px (message plates), `stroke-icon-marketing` 12px (144px icon grid),
`stroke-focus` 2px.

---

## 7. Type scale (numeric)

See [`typography.md`](typography.md) for families, weights and usage.

| Token | Size | Line height | Tracking | Family | PDF source |
|---|---|---|---|---|---|
| display-3xl | 120 | 128 | -2% | Bauhaus | Display 120 |
| display-2xl | 100 | 108 | -2% | Bauhaus | Display 100 |
| display-xl | 60 | 68 | -2% | Bauhaus | Display 60 |
| display-lg | 50 | 60 | -2% | Bauhaus | H1 title 50/60 |
| display-md | 44 | 52 | -1% | Bauhaus | H2 title (PDF prints "55/52") |
| display-sm | 36 | 44 | 0 | Bauhaus | H3 title 36/44 |
| display-xs | 28 | 36 | 0 | Bauhaus | Text 28 – 28/36 |
| text-2xl | 24 | 28 | 0 | Neutral | Text 24 – 24/28 · Eyebrow 24/28 |
| text-xl | 20 | 24 | 0 | Neutral | Text 20 – 20/24 |
| text-lg | 18 | 24 | 0 | Neutral | Text 18 · Body 18/24 |
| text-md | 16 | 24 | 0 | Neutral | Paragraph 16/24 · Body 16/24 |
| text-sm | 14 | 20 | 0 | Neutral | Caption 14/20 |
| text-xs | 12 | 18 | 0 | Neutral | *(S1 carry-over)* |

---

## 8. Layout — grid & containers (identical to S1)

Three breakpoints, each a fixed-margin column grid. Column width fills the content area.

| Breakpoint | Applies from | Design frame | Container | Columns | Gutter | Side margin | Content width |
|---|---|---|---|---|---|---|---|
| Desktop | ≥ 1024px | 1440 viewport | 1280 max | 12 | 32 | 32 | 1216 (col ≈ 72) |
| Tablet | 768 – 1023px | iPad Mini 768 | 768 | 6 | 32 | 32 | 704 |
| Mobile | < 768px | iPhone 375 | 375 | 4 | 16 | 16 | 343 |

| Token | px |
|---|---|
| container-max-width-desktop | 1280 |
| container-padding-desktop / -mobile | 32 / 16 |
| grid-gutter-desktop / -mobile | 32 / 16 |
| paragraph-max-width | 720 |
| width-xxs … width-6xl | 320 · 384 · 480 · 560 · 640 · 768 · 1024 · 1280 · 1440 · 1600 · 1920 |
| button-min-width-lg / -sm *(Veeam)* | 190 / 166 |
| button-fixed-width *(Veeam)* | 285 |

Responsive CSS aliases switch automatically: `--container-padding`, `--grid-gutter` (16 → 32 at
768px) and `--grid-columns` (4 → 6 → 12). Container grid presets inside the 1280 container (S1):
12, 6, 5, 3 and 2 columns.

> **Not used:** the Veeam PDF's web grid (1260px container, 75px columns, 30px gutter, 15px
> padding, 2 columns on mobile). We keep the S1 grid so every Saltbox project shares one grid.

### Banner sizes (PDF p.45)

| Banner | Size | Notes |
|---|---|---|
| Hero banner | 1920 × 538 | Static background, light scheme preferred, 1–2 CTAs, standard font size |
| Hero with video | 1920 × 1180 | Video autoplays below headline; 1–2 CTAs |
| New Visitors | 252 × 364 | Animated background allowed, 1–2 CTAs |
| Menu banner | 915 × 128 | Background image 1260px wide (per PDF), one CTA |

---

## Status

- From the PDF: brand palette, web & presentation palettes, button spec, banner sizes,
  type sizes, plate radius/stroke, icon grid.
- Derived (flagged in bold vs. plain above): intermediate ramp steps; line-heights for
  Display 120/100/60 (the PDF gives sizes only); `text-xs`; PRISM gradient stops (sampled).
- Deliberately not used: the PDF web grid and its 120px spacing step — S1's grid and spacing
  scale apply.
- Open question: the PDF prints **H2 as "55/52"** — a line-height smaller than the size and a
  size larger than H1 (50). We use **44/52** (fits between H1 50/60 and H3 36/44). Confirm
  with Veeam's Creative team.

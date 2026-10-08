# Typography

Veeam's corporate typeface is **ES Build**, which ships as three sets. Like S1, the system uses
one family for headings and another for body — the S1 rule "Display = headings font, Text =
body font" carries over directly.

| Role | Family | Token | CSS name | Files |
|---|---|---|---|---|
| **Headings & display** (H1–H4, Display 120/100/60, hero, pull quotes, prices, metrics) | **ES Build Bauhaus** ("Full Bauhaus" set) | `--font-family-display` | `'ES Build Bauhaus'` | `fonts/es-build-bauhaus/` |
| **Subheads, body copy & all UI** (paragraphs, labels, buttons, nav, forms, tables, captions, eyebrows) | **ES Build Neutral** | `--font-family-body` | `'ES Build Neutral'` | `fonts/es-build-neutral/` |
| **PowerPoint / Office headings & subheads** | **ES Build** (standard set) | `--font-family-brand` | `'ES Build'` | `fonts/es-build/` |

Each family: Regular 400, Medium 500, SemiBold 600, Bold 700 — each with an italic.
Load all three with one line: `<link rel="stylesheet" href="fonts/fonts.css">`.

### Why two families (from the PDF)

- **ES Build Bauhaus** drops the *ears and spurs* from the letterforms. That simplification
  makes it legible yet sophisticated at headline sizes — *"Use this Bauhaus Set for headlines or
  display text."* Its single-story `y` and geometric `a` are the look of the brand.
- **ES Build Neutral** keeps the full letterforms. Ears and spurs matter for accessibility in
  smaller copy — *"Use this Neutral Set for subheads and body copy."*
- **PowerPoint:** ES Build for headings and subheads, ES Build Neutral for body. **Bauhaus is
  never used in PowerPoint.**

### Fallbacks

| Situation | Use |
|---|---|
| Web (default stack) | `'ES Build …', 'Source Sans 3', 'Source Sans Pro', Arial, Tahoma, sans-serif` |
| Google Fonts environment (e.g. no custom-font upload) | Source Sans Pro — Light / Regular / Bold |
| MS Office apps when ES Build isn't installed | Tahoma Regular / Bold |
| Partner / co-branding request for a system font (rare) | Arial — Regular, Italic, Bold |
| Japanese | Meiryo (Kozuka for print) |
| Simplified / Traditional Chinese | Microsoft Yahei (SimHei / Microsoft JhengHei for print; Tahoma for e-cards) |
| Thai | Noto Sans Thai (Tahoma for PPT, banners, e-cards) |
| Korean | Noto Sans KR (Malgun Gothic for print, PPT, banners; Tahoma for e-cards) |

> **License:** ES Build is a licensed Veeam typeface. Use it only for Veeam work, keep this repo
> private, and never upload the font files to a public site or CDN other than the client's own.

---

## Type scale

Same naming pattern as S1 (`Display {size}` for headings, `Text {size}` for body), with the
Veeam sizes from the PDF's web *Title styles* and *Paragraph styles*.

### Display — ES Build Bauhaus

| Style | Size / line height | Tracking | Veeam name | Use |
|---|---|---|---|---|
| **Display 3xl** | 120 / 128 | -2% | Display 120 | Hero headline on campaign/event pages, LED screens. One per page. |
| **Display 2xl** | 100 / 108 | -2% | Display 100 | Hero headline alternative; big numbers |
| **Display xl** | 60 / 68 | -2% | Display 60 | Landing-page hero (most common), banners |
| **Display lg** | 50 / 60 | -2% | **H1** | Page title on content and storefront pages |
| **Display md** | 44 / 52 | -1% | **H2** | Section headings |
| **Display sm** | 36 / 44 | 0 | **H3** | Sub-section headings, PDP product name on mobile |
| **Display xs** | 28 / 36 | 0 | Text 28 (H4) | Card-group titles, modal titles, prices |

Line heights for Display 120/100/60 are not in the PDF; they're set to ~1.07–1.13× for tight,
confident headlines. H2 is printed as "55/52" in the PDF — we use 44/52 (see `tokens.md`).

### Text — ES Build Neutral

| Style | Size / line height | Veeam name | Use |
|---|---|---|---|
| **Text 2xl** | 24 / 28 | Text 24 · **Eyebrow** | Eyebrows (UPPERCASE), lead-in subheads, H5 |
| **Text xl** | 20 / 24 | Text 20 | Lead paragraphs, card titles, H6 |
| **Text lg** | 18 / 24 | Body 18/24 | **Marketing body copy** (default on landing pages) |
| **Text md** | 16 / 24 | Paragraph / Body 16/24 | **Default UI & storefront body**, inputs, large buttons |
| **Text sm** | 14 / 20 | Caption 14/20 | Captions, labels, table cells, small buttons, hints |
| **Text xs** | 12 / 18 | — *(S1)* | Legal, badges, timestamps. Never smaller. |

*Body bold 18/24* and *Body bold 16/24* = `Text lg/Semibold` and `Text md/Semibold`.

### Weights

| Weight | CSS | Use |
|---|---|---|
| Regular | 400 | Body, descriptions, placeholders |
| Medium | 500 | Labels, nav items, table headers, tags |
| SemiBold | 600 | **Headings (default)**, buttons, eyebrows, active nav, card titles |
| Bold | 700 | Display 120/100 when extra punch is needed, metric values |

Style names follow S1: `{Display|Text} {size}/{weight}` — e.g. `Display lg/Semibold`,
`Text sm/Medium`.

---

## Rules

### Headlines
- Headings are **ES Build Bauhaus SemiBold** in sentence case. Never all caps (eyebrows and
  buttons are the only uppercase text).
- **Gradient words:** only *'Securiti'* or *'Agent Commander'* may take the brand hero
  gradient (`.vds-text-gradient`), depending on the message. Never a whole sentence.
- **Green headlines** may be used to keep a layout's green share at 30–40% — only at Display
  sizes, SemiBold or heavier (Viridis on white is 2.0:1). For green text that must pass AA, use
  `text-secondary-brand` (`#007F49`).
- In *"securiti / Agent Commander"* lockups, 'securiti' is always smaller than 'Agent Commander'.
- It's **Securiti**, never "Security" — double-check every time.

### Messaging (PDF p.11 — confirm relevance with Veeam Creative before use)
- Primary: **The Data & AI Trust Company** ('and' or '&'; 'AI' / 'Trust' may break to a new line).
- Secondary 1: **Command your Data and AI Agents.** (wrap after '&'/'and' if needed)
- Secondary 2: **Agent Commander — Detect AI. Protect AI. Undo AI.**

### Eyebrows & buttons
- Eyebrow: `Text 2xl/Semibold` UPPERCASE in `text-secondary-brand` (`.vds-eyebrow`);
  `.vds-eyebrow--sm` (14/20, +4% tracking) in dense UI.
- Buttons: `Text md/Semibold` (large) or `Text sm/Semibold` (small), UPPERCASE, +2% tracking.

### Responsive
- Display sizes step down on mobile (< 768px): 120/100 → 60, 60 → 36, H1 50 → 36, H2 44 → 28.
- Text sizes stay the same across breakpoints.

### Accessibility
- Body text at least `Text md` (16px) for reading; `Text lg` on marketing pages.
- Don't override line heights; don't track tighter than -2%.
- Contrast ≥ 4.5:1 for `Text sm` and smaller; 3:1 for Display sizes.
- Emphasize with weight, not italics or underline.

---

## Component mapping (same roles as S1)

| Component | Style |
|---|---|
| Hero headline | Display xl/Semibold (Display 3xl on event pages) |
| Page title (H1) | Display lg/Semibold |
| Section heading (H2) | Display md/Semibold |
| Card / tile title | Text xl/Semibold in **Bauhaus** (`.vds-card__title`) |
| Product name on PDP | Display md/Semibold (Display sm on mobile) |
| Price | Display xs/Semibold, `text-brand-primary` (Navy) |
| Eyebrow | Text 2xl/Semibold UPPERCASE (`.vds-eyebrow`) |
| Body (marketing) | Text lg/Regular |
| Body (UI, storefront) | Text md/Regular |
| Form label | Text sm/Medium |
| Input text / placeholder | Text md/Regular |
| Hint / error | Text sm/Regular |
| Button (large / small) | Text md/Semibold · Text sm/Semibold, UPPERCASE |
| Nav item | Text sm/Medium (active: Semibold) |
| Table header / cell | Text xs/Medium · Text sm/Regular |
| Badge | Text xs/Medium |
| Caption | Text sm/Regular |
| Metric value | Display md/Semibold, Bauhaus |

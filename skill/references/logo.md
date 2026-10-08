# Logo

The Veeam logo is a bold **wordmark set within a cropped background plate**. Behind the
wordmark, the **Bounce Mark** (the "V" chevron) adds depth. Always use the files — never retype
"veeam" in ES Build or redraw the plate.

Files live in [`../assets/logos/`](../assets/logos/). The SVGs were extracted as vectors from the
PDF; the PNGs (favicon, app icon, Bounce Mark) were rendered from it at 300 dpi.

| File | What it is | Use on |
|---|---|---|
| `veeam-logo-primary.svg` | **Full Color, main version** — Viridis plate, white wordmark, Bounce Mark at 25% | White and light grounds, gradients (with white beneath), logo **≥ 200px wide** |
| `veeam-logo-clean.svg` | **Full Color, clean version** — no Bounce Mark | Logo **under 200px wide** (headers, footers, favicon-adjacent UI), Viridis grounds |
| `veeam-logo-mono-black.svg` | Monochrome black — wordmark knocked out of a black plate | One-color print, grey/neutral grounds |
| `veeam-logo-mono-white.svg` | Monochrome white — wordmark knocked out of a white plate | Black, dark and photo grounds; "Inversion" on Viridis |
| `veeam-favicon.png` | Square favicon, green gradient, white chevron | Browser tab (`<link rel="icon">`) |
| `veeam-app-icon.png` | Rounded-square app icon | App tiles, PWA manifest |
| `veeam-social-avatar.png` | Circular social avatar | Social profiles |
| `veeam-bounce-mark.png` | **Bounce Forward Mark** — low-poly glass "V" with glowing nodes | Key visuals, hero imagery (see `brand-elements.md`) |

### Primary vs. secondary (PDF p.38)
- **Primary** logo: Bounce-mark opacity 25%.
- **Secondary** logo: Bounce-mark opacity 20% — *use the secondary/clean logo when the logo
  width is under 200px.*
- Logo variants shown on: **Grey Mineral** (`#505861`), **Viridis** (`#00D15F` — use the white
  plate "Inversion"), **Black**.

### Colors

| Part | Value |
|---|---|
| Plate | Viridis `#00D15F` (Pantone 2420 C) |
| Bounce Mark in plate | Viridis 20% `#40DB87` (Pantone 2268 C) |
| Wordmark | White `#FFFFFF` |
| Monochrome | Black `#000000` / White `#FFFFFF` |

## Usage

**Do**
- Keep the logo clearly legible. On the brand gradient, place it over the **white** area of the
  gradient (the gradient starts white for exactly this reason) or use a white highlight beneath it.
- If contrast is still insufficient, switch to the inverted (white) logo.
- Keep clear space around the plate of at least the height of the wordmark's "v".
- In web headers use the clean logo at ~112px wide (≈ 34px tall).
- Co-branding (booths, partner pages): **95% Veeam / 5% partner**; use the Veeam + Partner
  horizontal lockup from Veeam's Quick Logo Reference Guide.

**Don't**
- Recolor the plate, use another green, or put the full-color logo on a busy area of the gradient.
- Stretch, rotate, outline, add shadows or effects, or crop the plate.
- Retype the wordmark or rebuild the Bounce Mark.
- Use the primary (Bounce Mark) version below 200px wide.

> Full logo guidelines live on Veeam's **Brand Design SharePoint**. Before publishing, confirm
> you're on the latest approved brand style: Veeam.CreativeTeam.Managers@veeam.com.

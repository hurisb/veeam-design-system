# Brand elements — key visual, motion, imagery & best practices

The "Veeam + Securiti AI" visual system is a **transitional style**: a bridge between the green
*Radical Resilience* identity and an upcoming large-scale rebrand, created to mark the
integration of Veeam and Securiti AI. Confirm you're working with the latest approved style
before starting: **Veeam.CreativeTeam.Managers@veeam.com**.

## Key visual (PDF p.6–7)

Every design includes **the brand gradient** plus **one of**:

1. **The Wave passing through the Bounce Mark** (full version), or
2. **The Wave only**, or
3. **Wireframe texture** (when the Bounce Mark doesn't fit).

| Element | What it is | Rules |
|---|---|---|
| **Gradient** (`--gradient-brand`) | Bright green → cyan → blue, with white to create contrast (typically beneath the logo) | Linear or radial. White goes beneath the logo. |
| **Bounce Mark** (`veeam-bounce-mark.png`) | Glass-like low-poly wireframe "V" with glowing nodes — intelligent data flow | Stand-alone mark *or* textural background where the low-poly structure emerges. A **Bounce Mark reflection** may sit below it. |
| **Wave** | Digital wave conveying motion and rhythm | Passes through the Bounce Mark in the primary visual; may be used alone on the gradient. Fades smoothly to transparency at the edges — no abrupt cuts. May extend beyond the layout. Across panels/carousels, keep the wave continuous. |
| **Patterns** (web, p.43) | Low-poly wireframe triangles on blue/green gradient | Use as section backgrounds and banner art. |

> Layer order: gradient background → wave / Bounce Mark → white area or blurred white plate →
> logo, tagline, messaging. Use the PDF's templates as the base for asset creation (source
> links are on PDF p.90).

## Green balance (PDF p.13, 35)
- Green must stay clearly visible: **never below 30%** of the composition, **ideal 35–40%**.
- Green headlines may reinforce it.
- On the web: the green comes from gradients, imagery and headlines. **Buttons stay Electric
  Azure** on light surfaces.

## Text on gradients & busy backgrounds (PDF p.13, 36)
- Always check readability. Add **blurred white plates** under text (`.vds-plate-blur`) or put
  text on a contrasting background.
- **Digital (RGB):** white text usually reads better over the light blue-green part.
- **Print (CMYK):** deep blue text (Navy `#0E0D72`) reads better over the white-green part.

## Imagery (PDF p.13, 43)
- Place photos inside **Bounce Mark counter-shape masks** (the angled/clipped frame) to
  integrate them with the system.
- Network/graph imagery: light nodes and connector lines, avatar circles, pill labels
  ("Structured Data", "AI Agents", "GDPR").
- Product UI on screens in real environments (data centers, laptops).
- Social carousels: one seamless composition flowing across slides.

## Illustration (PDF p.32–33)
- **Flat, two-dimensional** — shapes face the viewer; never isometric.
- **Viridis dominates; Sky is the usual complement.** Secondary palette in subtle ways for depth.
- **Never use Ignis (red)** in illustrations — it's reserved for alerts and watch-outs.
- Similar optical size, consistent shapes/textures/color treatments, balanced weight.

---

## Motion & plates (PDF p.47–54)

| Element | Spec | CSS |
|---|---|---|
| **Plates & shapes** | Corner radius **60px**; stroke **8px** (may vary with scaling). Text aligned to its content — icon left, visual right. | `--radius-plate`, `--stroke-plate`, `.vds-plate` |
| **Message on a plate — option 1** | Red plate, 60px radius, white text right of a white icon, subtle drop shadow | `.vds-plate--solid` |
| **Message on a plate — option 2** | White plate, 60px radius, 8px red outline, red text & icon | `.vds-plate` |
| **Message on a rounded plate (overlay)** | Translucent glass plate with a colorized stroke separated from the plate; more urgent = less transparent + extra outline | `.vds-plate--glass` |
| **Glass overlays** | Glass = Agent Commander "doing the work" (detecting issues). More complex info → more diffraction/blur. Tint adds context. | `backdrop-filter: blur()` |
| **Agent Commander dot patterns** | Option 1: gradient background with inner-circle opacity. Option 2: overlay on footage or white, with blinking threat circles. | — |
| **Timeline ("busbar")** | White containers with blue stroke that turn **green when connected**; 60px radius; plate 1200 × 1200 | `border-secondary-brand` for "connected" |
| **Diagram animation** | Gradient on all shapes that belong to one system; gradients only on interacting shapes (otherwise they signal usage/risk). **Icon color always matches its plate outline.** Highest contrast wins. | — |
| **Toggle animation** | Different transparency and darker tint on white tables; blur increases during state transitions | — |

**Color is contextual:** blue/purple = neutral · **green = good** · red/orange = bad / problem.

Web motion defaults (from the S1 baseline): transitions 200–400ms on `transform`/`opacity`
with `cubic-bezier(0.16, 1, 0.3, 1)`; respect `prefers-reduced-motion`.

---

## Other applications (summary)
- **LED screens / onsite branding / collaterals:** same key visual; the *Data Command Graph*
  diagram may accompany primary graphics (check messaging first).
- **Booths:** 95% Veeam / 5% partner; horizontal lockup on booths; vertical lockup only on
  counters when just the front panel is branded.
- **Vehicles:** gradient blue→green or green→blue front-to-back; mirrored Bounce Mark on both
  sides; centered on hood/bumper/trunk axis; review in three-quarter view.
- **Light theme** variants exist for all of the above (PDF p.22–25).

## Pre-publish checklist (PDF p.35–36)
- [ ] Brand gradient present + Wave/Bounce Mark/wireframe texture
- [ ] Green ≥ 30% of the composition (35–40% ideal)
- [ ] Logo clearly legible (white beneath it or inverted logo)
- [ ] Wave fades smoothly at the edges
- [ ] Text readable over the gradient (plate or contrasting ground)
- [ ] "Securiti" spelled correctly — not "Security"
- [ ] Messaging approved by Veeam Creative
- [ ] RGB for screen, CMYK for print

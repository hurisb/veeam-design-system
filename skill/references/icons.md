# Icons

Veeam uses **two kinds of icons**. Pick by context.

## 1. UI icons (product UI, storefronts, forms) — Untitled UI line, from S1

Inside interfaces we keep the S1 convention: **Untitled UI PRO line icons** — 24px grid, 2px
stroke, round caps and joins. The Veeam PDF doesn't define a UI icon set, and these match the
geometry of the arrows and checks shown in Veeam's web UI elements.

- Refer to icons by Untitled UI names: `arrow-right`, `search-lg`, `shopping-cart-01`,
  `check`, `x-close`, `chevron-down`, `alert-circle`, `shield-tick`, `cloud-01`, `server-01`.
- **CTA arrows:** Veeam tertiary buttons and many primary CTAs carry a trailing `arrow-right` (→).
- Color with `fg-*` tokens (`currentColor`): `fg-quaternary` inside inputs, `fg-secondary` for
  meaningful icons, `fg-brand-primary` for active/brand, `fg-*-primary` for states.
- Sizes: 16px (badges, dense rows), 20px (buttons, inputs), 24px (navigation, featured).

> Untitled UI PRO is licensed and not included in this repo — use the team library. The
> examples use a few hand-drawn inline SVGs in the same style.

## 2. Marketing icons — Veeam bespoke set

Bespoke to the Veeam identity and rooted in the Veeam Mark.

| Rule | Value |
|---|---|
| Signature | The Veeam Mark's **clipped 45° corner** appears at least once in every icon |
| Grid | 2" × 2" / **144px** |
| Line weight | **12pt / 12px**, uniform within each icon and across the set |
| Minimum size | **100 × 100px** |
| Color | Solid, or gradient **Gradient blue 1 `#008EE7` → Mint `#32F26F`** (`--gradient-icon`) — legible on white and dark |
| Examples | Artificial Intelligence, Bulb, Team, Multicloud mobility, Backup solution, Ransomware: Automation, Cloud Recovery Orchestration, Strategic advisory, Brain, Globe protected, Government, Money/finance, Infection, Tick |

Get the full set from Veeam's **Icons Library** (credentials are in the source PDF in
`resources/` — never paste them into code, tickets or chat).

**Technical icons** (for technical diagrams — backup server, repository, data mover, KVM hosts…)
come from the separate **Technical Icons Library**, in dark- and white-background versions.

## 3. UI illustration icons (web, PDF p.42)

Glassy, layered illustrations (radar target, nested squares, alert node, bug network) on white
or PRISM dark. Use them as feature visuals, not as inline UI icons.

## Rules
- Never mix Untitled UI line icons and Veeam marketing icons in the same component.
- Never redraw or approximate a Veeam marketing icon — request it from Veeam Creative.
- Ignis red appears in icons only to signal a threat (e.g. a red square on a radar target).
- An icon-only control always needs an accessible label.

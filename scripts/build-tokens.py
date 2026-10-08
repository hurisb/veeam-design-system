#!/usr/bin/env python3
"""
Veeam Design System — token build script (single source of truth).

Every token value lives in this file. Running it regenerates:

  tokens/tokens.json              W3C design-token (DTCG) format — Figma Tokens Studio, Style Dictionary
  tokens/veeam-tokens.css         CSS custom properties (light + opt-in dark theme)
  tokens/_veeam-tokens.scss       SCSS variables + Bootstrap 4 overrides for SFCC SFRA cartridges
  tokens/tailwind.preset.js       Tailwind CSS preset (v3 `presets: []`)
  tokens/pwa-kit-theme.js         Chakra UI theme for SFCC Composable Storefront (PWA Kit)
  fonts/fonts.css                 @font-face rules for ES Build, ES Build Neutral, ES Build Bauhaus
  skill/references/color-variables.md   semantic color tables (light + dark)

Usage (Python 3.8+, no dependencies):

    python3 scripts/build-tokens.py

Structure mirrors the S1 design system: the same spacing / radius scale, the
same semantic token names (text-*, border-*, fg-*, bg-*), the same type-scale
naming (Display 3xl…xs, Text 2xl…xs). Values come from the Veeam Inflection
Design System Guidelines PDF (version 052226). Values marked `derived` in
comments were interpolated to complete a ramp; everything else is from the PDF.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STEPS = ["25", "50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]

# ---------------------------------------------------------------------------
# 1. PRIMITIVES  (PDF = value printed in the guideline; others derived)
# ---------------------------------------------------------------------------
RAMPS = {
    # Neutral, light theme. PDF web neutrals: #F9F9F9 #F0F0F0 #ADACAF #505861 #232323,
    # PPT neutrals: #DBDEE1 #1D1F2A.
    "gray": {
        "25": "#fcfcfc", "50": "#f9f9f9", "100": "#f0f0f0", "200": "#dbdee1",
        "300": "#c3c6cb", "400": "#adacaf", "500": "#6e737b", "600": "#505861",
        "700": "#3b4049", "800": "#232323", "900": "#1d1f2a", "950": "#121318",
    },
    # Neutral, dark theme — navy-tinted to sit on the PRISM dark background (#0F172C, sampled).
    "gray-dark": {
        "25": "#fafafb", "50": "#f5f6f8", "100": "#eceef3", "200": "#e1e4ec",
        "300": "#c8ccd8", "400": "#959cb0", "500": "#7d859c", "600": "#5a637d",
        "700": "#34405e", "800": "#1e2a47", "900": "#162036", "950": "#0f172c",
    },
    # PRIMARY — Electric Azure. PDF: #E3EEFE (50), #3700FF (600, CTA default),
    # #283E8E (700, CTA hover / Gradient blue 2), #1D1E3F (800, Gradient blue 3),
    # #0E0D72 (900, Navy Blue "Dark Text").
    "brand": {
        "25": "#f5f8fe", "50": "#e3eefe", "100": "#ccd9fe", "200": "#a9b6ff",
        "300": "#8a8dff", "400": "#6b5cff", "500": "#4d2eff", "600": "#3700ff",
        "700": "#283e8e", "800": "#1d1e3f", "900": "#0e0d72", "950": "#0a0a45",
    },
    # SECONDARY — Viridis green. PDF: #E1F4EC #9CFFA3 #4AFF9C #32F26F (Mint)
    # #00D15F (Viridis) #009277 (hover on dark) #007F49 #02613F.
    "green": {
        "25": "#f2fdf6", "50": "#e1f4ec", "100": "#c6f7da", "200": "#9cffa3",
        "300": "#4aff9c", "400": "#32f26f", "500": "#00d15f", "600": "#009277",
        "700": "#007f49", "800": "#02613f", "900": "#014a30", "950": "#002e1e",
    },
    # Error — PDF system red #ED2B3D at 500.
    "error": {
        "25": "#fffafa", "50": "#fef2f3", "100": "#fde3e5", "200": "#fbc7cc",
        "300": "#f69aa3", "400": "#f15f6d", "500": "#ed2b3d", "600": "#d01a2c",
        "700": "#ad1524", "800": "#8c1520", "900": "#74161f", "950": "#400a0f",
    },
    # Warning — PDF Suma #FE8A25 (500), negative-gradient orange #FF6900 (600).
    "warning": {
        "25": "#fffaf5", "50": "#fff4ea", "100": "#ffe6cf", "200": "#ffcd9f",
        "300": "#feb06a", "400": "#fe9c45", "500": "#fe8a25", "600": "#ff6900",
        "700": "#c2510a", "800": "#9f3f0a", "900": "#80350c", "950": "#451905",
    },
}
# Success = the green ramp ("Green is good" — PDF p.52).
RAMPS["success"] = dict(RAMPS["green"])

# Named Veeam palette (all from the PDF, pages 8, 39, 58).
PALETTE = {
    "viridis": "#00d15f",          # Veeam green — logo plate, brand presence
    "viridis-20": "#40db87",       # Bounce-mark tint inside the logo
    "mint": "#32f26f",
    "sky": "#57e0ff",
    "electric-azure": "#3700ff",   # CTA / primary action
    "casia": "#8e71f4",
    "sol": "#ffd839",
    "suma": "#fe8a25",
    "ignis": "#ed2b3d",            # alerts & watch-outs only — never decorative
    "navy-blue": "#0e0d72",        # "Dark Text"
    "cyan": "#1ca8dd",             # PPT main
    "ocean": "#0058ff",            # PPT gradient end
    "lime": "#97d700",             # PPT main
    "orange": "#ff6900",           # PPT main / negative
    "deep-navy": "#002060",        # PPT main
    "deep-teal": "#002833",        # web blue family
    "gradient-green": "#00ff5e",
    "gradient-blue-1": "#008ee7",
    "gradient-blue-2": "#283e8e",
    "gradient-blue-3": "#1d1e3f",
    "grey-mineral": "#505861",
    "sand": "#cecbb8",
    "cream": "#fcf8eb",
    "ice": "#eef4f6",              # tertiary-button hover
    "white": "#ffffff",
    "black": "#000000",
}

# ---------------------------------------------------------------------------
# 2. BRAND ALIASES — the "primary-color / secondary-color" layer
# ---------------------------------------------------------------------------
BRAND_ALIASES = [
    ("color-primary", "#3700ff", "Electric Azure — buttons, links, active states, focus"),
    ("color-primary-hover", "#283e8e", "Primary hover / focus / active (PDF p.41)"),
    ("color-primary-subtle", "#e3eefe", "Light primary surface"),
    ("color-secondary", "#00d15f", "Viridis — brand presence (30–40% of a layout), logo, dark-theme CTA"),
    ("color-secondary-hover", "#009277", "Secondary hover"),
    ("color-secondary-subtle", "#e1f4ec", "Light secondary surface"),
    ("color-tertiary", "#57e0ff", "Sky — Viridis' complement in illustration and diagrams"),
    ("color-accent", "#8e71f4", "Casia — supplementary accent"),
    ("color-highlight", "#ffd839", "Sol — highlight; fills only, never text on white"),
    ("color-text-dark", "#0e0d72", "Navy Blue — brand dark text (headlines on light / gradient print)"),
    ("color-success", "#00d15f", "Good / connected / complete"),
    ("color-warning", "#fe8a25", "Caution"),
    ("color-error", "#ed2b3d", "Ignis — alerts, problems, destructive"),
    ("color-neutral-ink", "#1d1f2a", "Default text ink"),
    ("color-surface", "#ffffff", "Default page surface"),
    ("color-surface-dark", "#0f172c", "PRISM dark-theme background"),
]

# ---------------------------------------------------------------------------
# 3. SEMANTIC TOKENS — same names & roles as S1; (light alias, dark alias, use)
#    Aliases: "<ramp>-<step>", "white", "alpha-black-8".
# ---------------------------------------------------------------------------
SEMANTIC = [
    # Text — neutral
    ("text-primary", "gray-900", "gray-dark-50", "Headings, titles, prominent labels"),
    ("text-primary_on-brand", "white", "gray-dark-50", "Primary text on solid brand backgrounds"),
    ("text-secondary", "gray-700", "gray-dark-300", "Labels, section headings"),
    ("text-secondary_hover", "gray-800", "gray-dark-200", "Secondary text, hover"),
    ("text-secondary_on-brand", "brand-200", "gray-dark-300", "Secondary text on brand backgrounds"),
    ("text-tertiary", "gray-600", "gray-dark-400", "Body/supporting text, descriptions"),
    ("text-tertiary_hover", "gray-700", "gray-dark-300", "Tertiary text, hover"),
    ("text-tertiary_on-brand", "brand-200", "gray-dark-400", "Tertiary text on brand backgrounds"),
    ("text-quaternary", "gray-500", "gray-dark-400", "Subtle, low-contrast text (footer headings)"),
    ("text-quaternary_on-brand", "brand-300", "gray-dark-400", "Quaternary text on brand backgrounds"),
    ("text-white", "white", "white", "Always-white text"),
    ("text-placeholder", "gray-500", "gray-dark-500", "Input placeholders"),
    # Text — brand & semantic
    ("text-brand-primary", "brand-900", "gray-dark-50", "Navy brand headings (pricing headers, hero on light)"),
    ("text-brand-secondary", "brand-700", "gray-dark-300", "Brand accents, subheadings"),
    ("text-brand-secondary_hover", "brand-800", "gray-dark-200", "Brand secondary text, hover"),
    ("text-brand-tertiary", "brand-600", "green-400", "Links, metric numbers (Electric Azure)"),
    ("text-brand-tertiary_alt", "brand-600", "green-400", "Link buttons / tertiary CTA"),
    ("text-secondary-brand", "green-700", "green-400", "VEEAM: green headline/eyebrow text that must pass contrast"),
    ("text-on-brand-solid", "white", "gray-800", "VEEAM: label on bg-brand-solid (white on azure; ink on green in dark)"),
    ("text-on-brand-solid_hover", "white", "white", "VEEAM: label on bg-brand-solid_hover"),
    ("text-error-primary", "error-600", "error-400", "Error messages"),
    ("text-warning-primary", "warning-700", "warning-400", "Warning text (700 in light for contrast)"),
    ("text-success-primary", "success-700", "success-400", "Success text (700 in light for contrast)"),
    # Border
    ("border-primary", "gray-300", "gray-dark-700", "High-contrast: inputs, button groups, checkboxes"),
    ("border-secondary", "gray-200", "gray-dark-800", "Default: cards, tables, dividers"),
    ("border-secondary_alt", "alpha-black-8", "gray-dark-800", "Floating menus (dropdowns, notifications)"),
    ("border-tertiary", "gray-100", "gray-dark-800", "Low-contrast: subtle dividers, chart axes"),
    ("border-brand", "brand-600", "green-500", "Active/focused inputs, selected states, focus ring"),
    ("border-brand_alt", "brand-600", "gray-dark-700", "Brand border → gray in dark (banners, footers)"),
    ("border-secondary-brand", "green-500", "green-500", "VEEAM: green accent rule (card top borders, timelines 'connected')"),
    ("border-error", "error-500", "error-400", "Error borders"),
    ("border-error_subtle", "error-300", "error-500", "Subtle error borders"),
    # Foreground (icons, indicators)
    ("fg-primary", "gray-900", "white", "Highest-contrast icons"),
    ("fg-secondary", "gray-700", "gray-dark-300", "High-contrast icons"),
    ("fg-secondary_hover", "gray-800", "gray-dark-200", "Secondary icons, hover"),
    ("fg-tertiary", "gray-600", "gray-dark-400", "Medium-contrast icons"),
    ("fg-tertiary_hover", "gray-700", "gray-dark-300", "Tertiary icons, hover"),
    ("fg-quaternary", "gray-400", "gray-dark-600", "Low-contrast: button/help/input icons"),
    ("fg-quaternary_hover", "gray-500", "gray-dark-500", "Quaternary icons, hover"),
    ("fg-white", "white", "white", "Always-white icons"),
    ("fg-brand-primary", "brand-600", "green-500", "Primary brand icons, featured icons, progress bars"),
    ("fg-brand-primary_alt", "brand-600", "gray-dark-300", "Brand icon → gray in dark (active tabs)"),
    ("fg-brand-secondary", "green-500", "green-400", "Brand accents, arrows, 'good' indicators"),
    ("fg-brand-secondary_alt", "brand-500", "gray-dark-600", "Brand → gray in dark (brand buttons)"),
    ("fg-error-primary", "error-600", "error-500", "Primary error icons"),
    ("fg-error-secondary", "error-500", "error-400", "Input error icons, negative charts"),
    ("fg-warning-primary", "warning-600", "warning-500", "Primary warning icons"),
    ("fg-warning-secondary", "warning-500", "warning-400", "Secondary warning icons"),
    ("fg-success-primary", "success-600", "success-500", "Primary success icons"),
    ("fg-success-secondary", "success-500", "success-400", "Dots, online indicators, positive charts"),
    # Background
    ("bg-primary", "white", "gray-dark-950", "Page/card/component backgrounds"),
    ("bg-primary_alt", "white", "gray-dark-900", "Alt primary (→ secondary in dark)"),
    ("bg-primary_hover", "gray-50", "gray-dark-800", "Hover for white-bg components (menu items)"),
    ("bg-primary-solid", "gray-950", "gray-dark-900", "Dark solid: tooltips"),
    ("bg-secondary", "gray-50", "gray-dark-900", "Contrast against white (alternating sections)"),
    ("bg-secondary_alt", "gray-50", "gray-dark-950", "Alt secondary (→ primary in dark): border tabs"),
    ("bg-secondary_hover", "gray-100", "gray-dark-800", "Active nav items, date pickers"),
    ("bg-secondary-solid", "gray-600", "gray-dark-600", "Grey Mineral solid: featured icons, mineral sections"),
    ("bg-tertiary", "gray-100", "gray-dark-800", "Contrast against light bg: toggles"),
    ("bg-quaternary", "gray-200", "gray-dark-700", "Higher contrast: sliders, progress bars"),
    ("bg-overlay", "gray-950", "gray-dark-800", "Modal/dialog backdrop"),
    ("bg-brand-primary", "brand-50", "brand-800", "Light brand surfaces, check icons"),
    ("bg-brand-primary_alt", "brand-50", "gray-dark-900", "Brand fill → secondary in dark (active tabs)"),
    ("bg-brand-secondary", "brand-100", "brand-700", "Featured icons"),
    ("bg-brand-solid", "brand-600", "green-500", "Solid brand: primary buttons, toggles (azure light / green dark)"),
    ("bg-brand-solid_hover", "brand-700", "green-600", "Solid brand, hover"),
    ("bg-brand-section", "brand-800", "gray-dark-900", "Dark brand sections: CTAs, testimonials"),
    ("bg-brand-section_subtle", "brand-700", "gray-dark-950", "Subtle brand section: FAQ"),
    ("bg-secondary-brand", "green-50", "green-950", "VEEAM: light green surface"),
    ("bg-secondary-brand-solid", "green-500", "green-500", "VEEAM: solid Viridis (logo plate, green blocks)"),
    ("bg-tertiary-hover", "palette-ice", "palette-ice", "VEEAM: tertiary/text-button hover fill (#EEF4F6)"),
    ("bg-error-primary", "error-50", "error-950", "Light error fill"),
    ("bg-error-secondary", "error-100", "error-600", "Error featured icons"),
    ("bg-error-solid", "error-600", "error-600", "Solid error: buttons, metrics"),
    ("bg-error-solid_hover", "error-700", "error-500", "Solid error, hover"),
    ("bg-warning-primary", "warning-50", "warning-950", "Light warning fill"),
    ("bg-warning-secondary", "warning-100", "warning-600", "Warning featured icons"),
    ("bg-warning-solid", "warning-600", "warning-600", "Solid warning: featured icons"),
    ("bg-success-primary", "success-50", "success-950", "Light success fill"),
    ("bg-success-secondary", "success-100", "success-600", "Success featured icons"),
    ("bg-success-solid", "success-600", "success-600", "Solid success: featured icons, metrics"),
]

# Chart series (fixed order). Status colors (green/red/orange) are never series colors.
CHART = [("chart-1", "#3700ff"), ("chart-2", "#1ca8dd"), ("chart-3", "#8e71f4"), ("chart-4", "#0e0d72")]

# ---------------------------------------------------------------------------
# 4. GRADIENTS (PDF p.6-8, 28, 39, 58; PRISM stops sampled from p.39)
# ---------------------------------------------------------------------------
GRADIENTS = [
    ("gradient-brand", "linear-gradient(135deg, #ffffff 0%, #00ff5e 22%, #008ee7 52%, #283e8e 78%, #1d1e3f 100%)",
     "Signature key-visual gradient: White → Gradient green → Gradient blue 1/2/3. Every key visual needs it."),
    ("gradient-brand-radial", "radial-gradient(120% 120% at 0% 0%, #ffffff 0%, #00ff5e 25%, #008ee7 55%, #283e8e 80%, #1d1e3f 100%)",
     "Radial version of the brand gradient (white corner sits beneath the logo)."),
    ("gradient-brand-light", "linear-gradient(135deg, #ffffff 0%, #e1f4ec 30%, #9cffa3 60%, #00d15f 100%)",
     "Light green wash for hero areas that carry dark text."),
    ("gradient-hero-text", "linear-gradient(90deg, #00d15f 0%, #1976a6 50%, #3700ff 100%)",
     "PRISM Hero Font — gradient headline words ('Securiti', 'Agent Commander')."),
    ("gradient-tab-active", "linear-gradient(90deg, #15839a 0%, #3700ff 100%)", "PRISM Tab: Active."),
    ("gradient-negative", "linear-gradient(90deg, #e23e57 0%, #a0273a 100%)", "PRISM Negative stats."),
    ("gradient-dark-bg", "linear-gradient(180deg, #0c1427 0%, #1e3c6f 100%)", "PRISM dark-theme background."),
    ("gradient-icon", "linear-gradient(135deg, #008ee7 0%, #32f26f 100%)", "Marketing icons: Gradient blue 1 → Mint."),
    ("gradient-green-cyan", "linear-gradient(90deg, #00d15f 0%, #1ca8dd 100%)", "Presentation gradient (light BG)."),
    ("gradient-casia-azure", "linear-gradient(90deg, #8e71f4 0%, #3700ff 100%)", "Presentation gradient (light BG)."),
    ("gradient-cyan-ocean", "linear-gradient(90deg, #1ca8dd 0%, #0058ff 100%)", "Presentation gradient (light BG)."),
    ("gradient-mint-cyan", "linear-gradient(90deg, #4aff9c 0%, #1ca8dd 100%)", "Presentation gradient for dark BG."),
    ("gradient-alert", "linear-gradient(90deg, #ff6900 0%, #fe8a25 100%)", "Negative gradient (light BG)."),
    ("gradient-alert-dark", "linear-gradient(90deg, #ffd839 0%, #fe8a25 100%)", "Negative gradient for dark BG."),
]

# ---------------------------------------------------------------------------
# 5. TYPOGRAPHY
# ---------------------------------------------------------------------------
FALLBACK = "'Source Sans 3', 'Source Sans Pro', Arial, Tahoma, sans-serif"
FONTS = {
    "font-family-display": f"'ES Build Bauhaus', {FALLBACK}",   # headings & display
    "font-family-body": f"'ES Build Neutral', {FALLBACK}",      # subheads, body, UI
    "font-family-brand": f"'ES Build', {FALLBACK}",             # PowerPoint / Office headings only
}
WEIGHTS = {"regular": 400, "medium": 500, "semibold": 600, "bold": 700}
# name: (size, line-height, letter-spacing em, family, PDF reference)
TYPE = {
    "display-3xl": (120, 128, -0.02, "display", "Display 120"),
    "display-2xl": (100, 108, -0.02, "display", "Display 100"),
    "display-xl": (60, 68, -0.02, "display", "Display 60"),
    "display-lg": (50, 60, -0.02, "display", "H1 title 50/60"),
    "display-md": (44, 52, -0.01, "display", "H2 title (PDF prints 55/52 — see typography.md)"),
    "display-sm": (36, 44, 0, "display", "H3 title 36/44"),
    "display-xs": (28, 36, 0, "display", "Text 28 - 28/36 (H4)"),
    "text-2xl": (24, 28, 0, "body", "Text 24 - 24/28 / Eyebrow 24/28"),
    "text-xl": (20, 24, 0, "body", "Text 20 - 20/24"),
    "text-lg": (18, 24, 0, "body", "Text 18 / Body 18/24"),
    "text-md": (16, 24, 0, "body", "Paragraph 16/24 / Body 16/24"),
    "text-sm": (14, 20, 0, "body", "Caption 14/20"),
    "text-xs": (12, 18, 0, "body", "S1 carry-over (legal, badges) — not in PDF"),
}

# ---------------------------------------------------------------------------
# 6. SPACING / RADIUS / LAYOUT  (S1 scale kept; Veeam additions flagged)
# ---------------------------------------------------------------------------
SPACING = {
    "spacing-none": 0, "spacing-xxs": 2, "spacing-xs": 4, "spacing-sm": 6, "spacing-md": 8,
    "spacing-lg": 12, "spacing-xl": 16, "spacing-2xl": 20, "spacing-3xl": 24, "spacing-4xl": 32,
    "spacing-5xl": 40, "spacing-6xl": 48, "spacing-7xl": 64, "spacing-8xl": 80, "spacing-9xl": 96,
    "spacing-10xl": 128, "spacing-11xl": 160,
    "spacing-section": 120,  # VEEAM: largest vertical-rhythm step (PDF p.44)
}
VSPACE = [8, 16, 24, 32, 48, 64, 80, 120]  # PDF "Vertical spacing rules"
RADIUS = {
    "radius-none": 0, "radius-xxs": 2, "radius-xs": 4, "radius-sm": 6, "radius-md": 8,
    "radius-lg": 10, "radius-xl": 12, "radius-2xl": 16, "radius-3xl": 20, "radius-4xl": 24,
    "radius-plate": 60,  # VEEAM: message plates, glass overlays (PDF p.47)
    "radius-full": 9999,
    "radius-button": 6,  # VEEAM: all CTAs (PDF p.41)
}
STROKE = {"stroke-plate": 8, "stroke-icon-marketing": 12, "stroke-focus": 2}
LAYOUT = {
    "container-max-width": 1260, "container-padding": 15, "grid-gutter": 30, "grid-column": 75,
    "paragraph-max-width": 720,
    "button-min-width-lg": 190, "button-min-width-sm": 166, "button-fixed-width": 285,
}
BREAKPOINTS = {"xs": 0, "sm": 768, "md": 1024, "lg": 1260, "xl": 3840}
GRID_COLUMNS = {"xs": 2, "sm": 6, "md": 12, "lg": 12, "xl": 12}

# Component tokens — buttons (PDF p.41), per surface.
BUTTONS = {
    "light": {  # white / light surfaces
        "primary-bg": "#3700ff", "primary-fg": "#ffffff", "primary-bg-hover": "#283e8e", "primary-fg-hover": "#ffffff",
        "secondary-border": "#3700ff", "secondary-fg": "#3700ff", "secondary-bg-hover": "#283e8e", "secondary-fg-hover": "#ffffff",
        "tertiary-fg": "#3700ff", "tertiary-bg-hover": "#eef4f6", "tertiary-fg-hover": "#3700ff",
    },
    "mineral": {  # Grey Mineral #505861 surfaces
        "primary-bg": "#ffffff", "primary-fg": "#232323", "primary-bg-hover": "#232323", "primary-fg-hover": "#ffffff",
        "secondary-border": "#ffffff", "secondary-fg": "#ffffff", "secondary-bg-hover": "#ffffff", "secondary-fg-hover": "#232323",
        "tertiary-fg": "#ffffff", "tertiary-bg-hover": "#ffffff", "tertiary-fg-hover": "#232323",
    },
    "dark": {  # black / navy surfaces
        "primary-bg": "#00d15f", "primary-fg": "#232323", "primary-bg-hover": "#009277", "primary-fg-hover": "#ffffff",
        "secondary-border": "#00d15f", "secondary-fg": "#00d15f", "secondary-bg-hover": "#009277", "secondary-fg-hover": "#ffffff",
        "tertiary-fg": "#00d15f", "tertiary-bg-hover": "#eef4f6", "tertiary-fg-hover": "#007f49",
    },
}

# ---------------------------------------------------------------------------
# Resolution helpers
# ---------------------------------------------------------------------------
def resolve(alias):
    if alias == "white":
        return "#ffffff"
    if alias == "alpha-black-8":
        return "#00000014"
    if alias.startswith("palette-"):
        return PALETTE[alias[len("palette-"):]]
    ramp, step = alias.rsplit("-", 1)
    return RAMPS[ramp][step]


def var_ref(alias):
    if alias == "white":
        return "var(--color-white)"
    if alias == "alpha-black-8":
        return "rgb(0 0 0 / 8%)"
    if alias.startswith("palette-"):
        return f"var(--color-{alias[len('palette-'):]})"
    return f"var(--color-{alias})"


def px(n):
    return f"{n}px" if n else "0"


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(text)
    print("wrote", rel)


HEADER = "Generated by scripts/build-tokens.py — do not edit by hand. Veeam Design System (built on S1)."

# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
def build_css():
    L = [f"/* {HEADER} */", "", ":root {", "  /* ---- Primitives ---- */"]
    L.append("  --color-white: #ffffff;\n  --color-black: #000000;")
    for name, ramp in RAMPS.items():
        for s in STEPS:
            L.append(f"  --color-{name}-{s}: {ramp[s]};")
    L.append("\n  /* ---- Named Veeam palette ---- */")
    for k, v in PALETTE.items():
        if k not in ("white", "black"):
            L.append(f"  --color-{k}: {v};")
    L.append("\n  /* ---- Brand aliases (primary / secondary / …) ---- */")
    for k, v, _ in BRAND_ALIASES:
        L.append(f"  --{k}: {v};")
    L.append("\n  /* ---- Semantic colors (light) ---- */")
    for k, light, _, _ in SEMANTIC:
        L.append(f"  --{k}: {var_ref(light)};")
    L.append("\n  /* ---- Chart series ---- */")
    for k, v in CHART:
        L.append(f"  --{k}: {v};")
    L.append("\n  /* ---- Gradients ---- */")
    for k, v, _ in GRADIENTS:
        L.append(f"  --{k}: {v};")
    L.append("\n  /* ---- Typography ---- */")
    for k, v in FONTS.items():
        L.append(f"  --{k}: {v};")
    for k, v in WEIGHTS.items():
        L.append(f"  --font-weight-{k}: {v};")
    for k, (size, lh, ls, fam, _) in TYPE.items():
        L.append(f"  --font-size-{k}: {size / 16:g}rem; /* {size}px */")
        L.append(f"  --line-height-{k}: {lh / 16:g}rem; /* {lh}px */")
        L.append(f"  --letter-spacing-{k}: {ls:g}em;")
    L.append("\n  /* ---- Spacing / radius / stroke ---- */")
    for k, v in SPACING.items():
        L.append(f"  --{k}: {px(v)};")
    for v in VSPACE:
        L.append(f"  --vspace-{v}: {v}px;")
    for k, v in RADIUS.items():
        L.append(f"  --{k}: {px(v)};")
    for k, v in STROKE.items():
        L.append(f"  --{k}: {v}px;")
    L.append("\n  /* ---- Layout ---- */")
    for k, v in LAYOUT.items():
        L.append(f"  --{k}: {v}px;")
    for k, v in BREAKPOINTS.items():
        L.append(f"  --breakpoint-{k}: {v}px;")
    L.append("\n  /* ---- Buttons (light surface) ---- */")
    for k, v in BUTTONS["light"].items():
        L.append(f"  --button-{k}: {v};")
    L.append("}\n")

    dark = ["  /* Semantic colors (dark) */"] + [f"  --{k}: {var_ref(d)};" for k, _, d, _ in SEMANTIC]
    dark += ["  --color-surface: var(--color-gray-dark-950);", "  /* Buttons on dark */"]
    dark += [f"  --button-{k}: {v};" for k, v in BUTTONS["dark"].items()]
    L.append("/* Dark theme is opt-in: <html data-theme=\"dark\"> or class=\"theme-dark\" on any container. */")
    L.append("[data-theme=\"dark\"],\n.theme-dark {\n  color-scheme: dark;\n" + "\n".join(dark) + "\n}\n")
    L.append("/* Grey Mineral surface (#505861) — white buttons, per PDF p.41. */")
    L.append("[data-surface=\"mineral\"] {\n" + "\n".join(f"  --button-{k}: {v};" for k, v in BUTTONS["mineral"].items()) + "\n}\n")
    L.append("[data-surface=\"dark\"] {\n" + "\n".join(f"  --button-{k}: {v};" for k, v in BUTTONS["dark"].items()) + "\n}\n")
    write("tokens/veeam-tokens.css", "\n".join(L))

# ---------------------------------------------------------------------------
# Fonts
# ---------------------------------------------------------------------------
def build_fonts():
    fams = [("ES Build", "es-build", "ESBuild"), ("ES Build Neutral", "es-build-neutral", "ESBuildNeutral"),
            ("ES Build Bauhaus", "es-build-bauhaus", "ESBuildFullBauhaus")]
    styles = [("Regular", 400, "normal"), ("Italic", 400, "italic"), ("Medium", 500, "normal"),
              ("MediumItalic", 500, "italic"), ("SemiBold", 600, "normal"), ("SemiBoldItalic", 600, "italic"),
              ("Bold", 700, "normal"), ("BoldItalic", 700, "italic")]
    out = [f"/* {HEADER}\n * ES Build is a licensed Veeam typeface — internal/client use only, do not redistribute.\n"
           " * Usage: Headings & display → 'ES Build Bauhaus' · Subheads, body & UI → 'ES Build Neutral'\n"
           " *        PowerPoint/Office headings → 'ES Build' (Bauhaus is never used in PowerPoint). */\n"]
    for fam, folder, prefix in fams:
        for st, w, style in styles:
            out.append(
                "@font-face {\n"
                f"  font-family: '{fam}';\n"
                f"  src: url('./{folder}/{prefix}-{st}.woff2') format('woff2'),\n"
                f"       url('./{folder}/{prefix}-{st}.woff') format('woff');\n"
                f"  font-weight: {w};\n  font-style: {style};\n  font-display: swap;\n}}\n")
    write("fonts/fonts.css", "\n".join(out))

# ---------------------------------------------------------------------------
# JSON (DTCG)
# ---------------------------------------------------------------------------
def build_json():
    t = {"$description": HEADER, "color": {"base": {"white": {"$type": "color", "$value": "#ffffff"},
                                                    "black": {"$type": "color", "$value": "#000000"}}}}
    for name, ramp in RAMPS.items():
        t["color"][name] = {s: {"$type": "color", "$value": ramp[s]} for s in STEPS}
    t["color"]["palette"] = {k: {"$type": "color", "$value": v} for k, v in PALETTE.items()}
    t["color"]["brand-alias"] = {k: {"$type": "color", "$value": v, "$description": d} for k, v, d in BRAND_ALIASES}

    def ref(a):
        if a == "white":
            return "{color.base.white}"
        if a == "alpha-black-8":
            return "#00000014"
        if a.startswith("palette-"):
            return "{color.palette.%s}" % a[len("palette-"):]
        r, s = a.rsplit("-", 1)
        return "{color.%s.%s}" % (r, s)
    t["semantic"] = {
        "light": {k: {"$type": "color", "$value": ref(l), "$description": d} for k, l, _, d in SEMANTIC},
        "dark": {k: {"$type": "color", "$value": ref(dk), "$description": d} for k, _, dk, d in SEMANTIC},
    }
    t["chart"] = {k: {"$type": "color", "$value": v} for k, v in CHART}
    t["gradient"] = {k: {"$type": "gradient-css", "$value": v, "$description": d} for k, v, d in GRADIENTS}
    t["font"] = {
        "family": {k.replace("font-family-", ""): {"$type": "fontFamily", "$value": v} for k, v in FONTS.items()},
        "weight": {k: {"$type": "fontWeight", "$value": v} for k, v in WEIGHTS.items()},
    }
    t["typography"] = {
        k: {"$type": "typography", "$description": ref_,
            "$value": {"fontFamily": "{font.family.%s}" % fam, "fontSize": f"{size}px",
                       "lineHeight": f"{lh}px", "letterSpacing": f"{ls * 100:g}%"}}
        for k, (size, lh, ls, fam, ref_) in TYPE.items()}
    t["spacing"] = {k: {"$type": "dimension", "$value": f"{v}px"} for k, v in SPACING.items()}
    t["vspace"] = {str(v): {"$type": "dimension", "$value": f"{v}px"} for v in VSPACE}
    t["radius"] = {k: {"$type": "dimension", "$value": f"{v}px"} for k, v in RADIUS.items()}
    t["stroke"] = {k: {"$type": "dimension", "$value": f"{v}px"} for k, v in STROKE.items()}
    t["layout"] = {k: {"$type": "dimension", "$value": f"{v}px"} for k, v in LAYOUT.items()}
    t["breakpoint"] = {k: {"$type": "dimension", "$value": f"{v}px",
                           "$description": f"{GRID_COLUMNS[k]} columns"} for k, v in BREAKPOINTS.items()}
    t["button"] = {surf: {k: {"$type": "color", "$value": v} for k, v in vals.items()} for surf, vals in BUTTONS.items()}
    write("tokens/tokens.json", json.dumps(t, indent=2) + "\n")

# ---------------------------------------------------------------------------
# SCSS (SFRA / Bootstrap 4)
# ---------------------------------------------------------------------------
def build_scss():
    L = [f"// {HEADER}", "// Import BEFORE Bootstrap in your SFRA cartridge's global.scss so these override Bootstrap 4 defaults.", ""]
    L.append("// ---- Primitives")
    for name, ramp in RAMPS.items():
        for s in STEPS:
            L.append(f"$color-{name}-{s}: {ramp[s]};")
    for k, v in PALETTE.items():
        L.append(f"$color-{k}: {v};")
    L.append("\n// ---- Brand aliases")
    for k, v, _ in BRAND_ALIASES:
        L.append(f"${k}: {v};")
    L.append("\n// ---- Semantic (light)")
    for k, l, _, _ in SEMANTIC:
        L.append(f"${k.replace('_', '--')}: {resolve(l)};")
    L.append("\n// ---- Gradients")
    for k, v, _ in GRADIENTS:
        L.append(f"${k}: {v};")
    L.append("\n// ---- Type")
    for k, v in FONTS.items():
        L.append(f"${k}: {v};")
    for k, (size, lh, ls, fam, _) in TYPE.items():
        L.append(f"$font-size-{k}: {size / 16:g}rem; $line-height-{k}: {lh / 16:g}rem; $letter-spacing-{k}: {ls:g}em;")
    L.append("\n// ---- Spacing / radius / layout")
    for k, v in {**SPACING, **RADIUS, **LAYOUT}.items():
        L.append(f"${k}: {px(v)};")
    L.append("\n// ---- Bootstrap 4 overrides (SFRA)")
    L += [
        "$primary: $color-primary;", "$secondary: $color-secondary;", "$success: $color-success;",
        "$warning: $color-warning;", "$danger: $color-error;", "$info: $color-tertiary;",
        "$light: $color-gray-50;", "$dark: $color-gray-900;",
        "$body-color: $color-gray-900;", "$link-color: $color-primary;", "$link-hover-color: $color-primary-hover;",
        "$font-family-sans-serif: $font-family-body;", "$font-family-base: $font-family-body;",
        "$headings-font-family: $font-family-display;", "$headings-font-weight: 600;",
        "$font-size-base: 1rem;", "$line-height-base: 1.5;",
        "$h1-font-size: $font-size-display-lg;", "$h2-font-size: $font-size-display-md;",
        "$h3-font-size: $font-size-display-sm;", "$h4-font-size: $font-size-display-xs;",
        "$h5-font-size: $font-size-text-2xl;", "$h6-font-size: $font-size-text-xl;",
        "$border-radius: 6px;", "$border-radius-lg: 8px;", "$border-radius-sm: 4px;",
        "$btn-border-radius: 6px;", "$btn-border-radius-lg: 6px;", "$btn-border-radius-sm: 6px;",
        "$btn-padding-y: 12px;", "$btn-padding-x: 24px;", "$btn-padding-y-sm: 8px;", "$btn-padding-x-sm: 20px;",
        "$btn-font-weight: 600;", "$input-border-color: $color-gray-300;", "$input-focus-border-color: $color-primary;",
        "$grid-gutter-width: 30px;",
        "$grid-breakpoints: (xs: 0, sm: 768px, md: 1024px, lg: 1260px, xl: 3840px);",
        "$container-max-widths: (sm: 100%, md: 100%, lg: 1260px, xl: 1260px);",
    ]
    write("tokens/_veeam-tokens.scss", "\n".join(L) + "\n")

# ---------------------------------------------------------------------------
# Tailwind preset
# ---------------------------------------------------------------------------
def build_tailwind():
    colors = {"white": "#ffffff", "black": "#000000"}
    for name, ramp in RAMPS.items():
        colors[name] = {s: ramp[s] for s in STEPS}
    colors["veeam"] = dict(PALETTE)
    colors["primary"] = {"DEFAULT": "var(--color-primary)", "hover": "var(--color-primary-hover)", "subtle": "var(--color-primary-subtle)"}
    colors["secondary"] = {"DEFAULT": "var(--color-secondary)", "hover": "var(--color-secondary-hover)", "subtle": "var(--color-secondary-subtle)"}
    sem = {k: f"var(--{k})" for k, *_ in SEMANTIC}
    font_size = {k: [f"{s / 16:g}rem", {"lineHeight": f"{lh / 16:g}rem", "letterSpacing": f"{ls:g}em"}]
                 for k, (s, lh, ls, _, _) in TYPE.items()}
    spacing = {k.replace("spacing-", ""): px(v) for k, v in SPACING.items()}
    radius = {k.replace("radius-", ""): px(v) for k, v in RADIUS.items()}
    preset = {
        "theme": {
            "screens": {k: f"{v}px" for k, v in BREAKPOINTS.items() if v},
            "extend": {
                "colors": {**colors, "sem": sem},
                "fontFamily": {"display": FONTS["font-family-display"].split(", "),
                               "body": FONTS["font-family-body"].split(", "),
                               "brand": FONTS["font-family-brand"].split(", ")},
                "fontSize": font_size, "spacing": spacing, "borderRadius": radius,
                "maxWidth": {"container": "1260px", "paragraph": "720px"},
                "backgroundImage": {k.replace("gradient-", "gradient-"): v for k, v, _ in GRADIENTS},
            },
        }
    }
    js = (f"// {HEADER}\n// tailwind.config.js:  module.exports = {{ presets: [require('./tokens/tailwind.preset.js')], content: [...] }}\n"
          "// Semantic colors use CSS variables, so also load tokens/veeam-tokens.css. Example: bg-sem-bg-brand-solid, text-sem-text-primary\n"
          f"module.exports = {json.dumps(preset, indent=2)};\n")
    write("tokens/tailwind.preset.js", js)

# ---------------------------------------------------------------------------
# PWA Kit (Chakra UI v2) theme
# ---------------------------------------------------------------------------
def build_pwa():
    colors = {name: {s: RAMPS[name][s] for s in STEPS} for name in RAMPS}
    colors["veeam"] = dict(PALETTE)
    font_sizes = {k: f"{s / 16:g}rem" for k, (s, *_ ) in TYPE.items()}
    line_heights = {k: f"{lh / 16:g}rem" for k, (_, lh, *_ ) in TYPE.items()}
    theme = {
        "colors": colors,
        "fonts": {"heading": FONTS["font-family-display"], "body": FONTS["font-family-body"]},
        "fontSizes": font_sizes, "lineHeights": line_heights,
        "radii": {k.replace("radius-", ""): px(v) for k, v in RADIUS.items()},
        "space": {k.replace("spacing-", ""): px(v) for k, v in SPACING.items()},
        "breakpoints": {"base": "0em", "sm": "48em", "md": "64em", "lg": "78.75em", "xl": "240em"},
        "sizes": {"container": {"xl": "1260px"}},
    }
    btn = BUTTONS["light"]
    js = f"""// {HEADER}
// Composable Storefront (PWA Kit): merge into app/theme/index.js
//   import {{extendTheme}} from '@chakra-ui/react'
//   import veeamTheme from './veeam-theme'   // this file
//   export default extendTheme(veeamTheme)
// Then load fonts/fonts.css in your _document / app shell.
const tokens = {json.dumps(theme, indent=2)}

const Button = {{
  baseStyle: {{
    borderRadius: '6px', fontFamily: 'body', fontWeight: 600, textTransform: 'uppercase',
    letterSpacing: '0.02em', _focusVisible: {{outline: '2px solid {btn['primary-bg']}', outlineOffset: '2px', boxShadow: 'none'}}
  }},
  sizes: {{
    lg: {{h: 'auto', minW: '190px', px: '24px', py: '12px', fontSize: '1rem', lineHeight: '1.5rem'}},
    md: {{h: 'auto', minW: '166px', px: '20px', py: '8px', fontSize: '0.875rem', lineHeight: '1.25rem'}}
  }},
  variants: {{
    solid: {{bg: '{btn['primary-bg']}', color: '{btn['primary-fg']}', _hover: {{bg: '{btn['primary-bg-hover']}'}}, _active: {{bg: '{btn['primary-bg-hover']}'}}}},
    outline: {{border: '1px solid', borderColor: '{btn['secondary-border']}', color: '{btn['secondary-fg']}',
      _hover: {{bg: '{btn['secondary-bg-hover']}', borderColor: '{btn['secondary-bg-hover']}', color: '{btn['secondary-fg-hover']}'}}}},
    ghost: {{color: '{btn['tertiary-fg']}', _hover: {{bg: '{btn['tertiary-bg-hover']}'}}}},
    link: {{color: '{btn['tertiary-fg']}', textTransform: 'none'}}
  }},
  defaultProps: {{variant: 'solid', size: 'lg'}}
}}

const Heading = {{baseStyle: {{fontFamily: 'heading', fontWeight: 600, color: 'gray.900'}}}}

export default {{
  ...tokens,
  styles: {{global: {{body: {{fontFamily: 'body', color: 'gray.900', bg: 'white'}}}}}},
  components: {{Button, Heading}}
}}
"""
    write("tokens/pwa-kit-theme.js", js)

# ---------------------------------------------------------------------------
# color-variables.md
# ---------------------------------------------------------------------------
def build_color_md():
    groups = [("1. Text colors", "text-"), ("2. Border colors", "border-"),
              ("3. Foreground colors (icons, indicators)", "fg-"), ("4. Background colors", "bg-")]
    out = ["# Color Variables — semantic tokens with real values", "",
           "> Generated by `scripts/build-tokens.py` — edit values there, not here.", "",
           "This is the layer you actually apply. Bind every element to a **semantic** variable —",
           "never a raw hex or a primitive step. The token **names and roles are identical to S1**,",
           "so S1 component specs carry over unchanged; only the values are Veeam's.", "",
           "- Light theme is the default (Veeam's web guidance: *preferred light color scheme*).",
           "- Dark theme is **opt-in** (`data-theme=\"dark\"`) and follows Veeam's PRISM dark background",
           "  (`#0F172C`) — on dark, the primary action turns **green** (`#00D15F`), per the PDF button page.",
           "- Rows marked **VEEAM** are additions that don't exist in S1.",
           "- Rule of thumb: text → `text-*`, icons → `fg-*`, strokes → `border-*`, fills → `bg-*`.", "",
           "## 0. Brand aliases — primary, secondary, …", "",
           "Use these in marketing/site code when you mean *the brand color*, not a UI role.", "",
           "| Token | Value | Use |", "|---|---|---|"]
    for k, v, d in BRAND_ALIASES:
        out.append(f"| `{k}` | `{v}` | {d} |")
    out.append("")
    for title, prefix in groups:
        out += [f"## {title}", "", "| Variable | Light | Dark | Alias (light / dark) | When to use |", "|---|---|---|---|---|"]
        for k, l, dk, d in SEMANTIC:
            if k.startswith(prefix):
                tag = "**VEEAM** " if d.startswith("VEEAM:") else ""
                desc = d.replace("VEEAM: ", "")
                out.append(f"| `{k}` | `{resolve(l)}` | `{resolve(dk)}` | {l} / {dk} | {tag}{desc} |")
        out.append("")
    out += ["## 5. Chart series", "", "Fixed order; max four series. Status colors (green/red/orange) are never series colors.", "",
            "| Token | Value |", "|---|---|"] + [f"| `{k}` | `{v}` |" for k, v in CHART] + [""]
    out += ["## 6. Button tokens per surface (PDF p.41)", "",
            "| Token | Light surface | Grey Mineral surface | Dark surface |", "|---|---|---|---|"]
    for k in BUTTONS["light"]:
        out.append(f"| `--button-{k}` | `{BUTTONS['light'][k]}` | `{BUTTONS['mineral'][k]}` | `{BUTTONS['dark'][k]}` |")
    out += ["", "Set the surface with `data-surface=\"mineral\"` / `data-surface=\"dark\"` on the section; the",
            "button classes in `css/veeam.css` read these variables automatically.", "",
            "## Application rules", "",
            "- **Primary action = Electric Azure** (`bg-brand-solid`) on light; **Viridis green** on dark.",
            "- **Green carries the brand.** Keep 30–40% of a marketing layout green (gradient, imagery,",
            "  green headlines) — but green is never a light-theme button color.",
            "- **Color is contextual** (PDF p.52): blue/purple = neutral, green = good, red/orange = problem.",
            "- **Ignis red** (`#ED2B3D`) is for alerts and watch-outs only — never decorative or in illustrations.",
            "- `_hover` pairs with its base token; `_on-brand` sits on solid brand fills; `_alt` turns",
            "  neutral in dark.",
            "- Never rely on color alone for status — pair it with text and an icon.", "",
            "### Contrast flags", "",
            "| Pair | Ratio | Rule |", "|---|---|---|",
            "| `#00D15F` (Viridis) text on white | 2.0:1 | Never body text. Green headlines only at Display sizes **and** bold, or use `text-secondary-brand` (`#007F49`, 5.1:1). |",
            "| White text on `#00D15F` | 2.0:1 | Fails — on green use ink `#232323` (7.7:1), exactly as the PDF's dark-theme button does. |",
            "| White on `#3700FF` | 8.1:1 | Pass — primary CTA. |",
            "| White on `#009277` (dark-theme hover) | 3.9:1 | PDF-specified; OK for a hover state of a bold uppercase label, never for static text. |",
            "| `#3700FF` link on white | 8.1:1 | Pass. |",
            "| `#FFD839` (Sol) on white | 1.4:1 | Fills and dark backgrounds only. |",
            "| `text-placeholder` `#6E737B` on white | 4.8:1 | Pass. |", ""]
    write("skill/references/color-variables.md", "\n".join(out))


if __name__ == "__main__":
    build_css()
    build_fonts()
    build_json()
    build_scss()
    build_tailwind()
    build_pwa()
    build_color_md()

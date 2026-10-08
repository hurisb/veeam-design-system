# Getting Started — for everyone

This guide is for anyone on the Veeam project who wants to use the Veeam Design System and has
**never downloaded files from GitHub or installed a Claude Skill before.** No code or design
background needed.

- [What the Veeam design system covers](#what-the-veeam-design-system-covers)
- [Part 1 — Get the files from GitHub](#part-1--get-the-files-from-github)
- [Part 2 — Install the fonts on your computer](#part-2--install-the-fonts-on-your-computer)
- [Part 3 — Use it in Claude](#part-3--use-it-in-claude)
- [Part 4 — Look at the examples](#part-4--look-at-the-examples)
- [Part 5 — Example prompts (copy/paste)](#part-5--example-prompts-copypaste)
- [Part 6 — Troubleshooting](#part-6--troubleshooting)

---

## What the Veeam design system covers

**Colors**
- **Primary: Electric Azure `#3700FF`** — every button, link and selected state on light pages.
- **Secondary: Viridis green `#00D15F`** — the Veeam logo, the brand gradient, green headlines.
  Green should fill about a third of a marketing layout.
- Supporting: Sky (light blue), Casia (purple), Sol (yellow), Navy Blue (dark text), plus
  success / warning / error colors.
- The **brand gradient**: white → bright green → blue → navy.
- Colors are named by *meaning* (`text-primary`, `bg-brand-solid`, `border-error`) — the same
  names as S1 — and each has a light and dark value.

**Fonts — the ES Build family**
- **ES Build Bauhaus** — all headings and big display text.
- **ES Build Neutral** — body text, labels, buttons, forms, everything else.
- **ES Build** (standard) — headings in PowerPoint only.

**Spacing, grid, buttons**
- Exactly the S1 spacing scale (4, 8, 12, 16, 24, 32, 48, 64, 80 … px) and S1 grid: 12 columns
  on desktop, 6 on tablet, 4 on mobile, 32px gaps (16px on mobile), 1280px max width.
- Buttons with 6px corners and UPPERCASE labels.

**System colors & text grays**
- Four status colors — **success** (green), **warning** (orange), **error** (red), **info**
  (blue) — each with matching fill, border, icon and text tokens and clear rules for when to use them.
- Gray tones for text: headings, labels, body, captions and disabled, with contrast ratios.

**Logo & brand elements**
- The Veeam logo (green plate, white "veeam"), clean/mono versions, favicon, app icon, the
  glassy **Bounce Mark** "V", the Wave, plates and glass overlays.

**Components**
- Everything from S1 — inputs, selects, checkboxes, tabs, breadcrumbs, tables, cards, badges,
  alerts, modals — re-colored for Veeam.

**Commerce Cloud**
- Ready-made setups for SFRA, Composable Storefront (PWA Kit) and B2B/D2C on LWR.

---

## Part 1 — Get the files from GitHub

This repo is **private**.

### Step 1: Get access
1. Create a free GitHub account at [github.com/join](https://github.com/join) if you don't have one.
2. Send Huri your GitHub username. Huri adds you under **Settings → Collaborators → Add people**.
3. Accept the email invite. Until you do, the repo link shows "404 / not found".

### Step 2: Download (no coding)
1. Open **https://github.com/hurisb/veeam-design-system** while signed in.
2. Click the green **`< > Code`** button → **Download ZIP**.
3. Double-click the zip in Downloads to unzip it. You now have a `veeam-design-system` folder.

### For developers: clone instead
```bash
git clone https://github.com/hurisb/veeam-design-system.git
```

---

## Part 2 — Install the fonts on your computer

Designers (and anyone making docs or decks) need the fonts installed.

- The repo has web-font files (`.woff` / `.woff2`) in `fonts/`. Design tools like Figma's desktop
  app and most OS font managers need **`.otf` / `.ttf`** desktop files — ask Veeam Creative
  (Veeam.CreativeTeam.Managers@veeam.com) for the desktop versions of **ES Build**, **ES Build
  Neutral** and **ES Build Bauhaus**.
- No fonts yet? Use the official fallbacks: **Source Sans Pro** (Google Fonts) or **Tahoma**
  in Office, **Arial** only when a partner asks for a system font.
- Websites don't need any install — the pages load the fonts from `fonts/fonts.css`.

> The fonts are licensed to Veeam. Use them only for Veeam work and don't share them outside
> the project.

---

## Part 3 — Use it in Claude

The `skill/` folder teaches Claude the whole Veeam system. Do **one** of these.

### A. Claude.ai (website) or desktop app — as a Skill
1. Download the skill (you must be signed in to GitHub with access to the repo):
   **https://github.com/hurisb/veeam-design-system/releases/latest/download/veeam-design-system.zip**
   — don't unzip it.
2. In Claude: **Settings → Customize → Skills → Upload skill**, choose `veeam-design-system.zip`.
3. Make sure its toggle is **on**. Ask a Veeam question in any chat.

> Team or Enterprise plan? An org owner/admin can upload the same zip once in the organization
> admin settings (Skills section) so everyone gets it automatically.

### B. Claude Code — as a Skill
```bash
unzip dist/veeam-design-system.zip -d ~/.claude/skills/
```
Or only for one project: copy it to `.claude/skills/veeam-design-system` inside that project.

### C. No install (2 minutes)
- **Attach to a chat:** attach `skill/SKILL.md` plus the files in `skill/references/`.
- **Claude Project:** create a Project called "Veeam Design System" and upload the same files —
  everyone on the team can use it. Start messages with "using the Veeam design system files…".

> If you also use the **S1** skill, Claude may pick either one — say "for **Veeam**" in your
> prompt.

---

## Part 4 — Look at the examples

They're online — just open a link:

- https://saltbox-veeam-design-system.vercel.app/examples/ — all examples
- https://saltbox-veeam-design-system.vercel.app/examples/foundations/ — every color, status color, text gray, font size, button and spacing step
- https://saltbox-veeam-design-system.vercel.app/examples/homepage/ — a Veeam storefront homepage
- https://saltbox-veeam-design-system.vercel.app/examples/storefront/ — a Commerce Cloud product listing
- https://saltbox-veeam-design-system.vercel.app/examples/storefront/product.html — a product detail page

Please share these links only inside the project team.

---

## Part 5 — Example prompts (copy/paste)

### Developers (SFCC & web)
- "Using the Veeam design system, give me the SFRA SCSS to style the PDP 'Add to cart' button."
- "Set up the Veeam theme in our PWA Kit project — which files go where?"
- "Build a Veeam product tile as an LWC using our CSS tokens, no hard-coded colors."
- "Convert this Bootstrap card to Veeam tokens." *(paste code)*
- "What are the Veeam breakpoints and how do they map to SFRA's Bootstrap grid?"

### Designers
- "What font and size is an H2 on Veeam web pages?"
- "Give me the Veeam brand gradient stops as CSS."
- "What color does the primary button turn on a dark background?"
- "Design a 1920×538 hero banner for Agent Commander following Veeam rules."

### QA & reviewers
- "Check this storefront screenshot against Veeam brand rules — gradient, green balance, logo
  legibility, button colors, fonts." *(attach image)*
- "Is white text on Viridis green accessible?"
- "List hard-coded hex values in this component that should be Veeam tokens." *(paste code)*

### PMs, sales & leadership
- "In plain words, what are Veeam's main colors and fonts?"
- "Does this landing page mockup look on-brand for Veeam? What's off?" *(attach image)*
- "What messaging lines are approved for Agent Commander?"

### Onboarding
- "I know S1. What's different in the Veeam design system?"
- "Explain primary vs. secondary color in the Veeam system and when to use each."

---

## Part 6 — Troubleshooting

**GitHub shows "404 / not found".** Sign in and accept the collaborator invite.

**Example pages show a plain font.** You opened an HTML file from your computer — use the online links in Part 4.

**No "Skills" option in Claude.** Update the app, or use the no-install option (3C).

**Skill upload rejected: description too long.** Shorten the `description:` line in
`skill/SKILL.md` to one or two sentences, re-zip, and upload again.

**Claude answers with S1 or generic values.** Add "for Veeam" or "using the Veeam design
system" to your prompt.

**A color or size looks wrong.** Values live in `scripts/build-tokens.py` — tell Huri, or follow
"Changing a token" in the README.

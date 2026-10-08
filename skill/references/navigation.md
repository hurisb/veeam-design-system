
# Navigation Component Library

> **Veeam adaptation of S1.** Component names, variants and token *names* are inherited from the
> S1 design system unchanged; every color/type value has been re-resolved to Veeam tokens
> (see [`color-variables.md`](color-variables.md), [`typography.md`](typography.md)).
> Where the Veeam PDF specifies a component (buttons, cards, plates), the **Veeam spec** block wins.

This skill defines every component in the NAVIGATION group of the Veeam design system. Use these components — never recreate them from scratch — when building any navigation, wayfinding, action-triggering, or step-based UI.

---

## Component Inventory

### 1. Button

**Component:** `Buttons/Button`

The primary action component used throughout the system.

**Veeam spec (PDF p.41) — overrides the S1 values below**

| | Large (default) | Small |
|---|---|---|
| Padding (V / H) | 12 / 24 px | 8 / 20 px |
| Min width | 190 px | 166 px |
| Label | `Text md/Semibold` 16/24, UPPERCASE, +2% tracking | `Text sm/Semibold` 14/20, UPPERCASE |
| Radius | `radius-button` 6 | `radius-button` 6 |
| Fixed width | 285 px (`.vds-btn--fixed`) | 285 px |
| Mobile | 100% width (`.vds-btn--block-mobile`) | 100% width |

Hierarchy maps to Veeam names: `Primary` = solid · `Secondary` = outline · `Tertiary` = text button
with a trailing → arrow (hover gets an `#EEF4F6` fill). Hover, Focus and Active share one color.
Text is centered; the arrow icon is optional on Primary/Secondary.

| Surface | Primary default → hover | Secondary default → hover | Tertiary hover |
|---|---|---|---|
| Light (white) | `#3700FF` / white text → `#283E8E` | `#3700FF` outline & text → `#283E8E` fill, white text | `#EEF4F6` fill |
| Grey Mineral `#505861` | white / `#232323` text → `#232323`, white text | white outline → white fill, dark text | white fill, dark text |
| Dark (`#232323`, navy) | `#00D15F` / `#232323` text → `#009277`, white text | `#00D15F` outline → `#009277` fill | `#EEF4F6` fill |

CSS: `.vds-btn`, `.vds-btn--secondary`, `.vds-btn--tertiary`, `.vds-btn--sm` in `css/veeam.css`;
set the surface with `data-surface="mineral"` or `data-surface="dark"` on the section.
Tokens: `--button-primary-bg`, `--button-primary-bg-hover`, `--button-secondary-border`, … (see
`color-variables.md` §6). Only **one Primary per view**.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md`, `lg`, `xl` | `sm` |
| Hierarchy | `Primary`, `Secondary`, `Tertiary`, `Link color`, `Link gray` | `Primary` |
| State | `Default`, `Hover`, `Focused`, `Disabled`, `Loading` | `Default` |
| Icon only | `False`, `True` | `False` |

**Boolean properties:**
- `Icon leading` (default: on) — icon before the label
- `Icon trailing` (default: on) — icon after the label
- `Loading text` (default: on) — text shown during loading state

**Instance swaps:** `Icon leading swap`, `Icon trailing swap`

**When to use:**
- `Primary` — the single most important action on a screen (submit, save, continue). Limit to one per view.
- `Secondary` — supporting actions alongside a primary (cancel, back, secondary CTA)
- `Tertiary` — low-emphasis actions (reset, clear, less important options)
- `Link color` — inline navigation-style action using brand color
- `Link gray` — inline navigation-style action, neutral tone
- `Icon only` — toolbar actions, compact UI where the icon is universally understood (close, settings, share)
- `Loading` — show after user clicks to indicate processing; always include loading text for screen readers

**Tokens used**
- Color: `bg-brand-solid` #3700ff, `text-white` #ffffff, `bg-primary` #ffffff, `border-primary` #c3c6cb, `text-secondary` #3b4049, `text-tertiary` #505861, `text-brand-secondary` #283e8e, `fg-brand-secondary_alt` #4d2eff, `fg-tertiary` #505861, `fg-quaternary` #adacaf, `bg-brand-solid_hover` #283e8e, `bg-secondary_hover` #f0f0f0, …
- Radius: `radius-xs` 4, `radius-md` 8
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16
- Type: `Text sm/Semibold` 14/20, `Text md/Semibold` 16/24

---

### 2. Button Destructive

**Component:** `Buttons/Button destructive`

Red/destructive-themed button for irreversible or high-risk actions.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md`, `lg`, `xl` | `sm` |
| Hierarchy | `Primary`, `Secondary`, `Tertiary`, `Link` | `Primary` |
| State | `Default`, `Hover`, `Focused`, `Disabled`, `Loading` | `Default` |
| Icon only | `False`, `True` | `False` |

**Boolean properties:**
- `Icon leading` (default: on)
- `Icon trailing` (default: on)
- `Loading text` (default: on)

**Instance swaps:** `Icon leading swap`, `Icon trailing swap`

**When to use:**
- Delete, remove, revoke, cancel subscription, or any action that cannot be undone
- Always require confirmation (modal or inline) before executing the destructive action
- Use `Secondary` or `Tertiary` hierarchy for less prominent destructive options (e.g. "Remove" in a list item)

**Tokens used**
- Color: `bg-error-solid` #d01a2c, `text-white` #ffffff, `fg-error-secondary` #ed2b3d, `text-error-primary` #d01a2c, `bg-primary` #ffffff, `border-error_subtle` #f69aa3, `bg-error-solid_hover` #ad1524, `fg-error-primary` #d01a2c, `text-error-primary_hover` #ad1524, `bg-error-primary` #fef2f3, `fg-white` #ffffff
- Radius: `radius-xs` 4, `radius-md` 8
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16
- Type: `Text sm/Semibold` 14/20, `Text md/Semibold` 16/24

---

### 3. Button Utility

**Component:** `Buttons/Button utility`

Small icon-only utility button for compact controls.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Size | `xs`, `sm` | `xs` |
| Hierarchy | `Secondary`, `Tertiary` | `Secondary` |
| State | `Default`, `Hover`, `Focused`, `Disabled` | `Default` |

**Instance swap:** `Icon swap`

**When to use:**
- Inline table/list actions (edit, delete, duplicate, copy)
- Toolbar icon buttons in dense UIs
- Card action buttons (overflow menu trigger, bookmark)

**Tokens used**
- Color: `fg-quaternary` #adacaf, `bg-primary` #ffffff, `border-primary` #c3c6cb, `fg-quaternary_hover` #6e737b, `text-white` #ffffff, `bg-primary-solid` #121318, `bg-primary_hover` #f9f9f9
- Radius: `radius-sm` 6, `radius-md` 8
- Spacing: `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12
- Type: `Text xs/Semibold` 12/18

---

### 4. Button Close X

**Component:** `Buttons/Button close X`

Dedicated close/dismiss button.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md`, `lg` | `sm` |
| Dark background | `False`, `True` | `False` |
| State | `Default`, `Hover`, `Focused` | `Default` |

**When to use:**
- Closing modals, dialogs, toasts, banners, slideout panels
- `Dark background=True` — when placed over dark overlays or images

**Tokens used**
- Color: `fg-quaternary` #adacaf, `bg-primary` #ffffff, `fg-quaternary_hover` #6e737b, `bg-primary_hover` #f9f9f9, `fg-white` #ffffff
- Radius: `radius-md` 8
- Spacing: `spacing-md` 8

---

### 5. Social Button

**Component:** `Buttons/Social button`

Branded social login/signup button.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Social | `Google`, `Facebook`, `Apple`, `Twitter`, `Figma`, `Dribbble` | `Google` |
| Supporting text | `True`, `False` | `True` |
| Theme | `Brand`, `Gray`, `Color` | `Brand` |
| State | `Default`, `Hover`, `Focused` | `Default` |

**When to use:**
- Social sign-in / sign-up flows (OAuth login)
- `Brand` — uses the social platform's brand color
- `Gray` — neutral monochrome style
- `Color` — uses the social platform's full-color logo on a neutral button

**Tokens used**
- Color: `fg-white` #ffffff, `text-white` #ffffff, `bg-primary` #ffffff, `text-secondary` #3b4049, `border-primary` #c3c6cb, `text-secondary_hover` #232323, `bg-primary_hover` #f9f9f9, `fg-quaternary` #adacaf, `fg-quaternary_hover` #6e737b
- Radius: `radius-md` 8
- Spacing: `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16
- Type: `Text sm/Semibold` 14/20, `Text md/Semibold` 16/24

---

### 6. Social Button Group

**Component:** `Buttons/Social button group`

Pre-composed group of social login buttons.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Style | `Buttons`, `Icons` | `Buttons` |
| Theme | `Brand`, `Color`, `Gray` | `Brand` |

**When to use:**
- Login/register pages with multiple social providers
- `Icons` — compact icon-only row when space is limited

**Tokens used**
- Color: `text-secondary` #3b4049, `bg-primary` #ffffff, `border-primary` #c3c6cb, `fg-quaternary` #adacaf, `fg-white` #ffffff, `text-white` #ffffff
- Radius: `radius-md` 8
- Spacing: `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16
- Type: `Text sm/Semibold` 14/20, `Text md/Semibold` 16/24

---

### 7. Mobile App Store Badge

**Component:** `Mobile app store badge`

App store download badges.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Size | `md`, `lg` | `md` |
| Store | `Google Play`, `App Store`, `Mac App Store`, `Galaxy Store`, `AppGallery` | `Google Play` |
| Style | `Brand`, `Outline` | `Brand` |

**When to use:**
- Marketing pages, app landing pages, footer CTAs for app downloads

**Tokens used**
- Color: `fg-primary` #1d1f2a, `bg-primary` #ffffff

---

### 8. Tag

**Component:** `Tag`

Compact label for categorization, filtering, or status indication.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md`, `lg` | `sm` |
| Icon | `False`, `Country`, `Avatar`, `Dot` | `False` |
| Action | `Text only`, `X close`, `Count` | `Text only` |
| Checkbox | `False`, `True` | `False` |

**Instance swap:** `Flag swap` — swap the country flag icon

**When to use:**
- `Text only` — static labels (categories, status, metadata)
- `X close` — removable tags (filter chips, selected values, email recipients)
- `Count` — tags with a numeric count (issue counts, notification counts)
- `Checkbox` — selectable/toggleable tags (filter selection, multi-select chips)
- `Country` — tags with a country flag (locale, region)
- `Avatar` — tags with a user avatar (assigned users, mentions)
- `Dot` — status indicator tags (online/offline, severity)

**Tokens used**
- Color: `text-secondary` #3b4049, `bg-primary` #ffffff, `border-primary` #c3c6cb, `fg-quaternary` #adacaf, `bg-tertiary` #f0f0f0, `fg-success-secondary` #00d15f
- Radius: `radius-xs` 4, `radius-sm` 6, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8
- Type: `Text xs/Medium` 12/18, `Text sm/Medium` 14/20

---

### 9. Dropdown Menu

**Component:** `Dropdown menu`

General-purpose dropdown menu triggered by buttons, icons, or account elements.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Button`, `Icon`, `Avatar` | `Button` |
| Open | `False`, `True` | `False` |

**Boolean properties:**
- `Scrollbar` (default: on)
- `Chevron dropdown` (default: on)

**When to use:**
- `Button simple` / `Button advanced` — action menus from text buttons
- `Button link` — action menu from a link-styled trigger
- `Icon simple` / `Icon advanced` — kebab/meatball overflow menus, toolbar overflow
- `Search simple` / `Search advanced` — filterable dropdown menus
- `Integrations` — integration/app picker menus
- `Account *` — user/profile menus in navigation headers

**Tokens used**
- Color: `bg-primary` #ffffff, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-quaternary` #6e737b, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `fg-brand-primary` #3700ff, `bg-brand-solid` #3700ff, `fg-quaternary` #adacaf, `text-placeholder` #6e737b, `fg-success-secondary` #00d15f, …
- Radius: `radius-xs` 4, `radius-sm` 6, `radius-md` 8, `radius-lg` 10, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-3xl` 24
- Type: `Text xs/Regular` 12/18, `Text xs/Medium` 12/18, `Text xs/Semibold` 12/18, `Text sm/Regular` 14/20, `Text sm/Semibold` 14/20

---

### 10. Sidebar Navigation

**Component:** `Sidebar navigation`

Vertical sidebar navigation for applications.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Open | `False`, `True` | `False` |
| Style | `Simple`, `Dual-tier`, `Slim`, `Sections dividers`, `Sections subheadings` | `Simple` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Sub-components:**
- `_Nav item base` — individual nav item with icon, badge, dot, trailing icon, Current/State variants
- `_Nav item dropdown base` — expandable nav item with Open/Current variants
- `_Nav featured card` — promotional/contextual card within the sidebar (13 types: Progress bar, Progress circle, Image, Cookie preferences, Referral link, Onboarding steps, Upgrade CTA, Support CTA, Event CTA, Message, Current projects, Free trial CTA, QR code)
- `_Nav button` — icon/text navigation button with Current state
- `_Nav menu button` — hamburger/close toggle button
- `_Nav account card` — user account card (Card or Simple type)

**When to use:**
- `Simple` — flat nav list for apps with few top-level sections
- `Sections subheadings` — grouped nav with section headers for complex apps
- `Sidebar` — full sidebar with account card, featured card, and nested navigation
- Always use `Breakpoint=Mobile` for responsive mobile nav (typically as a slide-out overlay)

**Tokens used**
- Color: `bg-primary` #ffffff, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `border-primary` #c3c6cb, `bg-brand-solid` #3700ff, `fg-brand-primary_alt` #3700ff, `text-brand-secondary` #283e8e, `fg-quaternary` #adacaf, `bg-overlay` #121318, `fg-success-secondary` #00d15f, `utility-neutral-700` #3b4049, …
- Radius: `radius-xs` 4, `radius-sm` 6, `radius-md` 8, `radius-xl` 12, `radius-2xl` 16, `radius-full` 9999
- Spacing: `spacing-none` 0, `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24, `spacing-7xl` 64
- Type: `Text xs/Medium` 12/18, `Text xs/Semibold` 12/18, `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Text md/Regular` 16/24

---

### 11. Header Navigation

**Component:** `Header navigation`

Horizontal top navigation bar for applications.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Open | `False`, `True` | `False` |
| Style | `Simple`, `Dual-tier` | `Simple` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Boolean properties:**
- `Title?` (default: on) — show/hide the page title in the header

**When to use:**
- Application top bar with logo, nav links, search, and user account
- Pair with Sidebar navigation for apps that use both horizontal and vertical nav
- `Mobile` breakpoint collapses nav items into a hamburger menu

**Tokens used**
- Color: `text-primary` #1d1f2a, `text-tertiary` #505861, `text-quaternary` #6e737b, `fg-tertiary` #505861, `bg-primary` #ffffff, `border-primary` #c3c6cb, `bg-secondary` #f9f9f9
- Radius: `radius-md` 8
- Spacing: `spacing-none` 0, `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-3xl` 24
- Type: `Text sm/Semibold` 14/20, `Text md/Semibold` 16/24

---

### 12. Breadcrumbs

**Component:** `Breadcrumbs`

Hierarchical path navigation showing the user's location within the app.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Divider | `Chevron`, `Slash` | `Chevron` |
| Type | `Text`, `Text with line`, `Button` | `Text` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Sub-component:** `_Breadcrumb button base` — individual breadcrumb item.

| Property | Options | Default |
|---|---|---|
| Current | `False`, `True` | `False` |
| Type | `Button`, `Text` | `Text` |
| Icon | `False`, `True` | `True` |
| State | `Default`, `Hover`, `Focused` | `Default` |

**When to use:**
- `Text` — simple text breadcrumb trail
- `Text with line` — breadcrumbs with a bottom border separator line
- `Button` — clickable button-styled breadcrumbs
- `Account dropdowns` — breadcrumbs with dropdown menus at each level (e.g. org > team > project)
- Use for hierarchies 3+ levels deep; avoid for flat navigation structures

**Tokens used**
- Color: `bg-primary` #ffffff, `text-primary` #1d1f2a, `text-tertiary` #505861, `text-quaternary` #6e737b, `text-brand-secondary` #283e8e, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `bg-brand-solid` #3700ff, `fg-quaternary` #adacaf, `fg-white` #ffffff, `utility-neutral-300` #c3c6cb, `text-tertiary_hover` #3b4049, …
- Radius: `radius-none` 0, `radius-sm` 6, `radius-md` 8, `radius-lg` 10, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8
- Type: `Text sm/Regular` 14/20, `Text sm/Semibold` 14/20

---

### 13. Pagination

**Component:** `Pagination`

Page navigation for paginated content.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Page default`, `Page minimal center aligned`, `Card default`, `Card minimal right aligned`, `Card minimal left aligned`, `Card minimal center aligned`, `Card button group right aligned`, `Card button group left aligned`, `Card button group center aligned` | `Page default` |
| Shape | `Square`, `Circle` | `Square` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Boolean properties:**
- `Select (dropdown)` (default: on) — "Go to page" dropdown

**Sub-components:**
- `Pagination dot group` — dot/line indicators for carousels (Dot or Line style, md or lg size, optional Framed)
- `Carousel image` — image carousel with arrows (md or lg size)
- `_Carousel arrow` — left/right navigation arrows

**When to use:**
- `Page *` — standard table/list pagination with page numbers
- `Card *` — bottom-of-card pagination for card-based content (prev/next with optional numbers)
- `Card advanced` — pagination with "rows per page" selector
- `Pagination dot group` — carousel/slideshow indicators (prefer Dot for < 10 items, Line for visual emphasis)
- `Carousel image` — image gallery/slideshow navigation

**Tokens used**
- Color: `bg-primary` #ffffff, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-quaternary` #6e737b, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `fg-quaternary` #adacaf, `bg-primary_hover` #f9f9f9, `text-secondary_hover` #232323
- Radius: `radius-md` 8, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24
- Type: `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20

---

### 14. Horizontal Tabs

**Component:** `Horizontal tabs`

Horizontal tab bar for switching between content panels.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Button brand`, `Button gray`, `Underline`, `Button border`, `Button minimal` | `Button brand` |
| Size | `sm`, `md` | `sm` |
| Full width | `False`, `True` | `False` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Sub-component:** `_Tab button base` — individual tab with Badge and Icon toggles.

| Property | Options | Default |
|---|---|---|
| Current | `False`, `True` | `False` |
| Size | `sm`, `md` | `sm` |
| Type | `Button brand`, `Button gray`, `Underline`, `Line (vertical tabs)`, `Button white`, `Button minimal` | `Button brand` |
| State | `Default`, `Hover`, `Focus` | `Default` |

**When to use:**
- `Button brand` — primary tab style with brand-colored active state
- `Button gray` — neutral tab style for settings/admin UIs
- `Underline` — classic underline tab indicator (most common for content sections)
- `Button border` — outlined tabs for secondary tab groups
- `Button minimal` — minimal pill-style tabs
- `Full width=True` — tabs stretch to fill available width (good for mobile or equal-weight sections)

**Tokens used**
- Color: `bg-primary` #ffffff, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-quaternary` #6e737b, `text-brand-secondary` #283e8e, `bg-brand-primary_alt` #e3eefe, `fg-brand-primary_alt` #3700ff, `fg-brand-secondary_alt` #4d2eff, `border-primary` #c3c6cb, `fg-quaternary` #adacaf, `utility-neutral-700` #3b4049, `utility-neutral-200` #dbdee1, …
- Radius: `radius-sm` 6, `radius-md` 8, `radius-lg` 10, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16
- Type: `Text xs/Medium` 12/18, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Text md/Medium` 16/24, `Text md/Semibold` 16/24

---

### 15. Vertical Tabs

**Component:** `Vertical tabs`

Vertical tab bar for side-panel navigation within a content area.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Button primary`, `Button gray`, `Line`, `Button border`, `Button minimal` | `Button primary` |
| Size | `sm`, `md` | `sm` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**When to use:**
- Settings pages with many sections, documentation side nav, multi-step forms with visible section list
- `Line` — vertical line indicator (similar to sidebar nav style)
- Prefer Vertical tabs over Horizontal tabs when there are 6+ tab items

**Tokens used**
- Color: `bg-primary` #ffffff, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-quaternary` #6e737b, `text-brand-secondary` #283e8e, `bg-brand-primary_alt` #e3eefe, `fg-brand-primary_alt` #3700ff, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `fg-quaternary` #adacaf, `utility-neutral-700` #3b4049, `utility-neutral-200` #dbdee1, …
- Radius: `radius-sm` 6, `radius-md` 8, `radius-lg` 10, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16
- Type: `Text xs/Medium` 12/18, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Text md/Medium` 16/24, `Text md/Semibold` 16/24

---

### 16. Progress Steps

Multiple progress step components for multi-step workflows:

#### Progress Minimal Icons Connected
**Component:** `Progress steps / Progress minimal icons connected`

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md` | `sm` |
| Type | `Check`, `Number` | `Check` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

#### Progress Minimal Icons
**Component:** `Progress steps / Progress minimal icons`

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md` | `sm` |
| Type | `Check`, `Number` | `Check` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Boolean:** `Text` (default: on)

#### Progress Text with Line
**Component:** `Progress steps / Progress text with line`

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md` | `sm` |
| Breakpoint | `Mobile`, `Desktop` | `Mobile` |

#### Progress Icons Centered
**Component:** `Progress steps / Progress icons centered`

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md` | `sm` |
| Type | `Icon`, `Number`, `Featured icon` | `Icon` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Boolean:** `4th step` (default: on)

#### Progress Icons with Text
**Component:** `Progress steps / Progress icons with text`

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md` | `sm` |
| Type | `Icon`, `Number`, `Icon featured` | `Icon` |

**Step status options (sub-component `_Step base`):** `Incomplete`, `Current`, `Complete`

**When to use:**
- Multi-step forms, onboarding flows, checkout processes, wizards
- `Check` — completed steps show a checkmark
- `Number` — steps show their sequential number
- `Featured icon` — steps show a custom icon per step
- `Icons connected` — steps connected by a progress line (best for linear flows)
- `Icons centered` — centered layout with labels below (best for 3-4 steps)
- `Text with line` — minimal text-only steps with connecting line
- `Icons with text` — vertical step list with descriptions (best for complex flows with explanations)

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-brand-solid` #3700ff, `fg-brand-primary` #3700ff, `bg-success-solid` #009277, `text-secondary` #3b4049, `text-quaternary` #6e737b, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `fg-quaternary` #adacaf, `fg-white` #ffffff
- Radius: `radius-full` 9999
- Spacing: `spacing-sm` 6
- Type: `Text xs/Semibold` 12/18, `Text sm/Semibold` 14/20

---

### 17. Slide Out Menu

**Component:** `Slide out menu`

Side panel that slides in from the edge of the screen.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Placeholder`, `User profile`, `Messages`, `Message chat`, `Payment method`, `Payment details`, `Plan`, `Team members`, `Filters`, `File upload`, `Labels`, `Project details`, `Notification settings button groups`, `Notification settings checkboxes`, `Notifications`, `Order summary`, `Calendar event`, `User settings`, `A.I. assistant intro`, `A.I. assistant message` | `Placeholder` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Sub-component:** `_Slide out menu header` — panel header with optional Icon, Supporting text, Tabs.

**When to use:**
- `Placeholder` — start with this type and customize the content area
- `Filters` — filter panel for search/list pages
- `User profile` / `User settings` — profile editing without leaving the current page
- `Messages` / `Message chat` — messaging panel alongside main content
- `Payment *` / `Order summary` — checkout and billing flows
- `Notifications` — notification center panel
- `Calendar event` / `Create event` — event details and creation
- `A.I. assistant *` — AI chat panel
- Use slideout menus for secondary workflows that shouldn't replace the main content

**Tokens used**
- Color: `bg-primary` #ffffff, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-quaternary` #6e737b, `border-primary` #c3c6cb, `bg-brand-solid` #3700ff, `text-brand-secondary` #283e8e, `fg-brand-primary` #3700ff, `border-brand` #3700ff, `bg-overlay` #121318, `text-error-primary` #d01a2c, …
- Radius: `radius-none` 0, `radius-xs` 4, `radius-sm` 6, `radius-md` 8, `radius-lg` 10, `radius-xl` 12, `radius-2xl` 16, `radius-full` 9999
- Spacing: `spacing-none` 0, `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24, `spacing-4xl` 32, `spacing-5xl` 40, `spacing-6xl` 48, `spacing-7xl` 64
- Type: `Text xs/Regular` 12/18, `Text xs/Medium` 12/18, `Text xs/Semibold` 12/18, `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Text md/Regular` 16/24, `Text md/Medium` 16/24, `Text md/Semibold` 16/24, `Text lg/Semibold` 18/24, `Text lg/Bold` 18/24, `Text xl/Semibold` 20/24, `Display sm/Semibold` 36/44

---

## Shared Size Convention

Most navigation components use a consistent size scale:
- **xs** — micro actions (utility buttons, inline controls)
- **sm** — compact density; data-heavy UIs, toolbars, sidebars
- **md** — standard density; most pages and application chrome
- **lg** / **xl** — touch-friendly; mobile, marketing pages, hero CTAs

Always use the same size across related navigation elements for visual consistency.

---

## UX, Accessibility & Heuristic Best Practices

### Button Hierarchy
- Limit **one Primary button** per view/section — it should represent the main action
- Pair Primary with Secondary for the complementary action (e.g. "Save" + "Cancel")
- Use Tertiary or Link buttons for low-priority or ancillary actions
- Destructive buttons must always require confirmation before executing
- Never disable a button without explaining why (use a tooltip on the disabled button)
- Always show `Loading` state after click for async actions; include `Loading text` for accessibility

### Navigation Structure
- Use **Header navigation** for global app-level navigation (logo, primary sections, user menu)
- Use **Sidebar navigation** for section-level navigation within an app area
- Use **Tabs** for switching between views within the same page/context
- Use **Breadcrumbs** for hierarchical depth (3+ levels) — always show the full path
- Use **Progress steps** for sequential multi-step flows — never for general navigation

### Navigation Selection Guide
- **Top-level app sections (3-7 items):** Header navigation or Sidebar navigation
- **Sub-sections within a page (2-6 items):** Horizontal tabs
- **Sub-sections within a page (6+ items):** Vertical tabs
- **Hierarchical location indicator:** Breadcrumbs
- **Paginated data (tables, lists):** Pagination
- **Sequential workflow (onboarding, checkout):** Progress steps
- **Secondary panel content:** Slide out menu
- **Action menu from a button/icon:** Dropdown menu
- **Image/content carousel:** Pagination dot group + Carousel arrows

### Tags
- Use tags for categorization, filtering, and metadata display — not as buttons
- `X close` tags should have clear "remove" semantics (screen readers: "Remove [tag name]")
- `Checkbox` tags are interactive filter chips — group them logically
- Keep tag labels short (1-3 words); truncate with ellipsis if needed

### Responsive Design
- Use `Breakpoint=Mobile` variants for Sidebar navigation, Header navigation, Breadcrumbs, Tabs, Pagination, Progress steps, and Slide out menus on small screens
- On mobile, Header navigation should collapse to a hamburger menu
- On mobile, Sidebar navigation should be a full-screen overlay (Open=True)
- On mobile, prefer `Full width=True` for Horizontal tabs
- On mobile, Date picker modals are preferred over dropdowns
- Slide out menus on mobile should be full-width panels

### Accessibility
- Every button must have an accessible label — for `Icon only` buttons, provide an `aria-label`
- Navigation landmarks: wrap Sidebar in `<nav>`, Header in `<header>`, Breadcrumbs in `<nav aria-label="Breadcrumb">`
- Current page/tab must be indicated with `aria-current="page"` (mapped to `Current=True` variant)
- Tab panels: use `role="tablist"`, `role="tab"`, and `role="tabpanel"` semantics
- Breadcrumbs: last item (current page) should not be a link
- Progress steps: announce step status to screen readers ("Step 2 of 4: Current")
- Dropdown menus: support Escape to close, arrow keys to navigate items, Enter to select
- Focus must be visible on every interactive element (all components include `Focused` state)
- Slide out menus: trap focus within the panel while open; return focus to trigger on close
- Social buttons: include the provider name in the accessible label ("Sign in with Google")
</parameter>
</invoke>

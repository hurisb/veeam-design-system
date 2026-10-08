
# Data Display Component Library

> **Veeam adaptation of S1.** Component names, variants and token *names* are inherited from the
> S1 design system unchanged; every color/type value has been re-resolved to Veeam tokens
> (see [`color-variables.md`](color-variables.md), [`typography.md`](typography.md)).
> Where the Veeam PDF specifies a component (buttons, cards, plates), the **Veeam spec** block wins.

This skill defines every component in the DATA DISPLAY group of the Veeam design system. Use these components — never recreate them from scratch — when building any data presentation, feedback, layout structure, or content display UI.

---

## Component Inventory

### 1. Table

**Component:** `Table`

Data table with header row, sortable columns, and interactive cells.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Example | `Team members`, `Companies`, `Sales`, `Files` | `Team members` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |
| Dividers | `Divider line`, `Alternating fills` | `Divider line` |

**Sub-components:**

**Table header cell**:

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md` | `sm` |
| Text | `False`, `True` | `True` |
| Checkbox | `False`, `True` | `True` |

**Table cell**:

| Property | Options | Default |
|---|---|---|
| Type | `Text`, `Avatar`, `File type icon`, `Payment method`, `Badge`, `Badges multiple`, `Trend positive`, `Trend negative`, `Avatar group`, `Select dropdown`, `Progress bar`, `Star ratings`, `Action buttons`, `Action icons`, `Action dropdown icon` | `Text` |
| Size | `sm`, `md` | `sm` |
| State | `Default`, `Hover/selected` | `Default` |

**Boolean properties (cell):**
- `Lead action` (default: on) — checkbox/radio/toggle in the leading position
- `Supporting text` (default: on)
- `Lead text` (default: on)

**Table cell lead action** — `Checkbox`, `Radio`, or `Toggle`

**When to use:**
- Structured data: user lists, transactions, file management, CRM records
- `Divider line` — clean separator lines between rows (default, best for most cases)
- `Alternating fills` — zebra striping for dense tables with many columns
- Use `sm` size for data-dense tables; `md` for tables with fewer columns

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-secondary` #f9f9f9, `bg-brand-solid` #3700ff, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-quaternary` #6e737b, `text-brand-secondary` #283e8e, `fg-quaternary` #adacaf, `fg-brand-primary` #3700ff, …
- Radius: `radius-none` 0, `radius-xs` 4, `radius-sm` 6, `radius-md` 8, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24
- Type: `Text xs/Medium` 12/18, `Text xs/Semibold` 12/18, `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Text md/Semibold` 16/24

---

### 2. Badge

**Component:** `Badge`

Status indicator, label, or count badge.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md`, `lg` | `sm` |
| Type | `Pill color`, `Badge color`, `Badge modern` | `Pill color` |
| Icon | `False`, `Dot`, `Country`, `X close`, `Avatar`, `Icon trailing`, `Icon leading`, `Only` | `False` |
| Color | `Gray`, `Brand`, `Error`, `Warning`, `Success`, `Blue`, `Blue gray`, `Blue light`, `Gray blue`, `Indigo`, `Purple`, `Pink`, `Orange` | `Gray` |

**Instance swaps:** `Flag swap`, `Icon trailing swap`, `Icon leading swap`

**Related: Badge group** — badge paired with a text label (Leading or Trailing position).

**When to use:**
- `Pill color` — rounded pill badges for status labels, categories, counts
- `Badge color` — square-cornered badges for more structured contexts
- `Badge modern` — minimal outlined badge style
- `Dot` — minimal status indicator (online, new, active)
- `X close` — removable/dismissible badges
- Color semantics: `Error` = critical/failure, `Warning` = caution, `Success` = positive/complete, `Brand` = branded/highlighted, `Gray` = neutral/default

**Tokens used**
- Color: core `text-secondary` #3b4049, `bg-primary` #ffffff, `border-primary` #c3c6cb; utility palette: brand/yellow/green/slate/sky/indigo/purple/blue/pink/orange/red/neutral, steps 50/200/400/500/600/700
- Radius: `radius-sm` 6, `radius-md` 8, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12
- Type: `Text xs/Medium` 12/18, `Text sm/Medium` 14/20

---

### 3. Content Divider

**Component:** `Content divider`

Visual separator between content sections.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Heading`, `Text`, `Button`, `Button group icon`, `Button group`, `Button icon` | `Heading` |
| Style | `Single line`, `Dual line`, `Background fill` | `Single line` |

**When to use:**
- `Heading` — section breaks with a title
- `Text` — centered text label divider (e.g. "or", "and")
- `Button` / `Button icon` — dividers with action buttons (e.g. "Load more", "Add section")
- `Button group` — dividers with multiple action options

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-primary_hover` #f9f9f9, `bg-secondary` #f9f9f9, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-secondary_hover` #232323, `text-tertiary` #505861, `fg-quaternary` #adacaf
- Radius: `radius-md` 8
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12
- Type: `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Text md/Semibold` 16/24

---

### 4. Modal

**Component:** `Modal`

Dialog overlay for focused tasks, confirmations, and forms.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Stacked left aligned`, `Horizontal`, `Warning stacked left aligned`, `Warning horizontal`, `Destructive stacked left aligned`, `Destructive horizontal`, `Log in`, `Sign up 01`, `Sign up 02`, `Checkboxes`, `Toggles`, `Link field`, `Dropdown`, `Input field`, `Labels`, `Access request`, `Email invite`, `User invite`, `Stacked with team`, `Stacked with team and link`, `Stacked with team and invites`, `Verification code`, `2FA code`, `Password prompt`, `Centered photo`, `Centered photo carousel`, `Centered video carousel`, `Payment details`, `Payment details with image`, `Plan 01`, `Plan 02`, `Payment method`, `Date picker`, `File upload`, `Profile settings`, `User selection`, `Image crop`, `Form 01`, `Form 02`, `Calendar event`, `Banner appearance`, `Appearance settings`, `A.I. assistant`, `User settings`, `New project`, `Text editor` | `Stacked left aligned` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Sub-components:**
- **_Modal header** — Left aligned, Center aligned, or Horizontal left aligned; with optional X close, Featured icon, Divider
- **_Modal actions** — Horizontal/Vertical button layouts with optional Checkbox, Tertiary button, Destructive variant

**When to use:**
- `Stacked left aligned` / `Horizontal` — general confirmation/info dialogs
- `Warning *` — caution dialogs (yellow/warning icon)
- `Destructive *` — delete/remove confirmations (red destructive styling)
- Auth modals: `Log in`, `Sign up 01/02`, `Verification code`, `2FA code`, `Password prompt`
- Form modals: `Input field`, `Dropdown`, `Checkboxes`, `Toggles`, `Date picker`, `File upload`, `Text editor`
- User/team modals: `Email invite`, `User invite`, `User selection`, `Share project`, `Profile settings`, `User settings`
- Commerce modals: `Payment details`, `Payment method`, `Plan 01/02`
- Media modals: `Centered photo`, `Centered photo carousel`, `Centered video carousel`, `Image crop`

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-overlay` #121318, `bg-brand-solid` #3700ff, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `fg-error-primary` #d01a2c, `fg-success-primary` #009277, `fg-brand-primary` #3700ff, `text-brand-secondary` #283e8e, …; utility palette: neutral/sky/indigo/pink/blue/green/purple/red/orange/brand/fuchsia, steps 50/200/400/500/600/700
- Radius: `radius-xs` 4, `radius-sm` 6, `radius-md` 8, `radius-lg` 10, `radius-xl` 12, `radius-2xl` 16, `radius-3xl` 20, `radius-full` 9999
- Spacing: `spacing-none` 0, `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24, `spacing-4xl` 32, `spacing-5xl` 40, `spacing-7xl` 64
- Type: `Text xs/Regular` 12/18, `Text xs/Medium` 12/18, `Text xs/Semibold` 12/18, `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Text md/Regular` 16/24, `Text md/Medium` 16/24, `Text md/Semibold` 16/24, `Text lg/Semibold` 18/24, `Text lg/Bold` 18/24, `Text xl/Semibold` 20/24, `Display xs/Medium` 28/36, `Display xs/Semibold` 28/36, `Display lg/Medium` 50/60, `Display lg/Semibold` 50/60, `Display xl/Medium` 60/68, `Display xl/Semibold` 60/68, `Display 2xl/Semibold` 100/108

---

### 5. Empty State

**Component:** `Empty state`

Placeholder content shown when a section has no data.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Icon | `Featured icon`, `Illustration`, `File type icon`, `Folder icon` | `Featured icon` |
| Size | `sm`, `md`, `lg` | `sm` |

**Boolean properties:**
- `Featured icon` (default: on)

**Related: Illustration** — decorative illustrations (Cloud, Box, Documents, Credit card) in sm/md/lg sizes.

**When to use:**
- Empty tables, empty search results, first-time user states, no-data dashboards
- `sm` — inline empty states within cards or sidebars
- `md` — standard page-level empty states
- `lg` — full-page onboarding/first-run empty states
- Always include a clear CTA to help the user populate the empty area

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-secondary` #f9f9f9, `bg-brand-solid` #3700ff, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-white` #ffffff, `fg-secondary` #3b4049, `fg-quaternary` #adacaf, `fg-white` #ffffff, …
- Radius: `radius-xs` 4, `radius-md` 8, `radius-lg` 10, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24, `spacing-4xl` 32, `spacing-7xl` 64
- Type: `Text sm/Regular` 14/20, `Text sm/Semibold` 14/20, `Text md/Regular` 16/24, `Text md/Semibold` 16/24, `Text lg/Semibold` 18/24, `Text xl/Semibold` 20/24

---

### 6. Code Snippet

**Component:** `Code snippet`

Code block display with syntax highlighting area.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Simple`, `Tabs` | `Simple` |

**Boolean properties:**
- `Mask content` (default: on) — gradient mask at bottom for overflow
- `Actions` (default: on) — action buttons below the code
- `Header copy button` (default: on) — copy-to-clipboard button

**When to use:**
- API documentation, developer guides, integration setup instructions, code examples
- `Horizontal` — side-by-side code with description
- `Vertical` — stacked code block
- `Vertical with tabs` — multi-language/multi-file code examples

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-secondary` #f9f9f9, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-quaternary` #6e737b, `fg-quaternary` #adacaf, `utility-blue-600` #1570ef, `utility-green-600` #099250, `utility-pink-600` #dd2590, `utility-red-600` #d01a2c, …
- Radius: `radius-sm` 6, `radius-md` 8, `radius-xl` 12, `radius-3xl` 20
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-4xl` 32
- Type: `Text sm/Semibold` 14/20

---

### 7. Activity Feed

**Component:** `Activity feed`

Timeline of events or notifications.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Divider | `Divider`, `Connector`, `False`, `Line` | `Line` |
| Type | `Notifications`, `Messages` | `Notifications` |

**Sub-component: _Feed item base** — individual feed entry.

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md` | `sm` |
| Supporting item | `False`, `Labels`, `File`, `Text` | `False` |
| Connector | `True`, `False` | `True` |

**Boolean (item):** `New dot` (default: on) — unread indicator

**When to use:**
- Audit logs, notification history, comment threads, project activity
- `Notifications` — system events with icons and timestamps
- `Messages` — conversation-style feed with avatars
- `Connector` — visual line connecting sequential events (timeline style)

**Tokens used**
- Color: `bg-primary` #ffffff, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `text-secondary` #3b4049, `text-tertiary` #505861, `text-brand-secondary` #283e8e, `fg-success-secondary` #00d15f, `fg-white` #ffffff; utility palette: brand/blue/indigo/neutral, steps 50/200/300/700
- Radius: `radius-full` 9999
- Spacing: `spacing-none` 0, `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-4xl` 32
- Type: `Text xs/Regular` 12/18, `Text xs/Medium` 12/18, `Text sm/Regular` 14/20, `Text sm/Medium` 14/20

---

### 8. Alert

**Component:** `Alert`

Inline alert banner for contextual messages.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Color | `Default`, `Gray`, `Error`, `Warning`, `Success`, `Brand` | `Default` |
| Size | `Floating`, `Full-width` | `Floating` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Boolean properties:**
- `X close button` (default: on)
- `Actions` (default: on) — action buttons within the alert
- `Supporting text` (default: on)

**When to use:**
- `Error` — form validation errors, system errors, failed operations
- `Warning` — caution messages, deprecation notices, approaching limits
- `Success` — confirmation of completed actions, saved changes
- `Brand` — informational announcements, tips, feature highlights
- `Floating` — contained within a card/section
- `Full-width` — spanning the full page width (top banners)

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-primary_alt` #ffffff, `bg-brand-solid` #3700ff, `border-primary` #c3c6cb, `text-secondary` #3b4049, `text-tertiary` #505861, `text-brand-secondary` #283e8e, `fg-brand-primary` #3700ff, `fg-error-primary` #d01a2c, `fg-warning-primary` #ff6900, `fg-success-primary` #009277, `fg-quaternary` #adacaf, …
- Radius: `radius-none` 0, `radius-md` 8, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24, `spacing-4xl` 32
- Type: `Text sm/Regular` 14/20, `Text sm/Semibold` 14/20

---

### 9. Notification

**Component:** `Notification`

Toast/snackbar notification popup.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Primary icon`, `Image`, `Avatar`, `Gray icon`, `Error icon`, `Warning icon`, `Success icon`, `No icon`, `Progress indicator` | `Primary icon` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Boolean properties:**
- `X close button` (default: on)
- `Actions` (default: on)
- `Supporting text` (default: on)

**When to use:**
- Transient feedback: saved, sent, deleted, error, upload progress
- `Progress indicator` — for ongoing operations (file uploads, processing)
- `Avatar` — social notifications (new message from user, team invite)
- `Image` — rich notifications with preview thumbnails
- Notifications should auto-dismiss after 5-8 seconds unless they contain actions

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-secondary` #f9f9f9, `bg-quaternary` #dbdee1, `border-primary` #c3c6cb, `text-tertiary` #505861, `text-quaternary` #6e737b, `text-brand-secondary` #283e8e, `fg-primary` #1d1f2a, `fg-secondary` #3b4049, `fg-brand-primary` #3700ff, `fg-error-primary` #d01a2c, `fg-success-primary` #009277, …
- Radius: `radius-md` 8, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24, `spacing-4xl` 32
- Type: `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20

---

### 10. Card Header

**Component:** `Card header`

Reusable header for card containers.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Avatar | `False`, `True` | `False` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Boolean properties:**
- `Actions` (default: on) — action buttons
- `Dropdown icon` (default: on)
- `Supporting text` (default: on)
- `Divider` (default: on) — bottom border
- `Badge` (default: on)

**When to use:**
- Top section of any card component: settings cards, data cards, profile cards
- `Avatar=True` — for user/entity cards

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-brand-solid` #3700ff, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `border-secondary_alt` #00000014, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-white` #ffffff, `fg-quaternary` #adacaf
- Radius: `radius-sm` 6, `radius-md` 8, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24
- Type: `Text xs/Medium` 12/18, `Text sm/Regular` 14/20, `Text sm/Semibold` 14/20, `Text md/Semibold` 16/24

---

### 11. Charts


#### Line and Bar Chart
**Component:** `Line and bar chart`

| Property | Options | Default |
|---|---|---|
| Legend | `False`, `Top`, `Right` | `False` |
| Axis labels | `False`, `True` | `False` |
| Chart style | `Line`, `Bar` | `Line` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

#### Pie Chart
**Component:** `Pie chart`

| Property | Options | Default |
|---|---|---|
| Size | `xxs`, `xs`, `sm`, `md`, `lg` | `xxs` |
| Legend | `False`, `True` | `False` |

**Sub-component: _Pie chart** — `Hole`: `False`, `25%`, `50%`, `75%` (donut chart)

#### Activity Gauge
**Component:** `Activity gauge`

| Property | Options | Default |
|---|---|---|
| Size | `xs`, `sm`, `md`, `lg` | `xs` |
| Legend | `False`, `Bottom`, `Right` | `False` |

#### Radar Chart
**Component:** `Radar chart`

| Property | Options | Default |
|---|---|---|
| Legend | `False`, `Right`, `Bottom` | `False` |

#### Chart Marker
**Component:** `Chart marker` — hover tooltip on charts (`Line`, `Dash`, `Minimal` types)

**When to use:**
- `Line` chart — trends over time (revenue, traffic, growth)
- `Bar` chart — comparisons across categories (monthly sales, team performance)
- `Pie` chart — proportion/distribution (market share, budget allocation). Use donut (Hole > 0) for a modern look.
- `Activity gauge` — ring-based progress/completion (fitness, goal tracking)
- `Radar` chart — multi-dimensional comparisons (skill assessments, product feature comparisons)

**Tokens used** (from Figma — Line and bar chart)
- Color: core `border-tertiary` #f0f0f0, `text-tertiary` #505861, `bg-primary` #ffffff; utility palette: brand steps 200/300/400/500/600/700, `utility-neutral-200` #dbdee1
- Spacing: `spacing-none` 0, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24, `spacing-5xl` 40, `spacing-6xl` 48, `spacing-7xl` 64
- Type: `Text xs/Regular` 12/18, `Text xs/Medium` 12/18, `Text sm/Regular` 14/20

---

### 12. Command Bar

**Component:** `Command bar`

Keyboard-driven command palette (Cmd+K / Ctrl+K).

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Users`, `Actions`, `Users menu`, `Integrations menu`, `Command only`, `Empty state` | `Users` |
| Text | `Default`, `Stacked` | `Default` |

**When to use:**
- Power user quick-access: search users, trigger actions, navigate pages, launch integrations
- `Command only` — minimal search-only command palette
- `Actions` — command palette with action shortcuts
- `Stacked` text — two-line items with description

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-overlay` #121318, `bg-brand-solid` #3700ff, `bg-primary_hover` #f9f9f9, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-placeholder` #6e737b, `fg-secondary` #3b4049, `fg-quaternary` #adacaf, …
- Radius: `radius-none` 0, `radius-xs` 4, `radius-sm` 6, `radius-md` 8, `radius-lg` 10, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24, `spacing-4xl` 32, `spacing-5xl` 40, `spacing-11xl` 160
- Type: `Text xs/Semibold` 12/18, `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Text md/Regular` 16/24, `Text md/Semibold` 16/24, `Text lg/Semibold` 18/24

---

### 13. Inline CTA

**Component:** `Inline CTA`

Inline call-to-action banner within content areas.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Image`, `Actions`, `Email field`, `Change plan`, `Upgrade plan`, `Payment method`, `Receipt` | `Image` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**When to use:**
- Upgrade prompts, newsletter signups, plan change CTAs, payment reminders
- Place inline within page content (between sections, within settings)

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-brand-solid` #3700ff, `bg-brand-secondary` #ccd9fe, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-white` #ffffff, `text-placeholder` #6e737b, `fg-success-primary` #009277, `fg-quaternary` #adacaf, …
- Radius: `radius-none` 0, `radius-md` 8, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24
- Type: `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Text md/Regular` 16/24, `Text md/Medium` 16/24, `Text md/Semibold` 16/24, `Display sm/Semibold` 36/44

---

### 14. Video Player 16:9

**Component:** `Video player 16:9`

Standard 16:9 video player with controls.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md`, `lg` | `sm` |
| Playing | `False`, `True` | `False` |

**Boolean properties:**
- `Overlay action` (default: on) — centered play/pause overlay button
- `Actions bar` (default: on) — bottom control bar

**When to use:**
- Embedded video content, tutorials, media galleries, course content

**Tokens used**
- Color: `fg-white` #ffffff, `text-white` #ffffff
- Radius: `radius-sm` 6, `radius-md` 8, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24, `spacing-4xl` 32, `spacing-5xl` 40, `spacing-6xl` 48
- Type: `Text xs/Semibold` 12/18

---

### 15. Message

**Component:** `Message`

Chat message bubble with multiple content types.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Message`, `Message reply`, `File`, `Audio`, `Image`, `Video`, `Link preview`, `Link minimal`, `Writing` | `Message` |
| Sent | `False`, `True` | `False` |
| Actions panel | `False`, `True` | `False` |

**Boolean properties:**
- `Reactions` (default: on)
- `Status icon` (default: on) — read/unread/failed indicator

**Related: Message action** — input area (`Minimal`, `Textarea input`, `Advanced`)

**When to use:**
- Chat/messaging interfaces, support conversations, team communication
- `Sent=True` — messages sent by the current user (right-aligned bubble)
- `Sent=False` — received messages (left-aligned with avatar)
- `Writing` — typing indicator
- `File`, `Audio`, `Image`, `Video` — rich media message types
- `Link preview` / `Link minimal` — URL sharing with preview cards

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-primary_alt` #ffffff, `bg-secondary` #f9f9f9, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `border-brand` #3700ff, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-brand-secondary` #283e8e, `fg-brand-primary_alt` #3700ff, `fg-success-secondary` #00d15f, …
- Radius: `radius-none` 0, `radius-xs` 4, `radius-sm` 6, `radius-md` 8, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-3xl` 24
- Type: `Text xs/Regular` 12/18, `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text md/Regular` 16/24

---

### 16. Loading Indicator

**Component:** `Loading indicator`

Spinner/loading animation.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Style | `Dot circle`, `Line spinner`, `Line simple` | `Line simple` |
| Size | `sm`, `md`, `lg`, `xl` | `sm` |

**Boolean properties:**
- `Supporting text` (default: on) — "Loading..." text

**When to use:**
- Page loads, section refreshes, data fetching, lazy-loading content
- `sm` — inline loading (within buttons, table cells)
- `md`–`lg` — section-level loading
- `xl` — full-page loading

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-tertiary` #f0f0f0, `text-secondary` #3b4049, `fg-brand-primary` #3700ff
- Spacing: `spacing-xl` 16, `spacing-2xl` 20
- Type: `Text sm/Medium` 14/20, `Text lg/Medium` 18/24

---

### 17. Metric Item

**Component:** `Metric item`

KPI/metric display card.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Actions | `False`, `True` | `False` |
| Type | `Simple`, `Icon 01`, `Icon 02`, `Icon 03`, `Icon 04`, `Chart 01`, `Chart 02`, `Chart 03`, `Chart 04` | `Simple` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Boolean properties:**
- `Dropdown icon` (default: on)
- `Featured icon` (default: on)

**Sub-components:**
- **_Chart mini** — sparkline/mini chart (12 chart shapes, Positive/Negative trend)
- **_Change** — trend indicator with arrow and percentage (3 styles, Positive/Negative)

**When to use:**
- Dashboard KPIs, analytics summaries, financial metrics, performance indicators
- `Simple` — metric with label, value, and change indicator
- `Chart *` — metric with embedded sparkline chart
- `Icon *` — metric with featured icon

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-secondary` #f9f9f9, `bg-success-secondary` #c6f7da, `bg-success-solid` #009277, `bg-brand-secondary` #ccd9fe, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-brand-secondary` #283e8e, `text-success-primary` #007f49, …
- Radius: `radius-sm` 6, `radius-md` 8, `radius-lg` 10, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20
- Type: `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Text md/Semibold` 16/24, `Display sm/Semibold` 36/44, `Display md/Semibold` 44/52

---

### 18. Page Header

**Component:** `Page header`

Top-level page header with title, actions, and optional banner.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Style | `Simple`, `Avatar`, `Banner avatar`, `Banner simple`, `Banner avatar centered`, `Banner simple centered` | `Simple` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Boolean properties:**
- `Breadcrumbs` (default: on)
- `Supporting text` (default: on)
- `Actions` (default: on)
- `Search` (default: on)
- `Divider` (default: on)

**When to use:**
- `Simple` — standard page title with actions
- `Avatar` — profile/user page header
- `Banner *` — pages with hero/cover images (profile pages, project pages)
- `* centered` — centered layout for marketing-style pages

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-primary_hover` #f9f9f9, `bg-brand-solid` #3700ff, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-quaternary` #6e737b, `text-placeholder` #6e737b, `text-white` #ffffff, `fg-quaternary` #adacaf, …
- Radius: `radius-xs` 4, `radius-md` 8, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24, `spacing-4xl` 32, `spacing-7xl` 64
- Type: `Text xs/Medium` 12/18, `Text sm/Regular` 14/20, `Text sm/Semibold` 14/20, `Text md/Regular` 16/24, `Text xl/Semibold` 20/24

---

### 19. Section Header

**Component:** `Section header`

Header for content sections within a page.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Tabs | `False`, `True` | `False` |
| Type | `Buttons`, `Search`, `Button group` | `Buttons` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Boolean properties:**
- `Dropdown icon` (default: on)
- `Supporting text` (default: on)
- `Actions` (default: on)
- `Divider` (default: on)

**Related: Section label** — compact section label with optional Required indicator, Supporting text, Help icon, and Actions.

**When to use:**
- Above tables, card grids, form sections, content blocks
- `Tabs=True` — section header with integrated tab navigation
- `Search` — section with filterable content
- `Button group` — section with segmented view controls

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-primary_hover` #f9f9f9, `bg-brand-solid` #3700ff, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-quaternary` #6e737b, `text-placeholder` #6e737b, `text-white` #ffffff, `fg-quaternary` #adacaf, …
- Radius: `radius-xs` 4, `radius-sm` 6, `radius-md` 8
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20
- Type: `Text xs/Medium` 12/18, `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Text md/Regular` 16/24, `Text md/Semibold` 16/24

---

### 20. Section Footer

**Component:** `Section footer`

Footer for content sections and cards.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Section`, `Card` | `Section` |
| Button group | `True`, `False` | `True` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Boolean properties:**
- `Secondary button` (default: on)
- `Actions` (default: on)
- `Divider` (default: on)

**When to use:**
- Below form sections (save/cancel), below card content, pagination areas
- `Card` — footer contained within a card border
- `Section` — full-width section footer

**Tokens used**
- Color: `bg-primary` #ffffff, `bg-primary_hover` #f9f9f9, `bg-brand-solid` #3700ff, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `text-secondary` #3b4049, `text-secondary_hover` #232323, `text-tertiary` #505861, `text-white` #ffffff, `fg-quaternary` #adacaf
- Radius: `radius-md` 8
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24
- Type: `Text sm/Semibold` 14/20

---

## UX, Accessibility & Heuristic Best Practices

### Data Tables
- Always include sortable column headers for key data columns
- Use `Checkbox` lead action for bulk-select operations
- Keep tables horizontally scrollable on mobile (`Breakpoint=Mobile`)
- Use `Alternating fills` dividers for tables with 5+ columns to improve scanability
- Right-align numeric data columns; left-align text columns
- Place action buttons/icons in the rightmost column

### Feedback Components
- **Alerts** are persistent — use for important information that should remain visible
- **Notifications** are transient — use for confirmatory feedback that can auto-dismiss
- Use semantic colors consistently: `Error` for failures, `Warning` for caution, `Success` for confirmation
- Never use only color to convey meaning — always include an icon and text
- Destructive modals must require explicit confirmation (never auto-proceed)

### Empty States
- Always include a descriptive message explaining why the area is empty
- Always include a primary CTA to help the user take the next step
- Use illustrations for first-time/onboarding empty states; use icons for transient empty states

### Layout Structure
- Use **Page header** at the top of every page for consistent page identity
- Use **Section header** to introduce each distinct content block within a page
- Use **Card header** as the top of any card container
- Use **Section footer** for actions that apply to the section above
- Use **Content dividers** sparingly — whitespace is often sufficient

### Charts
- Always include axis labels when data context is not obvious
- Include a legend when showing 2+ data series
- Use Line charts for time-series trends; Bar charts for category comparisons
- Pie/donut charts should have no more than 5-7 segments
- Use mini charts in Metric items for at-a-glance trends

### Modals
- Keep modals focused on a single task — avoid multi-step flows in modals (use pages instead)
- Always include a close button (X) and an Escape key handler
- Trap keyboard focus within the modal while open
- Return focus to the triggering element when the modal closes
- Use `Destructive *` modal types only for irreversible actions

### Badges
- Badge colors must be used consistently across the app (e.g. `Error` always means the same thing)

### Accessibility
- Tables: use proper `<table>`, `<thead>`, `<tbody>`, `<th>` semantics; sortable headers need `aria-sort`
- Modals: use `role="dialog"`, `aria-modal="true"`, `aria-labelledby` pointing to the header
- Alerts: use `role="alert"` for error/warning; `role="status"` for success/info
- Notifications: use `role="status"` with `aria-live="polite"` for non-urgent; `aria-live="assertive"` for errors
- Loading indicators: use `aria-busy="true"` on the loading region; announce completion
- Charts: provide text alternatives (data tables or `aria-label` summaries)
- Video players: require captions/subtitles support and keyboard-accessible controls
- Command bar: support full keyboard navigation (arrow keys, Enter, Escape)
- Empty states: ensure the CTA button is focusable and clearly labeled

### Responsive Design
- Use `Breakpoint=Mobile` variants for Tables, Modals, Alerts, Notifications, Inline CTAs, Page headers, Section headers, Section footers, Metric items, and Card headers
- Tables on mobile should either horizontally scroll or transform to a card/list layout
- Modals on mobile should be full-screen or bottom-sheet style
- Metric items should stack vertically on mobile

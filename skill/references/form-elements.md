
# Form Elements Component Library

> **Veeam adaptation of S1.** Component names, variants and token *names* are inherited from the
> S1 design system unchanged; every color/type value has been re-resolved to Veeam tokens
> (see [`color-variables.md`](color-variables.md), [`typography.md`](typography.md)).
> Where the Veeam PDF specifies a component (buttons, cards, plates), the **Veeam spec** block wins.

This skill defines every component in the FORM ELEMENTS group of the Veeam design system. Use these components — never recreate them from scratch — when building any form, data-entry, or interactive-control UI.

---

## Component Inventory

### 1. Input Field

**Component:** `Input field`

A single-line text input with label, hint text, help icon, and leading/trailing add-ons.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md` | `sm` |
| Type | `Default`, `Leading dropdown`, `Trailing dropdown`, `Leading text`, `Payment input`, `Tags`, `Trailing button` | `Default` |
| Destructive | `False`, `True` | `False` |
| State | `Placeholder`, `Filled`, `Focused`, `Disabled` | `Placeholder` |

**Boolean properties:**
- `Label` (default: on) — field label above the input
- `Hint text` (default: on) — helper text below the input
- `Help icon` (default: on) — tooltip trigger icon beside the label
- `Required *` (default: on) — asterisk indicating required field
- `Icon leading` (default: on) — icon inside the input, left side
- `Time selector` (default: on) — time picker add-on (Date and time type)

**Instance swap:** `Icon swap` — swap the leading/trailing icon

**When to use:**
- `Default` — standard text entry (name, email, URL, etc.)
- `Password` — password entry with show/hide toggle
- `Leading dropdown` / `Trailing dropdown` — input paired with a dropdown (e.g. phone country code + number, currency selector + amount)
- `Leading text` — input with a static text prefix (e.g. "https://")
- `Payment input` — credit card number entry
- `Tags inner` / `Tags outer` — multi-value token entry (e.g. email recipients)
- `Trailing button` — input with an action button (e.g. search, copy)
- `Date and time` — date/time value entry
- `Number counter horizontal` / `Number counter vertical` — numeric stepper
- `OTP` — one-time passcode entry
- `File upload` — inline file attachment input

**Tokens used**
- Color: `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-placeholder` #6e737b, `fg-quaternary` #adacaf, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `border-brand` #3700ff, `bg-primary` #ffffff, `text-error-primary` #d01a2c, `border-error` #ed2b3d, `fg-success-primary` #009277, …
- Radius: `radius-sm` 6, `radius-md` 8
- Spacing: `spacing-none` 0, `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16
- Type: `Text xs/Regular` 12/18, `Text xs/Medium` 12/18, `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Text md/Regular` 16/24, `Text md/Medium` 16/24, `Text md/Semibold` 16/24

---

### 2. Textarea Input Field

**Component:** `Textarea input field`

Multi-line text input for longer-form content.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Default`, `Tags` | `Default` |
| Destructive | `False`, `True` | `False` |
| State | `Placeholder`, `Default`, `Focused`, `Disabled` | `Placeholder` |

**Boolean properties:**
- `Label` (default: on)
- `Hint text` (default: on)
- `Required *` (default: on)
- `Help icon` (default: on)
- `Resize handle` (default: on) — corner drag handle for resizing

**When to use:**
- Comments, descriptions, bio fields, notes, and any content that may exceed a single line
- `Tags inner` / `Tags outer` — multi-value entry within a textarea context

**Tokens used**
- Color: `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-placeholder` #6e737b, `fg-quaternary` #adacaf, `border-primary` #c3c6cb, `border-brand` #3700ff, `border-error` #ed2b3d, `border-error_subtle` #f69aa3, `text-error-primary` #d01a2c, `text-brand-tertiary` #3700ff, `bg-primary` #ffffff
- Radius: `radius-sm` 6, `radius-md` 8
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12
- Type: `Text xs/Regular` 12/18, `Text xs/Medium` 12/18, `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text md/Regular` 16/24

---

### 3. Verification Code Input Field

**Component:** `Verification code input field`

Segmented digit input for verification/OTP codes.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md`, `lg` | `sm` |
| Digits | `4`, `6` | `4` |

**Boolean properties:**
- `Label` (default: on)
- `Hint text` (default: on)

**When to use:**
- Email/phone verification flows, two-factor authentication, PIN entry

**Tokens used**
- Color: `text-tertiary` #505861, `text-secondary` #3b4049, `text-placeholder` #6e737b, `border-primary` #c3c6cb, `bg-primary` #ffffff, `utility-neutral-300` #c3c6cb
- Radius: `radius-lg` 10, `radius-xl` 12
- Spacing: `spacing-xxs` 2, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12
- Type: `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Display lg/Medium` 50/60, `Display xl/Medium` 60/68

---

### 4. Checkbox

**Component:** `Checkbox`

Individual checkbox or radio-style check with optional label and supporting text.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Checked | `False`, `True` | `False` |
| Indeterminate | `False`, `True` | `False` |
| Size | `sm`, `md` | `sm` |
| Type | `Checkbox`, `Radio` | `Checkbox` |
| Text | `False`, `True` | `False` |
| State | `Default`, `Hover`, `Focused`, `Disabled` | `Default` |

**Boolean properties:**
- `Supporting text` (default: on)

**When to use:**
- `Checkbox` type — multi-select options (e.g. "Select all that apply"), terms acceptance, preferences
- `Radio` type — single-select within a list where Radio group is not needed
- `Indeterminate` — parent checkbox with partially selected children (e.g. "Select all" in a table)

**Tokens used**
- Color: `text-secondary` #3b4049, `text-tertiary` #505861, `fg-white` #ffffff, `border-primary` #c3c6cb, `bg-primary` #ffffff, `bg-brand-solid` #3700ff, `bg-tertiary` #f0f0f0
- Radius: `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12
- Type: `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text md/Regular` 16/24, `Text md/Medium` 16/24

---

### 5. Toggle

**Component:** `Toggle`

On/off switch for binary settings.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Default`, `Slim` | `Default` |
| Pressed | `False`, `True` | `False` |
| Size | `sm`, `md` | `sm` |
| Text | `False`, `True` | `False` |
| State | `Default`, `Hover`, `Focus`, `Disabled` | `Default` |

**Boolean properties:**
- `Supporting text` (default: on)

**When to use:**
- Settings that take effect immediately (notifications, dark mode, feature flags)
- `Slim` — compact toggle for dense UIs (settings panels, table rows)
- Prefer Toggle over Checkbox when the change applies instantly without a form submission

**Tokens used**
- Color: `text-secondary` #3b4049, `text-tertiary` #505861, `fg-white` #ffffff, `border-secondary` #dbdee1, `bg-primary` #ffffff, `bg-brand-solid` #3700ff, `bg-brand-solid_hover` #283e8e, `bg-tertiary` #f0f0f0
- Radius: `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-md` 8, `spacing-lg` 12
- Type: `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text md/Regular` 16/24, `Text md/Medium` 16/24

---

### 6. Radio Group

**Component:** `Radio group`

A group of mutually exclusive options.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md` | `sm` |
| Type | `Icon simple`, `Icon card`, `Avatar`, `Payment icon`, `Radio button`, `Checkbox` | `Icon simple` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**Sub-component:** `Radio group item` — individual item within the group.

| Property | Options | Default |
|---|---|---|
| Selected | `False`, `True` | `False` |
| Size | `sm`, `md` | `sm` |
| Type | `Icon simple`, `Icon card`, `Avatar`, `Payment icon`, `Radio button`, `Checkbox` | `Icon simple` |
| State | `Default`, `Hover`, `Focused` | `Default` |
| Breakpoint | `Mobile`, `Desktop` | `Desktop` |

**Boolean properties (item):**
- `Badge` (default: on) — optional badge on the item

**When to use:**
- `Radio button` — standard radio selection (plan tiers, shipping method)
- `Icon simple` / `Icon card` — visual option picker with icons (layout options, category selection)
- `Avatar` — person/team selection
- `Payment icon` — payment method selection (Visa, Mastercard, etc.)
- `Checkbox` — checkbox-styled items within a radio group context

**Tokens used**
- Color: `text-secondary` #3b4049, `text-tertiary` #505861, `text-brand-secondary` #283e8e, `fg-secondary` #3b4049, `fg-white` #ffffff, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `border-brand` #3700ff, `bg-primary` #ffffff, `bg-brand-solid` #3700ff, `utility-green-500` #16b364
- Radius: `radius-xs` 4, `radius-sm` 6, `radius-md` 8, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-none` 0, `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20
- Type: `Text xs/Medium` 12/18, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Text md/Regular` 16/24, `Text md/Medium` 16/24, `Text md/Semibold` 16/24, `Text lg/Medium` 18/24, `Text lg/Semibold` 18/24, `Display sm/Semibold` 36/44, `Display md/Semibold` 44/52

---

### 7. Select

**Component:** `Select`

Single-selection dropdown.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Size | `sm`, `md` | `sm` |
| Type | `Default`, `Icon leading`, `Avatar leading`, `Dot leading`, `Search`, `Tags` | `Default` |
| State | `Placeholder`, `Default`, `Focused`, `Open`, `Disabled` | `Placeholder` |

**Boolean properties:**
- `Label` (default: on)
- `Hint text` (default: on)
- `Supporting text` (default: on)
- `Scroll bar` (default: on)
- `Required *` (default: on)
- `Help icon` (default: on)
- `Shortcut` (default: on) — keyboard shortcut hint

**Instance swap:** `Icon swap` — swap the leading icon

**When to use:**
- Choosing one option from a long list (country, timezone, category)
- `Search` — filterable select for large option sets
- `Icon leading` / `Avatar leading` / `Dot leading` — visual differentiation of options (status, user, category)
- `Tags` — selected value shown as tag/chip

**Tokens used**
- Color: `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-placeholder` #6e737b, `fg-quaternary` #adacaf, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `border-brand` #3700ff, `bg-primary` #ffffff, `bg-primary_hover` #f9f9f9, `fg-brand-primary` #3700ff, `fg-success-secondary` #00d15f, …
- Radius: `radius-xs` 4, `radius-sm` 6, `radius-md` 8, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12
- Type: `Text xs/Regular` 12/18, `Text xs/Medium` 12/18, `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text md/Regular` 16/24, `Text md/Medium` 16/24

---

### 8. Slider

**Component:** `Slider`

Range slider for selecting numeric values.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Label | `False`, `Bottom`, `Top floating` | `False` |
| Right control | `25%`, `50%`, `75%`, `100%` | `25%` |
| Left control | `0%`, `25%`, `50%`, `75%` | `0%` |

**When to use:**
- Price range filters, volume/brightness control, budget allocation
- Use two control handles for range selection (min/max)
- `Top floating` label — shows value in a floating tooltip above the handle
- `Bottom` label — shows value below the track

**Tokens used**
- Color: `text-primary` #1d1f2a, `text-secondary` #3b4049, `fg-brand-primary` #3700ff, `bg-primary` #ffffff, `bg-primary_alt` #ffffff, `bg-brand-solid` #3700ff, `bg-quaternary` #dbdee1, `border-secondary_alt` #00000014
- Radius: `radius-md` 8, `radius-full` 9999
- Spacing: `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12
- Type: `Text xs/Semibold` 12/18, `Text md/Medium` 16/24

---

### 9. Progress Bar

**Component:** `Progress bar`

Horizontal bar showing completion progress.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Progress | `0%` through `100%` (10% increments) | `0%` |
| Label | `False`, `Right`, `Bottom`, `Top floating`, `Bottom floating` | `False` |

**When to use:**
- File upload progress, onboarding completion, multi-step form progress, loading states

**Tokens used**
- Color: `text-secondary` #3b4049, `fg-brand-primary` #3700ff, `bg-primary` #ffffff, `bg-primary_alt` #ffffff, `bg-quaternary` #dbdee1, `border-secondary_alt` #00000014
- Radius: `radius-md` 8, `radius-full` 9999
- Spacing: `spacing-xs` 4, `spacing-md` 8, `spacing-lg` 12
- Type: `Text xs/Semibold` 12/18, `Text sm/Medium` 14/20

---

### 10. Progress Circle

**Component:** `Progress circle`

Circular/semi-circular progress indicator.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Size | `xxs`, `xs`, `sm`, `md`, `lg` | `xxs` |
| Shape | `Circle`, `Half circle` | `Circle` |

**Boolean properties:**
- `Label` (default: on) — percentage text inside the circle

**When to use:**
- Dashboard KPIs, storage usage, skill/score visualization
- `Half circle` — gauge-style meter (e.g. performance score)

**Tokens used**
- Color: `text-primary` #1d1f2a, `text-tertiary` #505861, `fg-brand-primary` #3700ff, `bg-primary` #ffffff, `bg-quaternary` #dbdee1
- Spacing: `spacing-xs` 4
- Type: `Text xs/Medium` 12/18, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Display xs/Semibold` 28/36, `Display sm/Semibold` 36/44, `Display md/Semibold` 44/52, `Display lg/Semibold` 50/60

---

### 11. Tooltip

**Component:** `Tooltip`

Contextual information popup triggered on hover/focus.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Supporting text | `False`, `True` | `False` |
| Arrow | `None`, `Bottom left`, `Bottom right`, `Left`, `Right`, `Bottom center`, `Top center` | `None` |

**Text property:** `Text` (default: "This is a tooltip")

**When to use:**
- Explaining icons, abbreviations, truncated text, or disabled controls
- Always pair with a keyboard-focusable trigger for accessibility

**Tokens used**
- Color: `text-white` #ffffff, `bg-primary` #ffffff, `bg-primary-solid` #121318
- Radius: `radius-md` 8
- Spacing: `spacing-xxs` 2, `spacing-md` 8, `spacing-lg` 12
- Type: `Text xs/Medium` 12/18, `Text xs/Semibold` 12/18

---

### 12. Help Icon

**Component:** `Help icon`

Question-mark icon that reveals a tooltip on interaction.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Open | `False`, `True` | `False` |
| Supporting text | `False`, `True` | `False` |
| Tooltip | `Top no arrow`, `Top arrow`, `Left`, `Top left`, `Bottom`, `Right`, `Top right` | `Top no arrow` |

**Boolean properties:**
- `Cursor` (default: on)

**When to use:**
- Beside form labels to explain field purpose or expected format
- On settings to clarify impact of a toggle or option

**Tokens used**
- Color: `text-white` #ffffff, `fg-quaternary` #adacaf, `fg-quaternary_hover` #6e737b, `bg-primary` #ffffff, `bg-primary-solid` #121318
- Radius: `radius-md` 8
- Spacing: `spacing-xxs` 2, `spacing-md` 8, `spacing-lg` 12
- Type: `Text xs/Medium` 12/18, `Text xs/Semibold` 12/18

---

### 13. File Upload

**Component:** `File upload`

Drag-and-drop file upload zone with queued file list.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Files queued | `True`, `False` | `False` |
| Type | `Progress bar`, `Progress fill` | `Progress bar` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**When to use:**
- Document uploads, image uploads, bulk file imports
- `Progress bar` — shows individual file progress as a bar
- `Progress fill` — shows progress as a fill overlay on the file icon

**Tokens used**
- Color: `text-secondary` #3b4049, `text-tertiary` #505861, `text-quaternary` #6e737b, `text-brand-secondary` #283e8e, `text-success-primary` #007f49, `fg-secondary` #3b4049, `fg-quaternary` #adacaf, `fg-brand-primary` #3700ff, `fg-white` #ffffff, `fg-success-primary` #009277, `border-primary` #c3c6cb, `border-secondary` #dbdee1, …
- Radius: `radius-none` 0, `radius-sm` 6, `radius-md` 8, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-3xl` 24
- Type: `Text xs/Regular` 12/18, `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20

---

### 14. Text Editor

**Component:** `Text editor`

Rich text editor with formatting toolbar.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Default`, `Floating toolbar` | `Default` |
| Size | `sm`, `md` | `sm` |

**Boolean properties:**
- `Scroll bar` (default: on)
- `Hint text` (default: on)

**Sub-components:**
- `Text editor toolbar` — `Simple` or `Advanced` type, with optional `Dropdowns`
- `Text editor tooltip` — `Simple` or `Advanced` formatting tooltip

**When to use:**
- Blog/article authoring, comment editing with formatting, email composition, note-taking
- `Default` — toolbar pinned at top
- `Floating toolbar` — toolbar appears on text selection

**Tokens used**
- Color: `text-primary` #1d1f2a, `text-tertiary` #505861, `fg-quaternary` #adacaf, `border-primary` #c3c6cb, `border-secondary_alt` #00000014, `bg-primary` #ffffff, `utility-neutral-900` #1d1f2a
- Radius: `radius-sm` 6, `radius-md` 8, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20
- Type: `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text md/Regular` 16/24

---

### 15. Button Group

**Component:** `Button group`

Segmented control / button bar for toggling between views or options.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Icon | `False`, `Leading`, `Only` | `False` |

**When to use:**
- View switchers (list/grid/map), filter toggles, segmented controls
- `Icon Only` — compact toolbar actions
- `Leading` — icon + text per segment

**Tokens used**
- Color: `text-secondary` #3b4049, `fg-quaternary` #adacaf, `border-primary` #c3c6cb, `bg-primary` #ffffff
- Radius: `radius-md` 8
- Spacing: `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16
- Type: `Text sm/Semibold` 14/20

---

### 16. Date Picker Dropdown

**Component:** `Date picker dropdown`

Date selection dropdown with calendar.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Opened | `False`, `True` | `False` |
| Type | `Dual dates`, `Single date` | `Dual dates` |
| State | `Placeholder`, `Active` | `Placeholder` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**When to use:**
- `Single date` — birthday, due date, event date
- `Dual dates` — date range (check-in/check-out, reporting period)
- `Available times` — date + time slot selection (booking, scheduling)

**Tokens used**
- Color: `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-quaternary` #6e737b, `text-placeholder` #6e737b, `text-brand-secondary` #283e8e, `fg-secondary` #3b4049, `fg-quaternary` #adacaf, `fg-brand-primary` #3700ff, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `bg-primary` #ffffff, `bg-brand-solid` #3700ff, …
- Radius: `radius-sm` 6, `radius-md` 8, `radius-2xl` 16, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24
- Type: `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Text md/Regular` 16/24

---

### 17. Date Picker Modal

**Component:** `Date picker modal`

Full-screen or centered modal date picker.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Dual dates`, `Single date` | `Dual dates` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**When to use:**
- Mobile date selection, complex date range picking, calendar-heavy flows where the dropdown would be too small

**Tokens used**
- Color: `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-white` #ffffff, `text-brand-secondary` #283e8e, `fg-secondary` #3b4049, `fg-quaternary` #adacaf, `fg-brand-primary` #3700ff, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `bg-primary` #ffffff, `bg-secondary` #f9f9f9, `bg-overlay` #121318, …
- Radius: `radius-sm` 6, `radius-md` 8, `radius-2xl` 16
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `container-padding-mobile` 16, `spacing-2xl` 20, `spacing-3xl` 24, `spacing-4xl` 32, `container-padding-desktop` 32, `spacing-8xl` 80
- Type: `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Text md/Regular` 16/24

---

### 18. Calendar

**Component:** `Calendar`

Full calendar view for event display and scheduling.

**Variant properties:**

| Property | Options | Default |
|---|---|---|
| Type | `Month view`, `Week view`, `Day view` | `Month view` |
| Breakpoint | `Desktop`, `Mobile` | `Desktop` |

**When to use:**
- Event/schedule management, booking systems, project timelines
- `Month view` — overview of events across a month
- `Week view` — detailed weekly schedule with time slots
- `Day view` — granular daily schedule

**Tokens used**
- Color: `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-quaternary` #6e737b, `text-brand-secondary` #283e8e, `fg-white` #ffffff, `fg-quaternary` #adacaf, `fg-brand-primary` #3700ff, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `bg-primary` #ffffff, `bg-brand-solid` #3700ff, …
- Radius: `radius-xxs` 2, `radius-sm` 6, `radius-md` 8, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-2xl` 20, `spacing-3xl` 24
- Type: `Text xs/Regular` 12/18, `Text xs/Medium` 12/18, `Text xs/Semibold` 12/18, `Text sm/Regular` 14/20, `Text sm/Medium` 14/20, `Text sm/Semibold` 14/20, `Text md/Semibold` 16/24, `Text lg/Semibold` 18/24, `Text lg/Bold` 18/24

---

### 19. Dropdown Menu

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
- `Button simple` / `Button advanced` — action menus from buttons
- `Icon simple` / `Icon advanced` — kebab/meatball menus, toolbar overflow
- `Search simple` / `Search advanced` — filterable dropdown menus
- `Account *` — user/profile menus in navigation

**Tokens used**
- Color: `text-primary` #1d1f2a, `text-secondary` #3b4049, `text-tertiary` #505861, `text-quaternary` #6e737b, `text-placeholder` #6e737b, `fg-white` #ffffff, `fg-quaternary` #adacaf, `fg-brand-primary` #3700ff, `border-primary` #c3c6cb, `border-secondary` #dbdee1, `bg-primary` #ffffff, `bg-brand-solid` #3700ff, …
- Radius: `radius-xs` 4, `radius-sm` 6, `radius-md` 8, `radius-lg` 10, `radius-xl` 12, `radius-full` 9999
- Spacing: `spacing-xxs` 2, `spacing-xs` 4, `spacing-sm` 6, `spacing-md` 8, `spacing-lg` 12, `spacing-xl` 16, `spacing-3xl` 24
- Type: `Text xs/Regular` 12/18, `Text xs/Medium` 12/18, `Text xs/Semibold` 12/18, `Text sm/Regular` 14/20, `Text sm/Semibold` 14/20

---

## Shared Size Convention

Most form components use a consistent size scale:
- **sm** — compact density; use in data-heavy UIs, tables, sidebars
- **md** — standard density; use in most forms and settings pages
- **lg** — touch-friendly; use in mobile-first or marketing/onboarding flows

Always use the same size across all form elements within a single form for visual consistency.

---

## UX, Accessibility & Heuristic Best Practices

### Labels & Help Text
- Always show `Label` on form fields (do not rely on placeholder text alone)
- Use `Hint text` to clarify expected format or constraints (e.g. "Must be at least 8 characters")
- Use `Help icon` for longer explanations that would clutter the form
- Mark required fields with `Required *`; alternatively, mark optional fields when most are required

### States
- Show `Focused` state on keyboard navigation for all interactive elements
- Use `Disabled` sparingly — prefer hiding unavailable options or explaining why they are disabled via a tooltip
- Use `Destructive=True` on Input fields only for real-time validation errors — never as the default state
- Always pair error states with clear, specific error messages in `Hint text`

### Input Selection Guide
- **< 5 options, single-select:** Radio group (all options visible)
- **< 5 options, multi-select:** Checkbox group
- **5-15 options, single-select:** Select dropdown
- **5+ options, multi-select:** searchable Select, or a scrollable Checkbox group
- **Binary on/off, immediate effect:** Toggle
- **Binary yes/no, form submission:** Checkbox
- **Numeric range:** Slider (with Input field for precise entry when needed)
- **Date/time:** Date picker dropdown (inline) or Date picker modal (mobile)
- **Long text:** Textarea input field
- **Rich text:** Text editor
- **File attachment:** File upload

### Grouping & Layout
- Group related fields with consistent spacing
- Place labels above inputs (not inline) for better scanning and mobile readability
- Align form elements to a consistent left edge
- Use Button group for 2-5 mutually exclusive view/filter toggles
- Place primary actions (submit) at the bottom-right of forms; destructive actions should require confirmation

### Accessibility
- Every form control must have a visible label (use the `Label` boolean — keep it on)
- Do not use color alone to convey state (error, success) — always include text or an icon
- Checkboxes and Radio groups must have a group label describing the question
- Toggles should describe what happens when on, not just the setting name (e.g. "Enable notifications" not just "Notifications")
- Ensure sufficient color contrast between input text, placeholder text, and backgrounds
- Support keyboard navigation: Tab to move between fields, Space/Enter to activate, Escape to close dropdowns
- Slider should always have a visible label and current value

### Responsive Design
- Use `Breakpoint=Mobile` variants for Radio group items, Date pickers, Calendars, and File upload on small screens
- On mobile, prefer full-width inputs and larger touch targets (Size=`lg` or `md`)
- Date picker modal is preferred over dropdown on mobile for better usability

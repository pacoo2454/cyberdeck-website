# CyberDeck Website — Design Document

**Project:** CyberDeck Marketing Website
**Stack:** HTML5 + CSS3 (no JavaScript, no PHP)
**Layout:** Single-page application with anchor-based section navigation
**Date:** March 2026

---

## 1. Project Overview

CyberDeck is a native mobile application that lets users remotely control Companion over a local network. The website serves three goals:

1. **Showcase** the app with screenshots and a compelling first impression
2. **Educate** users on how to install and use it
3. **Support** users by providing developer contact info

The design philosophy is **minimal and modern** — generous whitespace, a focused color palette, clean typography, and purposeful use of imagery. No heavy frameworks are needed; well-structured HTML and CSS is sufficient.

---

## 2. Visual Identity

### 2.1 Color Palette

The "Cyber" in CyberDeck suggests a dark, technical aesthetic. The palette below pairs a near-black background with a sharp cyan accent, creating a professional yet distinctly tech feel.

| Role              | Name             | Hex       | Usage                                              |
|-------------------|------------------|-----------|-----------------------------------------------------|
| Background        | Void Black       | `#0d0f14` | Page background, nav background                    |
| Surface           | Deep Slate       | `#161b25` | Section backgrounds, cards                         |
| Surface Alt       | Charcoal         | `#1e2535` | Alternating section tint, hover states             |
| Primary Accent    | Cyber Cyan       | `#00c8ff` | Nav links (active), buttons, highlights, borders   |
| Secondary Accent  | Soft Blue        | `#4a90d9` | Secondary buttons, links in body text              |
| Text Primary      | Off White        | `#e8eaf0` | All headings and body text                         |
| Text Secondary    | Muted Grey       | `#8892a4` | Subtitles, captions, metadata                      |
| Divider           | Subtle Line      | `#232b3a` | Horizontal rules, card borders                     |

### 2.2 Typography

Use Google Fonts (loaded via `<link>` in `<head>`) for zero-dependency web fonts.

| Role            | Font Family              | Weights   | Notes                                         |
|-----------------|--------------------------|-----------|-----------------------------------------------|
| Headings (H1–H3)| **Space Grotesk**        | 500, 700  | Modern, slightly geometric — fits the brand   |
| Body / UI       | **Inter**                | 400, 500  | Neutral, highly legible at all sizes          |
| Code / Labels   | **JetBrains Mono**       | 400       | Use for technical labels, version strings     |

**Type scale (desktop):**

| Element    | Size     | Weight | Line Height |
|------------|----------|--------|-------------|
| H1         | 3.5rem   | 700    | 1.1         |
| H2         | 2.25rem  | 700    | 1.2         |
| H3         | 1.375rem | 500    | 1.3         |
| Body       | 1rem     | 400    | 1.7         |
| Caption    | 0.875rem | 400    | 1.5         |
| Label/Mono | 0.8125rem| 400    | 1.4         |

Scale down H1 to ~2.25rem and H2 to ~1.6rem on mobile.

---

## 3. Layout & Grid

The site uses a centered content column with a maximum width of **1100px**, horizontally padded at `5vw` on smaller screens. A CSS custom property `--container-width: 1100px` keeps this consistent.

```css
.container {
  width: min(var(--container-width), 100% - 2 * 5vw);
  margin-inline: auto;
}
```

Sections alternate between `#0d0f14` (Void Black) and `#161b25` (Deep Slate) backgrounds for visual separation without needing dividers.

---

## 4. Site Structure

### 4.1 Page Skeleton (HTML)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CyberDeck — Remote Companion Control</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <!-- Google Fonts: Space Grotesk, Inter, JetBrains Mono -->
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header id="site-header"> ... </header>
  <main>
    <section id="home">     <!-- Section 1: Hero / Showcase --></section>
    <section id="guide">    <!-- Section 2: How to Use      --></section>
    <section id="contact">  <!-- Section 3: Developer Info  --></section>
  </main>
  <footer> ... </footer>
</body>
</html>
```

---

## 5. Component Specifications

### 5.1 Navigation Bar (`<header>`)

- **Position:** `position: sticky; top: 0;` so it stays visible while scrolling
- **Background:** Void Black with a subtle `backdrop-filter: blur(12px)` for a frosted glass effect. Use a semi-transparent background (`rgba(13, 15, 20, 0.85)`) so page content scrolls behind it.
- **Border Bottom:** 1px solid `#232b3a` (Divider)
- **Height:** 64px
- **Content:** Logo on the left, nav links on the right

**Logo area:** The app icon image (e.g. `icon.png`) displayed at 32×32px, followed by the wordmark "CyberDeck" in Space Grotesk 600 weight, Off White.

**Navigation links:** Three anchor links — `Home`, `Guide`, `Contact`. These use `scroll-behavior: smooth` (set on `<html>`) to animate scrolling to the target section. The active/hover state should color the link text in Cyber Cyan (`#00c8ff`).

```
[ 🟦 CyberDeck ]                 [ Home ]  [ Guide ]  [ Contact ]
```

**Responsive (≤768px):** Collapse nav links to a simple row below the logo, or keep them inline but reduce font size. Since JavaScript is excluded, a persistent compact row is the right approach.

---

### 5.2 Section 1 — Home (Hero + Showcase)

**Background:** Void Black
**Goal:** Make a strong first impression, communicate the app's purpose instantly.

**Layout:**

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   [App Icon 96px]                                   │
│   CyberDeck                   ← H1                  │
│   Remote control for Companion on your mobile device│
│                               ← Subheading          │
│   [App Store Badge]  [Google Play Badge]            │
│                                                     │
│   ─────────── Screenshots ───────────               │
│   [Screen 1]    [Screen 2]    [Screen 3]            │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Details:**

- The icon, H1, subheading, and badges form a centered hero block. Padding top/bottom: `8rem`.
- The subheading should be 1.2rem, Muted Grey, max-width ~540px, centered.
- App store badges are optional placeholders initially — simple linked images or styled `<a>` buttons reading "Available on iOS" / "Available on Android".
- The screenshots row uses CSS `display: flex; gap: 1.5rem; justify-content: center; flex-wrap: wrap;`. Each screenshot is displayed inside a styled phone "frame" div (rounded corners `border-radius: 2rem`, a thin 2px Divider border, subtle box-shadow). Max width per screenshot: 200px.
- A thin horizontal rule or gradient fade (using a CSS `border-image` linear gradient in Cyber Cyan → transparent) separates the hero from the screenshots.

---

### 5.3 Section 2 — Guide (How to Use)

**Background:** Deep Slate (`#161b25`)
**Goal:** Walk users through setup and daily use in a clear, approachable way.

**Layout:**

```
┌─────────────────────────────────────────────────────┐
│  How to Use CyberDeck          ← H2, centered        │
│  ─────────────────────────                           │
│                                                      │
│  Step 1: Install the App                             │
│  [Screenshot]    Description text alongside image   │
│                                                      │
│  Step 2: Connect to Companion                        │
│  Description text alongside image    [Screenshot]   │
│                                                      │
│  Step 3: Control Your Setup                          │
│  [Screenshot]    Description text alongside image   │
│                                                      │
└─────────────────────────────────────────────────────┘
```

**Details:**

- Each step is a two-column row: image on one side, text on the other, alternating left/right using `flex-direction: row` and `row-reverse`.
- On mobile (≤768px), stack to a single column with the image above the text.
- Step labels use the JetBrains Mono font in Cyber Cyan to look like terminal step numbers (e.g. `01 /`, `02 /`, `03 /`).
- H3 for step titles, body text for descriptions. Use `max-width: 480px` on the text column.
- Images use the same phone frame style as Section 1 for consistency.

**CSS grid snippet for a step row:**

```css
.guide-step {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}

.guide-step.reverse {
  direction: rtl; /* reverses column order */
}

.guide-step.reverse > * {
  direction: ltr; /* resets text direction for children */
}
```

---

### 5.4 Section 3 — Contact (Developer Info)

**Background:** Void Black
**Goal:** Humanize the project and make it easy to reach out for support.

**Layout:**

```
┌─────────────────────────────────────────────────────┐
│  About & Support               ← H2, centered       │
│  ─────────────────────────                          │
│                                                     │
│   ┌─────────────────┐   ┌────────────────────────┐  │
│   │  Developer       │   │  Support               │  │
│   │  [Avatar/Icon]   │   │  For bugs or help,     │  │
│   │  Name            │   │  reach out via:        │  │
│   │  Bio blurb       │   │  ✉ support@email.com   │  │
│   │  Links: GitHub   │   │  🐛 GitHub Issues      │  │
│   └─────────────────┘   └────────────────────────┘  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Details:**

- Two cards side by side, stacking to single column on mobile.
- Cards use Surface Alt background (`#1e2535`), `border-radius: 1rem`, `padding: 2rem`, and a 1px Divider border.
- A subtle Cyber Cyan left border accent (`border-left: 3px solid #00c8ff`) can distinguish card type.
- Contact links are styled as text links in Secondary Accent Blue, underline on hover.
- Avoid `<form>` elements since there's no server-side processing. Direct email links (`mailto:`) and external links (GitHub Issues) are the cleanest solution.

---

### 5.5 Footer

Minimal one-line footer:

```
© 2026 CyberDeck. All rights reserved.
```

- Background: Void Black, centered text, Muted Grey color, 0.875rem, padding `2rem 0`.
- Subtle top border in Divider color.

---

## 6. CSS Architecture

Organize `style.css` in this order:

1. **Custom Properties** — All colors, fonts, sizes as `:root` variables
2. **Reset / Base** — `*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }`, base `body` styles
3. **Typography** — Font imports, base `h1–h6`, `p`, `a`, `code` rules
4. **Layout Utilities** — `.container`, `.section`, spacing helpers
5. **Components** — Nav, hero, phone frame, guide step, cards, footer
6. **Media Queries** — All responsive overrides at the bottom, mobile-first or desktop-first (desktop-first is simpler for this scale)

**Key CSS Custom Properties:**

```css
:root {
  --color-bg:          #0d0f14;
  --color-surface:     #161b25;
  --color-surface-alt: #1e2535;
  --color-accent:      #00c8ff;
  --color-accent-soft: #4a90d9;
  --color-text:        #e8eaf0;
  --color-text-muted:  #8892a4;
  --color-divider:     #232b3a;
  --font-heading:      'Space Grotesk', sans-serif;
  --font-body:         'Inter', sans-serif;
  --font-mono:         'JetBrains Mono', monospace;
  --container-width:   1100px;
  --section-padding:   6rem 0;
  --radius-card:       1rem;
  --radius-phone:      2rem;
}
```

---

## 7. Responsive Breakpoints

| Breakpoint | Max Width | Changes                                              |
|------------|-----------|-------------------------------------------------------|
| Desktop    | > 1024px  | Full two-column layouts, max nav spacing              |
| Tablet     | ≤ 1024px  | Reduce padding, shrink H1 slightly                    |
| Mobile     | ≤ 768px   | Stack all columns, compact nav row, smaller type scale|
| Small      | ≤ 480px   | Tighten section padding further, full-width cards     |

---

## 8. Assets & Placeholders

| Asset                  | Format   | Recommended Size | Notes                                 |
|------------------------|----------|------------------|---------------------------------------|
| App icon               | PNG/SVG  | 96×96 (hero), 32×32 (nav) | SVG preferred for sharpness   |
| App screenshots        | PNG      | ~390×844px       | Portrait orientation, phone frames    |
| Developer avatar       | PNG/JPG  | 128×128px        | Optional, circular crop via CSS       |
| App Store badge        | SVG/PNG  | Standard Apple/Google assets | Link to store listing   |

During development, use placeholder images with a `background-color: var(--color-surface-alt)` and fixed dimensions until real screenshots are available.

---

## 9. Accessibility Notes

- Use semantic HTML elements: `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`, `<h1>`–`<h3>`.
- All images must have descriptive `alt` attributes.
- Anchor links must have visible focus styles (`:focus-visible` outline in Cyber Cyan).
- Color contrast: Off White (`#e8eaf0`) on Void Black (`#0d0f14`) exceeds WCAG AA requirements.
- Smooth scroll is declared on `html { scroll-behavior: smooth; }` — no JavaScript needed.

---

## 10. File Structure

```
cyberdeck-website/
├── index.html
├── style.css
└── assets/
    ├── icon.svg
    ├── screenshot-1.png
    ├── screenshot-2.png
    ├── screenshot-3.png
    └── avatar.png
```

A single `index.html` and `style.css` is all that's needed. There is no build process, no dependencies, and no server-side code.

---

*End of Design Document*

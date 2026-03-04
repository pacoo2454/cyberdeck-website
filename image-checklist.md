# CyberDeck Website — Image Checklist

A reference list of every image asset needed for the site. Place all files
in the `assets/` folder alongside `index.html`, unless noted otherwise.

---

## App Icon

| File | Used In | Recommended Size | Notes |
|------|---------|-----------------|-------|
| `assets/icon.svg` | Nav bar & hero section | SVG (scales to 32×32 and 96×96) | SVG preferred for sharpness at all sizes. A PNG works if SVG isn't available. |

---

## Screenshots — Home Page Showcase

These three appear in the scrolling row at the bottom of the home section.

| File | Description | Recommended Size |
|------|-------------|-----------------|
| `assets/screenshot-1.png` | Home / main screen of the app | ~390×844 px (portrait) |
| `assets/screenshot-2.png` | Connection screen | ~390×844 px (portrait) |
| `assets/screenshot-3.png` | Controls / button grid screen | ~390×844 px (portrait) |

---

## Screenshots — Guide Section

These appear alongside the step-by-step instructions. They can reuse the
showcase screenshots above if the content is the same — they don't need to
be six unique images.

| File | Description | Recommended Size |
|------|-------------|-----------------|
| `assets/screenshot-install.png` | App Store / Play Store listing, or first-launch screen | ~390×844 px (portrait) |
| `assets/screenshot-connect.png` | Connection / setup screen | ~390×844 px (portrait) |
| `assets/screenshot-control.png` | Button grid in active use | ~390×844 px (portrait) |

---

## Contact Section

| File | Used In | Recommended Size | Notes |
|------|---------|-----------------|-------|
| `assets/avatar.png` | Developer card in the Contact section | 128×128 px (square) | Displayed as a circle via CSS — crop tightly before saving. |

---

## Social Media Preview

| File | Used In | Required Size | Notes |
|------|---------|--------------|-------|
| `assets/og-image.png` | `og:image` and `twitter:image` meta tags — shown when the site is shared on social media, Discord, iMessage, etc. | **1200×630 px** | A simple branded graphic works well: app icon + "CyberDeck" wordmark on the dark background (`#0d0f14`). |

---

## App Store Badges

These are not currently wired up as image files — the site uses styled text
buttons as placeholders. When you have the official badge images, let me know
and I can swap them in.

| Badge | Where to Download | Notes |
|-------|------------------|-------|
| Apple App Store badge | [Apple Marketing Guidelines](https://developer.apple.com/app-store/marketing/guidelines/) | Apple requires use of their official artwork. |
| Google Play badge | [Google Play Badge Generator](https://play.google.com/intl/en_us/badges/) | Google also provides official badge assets. |

---

## Favicon & Touch Icons *(not yet added to the site)*

These need to be added to both `index.html` and `updates.html` once the
files are ready. Let me know when you have them and I can wire up the
`<link>` tags.

| File | Used In | Required Size | Notes |
|------|---------|--------------|-------|
| `assets/favicon.ico` or `assets/favicon.svg` | Browser tab, bookmarks | 32×32 px (ICO or SVG) | An export of the app icon works perfectly. |
| `assets/apple-touch-icon.png` | iOS/iPadOS home screen shortcut | **180×180 px** | Used when a visitor adds the site to their iPhone or iPad home screen. |

---

## Summary

| # | File | Status |
|---|------|--------|
| 1 | `assets/icon.svg` | ☐ Needed |
| 2 | `assets/screenshot-1.png` | ☐ Needed |
| 3 | `assets/screenshot-2.png` | ☐ Needed |
| 4 | `assets/screenshot-3.png` | ☐ Needed |
| 5 | `assets/screenshot-install.png` | ☐ Needed |
| 6 | `assets/screenshot-connect.png` | ☐ Needed |
| 7 | `assets/screenshot-control.png` | ☐ Needed |
| 8 | `assets/avatar.png` | ☐ Needed |
| 9 | `assets/og-image.png` | ☐ Needed |
| 10 | Apple App Store badge | ☐ Needed (download from Apple) |
| 11 | Google Play badge | ☐ Needed (download from Google) |
| 12 | `assets/favicon.ico` or `assets/favicon.svg` | ☐ Needed |
| 13 | `assets/apple-touch-icon.png` | ☐ Needed |

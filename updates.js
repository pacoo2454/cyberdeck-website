/**
 * CyberDeck — updates.js
 *
 * This file is your "database" for news and release notes.
 * To add a new update:
 *   1. Copy the template entry below.
 *   2. Paste it at the TOP of the CYBERDECK_UPDATES array (newest first).
 *   3. Fill in the fields, then save — the site updates automatically.
 *
 * ── TAGS ────────────────────────────────────────────────────────
 *   "Release"      → cyan   (new versions, feature launches)
 *   "Fix"          → amber  (bug fixes, patches)
 *   "Announcement" → blue   (news, plans, general updates)
 *
 * ── BODY TEXT & FORMATTING ──────────────────────────────────────
 *   The body field supports a simple Markdown-like syntax.
 *   You can write as much as you like — on the main page a preview
 *   is shown with a fade, and the full text appears on the Updates
 *   page. Use the following formatting in your strings:
 *
 *   **bold text**          →  bold
 *   *italic text*          →  italic
 *   - item                 →  bullet point (one per line)
 *   \n                     →  line break within a paragraph
 *   \n\n                   →  new paragraph or start of a list
 *
 *   Example body with mixed formatting:
 *   "Version 1.3.0 highlights:\n\n- **New feature** added\n- *Improved* performance\n\nUpdate through your app store."
 *
 * ── TEMPLATE (copy & paste to add a new entry) ──────────────────
 *   {
 *     id:    4,
 *     date:  "YYYY-MM-DD",
 *     tag:   "Release",
 *     title: "Short headline goes here",
 *     body:  "Your update text goes here. Use **bold**, *italic*, and\n\n- bullet points\n- like this\n\nfor longer patch notes."
 *   },
 * ────────────────────────────────────────────────────────────────
 */

const CYBERDECK_UPDATES = [
  {
    id:    3,
    date:  "2026-03-01",
    tag:   "Release",
    title: "Version 1.2.0 — Custom Layouts",
    body:  "Version 1.2.0 is now available with the following changes:\n\n- **Layout profiles** — save and switch between multiple button configurations without reconfiguring each time\n- **Improved reconnection** — the app recovers significantly faster after a network dropout or screen lock\n- **iPad support** — layout now scales correctly on all iPad screen sizes\n\nUpdate through your app store to get started."
  },
  {
    id:    2,
    date:  "2026-01-15",
    tag:   "Fix",
    title: "Connection Stability Improvements",
    body:  "Resolved an issue where the app would occasionally drop its connection when the phone screen locked. The app now maintains its session reliably in the background.\n\nIf you were experiencing frequent disconnects, this update should resolve them entirely."
  },
  {
    id:    1,
    date:  "2025-11-20",
    tag:   "Announcement",
    title: "CyberDeck is Now Available",
    body:  "After months of development and testing, **CyberDeck** is officially available on both the **App Store** and **Google Play**. Thank you to everyone who participated in the beta — your feedback shaped the app significantly.\n\nThe initial release supports:\n\n- Full button grid mirroring from Companion\n- Real-time sync of button labels and colours\n- Support for multiple pages"
  }
];

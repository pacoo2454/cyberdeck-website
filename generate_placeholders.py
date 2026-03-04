#!/usr/bin/env python3
"""
Regenerates CyberDeck screenshot placeholders in landscape orientation (844 × 390).
Run from the session root; writes directly to the website assets folder.
"""

import os
from PIL import Image, ImageDraw, ImageFont

ASSETS = '/sessions/optimistic-youthful-mayer/mnt/Website/assets'

# ── Palette ──────────────────────────────────────────────────────────
BG          = ( 13,  15,  20)
SURFACE     = ( 22,  27,  37)
SURFACE_ALT = ( 30,  37,  53)
ACCENT      = (  0, 200, 255)
ACCENT_DARK = (  0,  70,  90)
TEXT        = (232, 234, 240)
MUTED       = (136, 146, 164)
DIVIDER     = ( 35,  43,  58)

FONT_REG  = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
FONT_BOLD = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'

SW, SH = 844, 390   # Landscape dimensions

# ── Helpers ──────────────────────────────────────────────────────────
def font(size, bold=False):
    try:
        return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)
    except Exception:
        return ImageFont.load_default()

def text_w(draw, text, fnt):
    bb = draw.textbbox((0, 0), text, font=fnt)
    return bb[2] - bb[0]

def text_h(draw, text, fnt):
    bb = draw.textbbox((0, 0), text, font=fnt)
    return bb[3] - bb[1]

def cx(draw, text, fnt, canvas_w):
    return (canvas_w - text_w(draw, text, fnt)) // 2

def draw_centred(draw, text, y, fnt, fill, canvas_w):
    draw.text((cx(draw, text, fnt, canvas_w), y), text, fill=fill, font=fnt)

def rr(draw, x1, y1, x2, y2, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius,
                            fill=fill, outline=outline, width=width)

# ── Shared chrome ────────────────────────────────────────────────────
STATUS_H = 36   # thinner status bar in landscape
HEADER_H = 48   # app header
BOTTOM_H = 52   # bottom bar
CONTENT_TOP = STATUS_H + HEADER_H          # 84
CONTENT_BOT = SH - BOTTOM_H               # 338

def status_bar(draw):
    draw.rectangle([0, 0, SW, STATUS_H], fill=SURFACE)
    draw.text((14, 10), '9:41', fill=TEXT, font=font(11, bold=True))
    for i in range(3):
        draw.rectangle([SW-44+i*13, 12, SW-44+i*13+9, 24], fill=MUTED)

def app_header(draw, subtitle=None):
    y0, y1 = STATUS_H, STATUS_H + HEADER_H
    draw.rectangle([0, y0, SW, y1], fill=SURFACE)
    draw.line([0, y1, SW, y1], fill=DIVIDER, width=1)
    title_y = y0 + (HEADER_H - 14) // 2 - (4 if subtitle else 0)
    draw_centred(draw, 'CyberDeck', title_y, font(14, bold=True), TEXT, SW)
    if subtitle:
        draw_centred(draw, subtitle, title_y + 18, font(9), MUTED, SW)

def bottom_bar(draw):
    draw.rectangle([0, SH - BOTTOM_H, SW, SH], fill=SURFACE)
    draw.line([0, SH - BOTTOM_H, SW, SH - BOTTOM_H], fill=DIVIDER, width=1)
    draw.rounded_rectangle([SW//2-40, SH-14, SW//2+40, SH-8], radius=3, fill=DIVIDER)


# ── Screenshot 1 & 3: Button grid ────────────────────────────────────
def make_grid_screen(filename, page_name='Page 1', active=None):
    if active is None:
        active = set()
    img = Image.new('RGB', (SW, SH), BG)
    d   = ImageDraw.Draw(img)

    status_bar(d)
    app_header(d, subtitle=page_name)

    # 4 cols × 3 rows fits landscape content area nicely
    cols, rows = 4, 3
    pad   = 14
    gap   = 8
    content_h = CONTENT_BOT - CONTENT_TOP
    btn_w = (SW - 2 * pad - (cols - 1) * gap) // cols
    btn_h = (content_h - 2 * pad - (rows - 1) * gap) // rows
    f_btn = font(9)

    for row in range(rows):
        for col in range(cols):
            idx  = row * cols + col
            x    = pad + col * (btn_w + gap)
            y    = CONTENT_TOP + pad + row * (btn_h + gap)
            on   = idx in active
            fill    = ACCENT_DARK if on else SURFACE_ALT
            outline = ACCENT      if on else DIVIDER
            color   = ACCENT      if on else MUTED
            rr(d, x, y, x + btn_w, y + btn_h, 8, fill=fill, outline=outline)
            label = f'BTN {idx + 1}'
            lx = x + (btn_w - text_w(d, label, f_btn)) // 2
            ly = y + (btn_h - text_h(d, label, f_btn)) // 2
            d.text((lx, ly), label, fill=color, font=f_btn)

    bottom_bar(d)
    img.save(os.path.join(ASSETS, filename))
    print(f'✓ {filename}')


# ── Screenshot 2 & connect: Connection screen ─────────────────────────
def make_connect_screen(filename, heading='Connect to Companion'):
    img = Image.new('RGB', (SW, SH), BG)
    d   = ImageDraw.Draw(img)

    status_bar(d)
    app_header(d)

    # Two-column layout in landscape: heading+fields on left, saved devices on right
    content_h = CONTENT_BOT - CONTENT_TOP
    col_gap   = 20
    pad       = 20
    half      = (SW - 2 * pad - col_gap) // 2
    left_x    = pad
    right_x   = pad + half + col_gap

    f_head  = font(14, bold=True)
    f_label = font(10)
    f_field = font(12)
    f_btn   = font(12, bold=True)
    f_small = font(10)

    # Left column — form
    y = CONTENT_TOP + 14
    d.text((left_x, y), heading, fill=TEXT, font=f_head)
    y += 22
    d.text((left_x, y), 'Enter Companion details below', fill=MUTED, font=f_small)

    y += 22
    d.text((left_x, y), 'IP Address', fill=MUTED, font=f_label)
    y += 14
    rr(d, left_x, y, left_x + half, y + 36, 6, fill=SURFACE_ALT, outline=DIVIDER)
    d.text((left_x + 10, y + 10), '192.168.1.100', fill=MUTED, font=f_field)
    rr(d, left_x + half - 18, y + 10, left_x + half - 16, y + 26, 2, fill=ACCENT)
    y += 46

    d.text((left_x, y), 'Port', fill=MUTED, font=f_label)
    y += 14
    rr(d, left_x, y, left_x + half, y + 36, 6, fill=SURFACE_ALT, outline=DIVIDER)
    d.text((left_x + 10, y + 10), '8888', fill=TEXT, font=f_field)
    y += 50

    rr(d, left_x, y, left_x + half, y + 38, 8, fill=ACCENT)
    lbl = 'Connect'
    d.text((left_x + (half - text_w(d, lbl, f_btn)) // 2, y + 11), lbl, fill=BG, font=f_btn)

    # Right column — saved devices
    y2 = CONTENT_TOP + 14
    d.text((right_x, y2), '— Saved Devices —', fill=MUTED, font=f_label)
    y2 += 20
    for name, ip in [('Studio Mac', '192.168.1.50'), ('Laptop', '192.168.1.72')]:
        rr(d, right_x, y2, right_x + half, y2 + 44, 6, fill=SURFACE_ALT, outline=DIVIDER)
        d.text((right_x + 10, y2 + 8),  name, fill=TEXT,  font=f_label)
        d.text((right_x + 10, y2 + 24), ip,   fill=MUTED, font=f_small)
        y2 += 54

    bottom_bar(d)
    img.save(os.path.join(ASSETS, filename))
    print(f'✓ {filename}')


# ── Install / welcome screen ──────────────────────────────────────────
def make_welcome_screen(filename):
    img = Image.new('RGB', (SW, SH), BG)
    d   = ImageDraw.Draw(img)

    status_bar(d)

    # Side-by-side layout: icon centred in left half, text in right half
    mid     = SW // 2
    content_h = SH - STATUS_H

    # Left: app icon centred vertically
    icon_s = 80
    ix = (mid - icon_s) // 2
    iy = STATUS_H + (content_h - icon_s) // 2 - 10
    rr(d, ix, iy, ix + icon_s, iy + icon_s, 18, fill=SURFACE_ALT, outline=ACCENT, width=2)
    lx = ix + 14
    for i, lw in enumerate([52, 34, 44]):
        rr(d, lx, iy + 20 + i * 18, lx + lw, iy + 20 + i * 18 + 6, 3, fill=ACCENT)

    # Right: wordmark + features + button
    rx = mid + 20
    rw = SW - rx - 20

    f_big  = font(22, bold=True)
    f_sub  = font(11)
    f_body = font(10)
    f_btn  = font(12, bold=True)

    y = STATUS_H + 28
    d.text((rx, y), 'CyberDeck', fill=TEXT, font=f_big)
    y += 32
    d.text((rx, y), 'Remote Companion Control', fill=MUTED, font=f_sub)

    y += 24
    features = [
        'Control from anywhere in the room',
        'Real-time button sync',
        'Free  ·  iOS & Android',
    ]
    for feat in features:
        d.ellipse([rx, y + 3, rx + 6, y + 9], fill=ACCENT)
        d.text((rx + 14, y), feat, fill=MUTED, font=f_body)
        y += 20

    y += 16
    btn_w = min(rw, 180)
    rr(d, rx, y, rx + btn_w, y + 36, 8, fill=ACCENT)
    lbl = 'Get Started'
    d.text((rx + (btn_w - text_w(d, lbl, f_btn)) // 2, y + 10), lbl, fill=BG, font=f_btn)

    bottom_bar(d)
    img.save(os.path.join(ASSETS, filename))
    print(f'✓ {filename}')


# ── Run ──────────────────────────────────────────────────────────────
print(f'\nGenerating landscape screenshots ({SW}×{SH})...\n')

make_grid_screen('screenshot-1.png',        page_name='Page 1', active={0, 5, 10})
make_grid_screen('screenshot-3.png',        page_name='Page 2', active={2, 7, 9})
make_grid_screen('screenshot-control.png',  page_name='Page 1', active={1, 3, 6})
make_connect_screen('screenshot-2.png',     heading='Connect to Companion')
make_connect_screen('screenshot-connect.png', heading='Add Device')
make_welcome_screen('screenshot-install.png')

print('\nDone — all six screenshots written to assets/ in landscape orientation.\n')

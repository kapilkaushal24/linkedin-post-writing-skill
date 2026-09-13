"""
Thumbnail Template v3 — "Light Glossy-Card SaaS" system.
Direction confirmed by Kapil (2026-09-13) from tools/reference-thumbnails/:
closest to ChatGPT Image Aug 10 (AutoMapper), Gemini_...c5dy (Cache Upgrade
100->1), and the general "clean white/cream background, bold two-tone
headline, glossy rounded icon/comparison cards, big numbers as hero
graphics" language shared by those references.

This SUPERSEDES v2 (dark editorial, tools/make_thumbnail.py as of the prior
session) as the canonical template. v2 is kept as tools/legacy_v2_make_thumbnail.py
for reference only.

Three interchangeable content blocks — pick whichever matches the post:
  block_flow_cards        -> 3 rounded icon cards connected by arrows
                              (architecture / transformation chains)
  block_big_number        -> huge "before -> after" number graphic
                              (dramatic stat / degradation / improvement posts)
  block_comparison_cards  -> 2-3 bordered cards with check/x lists
                              (option comparisons, X vs Y posts)
"""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

FONT_DIR = "C:/Windows/Fonts/"
F_HEAD   = FONT_DIR + "segoeuib.ttf"
F_BLACK  = FONT_DIR + "impact.ttf"
F_LABEL  = FONT_DIR + "segoeuib.ttf"
F_BODY   = FONT_DIR + "segoeui.ttf"
F_BODY_SB= FONT_DIR + "segoeuisb.ttf" if False else FONT_DIR + "segoeuib.ttf"
F_MONO   = FONT_DIR + "consolab.ttf"
F_MONO_R = FONT_DIR + "consola.ttf"

AVATAR_PATH = "D:/Kapil/Projects/LinkedIn/Kapil-AI-1.jpg"

W, H = 1080, 1350          # post canvas (4:5)
NW, NH = 1200, 627         # newsletter canvas (1.91:1)

BG_TOP    = (248, 249, 252)
BG_BOTTOM = (237, 239, 245)
INK       = (18, 20, 28)
MUTED     = (107, 114, 128)
CARD_BG   = (255, 255, 255)
CARD_BORDER = (228, 231, 236)

ACCENTS = {
    "violet": (109, 40, 217),   # Pillar 1 — .NET / backend perf
    "blue":   (37, 99, 235),    # Pillar 2 — cloud-native / DevOps
    "teal":   (13, 148, 136),   # Pillar 3 — AI/ML/GenAI
    "amber":  (217, 119, 6),    # Pillar 4 — career, or newsletter accent
    "red":    (220, 38, 38),
    "green":  (22, 163, 74),
    "cyan":   (34, 211, 238),
}

# ---------------------------------------------------------------- helpers --

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i]-a[i])*t) for i in range(3))

def vgrad(size, top, bottom):
    w, h = size
    img = Image.new("RGB", size, top)
    d = ImageDraw.Draw(img)
    for y in range(h):
        d.line([(0, y), (w, y)], fill=lerp(top, bottom, y/max(h-1,1)))
    return img

def graph_paper(size, spacing=44, alpha=10):
    ov = Image.new("RGBA", size, (0,0,0,0))
    d = ImageDraw.Draw(ov)
    w,h = size
    for x in range(0, w, spacing):
        d.line([(x,0),(x,h)], fill=(120,124,135,alpha), width=1)
    for y in range(0, h, spacing):
        d.line([(0,y),(w,y)], fill=(120,124,135,alpha), width=1)
    return ov

def fit_font(path, text, max_width, start, min_size=36, draw=None):
    size = start
    tmp = draw or ImageDraw.Draw(Image.new("RGB",(10,10)))
    while size > min_size:
        f = ImageFont.truetype(path, size)
        bbox = tmp.textbbox((0,0), text, font=f)
        if bbox[2]-bbox[0] <= max_width:
            return f
        size -= 2
    return ImageFont.truetype(path, min_size)

def wrap(draw, text, font, max_width):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        test = (cur+" "+w_).strip()
        bbox = draw.textbbox((0,0), test, font=font)
        if bbox[2]-bbox[0] <= max_width or not cur:
            cur = test
        else:
            lines.append(cur); cur = w_
    if cur: lines.append(cur)
    return lines

def faux_bold_text(draw, xy, text, font, fill, extra=1):
    """Simulates a heavier weight by stamping the glyph a few times with a
    tiny offset — the system has no true 'Black' weight for Segoe UI."""
    x, y = xy
    for dx in range(0, extra+1):
        for dy in range(0, extra+1):
            draw.text((x+dx, y+dy), text, font=font, fill=fill)

def rrect(draw, box, r, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)

def soft_shadow(img, box, radius=18, blur=16, alpha=55, offset=(0,10)):
    ov = Image.new("RGBA", img.size, (0,0,0,0))
    d = ImageDraw.Draw(ov)
    x0,y0,x1,y1 = box
    d.rounded_rectangle([x0+offset[0], y0+offset[1], x1+offset[0], y1+offset[1]],
                         radius=radius, fill=(20,22,30,alpha))
    ov = ov.filter(ImageFilter.GaussianBlur(blur))
    img.alpha_composite(ov)

def arrow(draw, p1, p2, color, width=5, head=14):
    draw.line([p1,p2], fill=color, width=width)
    ang = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
    for da in (0.5, -0.5):
        a = ang + math.pi - da
        draw.line([p2, (p2[0]+head*math.cos(a), p2[1]+head*math.sin(a))], fill=color, width=width)

def repost_icon(draw, cx, cy, s, color, width=4):
    """LinkedIn-style repost glyph: two opposing arrows forming a loop."""
    x0,y0,x1,y1 = cx-s, cy-s*0.62, cx+s, cy+s*0.62
    draw.line([(x0, y0), (x1-8, y0)], fill=color, width=width)
    draw.polygon([(x1-9,y0-7),(x1-9,y0+7),(x1+5,y0)], fill=color)
    draw.line([(x1, y0), (x1, cy)], fill=color, width=width)
    draw.line([(x1, y1), (x0+8, y1)], fill=color, width=width)
    draw.polygon([(x0+9,y1-7),(x0+9,y1+7),(x0-5,y1)], fill=color)
    draw.line([(x0, y1), (x0, cy)], fill=color, width=width)

def circular_avatar(path, d):
    im = ImageOps.fit(Image.open(path).convert("RGB"), (d,d), Image.LANCZOS)
    mask = Image.new("L", (d,d), 0)
    ImageDraw.Draw(mask).ellipse([0,0,d,d], fill=255)
    out = Image.new("RGBA", (d,d), (0,0,0,0))
    out.paste(im, (0,0), mask)
    return out

def check_or_x(draw, cx, cy, ok=True, r=13):
    color = ACCENTS["green"] if ok else ACCENTS["red"]
    draw.ellipse([cx-r,cy-r,cx+r,cy+r], fill=color)
    if ok:
        draw.line([(cx-6,cy),(cx-1,cy+6),(cx+7,cy-7)], fill=(255,255,255), width=3)
    else:
        draw.line([(cx-6,cy-6),(cx+6,cy+6)], fill=(255,255,255), width=3)
        draw.line([(cx-6,cy+6),(cx+6,cy-6)], fill=(255,255,255), width=3)

def icon_glyph(draw, cx, cy, kind, color, s=30):
    """Minimal line-icon set drawn with primitives — no external icon assets."""
    lw = 5
    if kind == "db":
        draw.ellipse([cx-s,cy-s*0.7,cx+s,cy-s*0.35], outline=color, width=lw)
        draw.line([(cx-s,cy-s*0.5),(cx-s,cy+s*0.5)], fill=color, width=lw)
        draw.line([(cx+s,cy-s*0.5),(cx+s,cy+s*0.5)], fill=color, width=lw)
        draw.arc([cx-s,cy+s*0.15,cx+s,cy+s*0.5], 0, 180, fill=color, width=lw)
    elif kind == "code":
        f = ImageFont.truetype(F_MONO, int(s*1.7))
        tb = draw.textbbox((0,0), "</>", font=f)
        draw.text((cx-(tb[2]-tb[0])//2, cy-(tb[3]-tb[1])//2-6), "</>", font=f, fill=color)
    elif kind == "brace":
        f = ImageFont.truetype(F_MONO, int(s*1.7))
        tb = draw.textbbox((0,0), "{ }", font=f)
        draw.text((cx-(tb[2]-tb[0])//2, cy-(tb[3]-tb[1])//2-6), "{ }", font=f, fill=color)
    elif kind == "clock":
        draw.ellipse([cx-s,cy-s,cx+s,cy+s], outline=color, width=lw)
        draw.line([(cx,cy),(cx,cy-s*0.55)], fill=color, width=lw)
        draw.line([(cx,cy),(cx+s*0.4,cy+s*0.15)], fill=color, width=lw)
    elif kind == "bolt":
        pts = [(cx+8,cy-s),(cx-10,cy+6),(cx+2,cy+6),(cx-8,cy+s),(cx+12,cy-4),(cx+0,cy-4)]
        draw.polygon(pts, fill=color)
    elif kind == "loop":
        draw.arc([cx-s,cy-s,cx+s,cy+s], 30, 300, fill=color, width=lw)
        draw.line([(cx+s*0.55,cy-s*0.75),(cx+s*0.95,cy-s*0.55)], fill=color, width=lw)
    elif kind == "shield":
        pts = [(cx,cy-s),(cx+s*0.85,cy-s*0.5),(cx+s*0.85,cy+s*0.25),(cx,cy+s),
               (cx-s*0.85,cy+s*0.25),(cx-s*0.85,cy-s*0.5)]
        draw.polygon(pts, outline=color, width=lw)
    elif kind == "check":
        draw.ellipse([cx-s,cy-s,cx+s,cy+s], outline=color, width=lw)
        draw.line([(cx-s*0.45,cy+s*0.05),(cx-s*0.1,cy+s*0.4),(cx+s*0.5,cy-s*0.4)], fill=color, width=lw, joint="curve")
    else:
        draw.ellipse([cx-s,cy-s,cx+s,cy+s], outline=color, width=lw)

# --------------------------------------------------------- content blocks --

def block_flow_cards(draw, img, box, accent, steps, gap=46):
    """steps: list of (icon_kind, label) tuples, 3 recommended."""
    x0,y0,x1,y1 = box
    n = len(steps)
    total_w = x1-x0
    card_w = int((total_w - gap*(n-1)) / n)
    card_h = min(280, y1-y0)
    cy = (y0+y1)//2
    for i,(icon_kind, label) in enumerate(steps):
        cx0 = x0 + i*(card_w+gap)
        card_box = [cx0, cy-card_h//2, cx0+card_w, cy+card_h//2]
        soft_shadow(img, card_box, radius=22, blur=14, alpha=40)
        rrect(draw, card_box, 22, fill=CARD_BG, outline=CARD_BORDER, width=2)
        icon_glyph(draw, cx0+card_w//2, cy-40, icon_kind, accent, s=34)
        f = ImageFont.truetype(F_BODY_SB, 25)
        lines = wrap(draw, label, f, card_w-24)
        ly = cy + 26
        for ln in lines:
            tb = draw.textbbox((0,0), ln, font=f)
            draw.text((cx0+card_w//2-(tb[2]-tb[0])//2, ly), ln, font=f, fill=INK)
            ly += 32
        if i < n-1:
            ay = cy
            arrow(draw, (cx0+card_w+8, ay), (cx0+card_w+gap-8, ay), INK, width=5, head=13)

def block_big_number(draw, img, box, accent, left_text, right_text, caption=None):
    x0,y0,x1,y1 = box
    cy = (y0+y1)//2 - (30 if caption else 0)
    f_num = fit_font(F_BLACK, left_text, int((x1-x0)*0.38), 190, min_size=90, draw=draw)
    f_num2 = fit_font(F_BLACK, right_text, int((x1-x0)*0.38), 190, min_size=90, draw=draw)
    size = min(f_num.size, f_num2.size)
    f_num = ImageFont.truetype(F_BLACK, size)
    f_num2 = ImageFont.truetype(F_BLACK, size)

    lb = draw.textbbox((0,0), left_text, font=f_num)
    lw_, lh_ = lb[2]-lb[0], lb[3]-lb[1]
    rb = draw.textbbox((0,0), right_text, font=f_num2)
    rw_, rh_ = rb[2]-rb[0], rb[3]-rb[1]

    arrow_w = 90
    total_w = lw_ + arrow_w + rw_
    start_x = x0 + ((x1-x0) - total_w)//2
    ly = cy - lh_//2 - lb[1]
    draw.text((start_x, ly), left_text, font=f_num, fill=INK)
    ax0 = start_x + lw_ + 14
    ax1 = ax0 + arrow_w - 28
    arrow(draw, (ax0, cy), (ax1, cy), accent, width=10, head=22)
    rx = ax1 + 28
    ry = cy - rh_//2 - rb[1]
    draw.text((rx, ry), right_text, font=f_num2, fill=accent)

    if caption:
        f_cap = ImageFont.truetype(F_BODY, 27)
        cb = draw.textbbox((0,0), caption, font=f_cap)
        cw = cb[2]-cb[0]
        pad = 26
        box_y = cy + max(lh_,rh_)//2 + 46
        pbox = [x0 + ((x1-x0)-cw)//2 - pad, box_y, x0 + ((x1-x0)-cw)//2 + cw + pad, box_y+58]
        rrect(draw, pbox, 999, outline=CARD_BORDER, width=2, fill=CARD_BG)
        draw.text((pbox[0]+pad, box_y+13), caption, font=f_cap, fill=MUTED)

def block_comparison_cards(draw, img, box, accent, cards, gap=36):
    """cards: list of dicts {title, items:[(text,bool_ok)], border, code}"""
    x0,y0,x1,y1 = box
    n = len(cards)
    card_w = int((x1-x0 - gap*(n-1))/n)
    card_top = y0
    for i, card in enumerate(cards):
        cx0 = x0 + i*(card_w+gap)
        border_color = card.get("border", accent)
        n_items = len(card["items"])
        card_h = 120 + n_items*54 + (70 if card.get("code") else 0)
        card_box = [cx0, card_top, cx0+card_w, card_top+card_h]
        soft_shadow(img, card_box, radius=20, blur=14, alpha=40)
        rrect(draw, card_box, 20, fill=CARD_BG, outline=CARD_BORDER, width=2)
        draw.rounded_rectangle([cx0, card_top, cx0+card_w, card_top+10], radius=6, fill=border_color)

        f_title = fit_font(F_BODY_SB, card["title"], card_w-40, 30, min_size=20, draw=draw)
        draw.text((cx0+22, card_top+28), card["title"], font=f_title, fill=INK)

        f_item = ImageFont.truetype(F_BODY, 24)
        iy = card_top+80
        for text, ok in card["items"]:
            check_or_x(draw, cx0+34, iy+12, ok=ok, r=12)
            draw.text((cx0+58, iy), text, font=f_item, fill=INK)
            iy += 46
        if card.get("code"):
            f_code = ImageFont.truetype(F_MONO_R, 20)
            code_box = [cx0+18, iy+6, cx0+card_w-18, iy+56]
            rrect(draw, code_box, 8, fill=(24,26,35))
            draw.text((code_box[0]+14, code_box[1]+15), card["code"], font=f_code, fill=(167,243,208))

CONTENT_BLOCKS = {
    "flow_cards": block_flow_cards,
    "big_number": block_big_number,
    "comparison_cards": block_comparison_cards,
}

# --------------------------------------------------- alt style: dark checklist --
# A second, dark-navy style for "checklist before you do X" posts, requested
# 2026-09-13 as a one-off for the Sept 13 post. Kept as a named function
# (not in CONTENT_BLOCKS) since it's a full alternate canvas style, not a
# content block within the v3 light template — use it when a post's core
# payload IS a short checklist and the punchy dark look fits better.

DARK_BG_TOP    = (9, 13, 26)     # #090D1A
DARK_BG_BOTTOM = (13, 19, 36)    # #0D1324
DARK_WHITE     = (245, 247, 250)
DARK_MUTED     = (156, 163, 184)

def render_checklist_dark(out_path, headline_segments, items, accent="cyan",
                           name="Kapil Kaushal", handle="@kapilkaushal24",
                           cta="Follow for more"):
    """
    headline_segments: list of (text, color_key_or_None) — None renders white,
                        a color key (e.g. "cyan") renders that accent color.
                        Each segment is its own line, matching the reference
                        ("Ask" / "These Before" white, "You Add an Agent." cyan).
    items: list of checklist strings (each can wrap to 2 lines).
    cta:   bottom-right call to action, paired with a repost glyph. Pass
           None to omit.
    """
    accent_rgb = ACCENTS[accent]
    img = vgrad((W,H), DARK_BG_TOP, DARK_BG_BOTTOM).convert("RGBA")
    draw = ImageDraw.Draw(img)
    pad = 76

    # headline — tight poster leading, heavier faux-bold stamp for real
    # contrast against the checklist body copy below it
    f = fit_font(F_HEAD, max(t for t,_ in headline_segments), W-pad*2, 90, min_size=54, draw=draw)
    y = 100
    for text, color_key in headline_segments:
        color = ACCENTS[color_key] if color_key else DARK_WHITE
        for ln in wrap(draw, text, f, W-pad*2):
            faux_bold_text(draw, (pad, y), ln, f, color, extra=2)
            y += int(f.size*1.06)
    y += 30

    # thin accent rule separates the hook from the proof — a design beat,
    # not just a gap
    draw.rectangle([pad, y, pad+64, y+5], fill=accent_rgb)
    y += 54

    f_item = ImageFont.truetype(F_BODY, 33)
    r = 22
    for item in items:
        lines = wrap(draw, item, f_item, W-pad*2-72)
        line_h = 42
        block_h = max(2*r, len(lines)*line_h)
        cy = y + r
        draw.ellipse([pad-r, cy-r, pad+r, cy+r], outline=accent_rgb, width=4)
        draw.line([(pad-9,cy+1),(pad-2,cy+9),(pad+11,cy-8)], fill=accent_rgb, width=4)
        ty = cy - (len(lines)*line_h)//2 + 6
        for ln in lines:
            draw.text((pad+52, ty), ln, font=f_item, fill=DARK_WHITE)
            ty += line_h
        y += block_h + 50

    # footer: avatar/name on the left, follow + repost CTA on the right,
    # both centered on the same baseline for a balanced, intentional row
    av_d = 56
    row_cy = H - 108 + av_d//2
    av = circular_avatar(AVATAR_PATH, av_d)
    ring = Image.new("RGBA",(av_d+6,av_d+6),(0,0,0,0))
    ImageDraw.Draw(ring).ellipse([0,0,av_d+6,av_d+6], outline=accent_rgb, width=3)
    ax, ay = pad, H-108
    img.alpha_composite(ring,(ax-3,ay-3))
    img.alpha_composite(av,(ax,ay))
    draw = ImageDraw.Draw(img)
    f_name = ImageFont.truetype(F_BODY_SB, 27)
    f_handle = ImageFont.truetype(F_BODY, 22)
    draw.text((ax+av_d+20, ay+2), name, font=f_name, fill=DARK_WHITE)
    draw.text((ax+av_d+20, ay+32), handle, font=f_handle, fill=DARK_MUTED)

    if cta:
        f_cta = ImageFont.truetype(F_BODY_SB, 26)
        cb = draw.textbbox((0,0), cta, font=f_cta)
        cta_w = cb[2]-cb[0]
        icon_r = 17
        gap = 14
        text_x = W - pad - cta_w
        icon_cx = text_x - gap - icon_r
        repost_icon(draw, icon_cx, row_cy, icon_r, accent_rgb, width=4)
        draw.text((text_x, row_cy - (cb[3]-cb[1])//2 - cb[1]), cta, font=f_cta, fill=DARK_WHITE)

    img.convert("RGB").save(out_path, "PNG", quality=95)
    print("saved", out_path)

# ------------------------------------------------------------- main render --

def _headline(draw, img, pad, top_y, max_width, segments, size=76, min_size=48):
    """segments: list of (text, color_key or None-for-INK) rendered as
    successive wrapped lines, matching the two-tone poster headline style."""
    full_text = " ".join(s for s,_ in segments)
    f = fit_font(F_HEAD, full_text, max_width, size, min_size=min_size, draw=draw)
    # naive approach: wrap each segment independently onto its own line(s)
    y = top_y
    for text, color_key in segments:
        color = ACCENTS[color_key] if color_key else INK
        lines = wrap(draw, text, f, max_width)
        for ln in lines:
            faux_bold_text(draw, (pad, y), ln, f, color, extra=1)
            y += int(f.size*1.08)
        y += int(f.size*0.12)
    return y

def render_post(out_path, category, headline_segments, subtitle, block, block_kwargs,
                 accent="violet", brand_tag=None, name="Kapil Kaushal", handle="@kapilkaushal24"):
    img = vgrad((W,H), BG_TOP, BG_BOTTOM).convert("RGBA")
    img.alpha_composite(graph_paper((W,H)))
    draw = ImageDraw.Draw(img)
    pad = 74
    accent_rgb = ACCENTS[accent]

    f_cat = ImageFont.truetype(F_LABEL, 26)
    draw.text((pad, 60), category.upper(), font=f_cat, fill=accent_rgb)
    cb = draw.textbbox((0,0), category.upper(), font=f_cat)
    draw.rectangle([pad, 96, pad+64, 100], fill=accent_rgb)

    y = _headline(draw, img, pad, 128, W-pad*2, headline_segments, size=78, min_size=50)

    if subtitle:
        draw.rectangle([pad, y+10, pad+6, y+10+58], fill=accent_rgb)
        f_sub = ImageFont.truetype(F_BODY_SB, 27)
        for ln in wrap(draw, subtitle, f_sub, W-pad*2-40):
            draw.text((pad+26, y+12), ln, font=f_sub, fill=MUTED)
            y += 36
        y += 30
    else:
        y += 26

    zone_top = max(y, int(H*0.36))
    zone_bottom = int(H*0.82)
    CONTENT_BLOCKS[block](draw, img, (pad, zone_top, W-pad, zone_bottom), accent_rgb, **block_kwargs)

    # bottom brand pill + byline
    if brand_tag:
        f_bt = ImageFont.truetype(F_LABEL, 24)
        bb = draw.textbbox((0,0), brand_tag.upper(), font=f_bt)
        bw_ = bb[2]-bb[0]
        pill = [pad, H-190, pad+bw_+64, H-190+52]
        rrect(draw, pill, 999, fill=INK)
        draw.ellipse([pad+18, H-190+18, pad+30, H-190+30], fill=accent_rgb)
        draw.text((pad+42, H-190+13), brand_tag.upper(), font=f_bt, fill=(255,255,255))

    av_d = 58
    av = circular_avatar(AVATAR_PATH, av_d)
    ring = Image.new("RGBA",(av_d+6,av_d+6),(0,0,0,0))
    ImageDraw.Draw(ring).ellipse([0,0,av_d+6,av_d+6], outline=accent_rgb, width=3)
    ax, ay = pad, H-108
    img.alpha_composite(ring,(ax-3,ay-3))
    img.alpha_composite(av,(ax,ay))
    draw = ImageDraw.Draw(img)
    f_name = ImageFont.truetype(F_BODY_SB, 27)
    f_handle = ImageFont.truetype(F_BODY, 22)
    draw.text((ax+av_d+20, ay+2), name, font=f_name, fill=INK)
    draw.text((ax+av_d+20, ay+32), handle, font=f_handle, fill=MUTED)

    img.convert("RGB").save(out_path, "PNG", quality=95)
    print("saved", out_path)


def render_newsletter(out_path, issue_num, headline_segments, subtitle, block, block_kwargs,
                       accent="amber", name="Kapil Kaushal", handle="@kapilkaushal24"):
    img = vgrad((NW,NH), BG_TOP, BG_BOTTOM).convert("RGBA")
    img.alpha_composite(graph_paper((NW,NH)))
    draw = ImageDraw.Draw(img)
    pad = 64
    accent_rgb = ACCENTS[accent]

    f_mast = ImageFont.truetype(F_LABEL, 26)
    draw.text((pad, 42), "THE .NET HORIZON", font=f_mast, fill=accent_rgb)
    f_issue = ImageFont.truetype(F_BODY, 22)
    draw.text((pad, 74), issue_num.upper(), font=f_issue, fill=MUTED)
    draw.rectangle([pad, 106, pad+64, 110], fill=accent_rgb)

    left_w = int(NW*0.5)
    y = _headline(draw, img, pad, 132, left_w-pad, headline_segments, size=52, min_size=36)
    f_sub = ImageFont.truetype(F_BODY, 24)
    for ln in wrap(draw, subtitle, f_sub, left_w-pad)[:3]:
        draw.text((pad, y+8), ln, font=f_sub, fill=MUTED)
        y += 32

    av_d = 52
    av = circular_avatar(AVATAR_PATH, av_d)
    ring = Image.new("RGBA",(av_d+6,av_d+6),(0,0,0,0))
    ImageDraw.Draw(ring).ellipse([0,0,av_d+6,av_d+6], outline=accent_rgb, width=3)
    ax, ay = pad, NH-86
    img.alpha_composite(ring,(ax-3,ay-3))
    img.alpha_composite(av,(ax,ay))
    draw = ImageDraw.Draw(img)
    f_name = ImageFont.truetype(F_BODY_SB, 25)
    draw.text((ax+av_d+18, ay+12), f"{name}  ·  {handle}", font=f_name, fill=INK)

    CONTENT_BLOCKS[block](draw, img, (left_w+10, 70, NW-40, NH-70), accent_rgb, **block_kwargs)

    img.convert("RGB").save(out_path, "PNG", quality=95)
    print("saved", out_path)


if __name__ == "__main__":
    base = "D:/Kapil/Projects/LinkedIn/linkedin-post-writing-skill"

    # flagship reference (big_number block, mirrors the Cache Upgrade ref)
    render_post(
        f"{base}/tools/template_reference_example_v3.png",
        category=".NET / PERFORMANCE",
        headline_segments=[("The N+1 Bug", None), ("You Keep Shipping", "violet")],
        subtitle="One EF Core query. Hundreds of round trips.",
        block="big_number",
        block_kwargs=dict(left_text="1", right_text="247", caption="1 query in code ↓ 247 database round trips"),
        accent="violet", brand_tag=".NET Performance Insights",
    )

    # Sept 13 — AI amplifies weak backends (flow_cards: chain of 3)
    render_post(
        f"{base}/posts/September/13/thumbnail.png",
        category="AI + BACKEND ENGINEERING",
        headline_segments=[("Your Agent Didn't Break It.", None), ("Your API Did.", "violet")],
        subtitle="Agents don't fix slow backends. They expose them.",
        block="flow_cards",
        block_kwargs=dict(steps=[("bolt","Weak API\n(no caching)"), ("loop","AI Agent\nretries 3x"), ("clock","Timeout\ncascade")]),
        accent="violet", brand_tag="AI + Backend Notes",
    )

    # Sept 15 — async/await myth (flow_cards)
    render_post(
        f"{base}/posts/September/15/thumbnail.png",
        category=".NET / PERFORMANCE",
        headline_segments=[("Async Doesn't Create", None), ("a New Thread.", "violet")],
        subtitle="Here's what actually happens when you await.",
        block="flow_cards",
        block_kwargs=dict(steps=[("code","await\ncall"), ("loop","State\nmachine"), ("check","Thread\nreleased")]),
        accent="violet", brand_tag=".NET Performance Insights",
    )

    # Sept 16 — AI agent memory myth (comparison_cards)
    render_post(
        f"{base}/posts/September/16/thumbnail.png",
        category="AI ENGINEERING",
        headline_segments=[("Your AI Agent", None), ("Doesn't Have Memory.", "teal")],
        subtitle="Resent context isn't the same as remembered context.",
        block="comparison_cards",
        block_kwargs=dict(cards=[
            {"title":"Short-Term (Resent)","border":ACCENTS["red"],"items":[("Full transcript replayed",False),("No extraction step",False),("Competes for token budget",False)]},
            {"title":"Long-Term (Extracted)","border":ACCENTS["green"],"items":[("Discrete facts stored",True),("Entries expire/update",True),("Ranked like RAG",True)]},
        ]),
        accent="teal", brand_tag="AI Engineering Notes",
    )

    # Sept 17 — Alive != Ready (comparison_cards)
    render_post(
        f"{base}/posts/September/17/thumbnail.png",
        category="CLOUD-NATIVE / AKS",
        headline_segments=[("Your Pods Are Healthy.", None), ("Your Users Aren't.", "blue")],
        subtitle="Liveness and readiness checks answer different questions.",
        block="comparison_cards",
        block_kwargs=dict(cards=[
            {"title":"Liveness Probe","border":ACCENTS["blue"],"items":[("Is the process alive?",True),("Says nothing about traffic",False),("Failure = restart",True)]},
            {"title":"Readiness Probe","border":ACCENTS["green"],"items":[("Can it serve real requests?",True),("Checks DB, cache, deps",True),("Failure = pulled from LB",True)]},
        ]),
        accent="blue", brand_tag="Cloud-Native Playbook",
    )

    # Newsletter — MCP (big_number: 5 adapters -> 1 protocol)
    render_newsletter(
        f"{base}/newsletters/September/14/thumbnail.png",
        issue_num="Issue · September 2026",
        headline_segments=[("Tools,", None), ("Standardized.", "amber")],
        subtitle="Every team building AI agents invented the same integration layer. Badly.",
        block="big_number",
        block_kwargs=dict(left_text="5", right_text="1", caption="5 bespoke adapters ↓ 1 MCP server"),
        accent="amber",
    )

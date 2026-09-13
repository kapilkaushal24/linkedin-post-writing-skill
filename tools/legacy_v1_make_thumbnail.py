"""
LinkedIn thumbnail/poster generator for Kapil's post + newsletter branding.

Requires: Pillow (`pip install pillow`), Windows system fonts (Arial, Segoe UI,
Impact, Consolas — all present by default on Windows), and the avatar photo at
D:/Kapil/Projects/LinkedIn/Kapil-AI-1.jpg.

Two functions:
  make_post_thumbnail(...)   -> 1080x1350 portrait (4:5), for short feed posts.
  make_newsletter_cover(...) -> 1200x627 landscape (1.91:1), for newsletter issues.

The __main__ block below is this week's (Sept 13-17, 2026) batch as a worked
example — edit the calls (headline, eyebrow label, accent colors, code lines,
output path) for each new week rather than starting from scratch. Output paths
should follow CONTENT_CALENDAR_RULES.md: posts/<Month>/<Day>/thumbnail.png and
newsletters/<Month>/<Day>/thumbnail.png.

Color convention (keep consistent for brand recognition across posts):
  Pillar 1 (.NET/backend perf): violet  #8B5CF6 / #6D28D9
  Pillar 2 (cloud-native/DevOps): blue  #2B88D8 / #1E3A8A
  Pillar 3 (AI/ML/GenAI): teal          #14B8A6 / #0EA5E9
  Pillar 4 (career/interview): pick a distinct accent as needed, e.g. amber
  Crossover / hot-take posts: mix two pillar colors (e.g. violet + teal)
  Newsletter ("The .NET Horizon"): navy + gold #F5A623 + blue #3B82F6, distinct
  from the post palette so newsletter covers read as a separate "publication."
"""
import sys, os, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

FONT_DIR = "C:/Windows/Fonts/"
F_BOLD   = FONT_DIR + "arialbd.ttf"
F_BLACK  = FONT_DIR + "impact.ttf"
F_REG    = FONT_DIR + "segoeui.ttf"
F_SEMI   = FONT_DIR + "segoeuib.ttf"
F_MONO   = FONT_DIR + "consolab.ttf"
F_MONO_R = FONT_DIR + "consola.ttf"

AVATAR_PATH = "D:/Kapil/Projects/LinkedIn/Kapil-AI-1.jpg"

def hex2rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i]-a[i])*t) for i in range(3))

def vertical_gradient(size, top, bottom):
    w, h = size
    img = Image.new("RGB", size, top)
    draw = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(h-1, 1)
        draw.line([(0, y), (w, y)], fill=lerp(top, bottom, t))
    return img

def diagonal_glow(size, color, cx_ratio, cy_ratio, radius_ratio, alpha=140):
    w, h = size
    overlay = Image.new("RGBA", size, (0,0,0,0))
    d = ImageDraw.Draw(overlay)
    cx, cy = int(w*cx_ratio), int(h*cy_ratio)
    r = int(min(w,h)*radius_ratio)
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color+(alpha,))
    overlay = overlay.filter(ImageFilter.GaussianBlur(r//2))
    return overlay

def dot_grid(size, color, spacing=46, r=1, alpha=28):
    overlay = Image.new("RGBA", size, (0,0,0,0))
    d = ImageDraw.Draw(overlay)
    w,h = size
    for x in range(0, w, spacing):
        for y in range(0, h, spacing):
            d.ellipse([x-r,y-r,x+r,y+r], fill=color+(alpha,))
    return overlay

def fit_font(text, font_path, max_width, start_size, min_size=28):
    size = start_size
    while size > min_size:
        f = ImageFont.truetype(font_path, size)
        bbox = f.getbbox(text)
        if bbox[2]-bbox[0] <= max_width:
            return f
        size -= 2
    return ImageFont.truetype(font_path, min_size)

def wrap_to_width(draw, text, font, max_width):
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        test = (cur + " " + w).strip()
        bbox = draw.textbbox((0,0), test, font=font)
        if bbox[2]-bbox[0] <= max_width or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def rounded_rect(draw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def circular_avatar(path, diameter):
    im = Image.open(path).convert("RGB")
    im = ImageOps.fit(im, (diameter, diameter), Image.LANCZOS)
    mask = Image.new("L", (diameter, diameter), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse([0,0,diameter,diameter], fill=255)
    out = Image.new("RGBA", (diameter, diameter), (0,0,0,0))
    out.paste(im, (0,0), mask)
    return out

def make_post_thumbnail(out_path, eyebrow, headline_lines, accent_hex, accent_hex2,
                         name="Kapil Kaushal", tagline=".NET Cloud AI Engineer", handle="@kapilkaushal24",
                         code_lines=None, hashtag_pill=None):
    W, H = 1080, 1350
    top = hex2rgb("#0A0F1E")
    bottom = hex2rgb("#111827")
    img = vertical_gradient((W,H), top, bottom).convert("RGBA")

    accent = hex2rgb(accent_hex)
    accent2 = hex2rgb(accent_hex2)

    glow1 = diagonal_glow((W,H), accent, 0.85, 0.10, 0.34, alpha=110)
    glow2 = diagonal_glow((W,H), accent2, 0.05, 0.85, 0.30, alpha=80)
    img.alpha_composite(glow1)
    img.alpha_composite(glow2)
    img.alpha_composite(dot_grid((W,H), (255,255,255), spacing=54, r=1, alpha=14))

    draw = ImageDraw.Draw(img)

    # top accent bar
    draw.rectangle([0,0,W,10], fill=accent)

    pad = 82

    # eyebrow pill
    f_eyebrow = ImageFont.truetype(F_SEMI, 30)
    eb_bbox = draw.textbbox((0,0), eyebrow, font=f_eyebrow)
    eb_w = eb_bbox[2]-eb_bbox[0]
    pill_pad_x, pill_pad_y = 28, 16
    pill_box = [pad, 96, pad+eb_w+pill_pad_x*2, 96+ (eb_bbox[3]-eb_bbox[1]) + pill_pad_y*2 + 8]
    rounded_rect(draw, pill_box, radius=999, outline=accent, width=3)
    draw.text((pill_box[0]+pill_pad_x, pill_box[1]+pill_pad_y-2), eyebrow, font=f_eyebrow, fill=accent)

    # headline
    headline_top = pill_box[3] + 56
    f_head = ImageFont.truetype(F_BOLD, 84)
    max_w = W - pad*2
    all_lines = []
    for para in headline_lines:
        all_lines.extend(wrap_to_width(draw, para, f_head, max_w))
    # shrink font if too many lines
    while len(all_lines) > 5 and f_head.size > 54:
        f_head = ImageFont.truetype(F_BOLD, f_head.size - 4)
        all_lines = []
        for para in headline_lines:
            all_lines.extend(wrap_to_width(draw, para, f_head, max_w))

    line_h = int(f_head.size * 1.18)
    y = headline_top
    for ln in all_lines:
        draw.text((pad, y), ln, font=f_head, fill=(255,255,255,255))
        y += line_h
    headline_bottom = y + 10

    # optional code snippet chip
    content_bottom = headline_bottom
    if code_lines:
        chip_top = headline_bottom + 34
        f_code = ImageFont.truetype(F_MONO_R, 30)
        f_code_b = ImageFont.truetype(F_MONO, 30)
        line_h_c = 44
        chip_h = 40 + line_h_c*len(code_lines)
        chip_box = [pad, chip_top, W-pad, chip_top+chip_h]
        rounded_rect(draw, chip_box, radius=20, fill=(255,255,255,18))
        rounded_rect(draw, chip_box, radius=20, outline=(255,255,255,60), width=2)
        # traffic-light dots
        dot_y = chip_box[1]+24
        for i,c in enumerate([(255,95,86),(255,189,46),(39,201,63)]):
            cx = chip_box[0]+30+i*28
            draw.ellipse([cx-7,dot_y-7,cx+7,dot_y+7], fill=c)
        cy = chip_box[1]+56
        for ln in code_lines:
            draw.text((chip_box[0]+34, cy), ln, font=f_code_b if ln.strip().startswith(("public","private","→")) else f_code, fill=(148,226,213))
            cy += line_h_c
        content_bottom = chip_box[3]

    bar_h = 230
    bar_top = H - bar_h

    # large faint monogram watermark filling the lower gap (personal branding + anti-repost)
    mono_size = 430
    f_mono_wm = ImageFont.truetype(F_BLACK, mono_size)
    tmp = Image.new("RGBA", (900, 560), (0,0,0,0))
    td = ImageDraw.Draw(tmp)
    td.text((40, 40), "KK", font=f_mono_wm, fill=(255,255,255,20))
    tmp = tmp.rotate(-6, expand=True, resample=Image.BICUBIC)
    gap_center_y = (content_bottom + bar_top) // 2 if content_bottom < bar_top else (headline_bottom + bar_top)//2
    px = W//2 - tmp.width//2 + 40
    py = gap_center_y - tmp.height//2
    img.alpha_composite(tmp, (px, py))

    # small handle watermark line above footer
    f_wm = ImageFont.truetype(F_REG, 26)
    wm_text = "linkedin.com/in/kapilkaushal24"
    wb = draw.textbbox((0,0), wm_text, font=f_wm)
    ww = wb[2]-wb[0]
    draw.text((W-pad-ww, bar_top-46), wm_text, font=f_wm, fill=(255,255,255,60))

    # branding footer bar
    bar_h = 230
    bar_top = H - bar_h
    footer = Image.new("RGBA", (W, bar_h), (7,10,20,235))
    fd = ImageDraw.Draw(footer)
    fd.rectangle([0,0,W,4], fill=accent)
    img.alpha_composite(footer, (0, bar_top))

    draw = ImageDraw.Draw(img)
    avatar_d = 148
    av = circular_avatar(AVATAR_PATH, avatar_d)
    ring = Image.new("RGBA", (avatar_d+16, avatar_d+16), (0,0,0,0))
    rd = ImageDraw.Draw(ring)
    rd.ellipse([0,0,avatar_d+16,avatar_d+16], outline=accent, width=6)
    ax, ay = pad, bar_top + (bar_h-avatar_d)//2
    img.alpha_composite(ring, (ax-8, ay-8))
    img.alpha_composite(av, (ax, ay))

    name_x = ax + avatar_d + 34
    f_name = ImageFont.truetype(F_SEMI, 46)
    f_tag = ImageFont.truetype(F_REG, 30)
    name_y = bar_top + 62
    draw.text((name_x, name_y), name, font=f_name, fill=(255,255,255))
    draw.text((name_x, name_y+58), f"{tagline}  ·  {handle}", font=f_tag, fill=(170,178,196))

    if hashtag_pill:
        f_ht = ImageFont.truetype(F_SEMI, 26)
        hb = draw.textbbox((0,0), hashtag_pill, font=f_ht)
        hw = hb[2]-hb[0]
        hx2 = W - pad
        hx1 = hx2 - hw - 44
        hy1 = bar_top + (bar_h-70)//2
        rounded_rect(draw, [hx1,hy1,hx2,hy1+62], radius=999, fill=accent)
        draw.text((hx1+22, hy1+14), hashtag_pill, font=f_ht, fill=(10,10,15))

    img.convert("RGB").save(out_path, "PNG", quality=95)
    print("saved", out_path, img.size)


def make_newsletter_cover(out_path, issue_label, title, subtitle,
                           name="Kapil Kaushal", tagline=".NET Cloud AI Engineer"):
    W, H = 1200, 627
    top = hex2rgb("#0A0F1E")
    bottom = hex2rgb("#141B2E")
    img = vertical_gradient((W,H), top, bottom).convert("RGBA")
    gold = hex2rgb("#F5A623")
    blue = hex2rgb("#3B82F6")

    img.alpha_composite(diagonal_glow((W,H), gold, 0.9, 0.05, 0.30, alpha=90))
    img.alpha_composite(diagonal_glow((W,H), blue, 0.05, 0.95, 0.30, alpha=70))
    img.alpha_composite(dot_grid((W,H), (255,255,255), spacing=50, r=1, alpha=16))

    draw = ImageDraw.Draw(img)
    draw.rectangle([0,0,W,8], fill=gold)

    pad = 70
    f_masthead = ImageFont.truetype(F_SEMI, 30)
    draw.text((pad, 54), "THE .NET HORIZON", font=f_masthead, fill=gold)
    f_issue = ImageFont.truetype(F_REG, 26)
    draw.text((pad, 96), issue_label, font=f_issue, fill=(170,178,196))

    f_title = ImageFont.truetype(F_BOLD, 76)
    max_w = int(W*0.62)
    lines = wrap_to_width(draw, title, f_title, max_w)
    while len(lines) > 3 and f_title.size > 46:
        f_title = ImageFont.truetype(F_BOLD, f_title.size-4)
        lines = wrap_to_width(draw, title, f_title, max_w)
    y = 160
    for ln in lines:
        draw.text((pad, y), ln, font=f_title, fill=(255,255,255))
        y += int(f_title.size*1.15)

    f_sub = ImageFont.truetype(F_REG, 30)
    sub_lines = wrap_to_width(draw, subtitle, f_sub, max_w)
    y += 14
    for ln in sub_lines[:2]:
        draw.text((pad, y), ln, font=f_sub, fill=(196,203,219))
        y += 42

    # branding block bottom-left
    avatar_d = 96
    av = circular_avatar(AVATAR_PATH, avatar_d)
    ring = Image.new("RGBA", (avatar_d+14, avatar_d+14), (0,0,0,0))
    rd = ImageDraw.Draw(ring)
    rd.ellipse([0,0,avatar_d+14,avatar_d+14], outline=gold, width=5)
    ax, ay = pad, H-pad-avatar_d
    img.alpha_composite(ring, (ax-7, ay-7))
    img.alpha_composite(av, (ax, ay))

    draw = ImageDraw.Draw(img)
    f_name = ImageFont.truetype(F_SEMI, 34)
    f_tag = ImageFont.truetype(F_REG, 24)
    draw.text((ax+avatar_d+26, ay+10), name, font=f_name, fill=(255,255,255))
    draw.text((ax+avatar_d+26, ay+52), tagline, font=f_tag, fill=(170,178,196))

    # right-side "newsletter" badge
    f_badge = ImageFont.truetype(F_SEMI, 26)
    badge_text = "NEWSLETTER"
    bb = draw.textbbox((0,0), badge_text, font=f_badge)
    bw = bb[2]-bb[0]
    bx2, by1 = W-pad, H-pad-56
    bx1 = bx2-bw-48
    rounded_rect(draw, [bx1,by1,bx2,by1+56], radius=999, outline=blue, width=3)
    draw.text((bx1+24, by1+14), badge_text, font=f_badge, fill=blue)

    img.convert("RGB").save(out_path, "PNG", quality=95)
    print("saved", out_path, img.size)


if __name__ == "__main__":
    base = "D:/Kapil/Projects/LinkedIn/linkedin-post-writing-skill"

    # Sept 13 bonus post - crossover
    make_post_thumbnail(
        f"{base}/posts/September/13/thumbnail.png",
        eyebrow="HOT TAKE",
        headline_lines=["AGENTIC AI WON'T FIX", "YOUR SLOW BACKEND."],
        accent_hex="#8B5CF6", accent_hex2="#14B8A6",
        code_lines=["→ No caching", "→ N+1 queries", "→ No tracing"],
        hashtag_pill="#AgenticAI"
    )

    # Sept 15 - Pillar 1 .NET performance (violet)
    make_post_thumbnail(
        f"{base}/posts/September/15/thumbnail.png",
        eyebrow="MYTH BUSTED",
        headline_lines=["DOES ASYNC/AWAIT", "CREATE A NEW THREAD?"],
        accent_hex="#8B5CF6", accent_hex2="#6D28D9",
        code_lines=["await _db.Customers", "    .FindAsync(id);", "// no thread blocked"],
        hashtag_pill="#dotnet"
    )

    # Sept 16 - Pillar 3 AI/ML (teal)
    make_post_thumbnail(
        f"{base}/posts/September/16/thumbnail.png",
        eyebrow="AI ENGINEERING",
        headline_lines=["YOUR AI AGENT", "DOESN'T HAVE MEMORY."],
        accent_hex="#14B8A6", accent_hex2="#0EA5E9",
        code_lines=["→ Resent, not remembered", "→ No extraction pipeline", "→ Unbounded log ≠ memory"],
        hashtag_pill="#GenAI"
    )

    # Sept 17 - Pillar 2 cloud native (blue)
    make_post_thumbnail(
        f"{base}/posts/September/17/thumbnail.png",
        eyebrow="PRODUCTION LESSON",
        headline_lines=["YOUR PODS ARE HEALTHY.", "YOUR USERS AREN'T."],
        accent_hex="#2B88D8", accent_hex2="#1E3A8A",
        code_lines=["livenessProbe:  is it alive?", "readinessProbe: can it SERVE?"],
        hashtag_pill="#AKS"
    )

    # Newsletter cover - Sept 14
    make_newsletter_cover(
        f"{base}/newsletters/September/14/thumbnail.png",
        issue_label="ISSUE · SEPTEMBER 2026",
        title="Model Context Protocol",
        subtitle="Every team building tool-using agents invented the same integration layer. Badly."
    )

"""
Thumbnail Template v2 — premium editorial technical illustration system.
Implements the "Future-Ready LinkedIn Thumbnail" master prompt: dark navy
canvas, one dominant visual metaphor per concept, minimal geometric-sans
headline (2-6 words), restrained glow, subtle bottom branding.

This REPLACES the v1 "code editor chip" style (tools/make_thumbnail.py) as
the canonical template. All future thumbnails should be built by calling
`render_thumbnail()` with a metaphor function from the METAPHORS section.
"""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

FONT_DIR = "C:/Windows/Fonts/"
F_HEAD    = FONT_DIR + "segoeuib.ttf"     # headline (closest system geometric sans to Inter/Manrope)
F_HEAD_BLK= FONT_DIR + "seguisb.ttf" if False else FONT_DIR + "segoeuib.ttf"
F_LABEL   = FONT_DIR + "segoeuisl.ttf"    # small caps / category labels (light, editorial)
F_LABEL_M = FONT_DIR + "segoeui.ttf"
F_MONO    = FONT_DIR + "consolab.ttf"     # technical readouts (numbers, metrics)
F_MONO_R  = FONT_DIR + "consola.ttf"

AVATAR_PATH = "D:/Kapil/Projects/LinkedIn/Kapil-AI-1.jpg"

W, H = 1080, 1350

BG_TOP    = (7, 11, 24)      # #070B18
BG_BOTTOM = (11, 17, 34)     # #0B1122
WHITE     = (245, 247, 250)
MUTED     = (138, 147, 166)
FAINT     = (90, 98, 118)

ACCENTS = {
    "cyan":   (34, 211, 238),
    "blue":   (59, 130, 246),
    "violet": (139, 124, 246),
    "amber":  (245, 166, 35),
    "teal":   (45, 212, 191),
}

# ---------------------------------------------------------------- helpers --

def hx(rgb):
    return "#%02x%02x%02x" % rgb

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i]-a[i])*t) for i in range(3))

def vertical_gradient(size, top, bottom):
    w, h = size
    img = Image.new("RGB", size, top)
    d = ImageDraw.Draw(img)
    for y in range(h):
        d.line([(0, y), (w, y)], fill=lerp(top, bottom, y/max(h-1,1)))
    return img

def restrained_glow(size, color, cx_ratio, cy_ratio, radius_ratio, alpha=70):
    """A single soft, low-alpha glow. Restraint is the point — one only."""
    w, h = size
    ov = Image.new("RGBA", size, (0,0,0,0))
    d = ImageDraw.Draw(ov)
    cx, cy = int(w*cx_ratio), int(h*cy_ratio)
    r = int(min(w,h)*radius_ratio)
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color+(alpha,))
    return ov.filter(ImageFilter.GaussianBlur(r//2))

def architectural_grid(size, color=(255,255,255), spacing=90, alpha=7):
    """Extremely faint structural line grid — restraint over decoration."""
    w, h = size
    ov = Image.new("RGBA", size, (0,0,0,0))
    d = ImageDraw.Draw(ov)
    for x in range(0, w, spacing):
        d.line([(x,0),(x,h)], fill=color+(alpha,), width=1)
    for y in range(0, h, spacing):
        d.line([(0,y),(w,y)], fill=color+(alpha,), width=1)
    return ov

def fit_font(path, text, max_width, start, min_size=40, draw=None):
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

def rrect(draw, box, r, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)

def arrow(draw, p1, p2, color, width=3, head=12):
    draw.line([p1,p2], fill=color, width=width)
    ang = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
    for da in (0.5, -0.5):
        a = ang + math.pi - da
        draw.line([p2, (p2[0]+head*math.cos(a), p2[1]+head*math.sin(a))], fill=color, width=width)

def circular_avatar(path, d):
    im = ImageOps.fit(Image.open(path).convert("RGB"), (d,d), Image.LANCZOS)
    mask = Image.new("L", (d,d), 0)
    ImageDraw.Draw(mask).ellipse([0,0,d,d], fill=255)
    out = Image.new("RGBA", (d,d), (0,0,0,0))
    out.paste(im, (0,0), mask)
    return out

def dashed_line(draw, p1, p2, color, width=2, dash=10, gap=8):
    x1,y1 = p1; x2,y2 = p2
    dist = math.hypot(x2-x1, y2-y1)
    if dist == 0: return
    steps = int(dist // (dash+gap)) + 1
    ux, uy = (x2-x1)/dist, (y2-y1)/dist
    pos = 0
    while pos < dist:
        sx, sy = x1+ux*pos, y1+uy*pos
        epos = min(pos+dash, dist)
        ex, ey = x1+ux*epos, y1+uy*epos
        draw.line([(sx,sy),(ex,ey)], fill=color, width=width)
        pos += dash+gap

# --------------------------------------------------------------- METAPHORS --
# Each takes (draw, img, box) where box=(x0,y0,x1,y1) is the center zone,
# and an accent RGB tuple. Draw the ONE dominant visual metaphor only.

def metaphor_fanout(draw, img, box, accent, from_label="1 QUERY", to_label="247 CALLS", n=7):
    """Single node explodes into many — N+1 / query-explosion family."""
    x0,y0,x1,y1 = box
    cx_left = x0 + 90
    cy = (y0+y1)//2 - 20
    bw, bh = 150, 74
    lb = [cx_left-bw//2, cy-bh//2, cx_left+bw//2, cy+bh//2]
    origin = (lb[2]+2, cy)

    cluster_x0 = cx_left + bw//2 + 190
    cluster_x1 = x1 - 40
    rows, cols = 3, 3
    dot_r = 15
    pts = []
    idx = 0
    for r in range(rows):
        for c in range(cols):
            if idx >= n: break
            px = cluster_x0 + c*((cluster_x1-cluster_x0)//(cols-1))
            py = (y0+90) + r*95
            pts.append((px,py)); idx += 1

    # lines + dots drawn first, box + label drawn last so text always stays crisp
    for (px,py) in pts:
        dashed_line(draw, origin, (px,py), accent+(120,), width=2, dash=6, gap=6)
    for (px,py) in pts:
        draw.ellipse([px-dot_r,py-dot_r,px+dot_r,py+dot_r], fill=accent+(230,))

    rrect(draw, lb, 14, fill=(17,24,39,255), outline=WHITE+(255,), width=2)
    f = ImageFont.truetype(F_MONO, 26)
    tb = draw.textbbox((0,0), from_label, font=f)
    draw.text((cx_left-(tb[2]-tb[0])//2, cy-(tb[3]-tb[1])//2-4), from_label, font=f, fill=WHITE)

    f2 = ImageFont.truetype(F_MONO, 40)
    tb2 = draw.textbbox((0,0), to_label, font=f2)
    tx = cluster_x0 + (cluster_x1-cluster_x0)//2 - (tb2[2]-tb2[0])//2
    ty = pts[-1][1] + 70
    draw.text((tx,ty), to_label, font=f2, fill=accent)

def metaphor_before_after(draw, img, box, accent, left_label="80ms", right_label="6s", warn=(239,68,68)):
    """A calm short bar becomes a tall alarming bar — degradation under load."""
    x0,y0,x1,y1 = box
    base_y = y1 - 30
    bar_w = 130
    gap = 220
    lx = x0 + 140
    rx = lx + gap + bar_w
    lh, rh = 60, 300
    rrect(draw, [lx, base_y-lh, lx+bar_w, base_y], 10, fill=(255,255,255,22))
    rrect(draw, [rx, base_y-rh, rx+bar_w, base_y], 10, fill=warn+(210,))
    draw.line([(lx+bar_w, base_y-lh-10),(rx-14, base_y-rh-10)], fill=MUTED+(255,), width=2)
    arrow(draw, (lx+bar_w, base_y-lh-10), (rx-16, base_y-rh-12), MUTED, width=2, head=10)
    fL = ImageFont.truetype(F_MONO, 34)
    fR = ImageFont.truetype(F_MONO, 44)
    tb = draw.textbbox((0,0), left_label, font=fL)
    draw.text((lx+bar_w//2-(tb[2]-tb[0])//2, base_y-lh-52), left_label, font=fL, fill=WHITE)
    tb2 = draw.textbbox((0,0), right_label, font=fR)
    draw.text((rx+bar_w//2-(tb2[2]-tb2[0])//2, base_y-rh-58), right_label, font=fR, fill=warn)

def metaphor_dual_lane(draw, img, box, accent, left_title="EXPECTED", right_title="ACTUAL",
                        left_bad=True):
    """Two compared lanes — expectation vs mechanism (async myth, memory myth)."""
    x0,y0,x1,y1 = box
    lane_w = (x1-x0-60)//2
    l_box = [x0, y0+70, x0+lane_w, y1-20]
    r_box = [x0+lane_w+60, y0+70, x1, y1-20]
    for bx, title, is_left in [(l_box,left_title,True),(r_box,right_title,False)]:
        rrect(draw, bx, 16, outline=FAINT+(255,), width=2)
        f = ImageFont.truetype(F_LABEL_M, 26)
        draw.text((bx[0]+22, bx[1]-46), title, font=f, fill=MUTED)
        cx = (bx[0]+bx[2])//2
        cy = (bx[1]+bx[3])//2
        if is_left and left_bad:
            for i in range(3):
                yy = bx[1]+50+i*70
                draw.line([(bx[0]+30,yy),(bx[2]-30,yy)], fill=FAINT+(200,), width=10)
            draw.line([(bx[0]+20,bx[1]+20),(bx[2]-20,bx[3]-20)], fill=(239,68,68,220), width=6)
            draw.line([(bx[2]-20,bx[1]+20),(bx[0]+20,bx[3]-20)], fill=(239,68,68,220), width=6)
        elif not is_left:
            r = 46
            draw.ellipse([cx-r,cy-r-30,cx+r,cy+r-30], outline=accent+(255,), width=6)
            draw.arc([cx-r+14,cy-r-30+14,cx+r-14,cy+r-30-14], start=30, end=300, fill=accent+(255,), width=4)
            draw.line([(cx+r-8,cy-r-30+14),(cx+r+10,cy-r-30+2)], fill=accent+(255,), width=4)
            f2 = ImageFont.truetype(F_MONO_R, 22)
            draw.text((cx-58, cy+40), "state machine", font=f2, fill=MUTED)
        else:
            for i in range(2):
                yy = bx[1]+60+i*90
                rrect(draw, [bx[0]+30,yy,bx[2]-30,yy+50], 8, fill=(255,255,255,16))

def metaphor_status_mismatch(draw, img, box, accent, ok_text="LIVE", bad_text="NOT READY"):
    """A healthy node still failing its real job — probe/readiness family."""
    x0,y0,x1,y1 = box
    cx, cy = (x0+x1)//2, (y0+y1)//2
    s = 190
    hexpts = []
    for i in range(6):
        a = math.pi/6 + i*math.pi/3
        hexpts.append((cx+s/2*math.cos(a), cy+s/2*math.sin(a)))
    draw.polygon(hexpts, outline=WHITE+(255,), width=4, fill=(255,255,255,10))

    ok_c = (34,197,94)
    bad_c = (239,68,68)
    ox, oy = cx-100, cy-120
    draw.ellipse([ox-22,oy-22,ox+22,oy+22], fill=ok_c+(230,))
    draw.line([(ox-9,oy),(ox-2,oy+9),(ox+11,oy-10)], fill=WHITE+(255,), width=4)
    f = ImageFont.truetype(F_LABEL_M, 24)
    draw.text((ox+30, oy-16), ok_text, font=f, fill=ok_c)

    bx, by = cx+80, cy+130
    draw.ellipse([bx-22,by-22,bx+22,by+22], fill=bad_c+(230,))
    draw.line([(bx-9,by-9),(bx+9,by+9)], fill=WHITE+(255,), width=4)
    draw.line([(bx-9,by+9),(bx+9,by-9)], fill=WHITE+(255,), width=4)
    draw.text((bx+30, by-16), bad_text, font=f, fill=bad_c)

    dashed_line(draw, (x0+30, y0+30), (cx-70,cy-40), accent+(180,), width=3, dash=8, gap=6)
    arrow(draw, (cx-90,cy-55), (cx-70,cy-40), accent, width=3, head=10)

def metaphor_chaos_to_standard(draw, img, box, accent, n=4):
    """Several mismatched shapes converge into one clean interface — standardization."""
    x0,y0,x1,y1 = box
    cy = (y0+y1)//2
    shapes_x = x0+60
    target_x = x0 + int((x1-x0)*0.55)
    target_y = cy
    pts_y = [y0+40 + i*((y1-y0-80)//(n-1)) for i in range(n)]
    import random
    rnd = random.Random(7)
    for i,py in enumerate(pts_y):
        sides = rnd.choice([3,5,6])
        r = 34
        ang0 = rnd.random()*math.pi
        poly = [(shapes_x + r*math.cos(ang0+2*math.pi*k/sides), py + r*math.sin(ang0+2*math.pi*k/sides)) for k in range(sides)]
        draw.polygon(poly, outline=FAINT+(255,), width=3)
        dashed_line(draw, (shapes_x+r, py), (target_x-60, target_y), FAINT+(160,), width=2, dash=6, gap=6)

    rrect(draw, [target_x-40, target_y-90, target_x+70, target_y+90], 18, fill=accent+(40,), outline=accent+(255,), width=4)
    f = ImageFont.truetype(F_MONO, 26)
    draw.text((target_x-32, target_y-14), "MCP", font=f, fill=accent)
    node_x = min(target_x+170, x1-46)
    draw.ellipse([node_x-40,target_y-40,node_x+40,target_y+40], outline=WHITE+(255,), width=4)
    arrow(draw, (target_x+72,target_y), (node_x-42,target_y), WHITE, width=3, head=10)

METAPHORS = {
    "fanout": metaphor_fanout,
    "before_after": metaphor_before_after,
    "dual_lane": metaphor_dual_lane,
    "status_mismatch": metaphor_status_mismatch,
    "chaos_to_standard": metaphor_chaos_to_standard,
}

# ------------------------------------------------------------- main render --

def render_thumbnail(out_path, headline, metaphor, metaphor_kwargs=None,
                      category="", accent="cyan", name="Kapil Kaushal",
                      handle="@kapilkaushal24", brand_tag=None):
    """
    headline: 2-6 words, ALL CAPS recommended, short contradiction/number hook.
    metaphor: key into METAPHORS dict.
    category: small top-left label, e.g. ".NET PERFORMANCE" / "AI ENGINEERING".
    accent: key into ACCENTS dict — keep pillar-consistent across posts.
    brand_tag: optional small bottom-right tag, e.g. "THE .NET HORIZON".
    """
    accent_rgb = ACCENTS[accent]
    img = vertical_gradient((W,H), BG_TOP, BG_BOTTOM).convert("RGBA")
    img.alpha_composite(restrained_glow((W,H), accent_rgb, 0.82, 0.14, 0.30, alpha=55))
    img.alpha_composite(architectural_grid((W,H)))

    draw = ImageDraw.Draw(img)
    pad = 78

    # thin top accent rule + category label
    draw.line([(pad, 64),(pad+46, 64)], fill=accent_rgb, width=4)
    if category:
        f_cat = ImageFont.truetype(F_LABEL, 27)
        draw.text((pad+62, 50), category.upper(), font=f_cat, fill=MUTED)

    # headline — top 20-30% zone
    f_head = fit_font(F_HEAD, headline, W-pad*2, 96, min_size=56, draw=draw)
    lines = wrap(draw, headline, f_head, W-pad*2)
    while len(lines) > 3 and f_head.size > 52:
        f_head = ImageFont.truetype(F_HEAD, f_head.size-4)
        lines = wrap(draw, headline, f_head, W-pad*2)
    y = 128
    line_h = int(f_head.size*1.16)
    for ln in lines:
        draw.text((pad, y), ln, font=f_head, fill=WHITE)
        y += line_h
    headline_bottom = y + 20

    # center metaphor zone (40-50%)
    zone_top = max(headline_bottom, int(H*0.34))
    zone_bottom = int(H*0.86)
    METAPHORS[metaphor](draw, img, (pad, zone_top, W-pad, zone_bottom), accent_rgb, **(metaphor_kwargs or {}))

    # subtle bottom branding — never competes with headline
    draw.line([(pad, H-118),(W-pad, H-118)], fill=(255,255,255,26), width=1)
    av_d = 62
    av = circular_avatar(AVATAR_PATH, av_d)
    ring = Image.new("RGBA",(av_d+8,av_d+8),(0,0,0,0))
    ImageDraw.Draw(ring).ellipse([0,0,av_d+8,av_d+8], outline=accent_rgb, width=3)
    ax, ay = pad, H-92
    img.alpha_composite(ring,(ax-4,ay-4))
    img.alpha_composite(av,(ax,ay))
    draw = ImageDraw.Draw(img)
    f_name = ImageFont.truetype(F_LABEL_M, 28)
    f_handle = ImageFont.truetype(F_LABEL, 23)
    draw.text((ax+av_d+22, ay+2), name, font=f_name, fill=WHITE)
    draw.text((ax+av_d+22, ay+34), handle, font=f_handle, fill=MUTED)

    if brand_tag:
        f_bt = ImageFont.truetype(F_LABEL, 24)
        bb = draw.textbbox((0,0), brand_tag.upper(), font=f_bt)
        bw = bb[2]-bb[0]
        draw.text((W-pad-bw, ay+16), brand_tag.upper(), font=f_bt, fill=accent_rgb)

    img.convert("RGB").save(out_path, "PNG", quality=95)
    print("saved", out_path)


def render_newsletter_cover(out_path, issue_num, headline, subline, metaphor, metaphor_kwargs=None,
                             accent="amber", name="Kapil Kaushal"):
    Wn, Hn = 1200, 627
    accent_rgb = ACCENTS[accent]
    img = vertical_gradient((Wn,Hn), BG_TOP, BG_BOTTOM).convert("RGBA")
    img.alpha_composite(restrained_glow((Wn,Hn), accent_rgb, 0.88, 0.08, 0.30, alpha=55))
    img.alpha_composite(architectural_grid((Wn,Hn)))
    draw = ImageDraw.Draw(img)
    pad = 64

    f_mast = ImageFont.truetype(F_LABEL_M, 27)
    draw.text((pad, 46), "THE .NET HORIZON", font=f_mast, fill=accent_rgb)
    f_issue = ImageFont.truetype(F_LABEL, 22)
    draw.text((pad, 80), issue_num.upper(), font=f_issue, fill=MUTED)

    f_head = fit_font(F_HEAD, headline, int(Wn*0.56), 68, min_size=42, draw=draw)
    lines = wrap(draw, headline, f_head, int(Wn*0.56))
    y = 132
    for ln in lines:
        draw.text((pad, y), ln, font=f_head, fill=WHITE)
        y += int(f_head.size*1.14)
    f_sub = ImageFont.truetype(F_LABEL_M, 25)
    for ln in wrap(draw, subline, f_sub, int(Wn*0.5))[:2]:
        draw.text((pad, y+10), ln, font=f_sub, fill=MUTED)
        y += 34

    METAPHORS[metaphor](draw, img, (int(Wn*0.58), 70, Wn-40, Hn-100), accent_rgb, **(metaphor_kwargs or {}))

    draw.line([(pad, Hn-84),(Wn-pad, Hn-84)], fill=(255,255,255,26), width=1)
    av_d = 56
    av = circular_avatar(AVATAR_PATH, av_d)
    ring = Image.new("RGBA",(av_d+8,av_d+8),(0,0,0,0))
    ImageDraw.Draw(ring).ellipse([0,0,av_d+8,av_d+8], outline=accent_rgb, width=3)
    ax, ay = pad, Hn-66
    img.alpha_composite(ring,(ax-4,ay-4))
    img.alpha_composite(av,(ax,ay))
    draw = ImageDraw.Draw(img)
    f_name = ImageFont.truetype(F_LABEL_M, 25)
    draw.text((ax+av_d+20, ay+10), f"{name}  ·  @kapilkaushal24", font=f_name, fill=WHITE)

    img.convert("RGB").save(out_path, "PNG", quality=95)
    print("saved", out_path)


if __name__ == "__main__":
    base = "D:/Kapil/Projects/LinkedIn/linkedin-post-writing-skill"

    # flagship template-reference example (from the master prompt itself)
    render_thumbnail(
        f"{base}/tools/template_reference_example.png",
        headline="1 QUERY \u2192 247",
        metaphor="fanout", metaphor_kwargs=dict(from_label="1 QUERY", to_label="247 CALLS"),
        category=".NET Performance", accent="violet",
    )

    # Sept 13 — agentic AI vs backend fundamentals
    render_thumbnail(
        f"{base}/posts/September/13/thumbnail.png",
        headline="AI AMPLIFIES WEAK BACKENDS",
        metaphor="before_after", metaphor_kwargs=dict(left_label="FAST API", right_label="AGENT + TIMEOUT"),
        category="AI + Backend Engineering", accent="violet",
    )

    # Sept 15 — async/await myth
    render_thumbnail(
        f"{base}/posts/September/15/thumbnail.png",
        headline="ASYNC \u2260 NEW THREAD",
        metaphor="dual_lane", metaphor_kwargs=dict(left_title="EXPECTED", right_title="ACTUAL"),
        category=".NET Performance", accent="violet",
    )

    # Sept 16 — AI agent memory myth
    render_thumbnail(
        f"{base}/posts/September/16/thumbnail.png",
        headline="STORED \u2260 REMEMBERED",
        metaphor="dual_lane", metaphor_kwargs=dict(left_title="RESENT", right_title="EXTRACTED", left_bad=True),
        category="AI Engineering", accent="teal",
    )

    # Sept 17 — AKS readiness vs liveness
    render_thumbnail(
        f"{base}/posts/September/17/thumbnail.png",
        headline="ALIVE \u2260 READY",
        metaphor="status_mismatch", metaphor_kwargs=dict(ok_text="LIVE", bad_text="NOT READY"),
        category="Cloud-Native / AKS", accent="blue",
    )

    # Sept 14 — newsletter: Model Context Protocol
    render_newsletter_cover(
        f"{base}/newsletters/September/14/thumbnail.png",
        issue_num="Issue · September 2026",
        headline="Tools, Standardized.",
        subline="Every team building AI agents invented the same integration layer. Badly.",
        metaphor="chaos_to_standard", metaphor_kwargs=dict(n=4),
        accent="amber",
    )

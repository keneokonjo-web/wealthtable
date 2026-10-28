"""Logo suite, icons, avatars and art for the brand kit. Run: PYTHONPATH=/tmp/pylibs python3 scripts/brand/build_logos.py"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

OUT = KIT
os.makedirs(f'{OUT}/logos/svg', exist_ok=True)
os.makedirs(f'{OUT}/logos/png', exist_ok=True)

M = VEC['wt-monogram']; WM = VEC['wordmark']; TG = VEC['tagline']; LF = VEC['lockup-full']


def svg_wrap(w, h, inner, bg=None):
    b = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{b}{inner}</svg>'


def path_group(vec, x, y, scale, color):
    return f'<g transform="translate({x:.2f} {y:.2f}) scale({scale:.5f})"><path fill="{color}" fill-rule="evenodd" d="{vec["d"]}"/></g>'


# ------------------------------------------------------------------ text on a circle -> outlines
def circle_text(text, font_path, radius, size, color, sep_r=0):
    f = TTFont(font_path); gs = f.getGlyphSet(); cmap = f.getBestCmap(); upem = f['head'].unitsPerEm; s = size / upem
    hmtx = f['hmtx']
    items = []
    for ch in text:
        if ch == '|':
            items.append(('sep', size * 1.1))
        else:
            gn = cmap[ord(ch)]; items.append((gn, hmtx[gn][0] * s))
    n_gaps = len(items)
    total = sum(a for _, a in items)
    circ = 2 * math.pi * radius
    track = (circ - total) / n_gaps
    pos = 0; out = []
    for gn, adv in items:
        mid = pos + adv / 2
        ang = mid / radius * 180 / math.pi
        if gn == 'sep':
            # small diamond between phrases
            d = size * .16
            out.append(f'<g transform="rotate({ang:.3f}) translate(0 {-(radius + size * .36):.2f}) rotate(45)"><rect x="{-d / 2:.2f}" y="{-d / 2:.2f}" width="{d:.2f}" height="{d:.2f}" fill="{color}"/></g>')
        else:
            pen = SVGPathPen(gs)
            gs[gn].draw(TransformPen(pen, (s, 0, 0, -s, 0, 0)))
            d = pen.getCommands()
            if d:
                out.append(f'<g transform="rotate({ang:.3f}) translate({-adv / 2:.2f} {-radius:.2f})"><path d="{d}" fill="{color}"/></g>')
        pos += adv + track
    return ''.join(out)


BOD = f'{KIT}/fonts/BodoniModa-Regular-500.ttf'


def seal(color, bg=None, size=1000):
    c = size / 2
    inner = (f'<circle cx="{c}" cy="{c}" r="{c - 14}" fill="none" stroke="{color}" stroke-width="7"/>'
             f'<circle cx="{c}" cy="{c}" r="{c - 30}" fill="none" stroke="{color}" stroke-width="2"/>'
             f'<circle cx="{c}" cy="{c}" r="{c * .64}" fill="none" stroke="{color}" stroke-width="2"/>'
             f'<g transform="translate({c} {c})">{circle_text("THE WEALTH TABLE|LEAVE RICHER THAN YOU ARRIVED|", BOD, c * .745, c * .105, color)}</g>'
             + path_group(M, c - 168, c - 73, 336 / M['w'], color))
    return svg_wrap(size, size, inner, bg)


def seat_mark(color, bg=None, size=1000, seats=8):
    c = size / 2
    r_t, r_s, r_o = c * .32, c * .66, c * .9
    dots = ''.join(f'<circle cx="{c + r_s * math.cos(2 * math.pi * i / seats - math.pi / 2):.2f}" cy="{c + r_s * math.sin(2 * math.pi * i / seats - math.pi / 2):.2f}" r="{c * .075:.2f}" fill="{color}"/>' for i in range(seats))
    inner = (f'<circle cx="{c}" cy="{c}" r="{r_o}" fill="none" stroke="{color}" stroke-width="2.5"/>'
             f'<circle cx="{c}" cy="{c}" r="{r_t}" fill="none" stroke="{color}" stroke-width="5"/>' + dots +
             path_group(M, c - c * .21, c - c * .0925, (c * .42) / M['w'], color))
    return svg_wrap(size, size, inner, bg)


def monogram_ring(color, bg=None, size=1000):
    c = size / 2
    inner = (f'<circle cx="{c}" cy="{c}" r="{c - 14}" fill="none" stroke="{color}" stroke-width="7"/>'
             f'<circle cx="{c}" cy="{c}" r="{c - 36}" fill="none" stroke="{color}" stroke-width="2"/>'
             + path_group(M, c - 215, c - 93.5, 430 / M['w'], color))
    return svg_wrap(size, size, inner, bg)


def horizontal(color, bg=None, tagline=True):
    W, H = 2200, 520 if tagline else 440
    ms = 360 / M['h']                       # monogram height 360
    mw = M['w'] * ms
    x2 = 70 + mw + 90
    ws = 1060 / WM['w']
    wy = 60 if not tagline else 40
    inner = path_group(M, 70, (H - 360) / 2, ms, color)
    inner += f'<rect x="{70 + mw + 44}" y="{(H - 360) / 2}" width="4" height="360" fill="{color}"/>'
    inner += path_group(WM, x2, wy + (0 if tagline else 70), ws, color)
    if tagline:
        ts = 760 / TG['w']
        inner += path_group(TG, x2 + 30, wy + WM['h'] * ws + 60, ts, color)
    return svg_wrap(W, H, inner, bg)


def stacked(color, bg=None):
    return svg_wrap(LF['w'] + 120, LF['h'] + 120, path_group(LF, 60, 60, 1, color), bg)


def wordmark_only(color, bg=None):
    return svg_wrap(WM['w'] + 120, WM['h'] + 120, path_group(WM, 60, 60, 1, color), bg)


def monogram_only(color, bg=None):
    return svg_wrap(M['w'] + 120, M['h'] + 120, path_group(M, 60, 60, 1, color), bg)


LOGOS = {
    'primary-stacked': stacked, 'horizontal': horizontal, 'wordmark': wordmark_only, 'monogram': monogram_only,
    'seal': seal, 'table-mark': seat_mark, 'monogram-ring': monogram_ring,
}
TONES = {'olive': C['olive'], 'terracotta': C['terra'], 'ink': C['ink'], 'sand': C['sand'], 'white': '#FFFFFF'}

for name, fn in LOGOS.items():
    for tone, col in TONES.items():
        svg = fn(col)
        open(f'{OUT}/logos/svg/{name}-{tone}.svg', 'w').write(svg)
        # PNG (transparent), 2400px on the long side
        import re
        w, h = [float(x) for x in re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg).groups()]
        target = 2400; sc = target / max(w, h)
        render(f'logo_{name}_{tone}', page(f'<div style="width:{w}px;height:{h}px">{svg}</div>', int(w), int(h)), int(w), int(h), f'{OUT}/logos/png/{name}-{tone}.png', scale=sc, transparent=True)

# ------------------------------------------------------------------ icons (48 grid, 1.6 stroke)
def dots_ring(cx, cy, r, n, rr):
    return ''.join(f'<circle cx="{cx + r * math.cos(2 * math.pi * i / n - math.pi / 2):.2f}" cy="{cy + r * math.sin(2 * math.pi * i / n - math.pi / 2):.2f}" r="{rr}" fill="currentColor" stroke="none"/>' for i in range(n))


ICONS = {
    'table': '<circle cx="24" cy="24" r="8.5"/>' + dots_ring(24, 24, 16.5, 8, 2.3),
    'invitation': '<rect x="6" y="12" width="36" height="24" rx="2"/><path d="M6 14l18 13 18-13"/><circle cx="24" cy="27" r="3.4"/>',
    'calendar': '<rect x="7" y="10" width="34" height="31" rx="3"/><path d="M7 19h34M16 6v8M32 6v8"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="currentColor" stroke="none"/>' for x in (15, 24, 33) for y in (26, 33)),
    'location': '<path d="M24 43S11 30 11 20a13 13 0 0 1 26 0c0 10-13 23-13 23z"/><circle cx="24" cy="20" r="4.5"/>',
    'connection': '<circle cx="18" cy="24" r="11"/><circle cx="30" cy="24" r="11"/>',
    'opportunity': '<path d="M8 37l13-13 7 7 13-15"/><path d="M31 16h10v10"/>',
    'collaboration': '<circle cx="24" cy="17" r="9"/><circle cx="16.5" cy="30" r="9"/><circle cx="31.5" cy="30" r="9"/>',
    'ownership': '<circle cx="15" cy="24" r="8"/><path d="M23 24h19M35 24v7M41 24v5"/>',
    'wealth': '<circle cx="24" cy="24" r="16"/><circle cx="24" cy="24" r="11"/><path d="M24 18.5l5.5 5.5-5.5 5.5-5.5-5.5z"/>',
    'gallery': '<rect x="6" y="9" width="36" height="30" rx="2"/><path d="M6 33l11-11 8 8 5-5 12 11"/><circle cx="33" cy="17" r="3"/>',
    'conversation': '<rect x="18" y="6" width="12" height="22" rx="6"/><path d="M12 23a12 12 0 0 0 24 0M24 35v7M17 42h14"/>',
    'arrow': '<path d="M8 24h31M29 14l10 10-10 10"/>',
}
os.makedirs(f'{OUT}/icons/svg', exist_ok=True); os.makedirs(f'{OUT}/icons/png', exist_ok=True)
for n, body in ICONS.items():
    for tone, col in (('ink', C['ink']), ('olive', C['olive']), ('sand', C['sand'])):
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="96" height="96" fill="none" stroke="{col}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" color="{col}">{body}</svg>'
        open(f'{OUT}/icons/svg/{n}-{tone}.svg', 'w').write(svg)
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="512" height="512" fill="none" stroke="{C["olive"]}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" color="{C["olive"]}">{body}</svg>'
    render(f'icon_{n}', page(svg, 512, 512), 512, 512, f'{OUT}/icons/png/{n}.png', transparent=True)

# ------------------------------------------------------------------ avatars (1080 square, safe for circle crop)
os.makedirs(f'{OUT}/avatars', exist_ok=True)
AV = [
    ('olive-monogram', C['olive'], monogram_only(C['sand'])),
    ('terracotta-monogram', C['terra'], monogram_only(C['sand'])),
    ('sand-monogram', C['sand'], monogram_only(C['olive'])),
    ('ink-monogram', C['olive_d'], monogram_only(C['sand'])),
    ('olive-seal', C['olive'], seal(C['sand'])),
    ('sand-seal', C['sand'], seal(C['terra'])),
    ('terracotta-table-mark', C['terra'], seat_mark(C['sand'])),
    ('sand-ring', C['sand'], monogram_ring(C['olive'])),
]
for n, bg, svg in AV:
    inner = f'<div style="width:1080px;height:1080px;background:{bg};display:grid;place-items:center"><div style="width:{720 if "monogram" in n and "ring" not in n and "table" not in n else 860}px">{svg.replace("width=", "data-w=")}</div></div>'
    inner = inner.replace('<svg ', '<svg style="width:100%;height:auto;display:block" ', 1)
    render(f'avatar_{n}', page(inner, 1080, 1080), 1080, 1080, f'{OUT}/avatars/avatar-{n}.png')

# ------------------------------------------------------------------ art: patterns + backgrounds
os.makedirs(f'{OUT}/art', exist_ok=True)


def tile_seats(bg, fg, size=240):
    c = size / 2
    dots = ''.join(f'<circle cx="{c + 58 * math.cos(2 * math.pi * i / 8):.1f}" cy="{c + 58 * math.sin(2 * math.pi * i / 8):.1f}" r="5" fill="{fg}"/>' for i in range(8))
    return svg_wrap(size, size, f'<circle cx="{c}" cy="{c}" r="32" fill="none" stroke="{fg}" stroke-width="1.6"/><circle cx="{c}" cy="{c}" r="96" fill="none" stroke="{fg}" stroke-width=".8" opacity=".7"/>' + dots, bg)


def tile_monogram(bg, fg, size=300):
    return svg_wrap(size, size, path_group(M, 78, 112, 144 / M['w'], fg), bg)


def ripples(bg, fg, w=3000, h=2000, cx=2300, cy=1500, n=16, step=110, gold=None):
    rings = ''.join(f'<circle cx="{cx}" cy="{cy}" r="{150 + i * step}" fill="none" stroke="{gold if gold and i % 4 == 0 else fg}" stroke-width="{2.6 if gold and i % 4 == 0 else 1.4}" opacity="{max(.18, 1 - i * .045):.2f}"/>' for i in range(n))
    return svg_wrap(w, h, rings, bg)


def seats_large(bg, fg, w=3000, h=2000):
    c = (1500, 1000); out = ''
    for r, n, rr, op in ((330, 10, 22, 1), (560, 14, 16, .8), (790, 20, 12, .6), (1020, 26, 9, .45)):
        out += f'<circle cx="{c[0]}" cy="{c[1]}" r="{r - 96}" fill="none" stroke="{fg}" stroke-width="1.4" opacity="{op * .7}"/>'
        out += ''.join(f'<circle cx="{c[0] + r * math.cos(2 * math.pi * i / n):.1f}" cy="{c[1] + r * math.sin(2 * math.pi * i / n):.1f}" r="{rr}" fill="{fg}" opacity="{op}"/>' for i in range(n))
    out += f'<circle cx="{c[0]}" cy="{c[1]}" r="170" fill="none" stroke="{fg}" stroke-width="3"/>' + path_group(M, c[0] - 105, c[1] - 46, 210 / M['w'], fg)
    return svg_wrap(w, h, out, bg)


ART = [
    ('ripple-olive', ripples(C['olive'], C['sand'], gold=C['gold'])),
    ('ripple-sand', ripples(C['sand'], C['olive'], gold=C['gold'])),
    ('ripple-terracotta', ripples(C['terra'], C['sand'], cx=700, cy=500)),
    ('seats-large-sand', seats_large(C['sand'], C['terra'])),
    ('seats-large-olive', seats_large(C['olive'], C['sand'])),
]
for n, svg in ART:
    open(f'{OUT}/art/{n}.svg', 'w').write(svg)
    render(f'art_{n}', page(f'<div style="width:3000px;height:2000px">{svg}</div>', 3000, 2000), 3000, 2000, f'{OUT}/art/{n}.png')
for n, svg in (('pattern-seats-sand', tile_seats(C['sand'], C['olive'])), ('pattern-seats-olive', tile_seats(C['olive'], C['sand'])),
               ('pattern-seats-blush-terracotta', tile_seats(C['blush'], C['terra'])), ('pattern-monogram-terracotta', tile_monogram(C['terra'], '#a8604c')),
               ('pattern-monogram-sand', tile_monogram(C['sand'], '#e6dcc6'))):
    open(f'{OUT}/art/{n}.svg', 'w').write(svg)
    import base64
    uri = 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()
    render(f'art_{n}', page(f'<div style="width:3000px;height:2000px;background:url({uri}) 0 0/{240 if "seats" in n else 300}px"></div>', 3000, 2000), 3000, 2000, f'{OUT}/art/{n}.png')

flush()
print('logos, icons, avatars, art done')

"""Shared helpers for the brand kit generators."""
import json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KIT = os.path.join(ROOT, 'brand-kit')
TMP = '/tmp/claude-0/-home-user-wealthtable/6c09b34e-63a3-5f59-8e3d-2102b39edbcc/scratchpad/brand_html'
os.makedirs(TMP, exist_ok=True)
FILE = 'file://'

# ---- palette (matches the website) ----
C = dict(
    sand='#F8F2E5', blush='#F5EEE9', stone='#E3E1D4', olive='#4F5B2A', olive_d='#373F1D', terra='#8F4B38',
    ink='#262A1A', gold='#B8923A', white='#FFFFFF')

VEC = {n: json.load(open(f'{KIT}/_vector/{n}.json')) for n in ['wt-monogram', 'wordmark', 'tagline', 'lockup-full']}


def logo(name, color, width=None, height=None, extra=''):
    v = VEC[name]
    wh = ''
    if width: wh = f'width="{width}" height="{width * v["h"] / v["w"]:.2f}"'
    if height: wh = f'height="{height}" width="{height * v["w"] / v["h"]:.2f}"'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {v["w"]} {v["h"]}" {wh} {extra} role="img" aria-label="The Wealth Table">'
            f'<path fill="{color}" fill-rule="evenodd" d="{v["d"]}"/></svg>')


def logo_path(name):
    return VEC[name]['d']


def font_css():
    fd = f'{FILE}{KIT}/fonts/'
    faces = [
        ('Lexend Zetta', 200, 'normal', 'LexendZetta-Regular-200'), ('Lexend Zetta', 300, 'normal', 'LexendZetta-Regular-300'), ('Lexend Zetta', 400, 'normal', 'LexendZetta-Regular-400'),
        ('Hanken Grotesk', 300, 'normal', 'HankenGrotesk-Regular-300'), ('Hanken Grotesk', 400, 'normal', 'HankenGrotesk-Regular-400'), ('Hanken Grotesk', 500, 'normal', 'HankenGrotesk-Regular-500'), ('Hanken Grotesk', 600, 'normal', 'HankenGrotesk-Regular-600'),
        ('Antonio', 300, 'normal', 'Antonio-Regular-300'), ('Antonio', 400, 'normal', 'Antonio-Regular-400'), ('Antonio', 600, 'normal', 'Antonio-Regular-600'),
        ('Bodoni Moda', 400, 'normal', 'BodoniModa-Regular-400'), ('Bodoni Moda', 500, 'normal', 'BodoniModa-Regular-500'), ('Bodoni Moda', 700, 'normal', 'BodoniModa-Regular-700'),
        ('Bodoni Moda', 400, 'italic', 'BodoniModa-Italic-400'), ('Bodoni Moda', 500, 'italic', 'BodoniModa-Italic-500'),
    ]
    return '\n'.join(f"@font-face{{font-family:'{f}';font-weight:{w};font-style:{s};src:url('{fd}{fn}.ttf')}}" for f, w, s, fn in faces)


BASE_CSS = font_css() + f'''
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{--sand:{C['sand']};--blush:{C['blush']};--stone:{C['stone']};--olive:{C['olive']};--olive-d:{C['olive_d']};--terra:{C['terra']};--ink:{C['ink']};--gold:{C['gold']}}}
body{{font-family:'Hanken Grotesk',sans-serif;font-weight:300;color:var(--ink);-webkit-font-smoothing:antialiased}}
.wide{{font-family:'Lexend Zetta',sans-serif;text-transform:uppercase;font-weight:200;letter-spacing:.02em}}
.cond{{font-family:'Antonio',sans-serif;text-transform:uppercase;font-weight:300}}
.didone{{font-family:'Bodoni Moda',serif;font-weight:400}}
.cap{{font-size:12px;letter-spacing:.26em;text-transform:uppercase;font-weight:400}}
'''


def page(body, w, h, css='', bg='transparent'):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}html,body{{width:{w}px;height:{h}px;background:{bg};overflow:hidden}}{css}</style></head><body>{body}</body></html>'


JOBS = []


def render(name, html, w, h, out, scale=1, transparent=False, pdf=False):
    """Queue an HTML page for rendering to PNG (or PDF)."""
    p = os.path.join(TMP, name.replace('/', '_') + '.html')
    open(p, 'w', encoding='utf8').write(html)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    JOBS.append(dict(html=FILE + p, w=w, h=h, out=out, scale=scale, transparent=transparent, pdf=pdf))


def flush():
    jp = os.path.join(TMP, 'jobs.json')
    json.dump(JOBS, open(jp, 'w'))
    r = subprocess.run(['node', os.path.join(ROOT, 'scripts/brand/render.js'), jp], capture_output=True, text=True, cwd='/tmp/claude-0/-home-user-wealthtable/6c09b34e-63a3-5f59-8e3d-2102b39edbcc/scratchpad')
    print(r.stdout[-1500:], r.stderr[-1500:])
    JOBS.clear()

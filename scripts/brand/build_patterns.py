"""Brand kit pattern files (SVG tiles + PNG previews). Run: PYTHONPATH=/tmp/pylibs python3 scripts/brand/build_patterns.py"""
import sys, os, shutil, base64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
import patterns as PT

ART = f'{KIT}/art'
shutil.rmtree(ART, ignore_errors=True)
os.makedirs(f'{ART}/svg-tiles', exist_ok=True)
os.makedirs(f'{ART}/png', exist_ok=True)

SCALE = {'kente': 1.15, 'adire': 1.3, 'mudcloth': 1.15, 'beadwork': 1.3, 'chain': 1.4}
for name, fn in PT.PATTERNS.items():
    for cw, (bg, ln, ac) in PT.COLORWAYS.items():
        svg = fn(bg, ln, ac)
        open(f'{ART}/svg-tiles/pattern-{name}-{cw}.svg', 'w').write(svg)
        # full-size preview 3000 x 2000 (tile repeated, lines kept thin)
        w, h = [int(x) for x in __import__('re').search(r'width="(\d+)" height="(\d+)"', svg).groups()]
        uri = 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()
        s = SCALE[name]
        render(f'pat_{name}_{cw}', page(f'<div style="width:3000px;height:2000px;background:url({uri}) 0 0/{w * s * 1.6:.0f}px {h * s * 1.6:.0f}px"></div>', 3000, 2000), 3000, 2000, f'{ART}/png/pattern-{name}-{cw}.png')

# woven border strips
for cw, (bg, ln, ac) in PT.COLORWAYS.items():
    svg = PT.strip(1600, 64, ln, ac, bg)
    open(f'{ART}/svg-tiles/border-strip-{cw}.svg', 'w').write(svg)
    render(f'strip_{cw}', page(f'<div style="width:1600px;height:64px">{svg}</div>', 1600, 64), 1600, 64, f'{ART}/png/border-strip-{cw}.png')

# overview sheet
tiles = ''.join(
    f'<div style="height:300px;background:url(data:image/svg+xml;base64,{base64.b64encode(PT.PATTERNS[n](*PT.COLORWAYS[cw]).encode()).decode()}) 0 0/{int(__import__("re").search(r"width=.(\d+)", PT.PATTERNS[n](*PT.COLORWAYS[cw])).group(1)) * SCALE[n]:.0f}px;position:relative"><span style="position:absolute;left:10px;bottom:8px;font:600 12px Hanken Grotesk;letter-spacing:.14em;text-transform:uppercase;background:rgba(255,255,255,.85);padding:3px 8px">{n}</span></div>'
    for cw in ('ivory-burgundy', 'burgundy-gold') for n in PT.PATTERNS)
render('pattern_sheet', page(f'<div style="display:grid;grid-template-columns:repeat(5,1fr);width:1600px">{tiles}</div>', 1600, 600), 1600, 600, f'{ART}/overview.png')
flush()
print('patterns done')

"""Traces the raster logo files (transparent PNG) into true vector SVG paths with potrace.
Output: brand-kit/_vector/<name>.path (path data + viewBox) used by the logo builder."""
import sys, json, os
sys.path.insert(0, '/tmp/pylibs')
import numpy as np
from PIL import Image
import potrace

SRC = 'assets/img/logo/'
OUT = 'brand-kit/_vector/'
os.makedirs(OUT, exist_ok=True)
SCALE = 3

def trace(name):
    im = Image.open(SRC + name + '-cream.png').convert('RGBA')
    w, h = im.size
    a = np.array(im.split()[3].resize((w * SCALE, h * SCALE), Image.LANCZOS)) > 127
    bm = potrace.Bitmap(~a)
    pl = bm.trace(turdsize=6, turnpolicy=potrace.POTRACE_TURNPOLICY_MINORITY, alphamax=1.0, opticurve=True, opttolerance=0.25)
    d = []
    f = lambda p: f'{p.x / SCALE:.2f} {p.y / SCALE:.2f}'
    for curve in pl:
        d.append('M' + f(curve.start_point))
        for seg in curve.segments:
            if seg.is_corner:
                d.append('L' + f(seg.c) + 'L' + f(seg.end_point))
            else:
                d.append('C' + f(seg.c1) + ' ' + f(seg.c2) + ' ' + f(seg.end_point))
        d.append('Z')
    json.dump({'w': w, 'h': h, 'd': ''.join(d)}, open(OUT + name + '.json', 'w'))
    print(name, w, h, len(''.join(d)) // 1024, 'KB path')

for n in ['wt-monogram', 'wordmark', 'tagline', 'lockup-full']:
    trace(n)

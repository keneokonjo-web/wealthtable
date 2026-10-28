"""Posters: Lagos (invitation), Accra and Nairobi (recap). Run: PYTHONPATH=/tmp/pylibs python3 scripts/brand/build_posters.py"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

P = f'{FILE}{ROOT}/assets/img/photos/'
FL = f'{FILE}{ROOT}/assets/img/flags/'
OUT = f'{KIT}/posters'
os.makedirs(OUT, exist_ok=True)

GRAIN = ("data:image/svg+xml;utf8," + "<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 .3  0 0 0 0 .25  0 0 0 0 .15  0 0 0 .55 0'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")


def ripples_svg(cx, cy, n, step, color, w, h, r0=120, op=.5, hi=None):
    rings = ''.join(f'<circle cx="{cx}" cy="{cy}" r="{r0 + i * step}" fill="none" stroke="{hi if hi and i % 3 == 0 else color}" stroke-width="{1.8 if hi and i % 3 == 0 else 1}" opacity="{max(.12, op - i * .03):.2f}"/>' for i in range(n))
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="position:absolute;inset:0">{rings}</svg>'


def flag_chip(code, h=26):
    return f'<img src="{FL}{code}.svg" style="height:{h}px;width:{h * 1.5:.0f}px;border-radius:3px;box-shadow:0 0 0 1px rgba(38,42,26,.2);vertical-align:middle">'


CSS = f'''
.poster{{position:relative;width:1200px;height:1800px;background:{C['sand']};overflow:hidden}}
.grain{{position:absolute;inset:0;background:url("{GRAIN}");opacity:.16;mix-blend-mode:multiply;pointer-events:none}}
.frame{{position:absolute;inset:46px;border:1.6px solid {C['gold']}}}
.frame2{{position:absolute;inset:60px;border:.7px solid {C['gold']}}}
.c{{position:absolute;left:0;right:0;text-align:center}}
.lab{{font-family:'Lexend Zetta';font-weight:300;font-size:14px;letter-spacing:.34em;text-transform:uppercase;color:{C['terra']}}}
.rule{{display:flex;align-items:center;gap:22px;justify-content:center}}
.rule i{{display:block;width:90px;height:1px;background:{C['gold']}}}
.h1{{font-family:'Bodoni Moda';font-weight:400;font-size:104px;line-height:1.02;letter-spacing:-.01em;color:{C['olive_d']}}}
.h1 em{{font-style:italic;color:{C['terra']}}}
.body{{font-weight:300;font-size:27px;line-height:1.55;color:{C['ink']}}}
.diam{{display:inline-block;width:9px;height:9px;background:{C['gold']};transform:rotate(45deg);margin:0 22px;vertical-align:middle}}
.pill{{font-family:'Lexend Zetta';font-weight:300;font-size:14px;letter-spacing:.3em;text-transform:uppercase;color:{C['olive']}}}
'''

# ============================================================ LAGOS INVITATION
lagos = f'''
<div class="poster">
  <div style="position:absolute;inset:61px;overflow:hidden"><div style="position:absolute;left:-61px;top:-61px;width:1200px;height:1800px">{ripples_svg(600, 1190, 16, 66, C['gold'], 1200, 1800, r0=150, op=.42, hi=C['terra'])}</div></div>
  <div class="grain"></div><div class="frame"></div><div class="frame2"></div>
  <div class="c" style="top:118px"><div class="rule"><i></i><span class="lab">You are cordially invited</span><i></i></div></div>
  <div class="c" style="top:196px;display:grid;justify-items:center;gap:34px">{logo('wordmark', C['olive'], width=700)}
    <div style="display:flex;align-items:center;gap:20px">{flag_chip('ng', 24)}<span class="lab" style="letter-spacing:.55em;font-size:19px;margin-right:-.55em">Lagos</span></div></div>
  <div class="c h1" style="top:520px">From Conversation<br>to <em>Action.</em></div>
  <div class="c body" style="top:790px;padding:0 220px">A private gathering of women building, investing and owning for a more prosperous Africa.</div>
  <div class="c pill" style="top:962px">Connection<span class="diam"></span>Opportunity<span class="diam"></span>Collaboration</div>

  <div style="position:absolute;left:120px;right:120px;top:1040px;height:300px;display:grid;grid-template-columns:1.05fr 1fr 1fr;border-top:1px solid {C['gold']};border-bottom:1px solid {C['gold']}">
    <div style="padding:34px 0 0;text-align:center;border-right:1px solid {C['gold']}">
      <div class="lab" style="font-size:12px;color:{C['olive']}">Saturday</div>
      <div style="display:flex;justify-content:center;align-items:baseline;gap:14px;margin-top:10px"><span class="cond" style="font-size:132px;line-height:1;color:{C['olive_d']}">21</span><span class="lab" style="font-size:16px;line-height:1.7;text-align:left;color:{C['olive_d']}">November<br>2026</span></div>
      <div class="lab" style="font-size:12px;margin-top:16px;color:{C['olive']};letter-spacing:.2em">11:00 AM – 5:00 PM (WAT)</div></div>
    <div style="padding:46px 20px 0;text-align:center;border-right:1px solid {C['gold']}">
      <div class="lab" style="font-size:12px;color:{C['olive']}">Venue</div>
      <div class="didone" style="font-size:50px;line-height:1.05;margin-top:18px;color:{C['olive_d']}">Civic Centre</div>
      <div class="lab" style="font-size:12px;margin-top:16px;color:{C['olive']};letter-spacing:.2em">Victoria Island<br>Lagos, Nigeria</div></div>
    <div style="padding:46px 24px 0;text-align:center">
      <div class="lab" style="font-size:12px;color:{C['olive']}">Entry</div>
      <div class="didone" style="font-size:40px;line-height:1.15;margin-top:18px;color:{C['olive_d']}">By invitation<br><em>and approved</em><br>registration</div></div>
  </div>

  <div style="position:absolute;left:46px;right:46px;bottom:46px;height:372px;background:{C['olive']}">
    {ripples_svg(600, 520, 9, 56, C['sand'], 1108, 372, r0=80, op=.2)}
    <div class="c" style="top:62px;color:{C['sand']}"><div class="lab" style="color:{C['sand']};opacity:.8">Hosted by</div>
      <div class="didone" style="font-size:78px;line-height:1;margin-top:16px;color:{C['sand']}">Udo Okonjo</div>
      <div style="font-size:21px;margin-top:14px;letter-spacing:.04em;opacity:.9">Founder, Radiant Collective Capital</div></div>
    <div class="c" style="bottom:60px;display:grid;justify-items:center;gap:20px">{logo('tagline', C['sand'], width=340)}
      <div class="lab" style="color:{C['sand']};font-size:11px;opacity:.75;letter-spacing:.4em">thewealthtableglobal.com</div></div>
  </div>
</div>'''
render('poster_lagos', page(lagos, 1200, 1800, css=CSS, bg=C['sand']), 1200, 1800, f'{OUT}/poster-lagos-invitation.png', scale=3)
render('poster_lagos_pdf', page(lagos, 1200, 1800, css=CSS, bg=C['sand']), 1200, 1800, f'{OUT}/poster-lagos-invitation.pdf', pdf=True)
# website copy (same artwork, web size)
render('poster_lagos_web', page(lagos, 1200, 1800, css=CSS, bg=C['sand']), 1200, 1800, f'{ROOT}/assets/img/poster-lagos.jpg', scale=1)


# ============================================================ RECAP POSTERS
def recap(city, country_flag, photo, pos, title_html, date, venue, women, pull, label):
    return f'''
<div class="poster">
  <div class="grain"></div><div class="frame"></div><div class="frame2"></div>
  <div style="position:absolute;left:84px;right:84px;top:84px;height:930px;overflow:hidden;background:{C['stone']}">
    <img src="{P}{photo}.jpg" style="width:100%;height:100%;object-fit:cover;object-position:{pos}">
    <div style="position:absolute;left:0;right:0;bottom:0;height:300px;background:linear-gradient(180deg,rgba(38,42,26,0),rgba(38,42,26,.55))"></div>
    <div style="position:absolute;left:34px;bottom:30px;display:flex;align-items:center;gap:16px;color:{C['sand']}">{flag_chip(country_flag, 30)}<span class="lab" style="color:{C['sand']};font-size:15px">{label}</span></div>
  </div>
  <div class="c" style="top:1054px;display:grid;justify-items:center;gap:24px">
    <div class="rule"><i></i><span class="lab">{venue}</span><i></i></div>
    <div class="h1" style="font-size:96px">{title_html}</div>
  </div>
  <div style="position:absolute;left:150px;right:150px;top:1318px;display:grid;grid-template-columns:1fr 1fr 1fr;border-top:1px solid {C['gold']};border-bottom:1px solid {C['gold']};padding:22px 0;text-align:center">
    <div style="border-right:1px solid {C['gold']}"><div class="lab" style="font-size:11px;color:{C['olive']}">Date</div><div class="didone" style="font-size:34px;margin-top:8px;color:{C['olive_d']}">{date}</div></div>
    <div style="border-right:1px solid {C['gold']}"><div class="lab" style="font-size:11px;color:{C['olive']}">Women</div><div class="cond" style="font-size:58px;line-height:1;margin-top:6px;color:{C['olive_d']}">{women}</div></div>
    <div><div class="lab" style="font-size:11px;color:{C['olive']}">Location</div><div style="margin-top:12px;display:flex;justify-content:center;align-items:center;gap:12px">{flag_chip(country_flag, 26)}<span class="didone" style="font-size:30px;color:{C['olive_d']}">{city}</span></div></div>
  </div>
  <div class="c didone" style="top:1470px;font-style:italic;font-size:34px;line-height:1.25;padding:0 210px;color:{C['terra']}">{pull}</div>
  <div style="position:absolute;left:46px;right:46px;bottom:46px;height:176px;background:{C['olive']};display:grid;grid-template-columns:auto 1fr;align-items:center;padding:0 56px;gap:50px">
    <div>{logo('wordmark', C['sand'], width=330)}</div>
    <div style="text-align:right;color:{C['sand']}"><div class="lab" style="color:{C['sand']};opacity:.75;font-size:11px">Next gathering</div><div class="didone" style="font-size:40px;line-height:1.1;margin-top:8px">Lagos · 21 November 2026</div></div>
  </div>
</div>'''


posters = [
    ('accra', recap('Accra, Ghana', 'gh', 'a-6762', '50% 50%', 'Where it <em>continued.</em>', '3 October 2026', 'Cantonments, Accra', '≈ 25', 'Different women. Shared ambition. Bigger possibilities.', 'The Wealth Table Accra')),
    ('nairobi', recap('Nairobi, Kenya', 'ke', 'n-10863', '50% 40%', 'Where it all <em>began.</em>', '13 June 2026', 'Kwetu Nairobi', '24', 'The word of the day was Courage.', 'The Wealth Table Nairobi')),
]
# fix the venue/date order (function signature uses date, venue)
for n, html in posters:
    render(f'poster_{n}', page(html, 1200, 1800, css=CSS, bg=C['sand']), 1200, 1800, f'{OUT}/poster-{n}-recap.png', scale=1.25)
    render(f'poster_{n}_pdf', page(html, 1200, 1800, css=CSS, bg=C['sand']), 1200, 1800, f'{OUT}/poster-{n}-recap.pdf', pdf=True)
flush()
print('posters done')

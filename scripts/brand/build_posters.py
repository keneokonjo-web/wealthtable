"""Posters: Lagos invitation (typographic), Lagos invitation (photo), Accra and Nairobi recaps.
Palette follows the ORIGINAL invitation (ivory, burgundy, bronze gold). No green, no Nigerian flag.
Run: PYTHONPATH=/tmp/pylibs python3 scripts/brand/build_posters.py"""
import sys, os, base64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
import patterns as PT

P = f'{FILE}{ROOT}/assets/img/photos/'
FL = f'{FILE}{ROOT}/assets/img/flags/'
OUT = f'{KIT}/posters'
os.makedirs(OUT, exist_ok=True)

IVORY = '#F4EADB'; BURG = '#5A0F1C'; DEEP = '#43090F'; BAND = '#4A0A15'; BRONZE = '#8B6B2E'; GOLD = '#B8923A'; INK = '#2A1A1C'

GRAIN = ("data:image/svg+xml;utf8," + "<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 .35  0 0 0 0 .27  0 0 0 0 .16  0 0 0 .5 0'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>")


def uri(svg): return 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()


LATTICE = uri(PT.chain(BAND, '#C9A24B', '#C9A24B'))
STRIP = lambda w, h=44: PT.strip(w, h, '#C9A24B', '#E4CF9A')

CSS = f'''
.poster{{position:relative;width:1200px;height:1800px;background:{IVORY};overflow:hidden;color:{INK}}}
.grain{{position:absolute;inset:0;background:url("{GRAIN}");opacity:.22;mix-blend-mode:multiply;pointer-events:none}}
.vig{{position:absolute;inset:0;background:radial-gradient(120% 90% at 50% 40%,rgba(255,250,240,.0) 40%,rgba(120,80,30,.10) 100%);pointer-events:none}}
.c{{position:absolute;left:0;right:0;text-align:center}}
.ser{{font-family:'Bodoni Moda',serif;font-weight:500;text-transform:uppercase;letter-spacing:.34em;margin-right:-.34em}}
.it{{font-family:'Bodoni Moda',serif;font-style:italic;font-weight:400}}
.bz{{color:{BRONZE}}}.bg{{color:{BURG}}}
.press{{filter:drop-shadow(0 2px 0 rgba(255,255,255,.75)) drop-shadow(0 -1px 0 rgba(60,0,10,.28)) drop-shadow(0 6px 10px rgba(90,15,28,.12))}}
.vr{{width:1.5px;background:linear-gradient(180deg,transparent,{GOLD} 18%,{GOLD} 82%,transparent)}}
.band{{position:absolute;left:0;right:0;background:{BAND};overflow:hidden}}
.band::before{{content:"";position:absolute;inset:0;background:url({LATTICE}) 0 0/96px 96px;opacity:.07}}
.band::after{{content:"";position:absolute;inset:0;background:radial-gradient(90% 120% at 50% 0%,rgba(150,40,55,.35),rgba(0,0,0,0) 70%),linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.25));pointer-events:none}}
.band>*{{z-index:2}}
.goldrule{{position:absolute;left:0;right:0;height:7px;background:linear-gradient(90deg,#9c7a2e,#e0c27a 50%,#9c7a2e)}}
'''


def wm(color, width):
    return logo('wordmark', color, width=width)


# ====================================================================== A. LAGOS INVITATION (typographic)
A = f'''
<div class="poster"><div class="grain"></div><div class="vig"></div>
  <div class="c ser bg" style="top:104px;font-size:21px">You are cordially invited</div>
  <div class="c press" style="top:186px;display:grid;justify-items:center">{wm(BURG, 930)}</div>
  <div class="c" style="top:392px;display:flex;justify-content:center;align-items:center;gap:28px"><span style="width:90px;height:1.5px;background:{GOLD}"></span><span class="ser bg" style="font-size:40px;letter-spacing:.62em;margin-right:-.62em">Lagos</span><span style="width:90px;height:1.5px;background:{GOLD}"></span></div>
  <div class="c ser bz" style="top:520px;font-size:25px;letter-spacing:.3em">From conversation to action.</div>
  <div class="c it bg" style="top:606px;font-size:42px;line-height:1.38;padding:0 110px">A private gathering of women building,<br>investing and owning for a more prosperous Africa.</div>

  <div style="position:absolute;left:90px;right:90px;top:820px;height:210px;display:grid;grid-template-columns:1.4fr 1px 1.15fr 1px .95fr;align-items:center">
    <div style="text-align:center"><div class="ser bz" style="font-size:16px">Saturday</div><div class="ser bg" style="font-size:33px;letter-spacing:.06em;margin:14px 0 12px;white-space:nowrap;margin-right:0">21 November 2026</div><div class="ser" style="font-size:16px;letter-spacing:.24em;color:{INK}">11:00 AM – 5:00 PM (WAT)</div></div>
    <div class="vr" style="height:150px"></div>
    <div style="text-align:center"><div class="ser bg" style="font-size:30px;letter-spacing:.1em;margin-right:0">Civic Centre</div><div class="ser" style="font-size:16px;letter-spacing:.28em;margin-top:14px;color:{INK}">Victoria Island<br>Lagos</div></div>
    <div class="vr" style="height:150px"></div>
    <div class="ser" style="text-align:center;font-size:19px;letter-spacing:.2em;line-height:1.7;color:{INK}">By invitation<br>and approved<br>registration</div>
  </div>

  <div style="position:absolute;left:90px;right:90px;top:1090px;display:grid;grid-template-columns:1fr 1px 1fr 1px 1fr;align-items:center;text-align:center">
    <div class="ser bz" style="font-size:20px">Connection</div><div class="vr" style="height:34px"></div><div class="ser bz" style="font-size:20px">Opportunity</div><div class="vr" style="height:34px"></div><div class="ser bz" style="font-size:20px">Collaboration</div></div>

  <div class="c" style="top:1212px"><div class="ser bz" style="font-size:16px;letter-spacing:.4em">Hosted by</div>
    <div class="ser bg" style="font-size:54px;letter-spacing:.04em;text-transform:none;margin:16px 0 8px;margin-right:0">Udo Okonjo</div>
    <div class="it" style="font-size:26px;color:{INK}">Founder, Radiant Collective Capital</div></div>

  <div class="goldrule" style="top:1426px"></div>
  <div class="band" style="top:1433px;height:367px">
    <div style="position:absolute;left:70px;right:70px;top:34px">{STRIP(1060, 44)}</div>
    <div class="c it" style="top:136px;font-size:56px;color:#EBDDBE">Leave richer than you arrived.<sup style="font-size:.4em;vertical-align:1.25em;font-style:normal">™</sup></div>
    <div class="c ser" style="top:262px;font-size:14px;letter-spacing:.5em;color:#C9A24B">thewealthtableglobal.com</div>
  </div>
</div>'''

# ====================================================================== B. LAGOS INVITATION (photo, from a previous gathering, unlabelled)
B = f'''
<div class="poster"><div class="grain"></div><div class="vig"></div>
  <div style="position:absolute;left:72px;right:72px;top:72px;height:860px;overflow:hidden;background:#ddd">
    <img src="{P}a-6823.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 24%">
    <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(40,10,15,.28) 0%,rgba(40,10,15,0) 26%,rgba(40,10,15,0) 70%,rgba(40,10,15,.35) 100%)"></div>
    <div style="position:absolute;inset:14px;border:1.5px solid rgba(244,234,219,.7)"></div>
    <div class="c ser" style="top:46px;font-size:19px;color:#F4EADB">You are cordially invited</div>
  </div>
  <div class="c ser bz" style="top:972px;font-size:20px;letter-spacing:.34em">The Wealth Table Lagos</div>
  <div class="c" style="top:1020px;font-family:'Bodoni Moda',serif;font-weight:400;font-size:104px;line-height:1.02;letter-spacing:-.012em;color:{BURG}">From Conversation<br>to <em>Action.</em></div>
  <div class="c it bz" style="top:1262px;font-size:31px;line-height:1.4;padding:0 150px;color:{INK}">A private gathering of women building, investing and owning for a more prosperous Africa.</div>

  <div style="position:absolute;left:90px;right:90px;top:1380px;height:130px;display:grid;grid-template-columns:1.6fr 1px 1.15fr 1px 1fr;align-items:center">
    <div style="text-align:center"><div class="ser bg" style="font-size:24px;letter-spacing:.04em;white-space:nowrap;margin-right:0">Saturday 21 November 2026</div><div class="ser" style="font-size:14px;letter-spacing:.24em;margin-top:10px;color:{INK}">11:00 AM – 5:00 PM (WAT)</div></div>
    <div class="vr" style="height:96px"></div>
    <div style="text-align:center"><div class="ser bg" style="font-size:25px;letter-spacing:.08em;margin-right:0">Civic Centre</div><div class="ser" style="font-size:13px;letter-spacing:.2em;margin-top:10px;color:{INK}">Victoria Island, Lagos</div></div>
    <div class="vr" style="height:96px"></div>
    <div class="ser" style="text-align:center;font-size:15px;letter-spacing:.18em;line-height:1.7;color:{INK}">By invitation and<br>approved registration</div>
  </div>

  <div class="goldrule" style="top:1560px"></div>
  <div class="band" style="top:1567px;height:233px">
    <div style="position:absolute;left:70px;right:70px;top:26px">{STRIP(1060, 30)}</div>
    <div style="position:absolute;left:80px;right:80px;top:92px;display:flex;justify-content:space-between;align-items:center">
      <div class="press" style="opacity:.98">{wm('#EBDDBE', 430)}</div>
      <div style="text-align:right;color:#EBDDBE"><div class="ser" style="font-size:13px;letter-spacing:.4em;color:#C9A24B;margin-right:-.4em">Hosted by Udo Okonjo</div><div style="font-family:'Bodoni Moda',serif;font-size:44px;line-height:1.1;margin-top:10px">Lagos · 21 November 2026</div></div>
    </div>
  </div>
</div>'''


# ====================================================================== C. RECAP POSTERS (Accra, Nairobi): flags allowed here
def flag_chip(code, h=26):
    return f'<img src="{FL}{code}.svg" style="height:{h}px;width:{h * 1.5:.0f}px;box-shadow:0 0 0 1px rgba(255,255,255,.6);vertical-align:middle">'


def recap(city, code, photo, pos, title_html, date, venue, women, pull, label):
    return f'''
<div class="poster"><div class="grain"></div><div class="vig"></div>
  <div style="position:absolute;left:72px;right:72px;top:72px;height:930px;overflow:hidden;background:#ddd">
    <img src="{P}{photo}.jpg" style="width:100%;height:100%;object-fit:cover;object-position:{pos}">
    <div style="position:absolute;left:0;right:0;bottom:0;height:300px;background:linear-gradient(180deg,rgba(40,10,15,0),rgba(40,10,15,.6))"></div>
    <div style="position:absolute;inset:14px;border:1.5px solid rgba(244,234,219,.55)"></div>
    <div style="position:absolute;left:44px;bottom:42px;display:flex;align-items:center;gap:16px;color:#F4EADB">{flag_chip(code, 30)}<span class="ser" style="font-size:16px;letter-spacing:.3em">{label}</span></div>
  </div>
  <div class="c" style="top:1046px"><div class="ser bz" style="font-size:19px">{venue}</div>
    <div style="font-family:'Bodoni Moda',serif;font-size:100px;line-height:1.05;letter-spacing:-.012em;color:{BURG};margin-top:18px">{title_html}</div></div>
  <div style="position:absolute;left:140px;right:140px;top:1286px;display:grid;grid-template-columns:1fr 1px 1fr 1px 1fr;align-items:center;text-align:center">
    <div><div class="ser bz" style="font-size:13px">Date</div><div class="ser bg" style="font-size:25px;letter-spacing:.08em;margin-top:10px">{date}</div></div><div class="vr" style="height:76px"></div>
    <div><div class="ser bz" style="font-size:13px">Women</div><div class="ser bg" style="font-size:38px;letter-spacing:.06em;margin-top:6px">{women}</div></div><div class="vr" style="height:76px"></div>
    <div><div class="ser bz" style="font-size:13px">Location</div><div style="display:flex;justify-content:center;align-items:center;gap:12px;margin-top:10px">{flag_chip(code, 24)}<span class="ser bg" style="font-size:22px;letter-spacing:.1em">{city}</span></div></div>
  </div>
  <div class="c it" style="top:1430px;font-size:35px;line-height:1.3;padding:0 200px;color:{BURG}">{pull}</div>
  <div class="goldrule" style="top:1566px"></div>
  <div class="band" style="top:1573px;height:227px">
    <div style="position:absolute;left:70px;right:70px;top:24px">{STRIP(1060, 30)}</div>
    <div style="position:absolute;left:80px;right:80px;top:90px;display:flex;justify-content:space-between;align-items:center">
      <div class="press">{wm('#EBDDBE', 400)}</div>
      <div style="text-align:right;color:#EBDDBE"><div class="ser" style="font-size:13px;letter-spacing:.4em;color:#C9A24B;margin-right:-.4em">Next gathering</div><div style="font-family:'Bodoni Moda',serif;font-size:42px;line-height:1.1;margin-top:10px">Lagos · 21 November 2026</div></div></div>
  </div>
</div>'''


JOBS_SPEC = [
    ('poster-lagos-invitation', A, 3), ('poster-lagos-photo', B, 2),
    ('poster-accra-recap', recap('Accra, Ghana', 'gh', 'a-6762', '50% 50%', 'Where it <em>continued.</em>', '3 October 2026', 'Cantonments, Accra', '≈ 25', 'Different women. Shared ambition. Bigger possibilities.', 'The Wealth Table Accra'), 1.25),
    ('poster-nairobi-recap', recap('Nairobi, Kenya', 'ke', 'n-10863', '50% 40%', 'Where it all <em>began.</em>', '13 June 2026', 'Kwetu Nairobi', '24', 'The word of the day was Courage.', 'The Wealth Table Nairobi'), 1.25),
]
for name, html, sc in JOBS_SPEC:
    render(name, page(html, 1200, 1800, css=CSS, bg=IVORY), 1200, 1800, f'{OUT}/{name}.png', scale=sc)
    render(name + '_pdf', page(html, 1200, 1800, css=CSS, bg=IVORY), 1200, 1800, f'{OUT}/{name}.pdf', pdf=True)
flush()

# website copy of the typographic Lagos invitation
from PIL import Image
Image.open(f'{OUT}/poster-lagos-invitation.png').convert('RGB').resize((1200, 1800), Image.LANCZOS).save(f'{ROOT}/assets/img/poster-lagos-v2.jpg', quality=92, optimize=True, progressive=True)
# remove the superseded file names
for old in ('poster-accra-recap.png', ):
    pass
print('posters done')

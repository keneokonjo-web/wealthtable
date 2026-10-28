"""Social graphics: Instagram, LinkedIn, stories, carousel, highlight covers.
Run: PYTHONPATH=/tmp/pylibs python3 scripts/brand/build_social.py"""
import sys, os, math, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

P = f'{FILE}{ROOT}/assets/img/photos/'
FL = f'{FILE}{ROOT}/assets/img/flags/'
OUT = f'{KIT}/social'
for d in ('instagram', 'instagram-stories', 'instagram-highlights', 'linkedin', 'linkedin-carousel'):
    os.makedirs(f'{OUT}/{d}', exist_ok=True)

SC = dict(sand=C['sand'], olive=C['olive'], terra=C['terra'], blush=C['blush'], stone=C['stone'], deep=C['olive_d'])
URL = 'thewealthtableglobal.com'


def flag(code, h=30):
    return f'<img src="{FL}{code}.svg" style="height:{h}px;width:{h * 1.5:.0f}px;border-radius:3px;box-shadow:0 0 0 1px rgba(255,255,255,.55);vertical-align:middle">'


def rings(w, h, cx, cy, n, step, color, r0=100, op=.4, hi=None):
    r = ''.join(f'<circle cx="{cx}" cy="{cy}" r="{r0 + i * step}" fill="none" stroke="{hi if hi and i % 4 == 0 else color}" stroke-width="{1.6 if hi and i % 4 == 0 else .9}" opacity="{max(.1, op - i * .028):.2f}"/>' for i in range(n))
    return f'<svg style="position:absolute;inset:0" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{r}</svg>'


def icon(name, color, size=64):
    from build_logos_icons import ICONS
    return f'<svg viewBox="0 0 48 48" width="{size}" height="{size}" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" color="{color}">{ICONS[name]}</svg>'


SCSS = f'''
.card{{position:relative;overflow:hidden}}
.abs{{position:absolute}}
.lab{{font-family:'Lexend Zetta';font-weight:300;text-transform:uppercase;letter-spacing:.32em}}
.dd{{font-family:'Bodoni Moda';font-weight:400;letter-spacing:-.012em;line-height:1.04}}
.dd em{{font-style:italic}}
.ant{{font-family:'Antonio';font-weight:300;text-transform:uppercase;line-height:1}}
.hair{{height:1px;background:{C['gold']}}}
.dia{{display:inline-block;width:8px;height:8px;background:{C['gold']};transform:rotate(45deg);margin:0 18px;vertical-align:middle}}
.btn{{display:inline-flex;align-items:center;gap:18px;padding:22px 34px;font-family:'Lexend Zetta';font-weight:300;font-size:19px;letter-spacing:.2em;text-transform:uppercase}}
.btn.line{{border:1.5px solid currentColor}}
'''
# icons module (shares the same 48-grid definitions as the brand kit builder)
ICON_SRC = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build_logos.py')).read()
m = re.search(r'ICONS = \{.*?\n\}\n', ICON_SRC, re.S)
mod = "import math\n" + re.search(r'def dots_ring.*?\n\n\n', ICON_SRC, re.S).group(0) + m.group(0)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build_logos_icons.py'), 'w').write(mod)


def make(name, html, w, h, folder, scale=1):
    render(f'social_{name}', page(html, w, h, css=SCSS, bg='#fff'), w, h, f'{OUT}/{folder}/{name}.png', scale=scale)


def footer_row(w, color, left=True, y=None, pad=80):
    pos = f'bottom:{pad - 20}px' if y is None else f'top:{y}px'
    return (f'<div class="abs" style="left:{pad}px;right:{pad}px;{pos};display:flex;justify-content:space-between;align-items:center;color:{color}">'
            f'{logo("wordmark", color, width=250)}<span class="lab" style="font-size:17px;letter-spacing:.3em;opacity:.8">{URL}</span></div>')


def frame(w, h, color, inset=40):
    return f'<div class="abs" style="inset:{inset}px;border:1.4px solid {color};opacity:.9"></div>'


# =============================================================== IG POSTS 1080 x 1350
W, H = 1080, 1350


def typo_card(bg, fg, accent, kicker, headline, body='', art=None, extra=''):
    a = art or ''
    return f'''<div class="card" style="width:{W}px;height:{H}px;background:{bg};color:{fg}">{a}
  <div class="abs" style="left:80px;top:84px">{logo('wt-monogram', fg, width=96)}</div>
  <div class="abs lab" style="right:80px;top:96px;font-size:18px;color:{accent}">{kicker}</div>
  <div class="abs" style="left:80px;right:80px;top:300px"><div class="dd" style="font-size:112px">{headline}</div>
    <div style="margin-top:46px;font-size:33px;line-height:1.5;max-width:800px;opacity:.92">{body}</div>{extra}</div>
  {footer_row(W, fg)}</div>'''


ring_olive = lambda: rings(W, H, 940, 1160, 18, 78, C['sand'], op=.32, hi=C['gold'])
ring_sand = lambda: rings(W, H, 960, 1200, 18, 78, C['olive'], op=.22, hi=C['gold'])
ring_terra = lambda: rings(W, H, 140, 120, 18, 78, C['sand'], op=.28)

make('01-what-we-do', typo_card(SC['sand'], C['olive_d'], C['terra'], 'What we do',
     'A table where women <em style="color:%s">own</em> the conversation.' % C['terra'],
     'The Wealth Table is a purposefully designed gathering where women connect around real opportunities, shared ambitions and the future of wealth and ownership.', ring_sand()), W, H, 'instagram')

pill = ''.join(f'<div style="display:flex;align-items:center;gap:26px;padding:30px 0;border-top:1px solid rgba(248,242,229,.35)"><span class="ant" style="font-size:44px;opacity:.7;width:70px">0{i + 1}</span><span class="dd" style="font-size:78px">{t}</span></div>' for i, t in enumerate(['Connection', 'Opportunity', 'Collaboration']))
make('02-three-pillars', f'''<div class="card" style="width:{W}px;height:{H}px;background:{SC['olive']};color:{C['sand']}">{ring_olive()}
  <div class="abs" style="left:80px;top:84px">{logo('wt-monogram', C['sand'], width=96)}</div>
  <div class="abs lab" style="right:80px;top:96px;font-size:18px;color:{C['gold']}">What every gathering is built on</div>
  <div class="abs" style="left:80px;right:80px;top:330px">{pill}<div style="border-top:1px solid rgba(248,242,229,.35)"></div></div>
  <div class="abs" style="left:80px;right:80px;top:880px;font-size:33px;line-height:1.5;opacity:.9;max-width:780px">Real opportunities, shared ambitions, and the conversations that inspire women to make bigger moves.</div>
  {footer_row(W, C['sand'])}</div>''', W, H, 'instagram')

make('03-next-event-lagos', f'''<div class="card" style="width:{W}px;height:{H}px;background:{SC['terra']};color:{C['sand']}">{ring_terra()}
  {frame(W, H, 'rgba(248,242,229,.5)', 36)}
  <div class="abs" style="left:0;right:0;top:110px;text-align:center"><div class="lab" style="font-size:19px;color:{C['sand']}">Next gathering</div>
    <div style="margin-top:36px">{logo('wordmark', C['sand'], width=640)}</div>
    <div style="margin-top:26px;display:flex;justify-content:center;align-items:center;gap:20px">{flag('ng', 30)}<span class="lab" style="font-size:22px;letter-spacing:.55em;margin-right:-.55em">Lagos</span></div></div>
  <div class="abs" style="left:0;right:0;top:430px;text-align:center"><div class="ant" style="font-size:330px;letter-spacing:.01em">21</div><div class="lab" style="font-size:24px;margin-top:6px;letter-spacing:.5em;margin-right:-.5em">November 2026</div></div>
  <div class="abs" style="left:110px;right:110px;top:900px"><div class="hair"></div><div style="display:grid;grid-template-columns:1fr 1fr 1fr;padding:34px 0;text-align:center;gap:20px">
    <div><div class="lab" style="font-size:16px;opacity:.7">Saturday</div><div class="dd" style="font-size:34px;margin-top:12px">11:00 AM<br>– 5:00 PM</div></div>
    <div><div class="lab" style="font-size:16px;opacity:.7">Venue</div><div class="dd" style="font-size:34px;margin-top:12px">Civic Centre<br>Victoria Island</div></div>
    <div><div class="lab" style="font-size:16px;opacity:.7">Entry</div><div class="dd" style="font-size:34px;margin-top:12px">By invitation<br><em>only</em></div></div></div><div class="hair"></div></div>
  <div class="abs" style="left:0;right:0;top:1130px;text-align:center"><div class="dd" style="font-size:44px;font-style:italic;padding:0 160px">How do we move more women from success to ownership?</div></div>
  <div class="abs lab" style="left:0;right:0;bottom:78px;text-align:center;font-size:18px;opacity:.85">Register your interest · {URL}</div></div>''', W, H, 'instagram')

make('04-save-the-date', f'''<div class="card" style="width:{W}px;height:{H}px;background:{SC['sand']};color:{C['olive_d']}">{rings(W, H, 540, 640, 22, 64, C['olive'], r0=120, op=.3, hi=C['terra'])}
  {frame(W, H, C['gold'], 36)}
  <div class="abs" style="left:0;right:0;top:120px;text-align:center"><div class="lab" style="font-size:15px;color:{C['terra']}">Save the date</div></div>
  <div class="abs" style="left:0;right:0;top:350px;text-align:center"><div class="ant" style="font-size:460px;color:{C['olive_d']}">21</div>
    <div class="dd" style="font-size:72px;margin-top:0">November <em style="color:{C['terra']}">2026</em></div></div>
  <div class="abs" style="left:0;right:0;top:1000px;text-align:center"><div class="lab" style="font-size:17px">Lagos<span class="dia"></span>Civic Centre, Victoria Island</div>
    <div style="margin-top:34px">{logo('wordmark', C['olive'], width=520)}</div></div>
  <div class="abs lab" style="left:0;right:0;bottom:78px;text-align:center;font-size:17px;opacity:.7">{URL}</div></div>''', W, H, 'instagram')


def photo_card(name, photo, pos, kicker_html, headline, meta_html, bottom_html=''):
    return f'''<div class="card" style="width:{W}px;height:{H}px;background:#222;color:{C['sand']}">
  <img src="{P}{photo}.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos}">
  <div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(38,42,26,.5) 0%,rgba(38,42,26,0) 28%,rgba(38,42,26,.2) 52%,rgba(38,42,26,.88) 100%)"></div>
  <div class="abs" style="left:70px;top:70px">{logo('wt-monogram', C['sand'], width=92)}</div>
  <div class="abs" style="right:70px;top:84px;display:flex;align-items:center;gap:18px">{kicker_html}</div>
  <div class="abs" style="left:70px;right:70px;bottom:96px"><div class="dd" style="font-size:104px">{headline}</div>
    <div style="margin-top:34px;display:flex;gap:44px;align-items:center;flex-wrap:wrap;border-top:1px solid rgba(248,242,229,.5);padding-top:28px;font-size:26px">{meta_html}</div>{bottom_html}</div></div>'''


make('05-past-event-nairobi', photo_card('n', 'n-10816', '50% 40%',
     f'{flag("ke", 32)}<span class="lab" style="font-size:18px">Nairobi, Kenya</span>', 'Where it all <em>began.</em>',
     '<span class="lab" style="font-size:18px">13 June 2026</span><span class="lab" style="font-size:18px">24 women</span><span class="lab" style="font-size:18px">Kwetu Nairobi</span>'), W, H, 'instagram')
make('06-past-event-accra', photo_card('a', 'a-6823', '50% 28%',
     f'{flag("gh", 32)}<span class="lab" style="font-size:18px">Accra, Ghana</span>', 'Where it <em>continued.</em>',
     '<span class="lab" style="font-size:18px">3 October 2026</span><span class="lab" style="font-size:18px">≈ 25 women</span><span class="lab" style="font-size:18px">Cantonments</span>'), W, H, 'instagram')


def gallery_card(city, code, place, photos, bg, fg):
    imgs = [(photos[0], 'left:50px;top:210px;width:640px;height:720px', '50% 40%'), (photos[1], 'left:722px;top:210px;width:308px;height:344px', '50% 40%'), (photos[2], 'left:722px;top:586px;width:308px;height:344px', '50% 40%')]
    im = ''.join(f'<img class="abs" src="{P}{p}.jpg" style="{st};object-fit:cover;object-position:{pos}">' for p, st, pos in imgs)
    return f'''<div class="card" style="width:{W}px;height:{H}px;background:{bg};color:{fg}">
  <div class="abs" style="left:50px;top:60px;right:50px;display:flex;justify-content:space-between;align-items:center"><div style="display:flex;align-items:center;gap:18px">{flag(code, 32)}<span class="lab" style="font-size:18px">{place}</span></div>{logo('wt-monogram', fg, width=84)}</div>
  {im}
  <div class="abs" style="left:50px;right:50px;top:990px"><div class="dd" style="font-size:96px">{city} <em>gallery</em></div>
    <div style="margin-top:30px;display:flex;justify-content:space-between;align-items:center"><span class="btn line" style="color:{fg}">View the gallery <span>→</span></span><span class="lab" style="font-size:17px;opacity:.8">{URL}</span></div></div></div>'''


make('07-gallery-nairobi', gallery_card('Nairobi', 'ke', 'Nairobi, Kenya', ['n-10863', 'n-10840', 'n-10880'], C['sand'], C['olive_d']), W, H, 'instagram')
make('08-gallery-accra', gallery_card('Accra', 'gh', 'Accra, Ghana', ['a-6762', 'a-6797', 'a-6565'], C['olive'], C['sand']), W, H, 'instagram')

make('09-meet-the-founder', f'''<div class="card" style="width:{W}px;height:{H}px;background:{SC['stone']};color:{C['olive_d']}">
  <img class="abs" src="{P}n-10849.jpg" style="left:0;top:0;width:{W}px;height:760px;object-fit:cover;object-position:34% 38%;filter:grayscale(1) contrast(1.05)">
  <div class="abs" style="left:0;top:0;width:{W}px;height:760px;background:linear-gradient(180deg,rgba(38,42,26,.35),rgba(38,42,26,0) 35%)"></div>
  <div class="abs" style="left:70px;top:70px">{logo('wt-monogram', C['sand'], width=92)}</div>
  <div class="abs lab" style="right:70px;top:84px;font-size:18px;color:{C['sand']}">Meet the founder</div>
  <div class="abs" style="left:70px;right:70px;top:810px"><div class="dd" style="font-size:112px">Udo <em style="color:{C['terra']}">Okonjo</em></div>
    <div class="lab" style="font-size:19px;margin-top:26px;color:{C['terra']}">Founder, Radiant Collective Capital</div>
    <div style="margin-top:28px;font-size:29px;line-height:1.5;max-width:900px;opacity:.9">Entrepreneur, investor and board director. She created The Wealth Table from a simple conviction: when accomplished women gather for honest conversations about money, power and ownership, extraordinary possibilities emerge.</div></div></div>''', W, H, 'instagram')

make('10-leave-richer', f'''<div class="card" style="width:{W}px;height:{H}px;background:{SC['sand']};color:{C['olive_d']}">{rings(W, H, 540, 675, 20, 70, C['olive'], r0=140, op=.26, hi=C['terra'])}
  {frame(W, H, C['gold'], 36)}
  <div class="abs" style="left:0;right:0;top:140px;text-align:center">{logo('wt-monogram', C['olive'], width=150)}</div>
  <div class="abs" style="left:0;right:0;top:470px;text-align:center"><div class="dd" style="font-size:132px">Leave richer<br>than you <em style="color:{C['terra']}">arrived.</em></div></div>
  <div class="abs" style="left:0;right:0;top:1080px;text-align:center"><div class="lab" style="font-size:15px;color:{C['terra']}">Come to the table</div></div>
  <div class="abs lab" style="left:0;right:0;bottom:78px;text-align:center;font-size:17px;opacity:.7">{URL}</div></div>''', W, H, 'instagram')

who = ''.join(f'<div style="display:flex;gap:26px;padding:26px 0;border-top:1px solid rgba(248,242,229,.3);font-size:34px;line-height:1.3;align-items:baseline"><span class="ant" style="font-size:30px;opacity:.6;width:48px">0{i + 1}</span><span>{t}</span></div>' for i, t in enumerate(['An entrepreneur exploring expansion', 'A professional building wealth', 'An investor seeking new perspectives', 'A leader turning influence into ownership']))
make('11-who-its-for', f'''<div class="card" style="width:{W}px;height:{H}px;background:{SC['terra']};color:{C['sand']}">{ring_terra()}
  <div class="abs" style="left:80px;top:84px">{logo('wt-monogram', C['sand'], width=96)}</div>
  <div class="abs lab" style="right:80px;top:96px;font-size:18px">Who it is for</div>
  <div class="abs" style="left:80px;right:80px;top:290px"><div class="dd" style="font-size:96px">For women who are building, investing, <em>leading.</em></div></div>
  <div class="abs" style="left:80px;right:80px;top:740px">{who}<div style="border-top:1px solid rgba(248,242,229,.3)"></div></div>
  {footer_row(W, C['sand'])}</div>''', W, H, 'instagram')

steps = [('Register your interest', 'Join the waitlist for your table.'), ('Receive your invitation', 'Released in waves, to the list first.'), ('Choose your rate', '$200 RCC members · $300 non-members.'), ('Pay securely', 'In US dollars, or Nigerian naira.'), ('Come to the table', 'Confirmed on payment.')]
make('12-how-it-works', f'''<div class="card" style="width:{W}px;height:{H}px;background:{SC['sand']};color:{C['olive_d']}">{ring_sand()}
  <div class="abs" style="left:80px;top:84px">{logo('wt-monogram', C['olive'], width=96)}</div>
  <div class="abs lab" style="right:80px;top:96px;font-size:18px;color:{C['terra']}">How it works</div>
  <div class="abs" style="left:80px;right:80px;top:250px"><div class="dd" style="font-size:96px">Five steps to <em style="color:{C['terra']}">your seat.</em></div></div>
  <div class="abs" style="left:80px;right:80px;top:560px">{''.join(f'<div style="display:flex;gap:30px;align-items:baseline;padding:22px 0;border-top:1px solid {C["gold"]}"><span class="ant" style="font-size:52px;width:70px;color:{C["terra"]}">0{i + 1}</span><span style="flex:1"><span class="dd" style="font-size:44px;display:block">{a}</span><span style="font-size:24px;opacity:.8">{b}</span></span></div>' for i, (a, b) in enumerate(steps))}<div class="hair"></div></div>
  {footer_row(W, C['olive_d'])}</div>''', W, H, 'instagram')

make('13-participation', f'''<div class="card" style="width:{W}px;height:{H}px;background:{SC['olive']};color:{C['sand']}">{ring_olive()}
  <div class="abs" style="left:80px;top:84px">{logo('wt-monogram', C['sand'], width=96)}</div>
  <div class="abs lab" style="right:80px;top:96px;font-size:18px;color:{C['gold']}">Lagos · Participation</div>
  <div class="abs" style="left:80px;right:80px;top:290px"><div class="dd" style="font-size:96px">One gathering. <em>Two rates.</em></div>
    <div style="margin-top:36px;font-size:31px;line-height:1.5;max-width:800px;opacity:.9">Both rates provide access to the same premium gathering and experience. RCC members enjoy preferential participation rates.</div></div>
  <div class="abs" style="left:80px;right:80px;top:790px;display:grid;grid-template-columns:1fr 1fr;gap:28px">
    <div style="border:1.5px solid rgba(248,242,229,.6);padding:44px 40px"><div class="lab" style="font-size:18px;opacity:.8">RCC members</div><div class="ant" style="font-size:190px;margin-top:20px">$200</div></div>
    <div style="border:1.5px solid rgba(248,242,229,.6);padding:44px 40px"><div class="lab" style="font-size:18px;opacity:.8">Non-members</div><div class="ant" style="font-size:190px;margin-top:20px">$300</div></div></div>
  {footer_row(W, C['sand'])}</div>''', W, H, 'instagram')

make('14-success-to-ownership', typo_card(SC['stone'], C['olive_d'], C['terra'], 'The question',
     'How do we move more women from success to <em style="color:%s">ownership?</em>' % C['terra'], 'From conversation to action. An invitation-only gathering of women leaders, entrepreneurs, investors and wealth builders.', rings(W, H, 960, 1200, 18, 78, C['olive'], op=.2, hi=C['gold'])), W, H, 'instagram')

# =============================================================== STORIES 1080 x 1920
SW, SH = 1080, 1920
make('s1-next-event', f'''<div class="card" style="width:{SW}px;height:{SH}px;background:{SC['terra']};color:{C['sand']}">{rings(SW, SH, 540, 1000, 24, 74, C['sand'], r0=120, op=.3)}
  {frame(SW, SH, 'rgba(248,242,229,.5)', 40)}
  <div class="abs" style="left:0;right:0;top:230px;text-align:center"><div class="lab" style="font-size:15px">Next gathering</div><div style="margin-top:44px">{logo('wordmark', C['sand'], width=700)}</div>
    <div style="margin-top:30px;display:flex;justify-content:center;align-items:center;gap:20px">{flag('ng', 32)}<span class="lab" style="font-size:24px;letter-spacing:.55em;margin-right:-.55em">Lagos</span></div></div>
  <div class="abs" style="left:0;right:0;top:700px;text-align:center"><div class="ant" style="font-size:520px">21</div><div class="lab" style="font-size:28px;letter-spacing:.5em;margin-right:-.5em;margin-top:4px">November 2026</div></div>
  <div class="abs" style="left:0;right:0;top:1360px;text-align:center"><div class="dd" style="font-size:46px">Civic Centre, Victoria Island</div><div class="lab" style="font-size:19px;margin-top:20px;opacity:.85">11:00 AM – 5:00 PM (WAT) · By invitation</div></div>
  <div class="abs" style="left:0;right:0;top:1580px;text-align:center"><span class="btn" style="background:{C['sand']};color:{C['terra']}">Register your interest →</span></div>
  <div class="abs lab" style="left:0;right:0;bottom:100px;text-align:center;font-size:18px;opacity:.8">{URL}</div></div>''', SW, SH, 'instagram-stories')

make('s2-register', f'''<div class="card" style="width:{SW}px;height:{SH}px;background:{SC['sand']};color:{C['olive_d']}">{rings(SW, SH, 540, 960, 26, 70, C['olive'], r0=130, op=.26, hi=C['terra'])}
  {frame(SW, SH, C['gold'], 40)}
  <div class="abs" style="left:0;right:0;top:260px;text-align:center">{logo('wt-monogram', C['olive'], width=190)}</div>
  <div class="abs" style="left:0;right:0;top:620px;text-align:center"><div class="dd" style="font-size:150px">Come to<br>the <em style="color:{C['terra']}">table.</em></div></div>
  <div class="abs" style="left:0;right:0;top:1240px;text-align:center;font-size:36px;line-height:1.5;padding:0 140px">Invitations are released in waves, to the list before anyone else.</div>
  <div class="abs" style="left:0;right:0;top:1480px;text-align:center"><span class="btn" style="background:{C['olive']};color:{C['sand']}">Register your interest →</span><div class="lab" style="font-size:18px;margin-top:34px;opacity:.7">Link in bio</div></div></div>''', SW, SH, 'instagram-stories')


def story_photo(photo, pos, code, place, head, meta):
    return f'''<div class="card" style="width:{SW}px;height:{SH}px;background:#222;color:{C['sand']}">
  <img src="{P}{photo}.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos}">
  <div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(38,42,26,.55) 0%,rgba(38,42,26,0) 24%,rgba(38,42,26,.15) 52%,rgba(38,42,26,.9) 100%)"></div>
  <div class="abs" style="left:70px;top:110px">{logo('wt-monogram', C['sand'], width=110)}</div>
  <div class="abs" style="right:70px;top:128px;display:flex;align-items:center;gap:18px">{flag(code, 36)}<span class="lab" style="font-size:19px">{place}</span></div>
  <div class="abs" style="left:70px;right:70px;bottom:250px"><div class="dd" style="font-size:136px">{head}</div><div style="margin-top:36px;border-top:1px solid rgba(248,242,229,.5);padding-top:30px;display:flex;gap:44px;flex-wrap:wrap">{meta}</div></div>
  <div class="abs" style="left:70px;right:70px;bottom:100px;display:flex;justify-content:space-between;align-items:center"><span class="btn line" style="color:{C['sand']}">View the gallery →</span><span class="lab" style="font-size:17px;opacity:.8">{URL}</span></div></div>'''


mt = lambda t: f'<span class="lab" style="font-size:19px">{t}</span>'
make('s3-past-nairobi', story_photo('n-10816', '50% 40%', 'ke', 'Nairobi, Kenya', 'Where it all <em>began.</em>', mt('13 June 2026') + mt('24 women') + mt('Kwetu Nairobi')), SW, SH, 'instagram-stories')
make('s4-past-accra', story_photo('a-6823', '50% 28%', 'gh', 'Accra, Ghana', 'Where it <em>continued.</em>', mt('3 October 2026') + mt('≈ 25 women') + mt('Cantonments')), SW, SH, 'instagram-stories')

# =============================================================== HIGHLIGHT COVERS 1080 x 1920 (icon centred in a circle-safe zone)
HL = [('lagos', 'location', 'Lagos'), ('accra', 'table', 'Accra'), ('nairobi', 'gallery', 'Nairobi'), ('about', 'conversation', 'About'), ('faq', 'invitation', 'FAQ'), ('host', 'ownership', 'Host')]
for n, ic, lab in HL:
    make(f'highlight-{n}', f'''<div class="card" style="width:1080px;height:1920px;background:{C['olive']};color:{C['sand']};display:grid;place-items:center">
      <div style="width:900px;height:900px;border-radius:50%;border:2px solid {C['gold']};display:grid;place-items:center;position:relative"><div style="width:830px;height:830px;border-radius:50%;border:1px solid rgba(248,242,229,.4);display:grid;place-items:center">{icon(ic, C['sand'], 330)}</div></div></div>''', 1080, 1920, 'instagram-highlights')

# =============================================================== LINKEDIN
LW, LH = 1200, 627


def li_split(name, bg, fg, accent, kicker, headline, body, photo=None, pos='50% 50%', cta=True, art=True):
    right = (f'<img class="abs" src="{P}{photo}.jpg" style="right:0;top:0;width:520px;height:{LH}px;object-fit:cover;object-position:{pos}">' if photo else
             (rings(LW, LH, 1020, 300, 14, 56, fg, r0=60, op=.3, hi=C['gold']) if art else ''))
    return f'''<div class="card" style="width:{LW}px;height:{LH}px;background:{bg};color:{fg}">{right}
  <div class="abs" style="left:64px;top:56px">{logo('wt-monogram', fg, width=78)}</div>
  <div class="abs lab" style="left:64px;top:190px;font-size:17px;color:{accent}">{kicker}</div>
  <div class="abs" style="left:64px;top:228px;width:{600 if photo else 780}px"><div class="dd" style="font-size:{62 if photo else 70}px">{headline}</div>
    <div style="margin-top:22px;font-size:22px;line-height:1.5;opacity:.9;max-width:560px">{body}</div></div>
  <div class="abs lab" style="left:64px;bottom:44px;font-size:16px;opacity:.8">{URL}</div></div>'''


make('li-01-next-event-lagos', li_split('', C['terra'], C['sand'], C['sand'], 'Next gathering · Lagos', 'Saturday 21 November <em>2026</em>', 'The Wealth Table Lagos. Civic Centre, Victoria Island. By invitation and approved registration. Register your interest.'), LW, LH, 'linkedin')
make('li-02-what-we-do', li_split('', C['sand'], C['olive_d'], C['terra'], 'What we do', 'Women connecting around <em style="color:%s">ownership.</em>' % C['terra'], 'A purposefully designed gathering for real opportunities, shared ambitions and the future of wealth.'), LW, LH, 'linkedin')
make('li-03-past-nairobi', li_split('', C['olive'], C['sand'], C['gold'], 'Nairobi · 13 June 2026', 'Where it all <em>began.</em>', '24 remarkable women. One word for the day: Courage.', photo='n-10816', pos='50% 40%', art=False), LW, LH, 'linkedin')
make('li-04-past-accra', li_split('', C['olive'], C['sand'], C['gold'], 'Accra · 3 October 2026', 'Where it <em>continued.</em>', 'Approximately 25 women. An intimate evening at a private residence in Cantonments.', photo='a-6823', pos='50% 28%', art=False), LW, LH, 'linkedin')
make('li-05-founder', li_split('', C['stone'], C['olive_d'], C['terra'], 'About the founder', 'Udo <em style="color:%s">Okonjo</em>' % C['terra'], 'Entrepreneur, investor, board director and founder of Radiant Collective Capital.', photo='n-10849', pos='36% 36%', art=False), LW, LH, 'linkedin')
make('li-06-fees-lagos', f'''<div class="card" style="width:{LW}px;height:{LH}px;background:{C['sand']};color:{C['olive_d']}">{rings(LW, LH, 1040, 320, 14, 56, C['olive'], r0=60, op=.26, hi=C['gold'])}
  <div class="abs" style="left:64px;top:56px">{logo('wt-monogram', C['olive'], width=78)}</div>
  <div class="abs lab" style="left:64px;top:190px;font-size:17px;color:{C['terra']}">Lagos · 21 November 2026</div>
  <div class="abs dd" style="left:64px;top:228px;font-size:62px;width:600px">One gathering. <em style="color:{C['terra']}">Two rates.</em></div>
  <div class="abs" style="left:700px;top:150px;display:grid;gap:20px">
    <div style="border:1.5px solid {C['gold']};padding:30px 44px;width:400px"><div class="lab" style="font-size:16px">RCC members</div><div class="ant" style="font-size:100px;margin-top:8px">$200</div></div>
    <div style="border:1.5px solid {C['gold']};padding:30px 44px;width:400px"><div class="lab" style="font-size:16px">Non-members</div><div class="ant" style="font-size:100px;margin-top:8px">$300</div></div></div>
  <div class="abs lab" style="left:64px;bottom:44px;font-size:16px;opacity:.8">{URL}</div></div>''', LW, LH, 'linkedin')

# banners
make('li-banner-personal-1584x396', f'''<div class="card" style="width:1584px;height:396px;background:{C['olive']};color:{C['sand']}">{rings(1584, 396, 1380, 200, 12, 52, C['sand'], r0=50, op=.3, hi=C['gold'])}
  <div class="abs" style="left:96px;top:0;bottom:0;display:flex;align-items:center;gap:46px">{logo('wt-monogram', C['sand'], width=210)}<div style="width:2px;height:150px;background:{C['gold']}"></div><div>{logo('wordmark', C['sand'], width=560)}<div style="margin-top:26px">{logo('tagline', C['sand'], width=360)}</div></div></div></div>''', 1584, 396, 'linkedin')
make('li-banner-company-1128x191', f'''<div class="card" style="width:1128px;height:191px;background:{C['sand']};color:{C['olive_d']}">{rings(1128, 191, 1000, 96, 10, 40, C['olive'], r0=30, op=.26, hi=C['gold'])}
  <div class="abs" style="left:60px;top:0;bottom:0;display:flex;align-items:center;gap:30px">{logo('wt-monogram', C['olive'], width=110)}<div style="width:2px;height:80px;background:{C['gold']}"></div><div>{logo('wordmark', C['olive'], width=380)}<div style="margin-top:14px">{logo('tagline', C['terra'], width=250)}</div></div></div></div>''', 1128, 191, 'linkedin')

# =============================================================== LINKEDIN / IG CAROUSEL (1080 x 1350, 5 slides)
slides = [
    typo_card(SC['olive'], C['sand'], C['gold'], 'Slide 1', 'What is <em>The Wealth Table?</em>', 'A gathering where women connect around real opportunities, shared ambitions and the future of wealth and ownership.', ring_olive(), ''),
    typo_card(SC['sand'], C['olive_d'], C['terra'], 'Slide 2 · What it is', 'Not another <em style="color:%s">networking event.</em>' % C['terra'], 'Rather than conventional presentations or sales pitches, the focus is on participation, contribution and making things happen.', ring_sand()),
    typo_card(SC['terra'], C['sand'], C['sand'], 'Slide 3 · Who it is for', 'Women who are <em>ready</em> for their next move.', 'Entrepreneurs exploring expansion, professionals building wealth, investors seeking new perspectives, leaders turning influence into ownership.', ring_terra()),
    typo_card(SC['stone'], C['olive_d'], C['terra'], 'Slide 4 · Where', 'Nairobi. Accra. <em style="color:%s">Lagos.</em>' % C['terra'], 'Nairobi, 13 June 2026 · Accra, 3 October 2026 · Lagos, Saturday 21 November 2026 at the Civic Centre, Victoria Island.', rings(W, H, 960, 1200, 18, 78, C['olive'], op=.2, hi=C['gold'])),
    typo_card(SC['olive'], C['sand'], C['gold'], 'Slide 5 · Join us', 'Come to the table. <em>Leave richer than you arrived.</em>', 'Register your interest. Invitations are released in waves, to the list before anyone else.', ring_olive(), f'<div style="margin-top:50px"><span class="btn" style="background:{C["sand"]};color:{C["olive_d"]}">Register your interest →</span></div>'),
]
for i, s in enumerate(slides):
    make(f'slide-{i + 1}', s, W, H, 'linkedin-carousel')

flush()
print('social done')

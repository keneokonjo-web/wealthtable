"""Website share image (og.jpg), apple touch icon and the web copy of the Lagos poster."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
from PIL import Image
P = f'{FILE}{ROOT}/assets/img/photos/'
og = f'''<div style="width:1200px;height:630px;background:{C['sand']};position:relative;overflow:hidden">
 <div style="position:absolute;right:-60px;top:-40px;width:700px;height:700px;opacity:.35"><svg viewBox="0 0 700 700" width="700" height="700">{''.join(f'<circle cx="350" cy="350" r="{60 + i * 34}" fill="none" stroke="{C["olive"] if i % 4 else C["gold"]}" stroke-width="1"/>' for i in range(10))}</svg></div>
 <img src="{P}a-6797.jpg" style="position:absolute;right:0;top:0;width:470px;height:630px;object-fit:cover;object-position:62% 50%">
 <div style="position:absolute;left:70px;top:90px">{logo('lockup-full', C['olive'], width=430)}</div>
 <div style="position:absolute;left:70px;bottom:62px;font-family:'Lexend Zetta';font-weight:300;font-size:15px;letter-spacing:.3em;text-transform:uppercase;color:{C['terra']}">Nairobi · Accra · Lagos</div></div>'''
render('og', page(og, 1200, 630, bg=C['sand']), 1200, 630, f'{ROOT}/assets/img/og.png')
flush()
Image.open(f'{ROOT}/assets/img/og.png').convert('RGB').save(f'{ROOT}/assets/img/og.jpg', quality=90, optimize=True, progressive=True); os.remove(f'{ROOT}/assets/img/og.png')
# poster web copy from the 3x master
Image.open(f'{KIT}/posters/poster-lagos-invitation.png').convert('RGB').resize((1200, 1800), Image.LANCZOS).save(f'{ROOT}/assets/img/poster-lagos-v2.jpg', quality=92, optimize=True, progressive=True)
Image.open(f'{KIT}/avatars/avatar-olive-monogram.png').convert('RGB').resize((180, 180), Image.LANCZOS).save(f'{ROOT}/assets/img/apple-touch-icon.png')
print('site assets done')

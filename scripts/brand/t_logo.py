import sys; sys.path.insert(0,'/home/user/wealthtable/scripts/brand')
from lib import *
body=f'<div style="display:flex;gap:40px;padding:40px;background:{C["sand"]};align-items:center">{logo("wt-monogram",C["olive"],width=300)}{logo("wordmark",C["terra"],width=640)}</div><div style="padding:0 40px 40px;background:{C["sand"]}">{logo("lockup-full",C["ink"],width=480)}</div>'
render('t_logo',page(body,1100,700,bg=C['sand']),1100,700,'/tmp/claude-0/-home-user-wealthtable/6c09b34e-63a3-5f59-8e3d-2102b39edbcc/scratchpad/shots/t_logo.png')
flush()

import config
from compiz_wallpaper import getconfig
import execute


if not config.COMPIZ_ALONE:
    DCONF_ROOT = 'dconf write /org/compiz/profiles/unity/plugins/wallpaper/%s "%s"'
    cmd_getsize_h = 'dconf read /org/compiz/profiles/unity/plugins/core/hsize'
    cmd_getsize_v = 'dconf read /org/compiz/profiles/unity/plugins/core/vsize'
else:
    DCONF_ROOT = 'dconf write /org/compiz/profiles/Default/plugins/wallpaper/%s "%s"'
    cmd_getsize_h = 'dconf read /org/compiz/profiles/Default/plugins/core/hsize'
    cmd_getsize_v = 'dconf read /org/compiz/profiles/Default/plugins/core/vsize'


def f(key, val):
    cmd = DCONF_ROOT % (key, val)
    print(cmd)

h = execute.execute_and_output(cmd_getsize_h)
v = execute.execute_and_output(cmd_getsize_v)
h, v = int(h if len(h) > 0 else 1), int(v if len(v) > 0 else 1)
_map = getconfig(h * v)
for n in _map:
    v = _map[n]
    f(n, v)
# compiz wallpaper
imgs = _map['bg-image']
# hsetroot
print('DISPLAY=:0 hsetroot -fill "%s"' % imgs[0])

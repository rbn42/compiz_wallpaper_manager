import config
from compiz_wallpaper import getconfig
import os.path
import execute


if config.COMPIZ_ALONE:
    DCONF_ROOT = 'dconf write /org/compiz/profiles/Default/plugins/wallpaper/%s "%s"'
    cmd_getsize_h = 'dconf read /org/compiz/profiles/Default/plugins/core/hsize'
    cmd_getsize_v = 'dconf read /org/compiz/profiles/Default/plugins/core/vsize'
elif config.COMPIZ0_8:
    DCONF_ROOT = 'python ~/git/compiz_config/main.py ~/.config/compiz/compizconfig/Default.ini set wallpaper s0_%s "%s"'
    cmd_getsize_h = 'python ~/git/compiz_config/main.py ~/.config/compiz/compizconfig/Default.ini get core s0_hsize'
    cmd_getsize_v = 'python ~/git/compiz_config/main.py ~/.config/compiz/compizconfig/Default.ini get core s0_vsize'
else:
    DCONF_ROOT = 'dconf write /org/compiz/profiles/unity/plugins/wallpaper/%s "%s"'
    cmd_getsize_h = 'dconf read /org/compiz/profiles/unity/plugins/core/hsize'
    cmd_getsize_v = 'dconf read /org/compiz/profiles/unity/plugins/core/vsize'


def f(key, val):
    if config.COMPIZ0_8:
        key = key.replace('-', '_')
        # compiz0.8不支持长路径，需要缩短
        if 'bg_image' == key:
            count = 0
            shortcuts = []
            for path in val:
                count += 1
                p_shortcut = '%s/%0.4d%s' % (SHORTCUT_ROOT2,
                                             count, os.path.splitext(path)[1])
                print('ln -s "%s" %s' % (path, p_shortcut))
                #print('cp "%s" %s' % (path, p_shortcut))
                shortcuts.append(p_shortcut)
            val = shortcuts
        val = ''.join(['%s;' % n for n in val])
    cmd = DCONF_ROOT % (key, val)
    print(cmd)

SHORTCUT_ROOT = '/dev/shm/w1', '/dev/shm/w2',
if config.COMPIZ0_8:
    if os.path.exists(SHORTCUT_ROOT[0]):
        SHORTCUT_ROOT1, SHORTCUT_ROOT2 = SHORTCUT_ROOT
    else:
        SHORTCUT_ROOT2, SHORTCUT_ROOT1 = SHORTCUT_ROOT
    print('rm -r %s' % SHORTCUT_ROOT1)
    print('mkdir %s' % SHORTCUT_ROOT2)

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
#print('DISPLAY=:0 hsetroot -fill "%s"' % imgs[0])

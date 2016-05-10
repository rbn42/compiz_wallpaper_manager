import glob
import random
import os
import sys
import config
from compiz_wallpaper import getconfig

if not config.COMPIZ_ALONE:
    def f(key, val):
        cmd = 'dconf write /org/compiz/profiles/unity/plugins/wallpaper/%s "%s"'
        cmd = cmd % (key, val)
        print(cmd)

    IMAGES_MAX = 1  # eval(sys.argv[1].replace('x', '*'))o
    try:
        IMAGES_MAX = eval(sys.argv[1].replace('x', '*'))
    except:
        pass

    _map = getconfig(IMAGES_MAX)

    for n in _map:
        v = _map[n]
        f(n, v)

    # compiz wallpaper
    imgs = _map['bg-image']

    # hsetroot
    print('DISPLAY=:0 hsetroot -fill "%s"' % imgs[0])
else:
    import compiz_config
    h, v = compiz_config.getSize()
    _map = getconfig(h * v)
    for n, v in _map.items():
        n = 's0_' + n
        v = ''.join(['%s;' % i for i in v])
        config['wallpaper'][n] = v
        #print(n + '=' + v)

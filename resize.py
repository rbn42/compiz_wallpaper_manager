#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#import numpy as np
#import scipy.misc
import glob
import os.path
import Image

import sys
WIDTH,HEIGHT = sys.argv[1].split('x')
WIDTH,HEIGHT = int(WIDTH),int(HEIGHT)

l = 'jpg', 'jpeg', 'png'

l = [glob.glob('*.' + n) for n in l]
imgs = []
for ll in l:
    for n in ll:
        imgs.append(n)


for n in imgs:
    print(n)
    if 'info' in n:
        n_out = n.split('info')[1]
    else:
        n_out = n
    p_out = '../resize/raw_resize_%s.png' % n_out
    if os.path.exists(p_out):
        continue

    i = Image.open(n)
    w, h = i.size
    if n.startswith('middle_'):
        a = (h - w * HEIGHT / WIDTH) / 2
        i2 = i.crop((0, a, w, h - a))
    elif n.startswith('bottom_'):
        a = (h - w * HEIGHT / WIDTH) / 2
        i2 = i.crop((0, 2 * a, w, h))
    else:
        i2 = i.crop((0, 0, w, w * HEIGHT / WIDTH))
    i3 = i2.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
    i3.save(p_out, 'PNG', quality=100)
    continue

    i = scipy.misc.imread(n)
    a, b, c = i.shape
    i1 = i[:b * HEIGHT / WIDTH]
    print(i1.shape)
    i2 = scipy.misc.imresize(i1, (HEIGHT, WIDTH), 'cubic')
    print(i2.shape)
    scipy.misc.imsave(p_out, i2)

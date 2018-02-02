#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Greet

Usage:
  main.py <input_root> <output_root> <size>
  main.py -h | --help

Options:
  -h --help     Show this screen.
"""
from docopt import docopt
import scipy.misc
import numpy as np
arguments = docopt(__doc__)
input_root = arguments['<input_root>'] + '/'
output_root = arguments['<output_root>'] + '/'

import glob
import os.path
from PIL import Image

WIDTH, HEIGHT = arguments['<size>'].split('x')
WIDTH, HEIGHT = int(WIDTH), int(HEIGHT)

path_root = input_root
l = 'jpg', 'jpeg', 'png'

l = [glob.glob('%s/*.%s' % (path_root, n)) for n in l]
imgs = []
for ll in l:
    for n in ll:
        imgs.append(n)

for file_path in imgs:
    _, file_name = os.path.split(file_path)
    if 'info' in file_name:
        n_out = file_name.split('info')[1]
    else:
        n_out = file_name
    p_out = '%s/%s.png' % (output_root, n_out)
    if os.path.exists(p_out):
        continue

    i = Image.open(file_path)

    preserve = 1    # 消除边缘，有些图可能边缘有问题
    w, h = i.size
    x, y, w, h = 1, 1, w - 2, h - 2

    import imginfo
    from config import CONFIG_FILE
    o = imginfo.load(CONFIG_FILE)
    x1, y1, x2, y2 = o.get(file_name, {}).get('crop', [x, y, x + w, y + h])
    x, y, w, h = x1, y1, x2 - x1, y2 - y1

    try:
        i = i.crop((x, y, w, h))
    except BaseException:
        print('error:%s' % file_path)
        a = 1 / 0

    w, h = i.size
    # TODO 兼容下横屏竖屏的图片
    target_width, target_height = WIDTH, HEIGHT
    if file_name.startswith('middle_'):
        a = (h - w * target_height / target_width) / 2
        _crop = (0, a, w, h - a)
    elif file_name.startswith('bottom_'):
        a = (h - w * target_height / target_width) / 2
        _crop = (0, 2 * a, w, h)
    elif w * target_height > h * target_width:
        a = (w - h * target_width / target_height) / 2
        _crop = (a, 0, w - a, h)
    else:
        # top_
        _crop = (0, 0, w, w * target_height / target_width)

    try:
        i2 = i.crop(_crop)
    except BaseException:
        print(file_path)
        a = 1 / 0
    i3 = i2.resize((target_width, target_height), Image.ANTIALIAS)
    i3.save(p_out, 'PNG', quality=100)
    continue

    #i = scipy.misc.imread(file_path)
    #a, b, c = i.shape
    #i1 = i[:b * target_height/ target_width]
    #i2 = scipy.misc.imresize(i1, (HEIGHT, WIDTH), 'cubic')
    #scipy.misc.imsave(p_out, i2)

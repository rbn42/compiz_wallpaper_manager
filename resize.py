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
arguments = docopt(__doc__)
input_root = arguments['<input_root>'] + '/'
output_root = arguments['<output_root>'] + '/'

import glob
import os.path
import Image

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
    p_out = '%s/raw_resize_%s.png' % (output_root, n_out)
    if os.path.exists(p_out):
        continue

    i = Image.open(file_path)
    w, h = i.size
    if file_name.startswith('middle_'):
        a = (h - w * HEIGHT / WIDTH) / 2
        i2 = i.crop((0, a, w, h - a))
    elif file_name.startswith('bottom_'):
        a = (h - w * HEIGHT / WIDTH) / 2
        i2 = i.crop((0, 2 * a, w, h))
    else:
        i2 = i.crop((0, 0, w, w * HEIGHT / WIDTH))
    i3 = i2.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
    i3.save(p_out, 'PNG', quality=100)
    continue

    i = scipy.misc.imread(file_path)
    a, b, c = i.shape
    i1 = i[:b * HEIGHT / WIDTH]
    print(i1.shape)
    i2 = scipy.misc.imresize(i1, (HEIGHT, WIDTH), 'cubic')
    print(i2.shape)
    scipy.misc.imsave(p_out, i2)

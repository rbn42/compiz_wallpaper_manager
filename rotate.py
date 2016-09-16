#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Greet

Usage:
  main.py <input_root>  <output_root> (left|right)  
  main.py -h | --help

Options:
  -h --help     Show this screen.
"""

import os.path
import glob
import scipy.misc
import numpy as np
import json


def f(p_src, p_dst, left=False):
    if not os.path.exists(p_src):
        return
    existed_files = {json.loads(os.path.splitext(n)[0])[
        'name'] for n in os.listdir(p_dst)}
    for n in os.listdir(p_src):
        _json = os.path.splitext(n)[0]
        o = json.loads(_json)
        name = o['name']
        if name in existed_files:
            continue
        print(n)
        i = scipy.misc.imread(p_src + n)
        i = np.rollaxis(i, 1)
        if left:
            i = np.rot90(i)
            i = np.rot90(i)
    #    i=scipy.misc.imrotate(i,90)
        scipy.misc.imsave(p_dst + n, i)

from docopt import docopt
arguments = docopt(__doc__)

input_root = arguments['<input_root>'] + '/'
output_root = arguments['<output_root>'] + '/'
f(input_root, output_root, left=arguments['left'])

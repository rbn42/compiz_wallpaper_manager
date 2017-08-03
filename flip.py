#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Greet

Usage:
  main.py <path_root>
  main.py -h | --help

Options:
  -h --help     Show this screen.
"""
from docopt import docopt
arguments = docopt(__doc__)

import glob
import os.path
from PIL import Image

path_root = arguments['<path_root>']
imgs = glob.glob('%s/*.png' % path_root)
for path in imgs:
    dst = '%s_flip.png' % path
    if not os.path.exists(dst):
        print('convert -flop  "%s" "%s"' % (path, dst))

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os.path
import glob
import scipy.misc
import numpy as np
import imginfo
import shutil
import sys


def load_img(path):
    print('load image:%s' % path)
    img = scipy.misc.imread(path)
    img = img[:, :, :3]
    x, y, z = img.shape
    return img, x, y

for filename in sys.argv[1:]:
    info = imginfo.load(filename)

    if 'mean' not in info:
        img, width, height = load_img(filename)
        mean = np.mean(img) / 256.0
        info['mean'] = mean

    if 'topleftmean' not in info:
        img, width, height = load_img(filename)
        topleftmean = np.mean(img[:int(width / 2), :int(height / 2)]) / 256.0
        info['topleftmean'] = topleftmean

    imginfo.save(filename, info)

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
    if len(img.shape) == 3:
        x, y, z = img.shape
        img = img[:, :, :3]
    else:
        x, y = img.shape
    return img, x, y


for filename in sys.argv[1:]:
    info = imginfo.load(filename)

    if 'mean' not in info:
        img, height, width = load_img(filename)
        mean = np.mean(img) / 256.0
        info['mean'] = mean

    if 'topleftmean' not in info:
        img, height, width = load_img(filename)
        topleftmean = np.mean(img[:int(height / 2), :int(width / 2)]) / 256.0
        info['topleftmean'] = topleftmean

    keys = 'top10mean', 'top10'
    for key in keys:
        if key not in info:
            img, height, width = load_img(filename)
            value = np.mean(img[:int(height / 10)]) / 256.0
            info[key] = value

    key = 'top10center'
    if key not in info:
        img, height, width = load_img(filename)
        value = np.mean(img[:int(height / 10), int(width / 4):int(width * 3 / 4)]) / 256.0
        info[key] = value

    key = 'bottom10'
    if key not in info:
        img, height, width = load_img(filename)
        value = np.mean(img[-int(height / 10):]) / 256.0
        info[key] = value

    imginfo.save(filename, info)

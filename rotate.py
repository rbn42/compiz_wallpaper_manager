import os.path
import glob
import scipy.misc
import numpy as np


def f(p_src, p_dst, left=False):
    if not os.path.exists(p_src):
        return
    for n in os.listdir(p_src):
        print(n)
        if os.path.exists(p_dst + n):
            continue
        i = scipy.misc.imread(p_src + n)
        i = np.rollaxis(i, 1)
        if left:
            i = np.rot90(i)
            i = np.rot90(i)
    #    i=scipy.misc.imrotate(i,90)
        scipy.misc.imsave(p_dst + n, i)

p_src = './resize/'
p_dst = './resize_rotate/'
f(p_src, p_dst)
p_src = './raw_/'
f(p_src, p_dst)


p_src = './resize/'
p_dst = './resize_rotate_left/'
f(p_src, p_dst, left=True)
p_src = './raw_/'
f(p_src, p_dst, left=True)

import glob
import random
import os
import sys


def getconfig(num=1):
    # find images
    exts = 'jpg', 'jpeg', 'png', 'gif'
    if os.path.exists('mark_rotate_normal'):
        l = [glob.glob('./raw_/*.' + n) for n in exts]
        l += [glob.glob('./resize/*.' + n) for n in exts]
    elif os.path.exists('mark_rotate_right'):
        l = [glob.glob('./resize_rotate/*.' + n) for n in exts]
    elif os.path.exists('mark_rotate_left'):
        l = [glob.glob('./resize_rotate_left/*.' + n) for n in exts]
    imgs = []
    for ll in l:
        for n in ll:
            n = os.path.abspath(n)
            imgs.append(n)
    random.shuffle(imgs)
    imgs = imgs[:num]

    # compiz wallpaper
    return {
        "bg-color1": ['#000000ff'] * len(imgs),
        "bg-color2": ['#000000ff'] * len(imgs),
        "bg-fill-type": [0] * len(imgs),
        "bg-image": imgs,
        "bg-image-pos": [0] * len(imgs),
        #"cycle-wallpapers": "false",
    }

if __name__ == '__main__':
    print(getconfig(10))

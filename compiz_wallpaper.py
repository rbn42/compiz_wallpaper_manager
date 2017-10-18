import glob
import os
import random
import sys
import subprocess
import re


def getconfig(num=1, root='.', randomize=True):

    cmd = "xrandr --query --verbose"
    s = subprocess.check_output(cmd, shell=True).decode()
    for line in s.split('\n'):
        if 'disconnected' not in line:
            if 'connected' in line:
                r = '\) (.+) \('
                orientation = re.findall(r, line)[0]
                break

    # find images
    exts = 'jpg', 'jpeg', 'png', 'gif'
    if 'normal' == orientation:
        l = [glob.glob(root + '/raw_/*.' + n) for n in exts]
        l += [glob.glob(root + '/resize/*.' + n) for n in exts]
    elif 'right' == orientation:
        l = [glob.glob(root + '/resize_rotate/*.' + n) for n in exts]
    elif 'left' == orientation:
        l = [glob.glob(root + '/resize_rotate_left/*.' + n) for n in exts]
    imgs = []
    for ll in l:
        for n in ll:
            n = os.path.abspath(n)
            imgs.append(n)
    imgs.sort()
    if randomize:
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

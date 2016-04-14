import glob
import random
import os
import sys
IMAGES_MAX =1 # eval(sys.argv[1].replace('x', '*'))o
try:
    IMAGES_MAX = eval(sys.argv[1].replace('x', '*'))
except:
    pass

#find images
exts = 'jpg', 'jpeg', 'png','gif'
if os.path.exists('mark_rotate_normal'):
    l = [glob.glob('./raw_*.' + n) for n in exts]
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
imgs = imgs[:IMAGES_MAX]

def f(key, val):
    cmd = 'dconf write /org/compiz/profiles/unity/plugins/wallpaper/%s "%s"'
    cmd = cmd % (key, val)
    print(cmd)

#compiz wallpaper
f("bg-color1", ['#000000ff'] * len(imgs))
f("bg-color2", ['#000000ff'] * len(imgs))
f("bg-fill-type", [0] * len(imgs))
f("bg-image", imgs)
f("bg-image-pos", [0] * len(imgs))
f("cycle-wallpapers", "false")

#hsetroot
print('DISPLAY=:0 hsetroot -fill "%s"' % imgs[0])

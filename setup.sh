#!/bin/bash
mkdir ./raw
mkdir ./raw_
mkdir ./resize
mkdir ./resize_rotate
mkdir ./resize_rotate_left

python ./bin/resize.py /media/$USER/dmzj/wallpaper_raw  ~/Pictures/compiz/resize/ 1920x1080 #分辨率
#bash ./bin/resize.sh 3840x2160 #分辨率

python ./bin/rotate.py ./resize ./resize_rotate  right
python ./bin/rotate.py ./resize ./resize_rotate_left left
python ./bin/rotate.py ./raw_ ./resize_rotate right
python ./bin/rotate.py ./raw_ ./resize_rotate_left left

./bin/compiz.sh

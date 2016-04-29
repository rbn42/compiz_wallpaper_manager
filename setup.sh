#!/bin/bash
mkdir ./raw
mkdir ./raw_
mkdir ./resize
mkdir ./resize_rotate
mkdir ./resize_rotate_left

python ./bin/resize.py 1920x1080 #分辨率
#bash ./bin/resize.sh 3840x2160 #分辨率
python ./bin/rotate.py

./bin/compiz.sh

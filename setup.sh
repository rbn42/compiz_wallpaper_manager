#!/bin/bash
mkdir ./raw
#mkdir ./raw_
mkdir ./resize
mkdir ./resize_rotate
mkdir ./resize_rotate_left

python ./bin/resize.py ./raw ./resize 1920x1080 #分辨率
#bash ./bin/resize.sh 3840x2160 #分辨率

#flip
#python ./bin/flip.py ./resize | bash

python ./bin/rotate.py ./resize ./resize_rotate  right
python ./bin/rotate.py ./resize ./resize_rotate_left left
#python ./bin/rotate.py ./raw_ ./resize_rotate right
#python ./bin/rotate.py ./raw_ ./resize_rotate_left left

./bin/compiz.sh

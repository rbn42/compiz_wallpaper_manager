#!/bin/bash
mkdir ./raw
#mkdir ./raw_
mkdir ./resize
mkdir ./resize_rotate
mkdir ./resize_rotate_left

WIDTH=1920
HEIGHT=1080
python ./bin/resize.py ./raw ./resize $WIDTH"x"$HEIGHT #1920x1080 #分辨率
#bash ./bin/resize.sh 3840x2160 #分辨率
#竖屏
python ./bin/resize.py ./raw_portrait ./resize_rotate $HEIGHT"x"$WIDTH 
python ./bin/resize.py ./raw_portrait ./resize_rotate_left $HEIGHT"x"$WIDTH 

#flip
#python ./bin/flip.py ./resize | bash

python ./bin/rotate.py ./resize ./resize_rotate  right
python ./bin/rotate.py ./resize ./resize_rotate_left left
#python ./bin/rotate.py ./raw_ ./resize_rotate right
#python ./bin/rotate.py ./raw_ ./resize_rotate_left left

 python bin/add_info.py resize*/*.png
                  
./bin/compiz.sh

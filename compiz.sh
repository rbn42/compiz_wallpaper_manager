#!/bin/bash 
#crontab -e
#* * * * *   bash ~/Pictures/compiz/bin/compiz.sh

#壁纸目录
export WALLPAPER_ROOT=~/Pictures/compiz
source ~/config/rc/displayrc

#加载壁纸
python $(dirname "$0")/compiz.py $WALLPAPER_ROOT | bash

#compiz0.8用
python ~/git/compiz_config/main.py ~/.config/compiz/compizconfig/Default.ini submit

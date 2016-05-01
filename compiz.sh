#!/bin/bash 
#crontab -e
#* * * * *   bash ~/Pictures/compiz/bin/compiz.sh

cd ~/Pictures/compiz/  #根目录
#限定加载图片的最大数目
#IMAGES_MAX=3x3  
IMAGES_MAX=$(dconf read /org/compiz/profiles/unity/plugins/core/hsize)x$(dconf read /org/compiz/profiles/unity/plugins/core/vsize)
#echo $IMAGES_MAX

#这部分是为hsetroot设定的环境变量,和compiz壁纸无关.
PID=$(pgrep gnome-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

#加载壁纸
python bin/compiz.py $IMAGES_MAX | bash

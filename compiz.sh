#!/bin/bash 
#crontab -e
#* * * * *   bash ~/Pictures/compiz/bin/compiz.sh

#这部分是为hsetroot设定的环境变量,和compiz壁纸无关.
PID=$(pgrep gnome-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

#加载壁纸
cd ~/Pictures/compiz/  #根目录
python ./bin/compiz.py | bash


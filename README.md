compiz的wallpaper插件可以为不同的工作区设置不同壁纸,不过手动设置很麻烦,所以我写了点脚本.下面是设置方法.

准备
=
1.安装依赖
```bash
sudo apt-get install -y compiz-plugins-extra compizconfig-settings-manager
sudo apt-get install -y python-pil python-numpy python-scipy 
sudo apt install dconf-editor -y
```
2.打开ccsm,搜索wallpaper,在前面打上勾,然后最好注销重新登入.
```bash
ccsm
```

安装
=
0.把本目录下载到~/Pictures/compiz/bin/.如果要配置到其他目录,需要改动下[compiz.sh](compiz.sh)  
1.把图片放入~/Pictures/compiz/raw/目录,脚本会自动调整图片分辨率;或者放入 ~/Pictures/compit/raw\_/目录,不调整分辨率直接使用.  
2.修改[setup.sh](setup.sh)中的分辨率  
3.运行
```bash
cd ~/Pictures/compiz/
bash bin/setup.sh 
```

随机变换壁纸
=
把[compiz.sh](compiz.sh)加入到crontab  
```bash 
crontab -e
*/10 * * * *   bash ~/Pictures/compiz/bin/compiz.sh
```

旋转屏幕   
=
```bash
~/bin/rot.sh normal  
~/bin/rot.sh left  
~/bin/rot.sh right  
```

1.可以把这些命令加入到[~/.cache/rofi-2.runcache文件](https://github.com/rbn42/home/blob/master/config/rofi/rofi-2.runcache),配合rofi使用.  
2.[~/bin/rot.sh的范例](https://github.com/rbn42/home/blob/master/bin/rot.sh).

Ubuntu Unity8将不再使用compiz,所以将来可能不再有多壁纸功能了.

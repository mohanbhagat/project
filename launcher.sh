#!/bin/sh
sleep 3
sudo alsactl restore -f /etc/asound.state
sleep 10
python3 /home/pi/12/main.py > /mnt/ramdisk/voice.txt 2>&1


#!/bin/bash

ps -ef | grep together.py | grep -v grep | awk '{print $2}' | xargs kill -9
sudo killall pulseaudio 
sudo pulseaudio --start

python3 together.py

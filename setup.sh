#!/bin/bash

GREEN='\033[1;32m'
# RED='\033[1;31m'

echo -e "installing ......." 
#  copying  the  createFlaskWsgi  folder to  /usr/local/share
cp -r createFlaskWsgi /usr/local/share
#  copying  the  createwsgi  script to  /usr/local/bin
cp createwsgi /usr/local/bin

echo -e "$GREEN flaskk wsgi script setup  installed successfully";




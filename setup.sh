#!/bin/bash

GREEN='\033[1;32m'
# RED='\033[1;31m'
NC='\033[0m' # No Color
# echo -e "installing ......." 
#  copying  the  createFlaskWsgi  folder to  /usr/local/share
cp -r createFlaskWsgi /usr/local/share/
#  copying  the  createwsgi  script to  /usr/local/bin
cp -r createwsgi /usr/local/bin

echo -e "$GREEN flask wsgi script setup  installed successfully $NC";




#!/bin/bash
#sets up the adventure 
#assumes the git repo has been checked out at /home/pi/raspi-adventure

#mv to .raspi-adventure, to hide the files
mv raspi-adventure .raspi-adventure

#requirements
sudo apt-get -y install python-dev 
sudo easy_install python-daemon
sudo easy_install PIL
sudo easy_install requests

#start server
.raspi-adventure/checker.py

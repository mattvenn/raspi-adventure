#!/bin/bash
""" 
sets up the adventure 
assumes the git repo has been checked out at /home/pi/raspi-adventure
"""

#mv to .raspi-adventure, to hide the files
mv raspi-adventure .raspi-adventure

#start server
.raspi-adventure/checker.py

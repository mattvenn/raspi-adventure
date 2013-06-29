# Adventure game for learning python on the raspberry pi

Strictly first draft, comments welcomed!
Commandline based, you have to fulfil a number of programming tasks including:

* file IO
* sockets
* requesting pages from websites 
* posting to websites
* creating images with PIL
* regular expressions

This has been designed for already fairly advanced programmers (though not necessarily in python). More levels could be added to cater for beginners.

# Installation

Fetch this repo with

    cd ~/
    git clone git@github.com:mattvenn/raspi-adventure.git

And set it up like this (have a read of the script first):

    ./raspi-adventure/setup.sh

Which should install the list of requirements, install the start script, move the install directory to .raspi-adventure (for obfuscation).

## Starting the game server

This has been designed for the pi, with the default install directory as /home/pi/.raspi-adventure. You can override with the option --root-dir

    python ~/.raspi-adventure/checker.py

Log is written to /tmp/log.file. You can also use the --no-detach argument to stop the checker from daemonising and to see output on stdout.

# To start!

type
 
    start_adventure

on the commandline, it will ask your name, and if all is well you'll be directed to the first clue.

If you get an error, then try and fix it (first thing to do is try running with --no-detach or check the logs at /tmp/log.file). And please let me know!

# Todo

* the game will fail if 2 people are running and both get onto the sockets level at once
* make it easier to add levels (better framework)
* install an init script to start the daemon at boot

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

This has been designed for the raspberry pi, so you'd need to change a few paths (hard coded) in the source. Also, it expects you to be logged in as pi, so that would need to be changed too.

If you're on a pi, then fetch this repo with

    cd ~/
    git clone git@github.com:mattvenn/raspi-adventure.git

And set it up like this (have a read of the script first):

    ./raspi-adventure/setup.sh

Which should install the list of requirements, install the start script, move the install directory, then start the game server.

## Restarting the game server after a reboot

The game server will need restarting on reboot like this:

    python ~/.raspi-adventure/checker.py

Note the . in front of the path, which is used to obfuscate the files that could be used for cheating!

# To start!

type
 
    start_adventure

on the commandline, it will ask your name, and if all is well you'll be directed to the first clue.

If you get an error, then try and fix it (first thing to do is remove the daemonising at the end of checker.py to start seeing the logging). And please let me know!

# Todo

* the game will fail if 2 people are running and both get onto the sockets level at once
* make it easier to add levels (better framework)
* install an init script to start the daemon at boot

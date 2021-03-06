# The Aim

To pass this, the first stage of the adventure, you must write a python program that creates a file. This file must be 100 lines long, be in the directory given in your start message, and called file.txt

The odd lines of the file must be 'raspberry', and the even lines 'pi'. So the first 4 lines of the file would look like this:

    raspberry
    pi
    raspberry
    pi


Once the file has been created correctly you will receive your clue to begin the 2nd part of the adventure...

If you get stuck, remember that you'll easily be able to find examples of python programs on the internet!

# What you'll need to know...

## Editing program files

Use nano, an easy to use editor. Just type

    nano

on the command line to get started. Then control-X to exit. Nano will ask you if you want to save your file.

## Running program files

If you saved your program file as test.py, then you can run it like this

    python test.py

## Opening a file to write

    file_handle = open('filename','w')

The 'w' is to tell python that we want to write to the file.

## Writing lines to a file

    file_handle.write('a line\n')

We need a \n at the end of the line so that it becomes a new line. The \n character is how Linux makes new lines.

## While loops in python

You can repeat a loop using syntax like this:

    var = 0
    while var < 10:
        var += 1
        print var

## Closing files

    file_handle.close()

It's always good practice to close a file once it's been written to.

# Further reading

* http://docs.python.org/2/tutorial/inputoutput.html

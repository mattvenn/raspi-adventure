# The Aim

To pass this, the first stage of the adventure, you must write a python program that creates a file. The file must be 100 lines long.

The odd lines of the file must be 'raspberry', and the even lines 'pi'. So the first 4 lines of the file would look like this:

    raspberry
    pi
    raspberry
    pi

The file must be in this directory.

Once the file have been created correctly you will receive your clue to begin the 2nd part of the adventure...

# What you'll need to know...

## Opening a file to write

    file_handle = open('filename','w')

The 'w' is to tell python that we want to write to the file.

## Writing lines to a file

    file_handle.write('a line\n')

We need a \n at the end of the line so that it becomes a new line. The \n character is how Linux makes new lines.

## Closing files

    file_handle.close()

It's always good practice to close a file once it's been written to.

# Further reading

http://docs.python.org/2/tutorial/inputoutput.html
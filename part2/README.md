# The Aim

To pass this, the first stage of the adventure, you must write a python program that creates 100 files. The files must be called 1, 2, 3, 4 ... all the way to 100.

The files must be in this directory.

The first file must have 1 line in it, the 2nd file 2 lines, all the way up until the 100th file has 100 lines in it.

Once the files have been created you will receive your clue to begin the 2nd part of the adventure...

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

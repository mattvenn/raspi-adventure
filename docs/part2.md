# The Aim

Now you must write a python program that creates 100 files. The files must be called 1, 2, 3, 4 ... all the way to 100.

The files must be in the directory given to you in the message.

The first file must have 1 line in it, the 2nd file 2 lines, all the way up until the 100th file has 100 lines in it. You can decide what is on each line.

Once the files have been created you will receive your clue to begin the 3rd part of the adventure...

# What you'll need to know...

## Using the range() builtin

Another way of doing a number of loops is using the range builtin:

    for var in range(10):
        print var

This avoids having to initialise a variable and incrementing it manually. Try it in ipython. Read about how to start range() from 1 instead of 0 here:

    http://docs.python.org/release/1.4/tut/node30.html

## Converting from an int to a string

    str(10)

returns the string '10'. In python we also have float() and int() for similar conversions.

# Further reading

* http://docs.python.org/2/tutorial/inputoutput.html

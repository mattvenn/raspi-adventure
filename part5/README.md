# The Aim

There is a web server running on port 8080 of the pi. You need to fetch the page at /. This page will have a challenge code in it, which you will need to recover from the page.

After getting the challenge code, multiply it by 2 and then post it back to the same server. The data sent to the server must have one key and one value. The key is 'response' and the value is the challenge code multipled by 2.

# What you'll need to know...

## The requests library

Requests is a great library that makes it easy to fetch and post to web servers on the internet (or the pi). You can read about it here: http://docs.python-requests.org/en/latest/

## Fetching a page

You can fetch a page as simply as

    r = requests.get(url)

But your url will have to be correct (starts with http, has the correct host name and has the port number included). If you're not familiar with constructing urls, have a read of http://en.wikipedia.org/wiki/Uniform_resource_locator

## Capturing the challenge code

There are lots of ways to do this, after fetching the file we could

* copy the code out by hand
* parse the HTML
* use regular expressions

Because we're advanced programmers, we'll focus on the second 2 options. If you want to learn about HTML parsing, then have a look at this answer on stack overflow: http://stackoverflow.com/questions/3276040/how-can-i-use-the-python-htmlparser-library-to-extract-data-from-a-specific-div

It's actually quite a complicated way to complete this task because we only need to match one thing and we know the exact format of it. Regular expressions would be simpler in this case.

## Regular expressions

Regular expressions are an incredibly powerful tool for matching patterns and extracting data from text. The topic is huge, so we can only just touch on it here, but if you aspire to be a powerful programmer then you should think about learning! 

You can read more about how to match patterns on this page: http://docs.python.org/2/howto/regex.html#regex-howto

Try this in ipython, and play around with it.

* `.*` matchs any number of any characters.
* `\w+` is the way we specify a regular expression to match some number of word characters (includes all of A-Z, a-z). 
* The () brackets 'capture' data for us to read later. 

    import re
    text = "raspberry pi is cool"
    match = re.search('rasp.*is (\w+)',text)
    if match:
        print match.group()
        print match.group(1)

Clue: to match digits, you'd need \d+ intead of \w+

## Posting to a page

Once you have your challenge code, you can post it back to the server using the post method, detailed here: http://docs.python-requests.org/en/latest/user/quickstart/#more-complicated-post-requests

# Further reading

More on regular expressions: http://docs.python.org/2/howto/regex.html#regex-howto
Python's HTMLParser: http://docs.python.org/2/library/htmlparser.html

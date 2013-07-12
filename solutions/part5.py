from socket import gethostname; 
import requests
import re

#get the page
host = gethostname()
url = 'http://' + host + ':8080/'
r = requests.get(url)
print "fetched:", r.text

#find the code
match = re.search('challenge=(\d+)',r.text)
if match:
    print match.group(1)
    code = int(match.group(1))
    code = code * 2
    #make a post request
    payload = {'response': code }
    print "sending:", payload
    r = requests.post(url, data=payload)
    print r.text
    print r.status_code
else:
    print "couldn't read the page"

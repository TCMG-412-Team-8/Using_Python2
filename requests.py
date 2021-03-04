import re
from collections import Counter 

log_line = 'local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150'

pattern= r'[0-z]+.[a-z]+'

Regexp ={}

for line in open('logfile.log'):
    match = re.search(pattern, line)
    try:
        filename = match.groups()
    except AttributeError:
        filename = match
    if filename in Regexp:
        Regexp[filename] += 1
    else:
        Regexp[filename] = 1

print (Regexp)
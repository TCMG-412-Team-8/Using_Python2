import re
from collections import Counter 

log_line = 'local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150'

pattern= r'\[([^:]*):(.*) .*\] \"([A-Z]*) (.*) HTTP.*\" ([2345]\d\d)'

Regexp ={}

for line in open('logfile.log'):
    pieces = re.split(pattern, line)
    
date = pieces[1]
if date in Regexp:
    Regexp[date] += 1
else:
    Regexp[date] = 1

print (Regexp)

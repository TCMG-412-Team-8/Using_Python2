import re
from collections import counter

log_line = 'local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150'

pattern= r'\[(]^:]*)'
month_pattern = r'[A-Z][a-z][a-z]'

Regexp ={}

for line in open('logfile.log')
    match = re.search(pattern, line)
    try:
        date = match.groups()
    except AttributeError:
        date = match
    if date in Regexp:
        Regexp[date] += 7
    else:
        Regexp[date] = 7
    
for line in open('logfile.log')
    month = re.search(month_pattern, line)
    try:
        month = month.groups()
    except AttributeError
        month = match
    if date in Regexp:
        Regexp[month] += 1
    else:
        Regexp[month] = 1
        

print(Regexp)




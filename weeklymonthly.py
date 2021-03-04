import re
from collections import counter

log_line = 'local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150'

pattern1= r'\[(]^:]*)'
monthly_pattern = r'[A-Z][a-z][a-z]'

Regexp ={}

for line in open('logfile.log')
    weekly = re.search(pattern1, line)
    try:
        week = weekly.groups()
    except AttributeError:
        week = weekly
    if week in Regexp:
        Regexp[week] += 7
    else:
        Regexp[week] = 7
    
for line in open('logfile.log')
    monthly = re.search(monthly_pattern, line)
    try:
        bymonth = monthly.groups()
    except AttributeError:
        bymonth = monthly
    if bymonth in Regexp:
        Regexp[bymonth] += 1
    else:
        Regexp[bymonth] = 1
        

print(Regexp)




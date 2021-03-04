import re

log_line = 'local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150'

month_pattern= r'[A-Z][a-z][a-z]'


with open('logfile.log') as logfile:
    for line in ('logfile.log'):
        month = re.search(month_pattern,line)
    files = [open('month.log' % i, 'w') for i in range(0,13)]
    for i, line in enumerate(logfile):
        files[i % 13].write(line)
    for f in files:
        f.close()
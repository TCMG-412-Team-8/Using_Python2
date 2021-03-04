import re
from collections import Counter 

log_line = 'local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150'

pattern= r'\[([^:]*):(.*) .*\] \"([A-Z]*) (.*) HTTP.*\" ([2345]\d\d)'

Regexp ={}

for line in open('logfile.log'):
    pieces = re.split(pattern, line)
    
request = pieces[4]
def most_frequent(pieces):
    occurence_count = Counter(pieces)
    return occurence_count.most_common(4)[0][0]
print(most_frequent(pieces))
print (Regexp)
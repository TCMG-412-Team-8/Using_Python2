import re
from collections import Counter 

log_line = 'local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150'

pattern= r'\[([^:]*):(.*) .*\] \"([A-Z]*) (.*) HTTP.*\" ([2345]\d\d)'

code_dict ={}

for line in open('logfile.log'):
    match = re.search(pattern, line)
    try:
        filename = match.groups()[3]
    except AttributeError:
        filename = match
    if filename in code_dict:
        code_dict[filename] += 1
    else:
        code_dict[filename] = 1


values = list(code_dict.values())
keys = list(code_dict.keys())

# calculates the max and the minimum number of files 
m = max (values)
n = min (values)
i = values.index(m)
z = values.index(n)

print("The most requested file was:",keys[i])
print("The least requested file was:",keys[z])

import re

log_line = 'local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150'

jan_pattern= r'Jan'
Feb_pattern= r'Feb'
March_pattern = r'Mar'
April_pattern = r'Apr'
May_pattern = r'May'
June_pattern = r'Jun'
July_pattern = r'Jul'
August_pattern = r'Aug'
September_pattern = r'Sep'
Oct_pattern = r'Oct'
Nov_pattern = r'Nov'
Dec_pattern = r'Dec'


jan = 0 
feb = 0
mar = 0
apr = 0
may = 0
jun = 0
jul = 0
aug = 0 
sep = 0
oct = 0
nov = 0
dec = 0

janlogs= open('Janlogs.log', 'w')
feblogs= open('feblogs.log', 'w')
marlogs= open('marlogs.log', 'w')
aprlogs= open('aprlogs.log', 'w')
maylogs= open('maylogs.log', 'w')
junlogs= open('junlogs.log', 'w')
Jullogs= open('Jullogs.log', 'w')
auglogs= open('auglogs.log', 'w')
seplogs= open('Seplogs.log', 'w')
octlogs= open('octlogs.log', 'w')
novlogs= open('novlogs.log', 'w')
declogs= open('declogs.log', 'w')


month_dict = {}
for line in open('logfile.log'):
    if re.search(jan_pattern,line):
        jan +=1 
        janlogs.write(line)
    if re.search(Feb_pattern,line):
        feb +=1 
        feblogs.write(line)
    if re.search(March_pattern,line):
        mar +=1 
        marlogs.write(line)
    if re.search(April_pattern,line):
        apr +=1 
        aprlogs.write(line)
    if re.search(May_pattern,line):
        may +=1 
        maylogs.write(line)
    if re.search(June_pattern,line):
        jun +=1 
        junlogs.write(line)
    if re.search(July_pattern,line):
        jul +=1 
        Jullogs.write(line)
    if re.search(August_pattern,line):
        aug +=1 
        auglogs.write(line)
    if re.search(September_pattern,line):
        sep +=1 
        seplogs.write(line)
    if re.search(Oct_pattern,line):
        oct +=1 
        octlogs.write(line)
    if re.search(Nov_pattern,line):
        nov +=1 
        novlogs.write(line)
    if re.search(Dec_pattern,line):
        dec +=1 
        declogs.write(line)

print = ('Total responses in January were', jan)
print = ('Total responses in Febuary were', feb)
print = ('Total responses in March were', mar)
print = ('Total responses in April were', apr)
print = ('Total responses in May were', may)
print = ('Total responses in June were', jun)
print = ('Total responses in July were', jul)
print = ('Total responses in August were', aug)
print = ('Total responses in September were', sep)
print = ('Total responses in October were', oct)
print = ('Total responses in November were', nov)
print = ('Total responses in December were', dec)


    



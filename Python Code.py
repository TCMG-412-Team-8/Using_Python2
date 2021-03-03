import os.path
import requests
import re
if os.path.isfile('logfile.log'):
    print ("Opening File")
else:
    print('Downloading file request')

    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    r = requests.get(url,allow_redirects=True)

    open('logfile.log','wb').write(r.content)

    print(r.status_code)
    print(r.encoding)
reader = open("logfile.log", "r")
reader.seek(0)

line_number = reader.tell()
total = 0
current = 0
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
failed_requests = 0
redirected = 0
while(reader.readline()!=""):
    reader.seek(line_number)
    line = reader.readline()
    line_number = reader.tell()

    if line.count("1994") != 0:
        total += 1
    if line.count("1995") != 0:
        current += 1
        total += 1

    if re.search("\".*\" 4..", line) != None:
        failed_requests += 1
    if re.search("\".*\" 3..", line) != None:
        redirected += 1
<<<<<<< Updated upstream

print("The total amount of requests are:",total)
print("This is the total amount of requests in the last year (1995):",current)
=======


print("The total amount of requests are:",total)
print("This is the total amount of requests in the last year (1995):",current)

>>>>>>> Stashed changes
print("Percentage of failed requests:",round(failed_requests/total*100,3),"%")
print("Percentage of redirects:",round(redirected/total*100,3),"%")
reader.close()










import re

things = {}
for line in open('logfile.log'):
    pieces = re.split("\[([^:]*):(.*) .*\] \"([A-Z]*) (.*) HTTP.*\" ([2345]\d\d)"gm, line)
    #I am so damn confused. I take nap. I be back at 5pm.
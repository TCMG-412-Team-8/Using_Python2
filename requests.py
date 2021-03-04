import re

things = {}
for line in open('logfile.log'):
    pieces = re.split(r"\[([^:]*):(.*) .*\] \"([A-Z]*) (.*) HTTP.*\" ([2345]\d\d)", line)
    #I am so damn confused. I take nap. I be back at 5pm.
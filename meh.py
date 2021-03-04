import re

things = {}

for line in open('logfile.log'):
  
  # Use the Regex module to split out the filename from the line
  pieces = re.split(r"\[([^:]*):(.*) .*\] \"([A-Z]*) (.*) HTTP.*\" ([2345]\d\d)", line)
  
  
  # Let's further say that we can get the filename part at the 4th list element
  filename = pieces[4]
  # Check and see if a key that matches 'filename' exists using the 'in' operator
  if filename in things:
    # So we've already added this file -- let's increment the counter
    things[filename] += 1
  else:
    # This is a new filename -- let's add it to the dictionary
    things[filename] = 1

print(things)
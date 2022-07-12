#file
#------------
#Abraham Lincoln
#Andrew P Garfield
#Connor Milliken
#Jordan Alexander Williams
#Madonna
#programming is cool


#Expected Output
#----------------
#Abraham Lincoln
#Andrew P Garfield
#Connor Milliken
#Jordan Alexander Williams
#None
#None


#Regex project
#-----------------
#Use python to read the file regex_test.txt and print 
# the last name on each line using regular expressions 
# and groups (return None for names with no first and 
# last name, or names that aren't properly capitalized)

import re
#^almost forgot this again.
with open ("regex_test.txt") as f:
    data = f.readlines()
#^ Pref opening learned in class
pattern = re.compile("([A-J][a-zA-W ]+)")
#                         ^this letter right here...smh
#OUT OF ALL THE PLACES TO GET THROWN OFF, IT WAS THE DANG J!
for person in data:
    match = pattern.search(person)
#used same for: as my in class exercise #3
    if match:
        print(match.group())
#went simple for my first try and worked.
    else:
        print(None)
#got this^ else: on my first remembering guess.

#Did not use:
#match = pattern.match(data)
#found = pattern.findall(data)
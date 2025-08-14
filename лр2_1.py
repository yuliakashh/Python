s="""орпр
catapult and cat
catcat
concat
dog cat
"cat"
!cat?"""
s=s.split('\n')
import re
for string in s:
    if re.findall(r"(\b(cat)$)",string):
        print (string)


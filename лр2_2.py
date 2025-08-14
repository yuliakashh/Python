import re
s="""I need to understand the humann mind
humanity"""
s=s.split("\n")
for string in s :
    print(re.sub(r"(human)","computer",string))

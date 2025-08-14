import re
s="""There’ll be no more "Aaaaaaaaaaaaaaa" aaaaa
AaAaAaA AaAaAaA"""
s=s.split('\n')
for string in s:
    print(re.sub(r"(a|A)+", "argh", string,count=1))

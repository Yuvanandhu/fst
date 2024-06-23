import re
string = "This is Regular Expression Example Program"
pattern = "[a-m]"
result = re.findall(pattern,string)
print(result)

import re
string = "Welcome To Computer Science and Computer Applications"
pattern = r"Computer$"
match = re.search(pattern,string)
if match :
    print("match found !")
else:
    print("match not found!")

import re
s = 'vel.murgan'
match = re.search(r'.',s)
print(match)
match = re.search(r'/.',s)
print (match) 

import re
match = re.search(r'Science','Govt.arts College:Department Of Computer Science')
print(match)
print(match.group())
print('Start Index :',match.start())
print('End Index :',match.start())
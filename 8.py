import re
string="this is regular expression example program "
pattern="[a-z]"
res=re.findall(pattern,string)
print(res)

import re
string="welcome to computer science and computer applicatons"
pattern=r"computer $"
match=re.search(pattern,string)
if match:
    print("match found !")
else:
    print("match not found.")
    
import re
s='COMPUTER.SCIENCE'
match=re.search(r'.',s)
print(match)
match=re.search(r'\.',s)
print(match)

import re 
match=re.search(r'science','govt.arts college :department of computer science')
print(match)
print(match.group())
print('start index:',match.start())
print('end index :',match.end())   
"""import re
hand=open('my_data.txt')
#ls=list()
num=0
for line in hand:
    #print(line)
    line=line.rstrip()
    y=re.findall('[0-9]+',line)
    #print(y)
    #z=int(y)
    for z in y:
        num= num+int(y)
        print(num)
    numlist.append(int(my_number))
print('Maximum:', my_number)"""

import re
fhand = open('my_data.txt')
num = 0
for line in fhand:
    line = line.strip()
    x = re.findall('[0-9]+',line)
    for values in x:
        num = num + int(values)
        print(num)
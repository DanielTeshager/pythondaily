#!/usr/bin/env python3
import random

#machine generates 4 digits number
machinenumber = list(str(random.randint(1000,9999)))

#machince converts the generated number to string and to list

#machine prompts users to put 4 digit number 

#define cowbull dicttionary
cowbull = {}
found = False
while found!=True:
    usernumber = list(input('type 4 digit number: >> '))
    for i in range(0,len(machinenumber)):
        if usernumber[i] == machinenumber[i]:
            cowbull['cow'] = cowbull.get('cow',0)+1
            cowbull['bull'] = cowbull.get('bull',0)+1
        elif usernumber[i] in machinenumber:
            cowbull['bull'] = cowbull.get('bull',0)+1
    if list(cowbull.values()) == [4,4]:
        found=True
        print("100% Sucess ",usernumber,machinenumber,sep=" ")
    else:
       print('currentcowbull: ',cowbull)
       #print('current machine number: ',machinenumber)
       cowbull.clear()


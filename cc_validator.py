#!/usr/bin/env python3
import re
import string
from itertools import groupby

cc = input().strip()
cclen = len(cc)
#maxlen = 19 assuming the creditard numbers are - separated
maxlen = 19
#minlen = 16
minlen = 16
if cclen not in [maxlen,minlen]:
    #print('Invalid Credit Card number: {}'.format(cc))
    print('Invalid')
else:
    #check availablity of invalid characters '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    #remove - and check isdigit and size
    validstrat = re.search(r'^[4-6]+',cc)
    #print('Valid Start ==>',validstrat[0])
    #math 16 digits
    validcount = re.findall(r'(?:[0-9]{4}-){3}[0-9]{4}$|[0-9]{16}$',cc)[0]
    #print('Valid Count ==>',validcount)
    if validstrat!=None:
        if len(validcount)==minlen:
            if int(max(len(list(g)) for _,g in groupby(cc))) >=4:
                print('Invlaid')
                #print('Invalid max consequtive number threshold passed')
            else:
                print('Valid')
        elif len(validcount)==maxlen:
            if max(len(list(g)) for _,g in groupby(re.sub(r'(-)','',cc)))>=4:
                print('Valided')
                #print('Invalid max consequitive number threshold passed')
            else:
                print('Valid')
        
        else:
            #print('Dashed cc is Invalid')
             print('Invalid')
    else:
        #print('Invalid CC number doesn\'t start with 4,5 or 6')
        print('Invalid')
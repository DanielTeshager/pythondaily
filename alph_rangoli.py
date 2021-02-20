#!/usr/bin/env python3
import string 
size = 3
myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    
for i in range(size-1, -size, -1):
    x = abs(i)
    line = myStr[size:x:-1]+myStr[x:size]
    print ("--"*x+ '-'.join(line)+"--"*x)



#size = 3
#mystr = 'abc'
#range(2,-3,-1) [2,1,0,-1,-2]
#abs(i) converts i to positive except when i == 0
#line first iteration
#'abc'[3:2:-1]+'abc'[2:3] ==> 'c"
#line second iteration
#'abc'[3:1:-1]

#!/usr/bin/env python3
if __name__ == '__main__':
    s = input()
alnum = len(list(filter(lambda x:x.isalnum(), s)))
alnum = True if alnum > 0 else False
anyalpha = len(list(filter(lambda x:x.isalpha(), s)))
anyalpha = True if anyalpha > 0 else False
anydigit = len(list(filter(lambda x:x.isdigit(), s)))
anydigit = True if anydigit > 0 else False
anylower = len(list(filter(lambda x: x.islower(), s)))
anylower = True if anylower > 0 else False
anyupper = len(list(filter(lambda x: x.isupper(), s)))
anyupper = True if anyupper > 0 else False

print(alnum,anyalpha,anydigit,anylower,anyupper,sep='\n')

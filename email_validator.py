#!/usr/bin/env python3
import re
def fun(s):
    # return True if s is a valid email, else return False
    #check if @ is available
    if s.count('@')==1:
        username,domain = tuple(s.split('@'))
        if (re.search(r'[^\w_-]',username)==None) & ('.' in domain) & len(username)>=2:
            dname, ext = tuple(domain.split('.'))
            if (dname.isalnum()) & (len(ext)<=3):
                return True
            else:
                return False
    else:
        return False     
            

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
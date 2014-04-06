#!/usr/bin/python
import praw
import re

#Todo: add exception handling

def parse_mgs(body):
    
    user = ''
    amount = 0
    
    find_user = re.search(r'/u/[^\s]+', body, re.IGNORECASE)

    if find_user:
        user = str(find_user.group())
        #print find_user.group()
    else:
        print'fail'

    find_amount = re.search(r'\xd0[^\s]+', body, re.IGNORECASE)

    if find_amount:
        amount = int(find_amount.group()[1:])
        #print find_amount.group()[1:]
    else:
        print'fail'
    
    return [user, amount]

#!/usr/bin/python
import praw
import finder
import ast
from pprint import pprint

username = open("username.txt", "r").read().rstrip()
password = open("password.txt", "r").read().rstrip()
pool = ast.literal_eval(open("pool.txt", "r").read().rstrip())

r = praw.Reddit(user_agent = '/u/dradding')
r.login(username, password)

def send_msg():
    r.send_message('dradding', 'testing', 'success')

def get_unread():
    inbox = r.get_inbox(limit = 1)
    #inbox = r.get_unread(limit = 1)
    for msg in inbox:
        msg = vars(msg)
        info = finder.parse_mgs(msg['body'])
        for ticket in range(info[1]):
            pool.append(info[0])
    f=open("pool.txt","w")
    f.write(pool)
    f.close()

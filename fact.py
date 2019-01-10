#!/usr/bin/env python3
from _thread import start_new_thread
threadId = 1

def factor(n):
    global threadId
    if n<1:
        print ("{}: {}".format("Нить", threadId))
        threadId += 1
        return 1
    else:
        returnNum = n * factor(n - 1)
        print(str(n) + '! = ' + str(returnNum))
        return returnNum

start_new_thread(factor, (5, ))
start_new_thread(factor, (4, ))

c = input("ЖДЁМ")
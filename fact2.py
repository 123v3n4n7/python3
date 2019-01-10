#!/usr/bin/env python3
import threading
import datetime

class myThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadId = counter
        self.name = name
        self.counter = counter

    def run(self):
        print("запуск " + self.name)
        print_date(self.name, self.counter)
        print("Выход " + self.name)

def print_date (thredName, counter):
    datafileds = []
    today = datetime.date.today()
    datafileds.append(today)
    print("{}[{}]: {}".format(thredName, counter, datafileds[0]))

Thread1 = myThread("Нить1", 1)
Thread2 = myThread("Нить2", 2)

Thread1.start()
Thread2.start()

Thread1.join()
Thread2.join()
print("Выход")
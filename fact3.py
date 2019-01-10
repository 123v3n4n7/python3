import threading
import datetime

exitFlag = 0
threadLock = threading.Lock()
threads = []


class myThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadId = counter
        self.name = name
        self.counter = counter

    def run(self):
        print ("Запуск " + self.name)
        threadLock.acquire()
        print_date(self.name, self.counter)
        threadLock.release()
        print ("Выход " + self.name)

def print_date(threadName, counter):
    datefields = []
    today = datetime.date.today()
    datefields.append(today)
    print("{}[{}]: {}".format(threadName, counter, datefields[0]))


thread1 = myThread("Нить", 1)
thread2 = myThread("Нить", 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
print("Выход")
import os
from urllib.request import urlopen
import requests
from threading import Thread
from queue import Queue

class DownloadThread(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            url = self.queue.get()
            self.download_file(url)
            self.queue.task_done()

    def download_file(self, url):
        handle = urlopen(url)
        fname = os.path.basename(url)

        with open(fname, 'wb') as f:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f.write(chunk)

def main(urls):

    queue = Queue()

    for i in range(5):


    for item, url in enumerate(urls):
        name = "Поток {}".format(item+1)
        thread = DownloadThread(url, name)
        thread.start()


if __name__ == "__main__":
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]

    main(urls)
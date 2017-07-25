"""

multi_threading_se.py is used to fasten the process of saving images from the extracted links. Later it
can be used for other purpose also.

"""
import queue
import threading
import urllib.request
import os


def multi_threading_se(t_links):
    def do_work(thread_name, url):
        images_dir = os.path.join(os.getcwd(), 'Images')
        urllib.request.urlretrieve(url, (os.path.join(images_dir, url[-6:])))
        print(thread_name + ' is now saving ' + url[-10:])

    def worker():
        while True:
            item = q.get()
            if item is None:
                break
            do_work(threading.current_thread().name, item)
            q.task_done()

    q = queue.Queue()
    threads = []
    for i in range(8):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for item in t_links:
        q.put(item)

    # block until all tasks are done
    q.join()

    # stop workers
    for i in range(8):
        q.put(None)

    for t in threads:
        t.join()

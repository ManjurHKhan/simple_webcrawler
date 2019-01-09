__project__ = "Basic Webcrawler"

import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

# PROJECT_NAME = 'thenewboston'
# HOMEPAGE = 'https://thenewboston.com/'
# HOMEPAGE = 'https://www.youtube.com/user/thenewboston'
HOMEPAGE = input("What page do you want to crawl?\n")
if HOMEPAGE == '':
    exit()
PROJECT_NAME = DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + 'crawled.txt'
NUMBER_OF_THREADS = 100

queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print("links in the queue -- %d" % (len(queued_links)))
        create_jobs()

create_workers()
crawl()
from __future__ import print_function
import subprocess
import threading
from queue import Queue
from queue import Empty

def call_ping(ip):
    #if subprocess.call(["ping", "-c", "1", ip]):
    if subprocess.call("ping -c 1 -w 1 %s" % ip,shell = True,stdout = open('/dev/null','w'))==0:
        print("{0} is alive".format(ip))
    else:
        print("{0} is unreacheable".format(ip))

def is_reacheable(q):
    try:
        while True:
            ip = q.get_nowait()
            call_ping(ip)
    except Empty:
        pass

def main():
    q = Queue()
    with open('ips.txt') as f:
        for line in f:
            line = line.strip()  
            q.put(line)

    threads = []
    for i in range(10):
        thr = threading.Thread(target=is_reacheable, args=(q,))
        thr.start()
        threads.append(thr)

    for thr in threads:
        thr.join()

if __name__ == '__main__':
    main()


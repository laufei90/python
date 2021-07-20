from __future__ import print_function
import subprocess
import threading

def is_reacheable(ip):
    #if subprocess.call(["ping", "-c", "1","-w","1",ip])==0:
    if subprocess.call("ping -c 1 -w 1 %s" % ip,shell = True,stdout = open('/dev/null','w'))==0:
        print("{0} is alive".format(ip))
    else:
        print("{0} is unreacheable".format(ip))

def main():
    fo = open("ips.txt", "r")        
    threads = []
    for line in fo.readlines():
        line = line.strip()  
        thr = threading.Thread(target=is_reacheable, args=(line,))
        thr.start()
        threads.append(thr)

    for thr in threads:
        thr.join()

if __name__ == '__main__':
    main()

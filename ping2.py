from __future__ import print_function
import subprocess
import threading
 
def is_reachable(ip):
  if subprocess.call(["ping", "-c", "2", ip])==0:#只发送两个ECHO_REQUEST包
    print("{0} is alive.".format(ip))
  else:
    print("{0} is unalive".format(ip))
if __name__ == "__main__":
  ips = ["www.baidu.com","192.168.0.1"]
  threads = []
  for ip in ips:
    thr = threading.Thread(target=is_reachable, args=(ip,))#参数必须为tuple形式
    thr.start()#启动
    threads.append(thr)
  for thr in threads:
    thr.join()

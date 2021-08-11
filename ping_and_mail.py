
import subprocess
import yagmail
import time

tv_ip="192.168.15.185"
is_on_watching=0
start_time=int(time.time())
on_time=int(time.time())
end_time=int(time.time())
log_file="/home/ubuntu/log/tv.log"

def write_log(str):
    with open(log_file,"a") as f:
        f.write(str+"\n")


def to_mail(content_str): 
    yag = yagmail.SMTP(user="***@163.com", password="****", host='smtp.163.com')
    subject = "看电视提醒"
    contents = content_str
    email_name = "niufee@qq.com"
    yag.send(email_name, subject, contents)
    yag.close()

while True :
    if subprocess.call("ping -c 1 -w 1 %s" % tv_ip,shell = True,stdout = open('/dev/null','w'))==0:
        #alived
        if  is_on_watching == 0 :
            start_time=int(time.time())
            write_log("开始看电视时间：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))))
        else :
            on_time=int(time.time())

        is_on_watching=1
    
    else:
         #unreacheable
        if  is_on_watching == 1 :
            end_time=int(time.time())
            write_log("停止看电视时间：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))))

        is_on_watching=0
         
    cal_watch_time=on_time-start_time
    #print("看电视时间：{}s".format(cal_watch_time))
    if cal_watch_time >= 3600 :
       to_mail("你家的娃看电视超过一个小时了,开始时间:{}.".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))))
    
    time.sleep(60)




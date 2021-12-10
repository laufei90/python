from win10toast import ToastNotifier
import win32api
import win32con
import time
# toast通知
def time_toast(head,content):
    toaster = ToastNotifier()
    toaster.show_toast(head,content,duration=4)
# 获取Caps Lock键状态
def get_Caps_Lock_status():
    return win32api.GetKeyState(win32con.VK_CAPITAL) 
# 获取Num Lock键状态
def get_Num_Lock_status():
    return win32api.GetKeyState(win32con.VK_NUMLOCK) 

time_list=["06:00:00","08:40:00","10:00:00","12:00:00","14:00:00","16:00:00","17:30:00","20:00:00","22:00:00","24:00:00"]
Caps_Lock_status=get_Caps_Lock_status()
Num_Lock_status=get_Num_Lock_status()
while True:
    time.sleep(0.5)
    now_Caps_Lock_status=get_Caps_Lock_status()
    if now_Caps_Lock_status != Caps_Lock_status:
        if now_Caps_Lock_status == 1:
            time_toast("Caps_Lock_status","开启大写模式!")
        else:
            time_toast("Caps_Lock_status","关闭大写模式!")
        Caps_Lock_status=now_Caps_Lock_status
    
    now_Num_Lock_status=get_Num_Lock_status()
    if now_Num_Lock_status != Num_Lock_status:
        if now_Num_Lock_status == 1:
            time_toast("Num_Lock_status","开启数字键盘!")
        else:
            time_toast("Num_Lock_status","关闭数字键盘!")
        Num_Lock_status=now_Num_Lock_status
           
    mark_time=time.strftime("%H:%M:%S", time.localtime())
    if mark_time in time_list:
        time_toast("休息提醒","您需要休息片刻啦!")
    
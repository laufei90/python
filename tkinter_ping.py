import subprocess
from tkinter import *
from tkinter import scrolledtext

cmd="ping -n 1 -w 1 192.168.15.185"
def ping_clicked():
    result = subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True)
    result.wait()
    txt.insert(INSERT, result.stdout.read().decode("gbk").strip()+'\r\n')
    txt.insert(INSERT,"------------------------------------------------------\r\n")
    
window = Tk()
window.title("Ping with Tkinter")
window.geometry("540x300")
txt = scrolledtext.ScrolledText(window, width=60, height=20)
txt.grid(column=0, row=0)
btn = Button(window, text="Start Ping", command=ping_clicked,bg="orange", fg="red")
btn.grid(column=1, row=0)
window.mainloop()
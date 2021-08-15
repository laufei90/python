import subprocess
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import platform

ping31="ping -n 1 -w 1 192.168.31.31"
yourIP="ipconfig"
sys_info=platform.platform()
process32="ssh 192.168.31.32 'ps -ef | grep recording'"
audiotest33="ssh 192.168.31.32 './audiotest'"

def fun_clicked(str):
    result = subprocess.Popen(str, stdout=subprocess.PIPE,shell=True)
    result.wait()
    txt.insert(INSERT, result.stdout.read().decode("gbk").strip()+'\r\n')
    txt.insert(INSERT,"------------------------------------------------------\r\n")

def fun_print(str):
    result=str.strip()
    txt.insert(INSERT, result+'\r\n')
    txt.insert(INSERT,"------------------------------------------------------\r\n")
    pass

def quit():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

window = Tk()
logo = PhotoImage(file='iconbitmap.gif')
window.call('wm', 'iconphoto', window._w, logo)
window.title("Ping with Tkinter")
window.geometry("700x400")
txt = scrolledtext.ScrolledText(window, width=80, height=30)
txt.grid(column=0, row=0,rowspan=6, padx=5, pady=5)
btn = Button(window, text="Ping 31.31", command=lambda:fun_clicked(ping31),bg="orange", fg="green",width=13,height=2)
btn.grid(column=1, row=0)
btn = Button(window, text="Your IP", command=lambda:fun_clicked(yourIP),bg="orange", fg="green",width=13,height=2)
btn.grid(column=1, row=1)
btn = Button(window, text="Sys info", command=lambda:fun_print(sys_info),bg="orange", fg="green",width=13,height=2)
btn.grid(column=1, row=2)
btn = Button(window, text="Process 31.32", command=lambda:fun_clicked(process32),bg="orange", fg="green",width=13,height=2)
btn.grid(column=1, row=3)
btn = Button(window, text="Audiotest 31.32", command=lambda:fun_clicked(audiotest33),bg="orange", fg="green",width=13,height=2)
btn.grid(column=1, row=4)

btn_quit = Button(window, text="Quit", command=quit,bg="orange", fg="red",width=13,height=2)
btn_quit.grid(column=1, row=5)
window.mainloop()
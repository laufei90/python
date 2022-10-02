import time
from tkinter import Tk,Label

class TimeShow():#实现倒计时
    
    def __init__(self,time_show=5):
        self.timeShowWin=Tk()
        self.timeShowWin.overrideredirect(True)
        self.timeShowWin.attributes('-alpha',1)
        self.timeShowWin.attributes('-topmost',True)
        self.timeShowWin.attributes('-transparentcolor','black')   
        self.time_show = time_show
        self.time_label=Label(self.timeShowWin,text='计时:{:02}分{:02}秒'.format(self.time_show // 60 ,self.time_show % 60),font=('楷体',80),fg='red',bg='black')
        self.time_label.pack(fill='x',anchor='center')
        #第1个加号是距离屏幕左边的宽，第2个加号是距离屏幕顶部的高。
        self.timeShowWin.geometry('+'+str(int(self.timeShowWin.winfo_screenwidth()/2))+'+'+str(120))
        self.timeShowWin.after(1,self.show)

    def show(self):
        while self.time_show >= 0:
            #print('time_label={}'.format(self.time_label))
            self.time_label['text']= '计时:{:02}分{:02}秒'.format(self.time_show // 60 ,self.time_show % 60)
            self.timeShowWin.update()
            self.time_show -= 1
            time.sleep(1)
        self.timeShowWin.destroy()
    
    def start(self):
        #print('ok')
        self.timeShowWin.mainloop()
        

if __name__ == '__main__':
    a=TimeShow(30)
    a.start()

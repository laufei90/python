
from landscape.lib.sysstats import MemoryStats

class Memory():
    def __init__(self):
        memstats = MemoryStats("/proc/meminfo")
        self.Memory_usage=memstats.used_memory_percentage
        self.Swap_usage=memstats.used_swap_percentage
    def memory_message(self):
        return self.Memory_usage
    def swap_message(self):
        return self.Swap_usage

class Memory_format(Memory):
    def __init__(self):
        print("重新定义构造函数，并继承父类的构造函数，按格式打印")
        #Memory.__init__(self)
        super(Memory_format,self).__init__()
    def memory_message(self):
        return "Memory usage:%d%%" % self.Memory_usage
    def swap_message(self):
        return "Swap usage:%d%%" % self.Swap_usage

class Memory_check(Memory):
    
    def memory_check(self):
        if self.Memory_usage < 80:
           return "Memory_usage is normal"
        else:
           return "Memory_usage is more than 80%"
    def swap_check(self):
        if self.Swap_usage < 80:
           return "Swap_usage is normal"
        else:
           return "Swap_usage is more than 80%"

class status(Memory_format,Memory_check):
    def all_status(self):
        print(self.memory_message(),self.memory_check(),sep=',')
        print(self.swap_message(),self.swap_check(),sep=',')

mem=status()
mem.all_status()



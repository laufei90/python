import psutil

def memissue():
    print('内存信息：')
    mem = psutil.virtual_memory()
    # 单位换算为 MB
    memtotal = mem.total / 1024 / 1024
    memused = mem.used / 1024 / 1024
    membaifen = memused / memtotal * 100
    print('内存使用量：%.2fMB' % memused)
    print('内存总量：%.2fMB' % memtotal)
    print('内存百分比：%.2f' % membaifen)

def cuplist():
    print('磁盘信息：')
    #disk = psutil.disk_partitions()
    diskuse = psutil.disk_usage('/')
    # 单位换算为 GB
    diskused = diskuse.used / 1024 / 1024 / 1024
    disktotal = diskuse.total / 1024 / 1024 / 1024
    diskbaifen = diskused / disktotal * 100
    print('磁盘使用量：%.2fGB' % diskused)
    print('磁盘总量：%.2fGB' % disktotal)
    print('磁盘百分比：%.2f' % diskbaifen)

if __name__ == '__main__':    
    print('*******************')
    memissue()
    cuplist()


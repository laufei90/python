#!/usr/bin/python
#-*- coding: UTF-8 -*-
import os
import fnmatch
import time

def is_file_match(filename, patterns):
    for pattern in patterns:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False

def find_specific_files(dirpath, patterns=['*'], exclude_dirs=[]):
    for dirpath, dirnames, filenames in os.walk(dirpath):
        for filename in filenames:
            if is_file_match(filename, patterns):
                yield os.path.join(dirpath, filename)

        for d in exclude_dirs:
            if d in dirnames:
                dirnames.remove(d)

if __name__ == '__main__':
    patterns=['*.html','*.txt','*.py']
    exclude_dirs=['mk']
    print("-----------匹配的所有文件--------------")
    all_specific_files=find_specific_files(".",patterns,exclude_dirs)
    for item in all_specific_files:
        print(item)

    print("-----------删除过期15天文件----------------")
    all_specific_files=find_specific_files(".",patterns,exclude_dirs)
    for item in all_specific_files:
        expiry_days=time.time()-os.path.getmtime(item)
        if expiry_days > 15*86400:
           os.remove(item)
           print(item ,",15 days expired files")

    print("-----------最大的4个文件----------------")
    size_specific_files=find_specific_files(".",patterns,exclude_dirs)
    size_files={name:os.path.getsize(name) for name in size_specific_files}
    size_result=sorted(size_files.items(),key=lambda d:d[1],reverse=True)[:4]
    for i,t in enumerate(size_result,1):
        print(i,t[0],t[1])

    print("-----------最老的4个文件----------------")
    time_specific_files=find_specific_files(".",patterns,exclude_dirs)
    time_files={name:os.path.getmtime(name) for name in time_specific_files}
    time_result=sorted(time_files.items(),key=lambda d:d[1])[:4]
    for i,t in enumerate(time_result,1):
        print(i,t[0],t[1])

    print("-----------删除特定的文件----------------")
    del_specific_files=find_specific_files(".",patterns=['*.php'],exclude_dirs=['mk'])
    for name in del_specific_files:
        os.remove(name)
        print(name ,",deleted")
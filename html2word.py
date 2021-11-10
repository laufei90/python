#!/usr/bin/python
#-*- coding: UTF-8 -*-
import os
import fnmatch
import shutil
import pypandoc as ppd

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
    target_dir="简书保存2021-11-11"
    print("---------目标目录备份为***_bak---------")
    shutil.copytree(target_dir,target_dir+"_bak")
    patterns=['*.html']
    exclude_dirs=['']
    print("-----------匹配的所有文件--------------")
    all_specific_files=find_specific_files(target_dir,patterns,exclude_dirs)
    print("-------转换html文件为docx文件-----------")
    for item in all_specific_files:
        #print(item)
        short_name=os.path.splitext(item)[0]
        print("--转换html2word中：",item,"-----------")
        ppd.convert_file(item,'docx',outputfile=short_name+".docx")

    print("-----------删除原html文件---------------")
    del_specific_files=find_specific_files(".",patterns,exclude_dirs)
    for name in del_specific_files:
        os.remove(name)
        #print(name ,",deleted")
    

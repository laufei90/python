#!/usr/bin/python
#-*- coding: UTF-8 -*-
import os
import re
import fnmatch
import wordcloud
from html2text import html2text
import matplotlib.pyplot as plt

#删除字符
def detele_character(text):
    temp_delete_english = re.sub('[a-zA-Z]','',text)
    temp_delete_digit = re.sub('[\d]','',temp_delete_english)
    temp=temp_delete_digit
    return temp

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

def search_words_in_files(all_files):
    all_words=""
    for item in all_files:
        with open(item, 'r', encoding='utf-8') as f:
            lines=f.readlines()
        html_words=""
        for line in lines:
            if not line.strip().startswith("<img"):
                html_words = html_words + line
        text_words=html2text(html_words)
        #print("-----------完成读取文件："+ item)
        all_words = all_words + text_words
    return all_words

if __name__ == '__main__':
    patterns=['*.html']
    #exclude_dirs=['mk']
    delwords = {"使用","比如","和","文件","或者","运行","可以使用","同时","模拟实验", \
        "通过","测试","安装","但是","目录","需要注意的是"
        }
    print("-----------匹配所有html文件--------------")
    all_specific_files=find_specific_files(".",patterns)
    print("---------从文件中提取出所有文本------------")
    all_words = search_words_in_files(all_specific_files)
    delete_all_words = detele_character(all_words)
    print("--------------生成词云图-----------------")
    w = wordcloud.WordCloud(font_path = "msyh.ttc",\
                           width = 1000,height = 700 ,background_color = "white",\
                        stopwords = delwords , max_words = 50)
    w.generate(delete_all_words)
    print("-----写入到my_jianshu_report.png---------")
    w.to_file("my_jianshu_report.png")


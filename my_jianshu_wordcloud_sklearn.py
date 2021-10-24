#!/usr/bin/python
#-*- coding: UTF-8 -*-
from operator import lshift
import os
import re
import fnmatch
from html2text import html2text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

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
    all_words=[]
    for item in all_files:
        with open(item, 'r', encoding='utf-8') as f:
            lines=f.readlines()
        html_words=""
        for line in lines:
            if not line.strip().startswith("<img"):
                html_words = html_words + line
        text_words=html2text(html_words)
        delete_text_words=detele_character(text_words)
        #print("-----------完成读取文件："+ item)
        all_words.append(delete_text_words)
    return all_words

if __name__ == '__main__':
    patterns=['*.html']
    #exclude_dirs=['mk']
    delwords = {"__"}
    print("-----------匹配所有html文件--------------")
    all_specific_files=find_specific_files(".",patterns)
    print("---------从文件中提取出所有文本------------")
    list_all_words = search_words_in_files(all_specific_files)
    #print(delete_all_words)
    print("-------sklearn KMeans机器学习分类---------")
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(list_all_words)
    K = 3
    model = KMeans(n_clusters=K, init='k-means++', max_iter=100, n_init=1)
    model.fit(X)
    print("---------打印类群的前十个词语------------")
    print("Top terms per cluster:")
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    #print(order_centroids)
    terms = vectorizer.get_feature_names()
    for i in range(K):
        print("Cluster %d:" % i),
        for ind in order_centroids[i, :10]:
            print(ind, terms[ind]),
        print("\n")


# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:21:15 2017

@author: Administrator
"""

import urllib2
import urllib
import re
import itertools
from string import maketrans
import string
import requests
import os
import time


user_agent = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent}

def buildUrls(word):
    word = urllib.quote(word)
    url = r'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&word={word}&face=&istype=&qc=&nc=1&fr=&pn={pn}&rn=60'
    urls = (url.format(word=word,pn=x) for x in itertools.count(start=0,step=60))
    return urls

str_table = {
'_z2C$q': ':',
'_z&e3B': '.',
'AzdH3F': '/'
}


char_table = maketrans('wkv1ju2it3hs4g5rq6fp7eo8dn9cm0bla','abcdefghijklmnopqrstuvw1234567890')

def decode(url):
    for key ,value in str_table.items():
        url = url.replace(key,value)
    return url.translate(char_table)
pattern = re.compile('"objURL":"(.*?)"')


word = raw_input('请输入要检查的关键词：\n'.decode('utf-8').encode('gbk'))
word = word.decode('gbk').encode('utf-8')
path = 'D:\\test\\'
fold = path + raw_input('请输入目录名（英文）：\n'.decode('utf-8').encode('gbk'))
if not os.path.exists(fold):
    os.mkdir(fold)
path_a = fold +'\\'
n = 1
url_box = buildUrls(word)
for i in url_box:
    req = urllib2.Request(i,headers = headers)
    url_jpg = pattern.findall(urllib2.urlopen(req).read())
    print len(url_jpg)
    if len(url_jpg) == 0:
        
        break
    for j in url_jpg:
        url_new = decode(j)
        filename = path_a + string.zfill(n,5) + '.jpg'
        n += 1
        print '请求链接：' + url_new
        try :
            req = requests.get(url_new,timeout = 2)
            if req.status_code != requests.codes.ok:
                print '-------------'
                print '请求不成功' + url_new
                continue
        except:
            continue
        with open(filename,'wb') as f:
            f.write(req.content)
            f.close()
            time.sleep(0.1)
            print '成功下载：' + url_new + '命名为：' + filename 
                

        
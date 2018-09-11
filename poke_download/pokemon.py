# coding=utf-8
import sys
import re
import urllib2
from bs4 import BeautifulSoup

def OpenPage(url):
    #需要有请求头
    Myheaders = {}
    #构造request请求
    #第一个参数是url 第二个参数是请求头
    #返回值是一个request请求对象
    req = urllib2.Request(url,headers=Myheaders)
    #激活请求，获取响应
    f = urllib2.urlopen(req)
    data = f.read()
    #decode() encode()
    #ignore replace xml...replace
    #print data
    return data

def ParseMainPage(page):
    soup = BeautifulSoup(page,"html.parser")
    GetList = soup.find_all(ep_id=True)
    UrlList = []
    print GetList
    for item in GetList:
        print item
    return UrlList

def TEST():
    page = OpenPage("https://www.bilibili.com/bangumi/media/md5707")
    # page = 'duration":1490328,"ep_id":100704,"episode_status"'
    url_list = re.findall('"ep_id":[0-9]*',page)
    url_list = ["https://www.bilibili.com/bangumi/play/ep"+value[8:] for value in url_list]
    for line in url_list:
        print line
TEST()



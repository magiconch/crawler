#!/usr/bin/python
#coding:utf-8
'''
用BeautifulSoup4 爬虫库爬取汤老师心爱的小说
'''
import urllib2
import re
from bs4 import BeautifulSoup
#需要的资源

#urllib2 进行url请求
#根据Url获取对应服务器端的响应
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
    return data.decode("GBK",errors="ignore").encode("utf-8")

def Test1():
    url = "http://www.shengxu6.com/book/2967.html"
    print OpenPage(url)

#import urllib2
#print type(urllib2)
#从主页获取各个章节的url
def ParseMainPage(page):
    #html.parser Python自带的标准html解析引擎
    #格式化html文件内容,bs4 内部类 的实例化
    soup = BeautifulSoup(page,"html.parser")
    
    #re.compile href="read" a标签
    #在soup类中，查找全部符合条件的标签
    #soup.find_all("a")
    #re.compile("read")
    GetList = soup.find_all(href=re.compile("read"))
    #print GetList[0]["href"]
    #获取到了所有符合条件的a标签
    UrlList = []
    for item in GetList:
        UrlList.append("http://www.shengxu6.com" + item["href"])   
    return UrlList


def Test2():
    url = "http://www.shengxu6.com/book/2967.html"
    page = OpenPage(url) 
    GetResult = ParseMainPage(page)

    print type(GetResult)

#获取章节内容 提取标题和正文
def ParseDetailPage(page):

    soup = BeautifulSoup(page,"html.parser")
    #返回查找列表，里面的每个元素都是一个标签类
    Title = soup.find_all(class_="panel-heading")[0].get_text()
    #获取标签包含的正文 get_text()
    Content = soup.find_all(class_="content-body")[0].get_text()
     
    return Title,Content

def Test3():
    url = "http://www.shengxu6.com/read/2967_2008175.html"
    page = OpenPage(url)
    x = ParseDetailPage(page)
    print x

#最后一步 把获取到的内容保存进txt文件里
def WriteDataToFile(data):
    with open("output.txt","a+") as f:
        f.write(data)

def Test4():
    WriteDataToFile("11234567890")

#串联所有的步骤，实现完整的爬虫项目
if __name__ == "__main__":
    url = raw_input("请输入要爬取的小说网址:")
    #url = "http://www.shengxu6.com/book/2967.html"
    #获取首页响应内容
    Main = OpenPage(url)
    #解析首页内容，得到各个章节的网址列表
    UrlList = ParseMainPage(Main)
    print "Clone Begin..."
    for item in UrlList:
        print "Clone:" + item
        #遍历各个章节的url,获取各个章节的响应内容
        detail = OpenPage(item)
        #解析各章节，获取标题和正文
        Title,Content = ParseDetailPage(detail)
        #此处会出现编码错误
        data = "\n\n" + Title + "\n\n" + Content
        WriteDataToFile(data.encode("utf-8"))
    print "Clone done"




   
   

 



#!/usr/binn/python
# coding:utf-8
'''
爬取小说并下载
'''
import urllib2
import re
import sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding("utf-8")
# 构造请求头

def OpenPage(url):
	myhead = {}
	req = urllib2.Request(url, headers=myhead)
	f = urllib2.urlopen(req)
	data = f.read()
	return data.decode("GBK", errors="ignore").encode("utf-8")

def ParseMainPage(page, novel_main_url):
	soup = BeautifulSoup(page,"html.parser")
	GetList = soup.find_all(href=re.compile(".html"))
	#这里只需要链接
	UrlList = []
	for item in GetList:
		UrlList.append(novel_main_url + item["href"])
	if UrlList[-1] == (novel_main_url + "index.html"):
		del UrlList[-1]
	return UrlList

def ParseDetailPage(page):

	soup = BeautifulSoup(page,"html.parser")
	Title = soup.find_all(id="title")[0].get_text()
	Content = soup.find_all(id=re.compile("content"))[0].get_text()
	return Title, Content

def WriteDataToFile(data, query):
    with open(query, 'a+') as f:
        f.write(data)

def GetUrl(query):
    # TODO
    pass

if __name__ == "__main__":
    # query = raw_input("请输入要下载的小说书名：")
    # url = GetUrl(query)
    url = raw_input("请输入要下载的小说地址")
    query = raw_input("请输入下载后文件名")
    page = OpenPage(url)
    url_list = ParseMainPage(page)
    print "Download Begin"
    for chapter_url in url_list:
        chapter_page = OpenPage(chapter_url)
        title, content = ParseMainPage(page)
        print title
        data = "\n\n" + title + "\n\n" + content
        WriteDataToFile(data.encode("utf-8"), query)
    print "Download End"


#!/usr/binn/python
#coding:utf-8
'''
爬取难道我是神
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
	req = urllib2.Request(url,headers=myhead)
	f = urllib2.urlopen(req)
	data = f.read()
	return data.decode("GBK",errors="ignore").encode("utf-8")

def ParseMainPage(page):
	soup = BeautifulSoup(page,"html.parser")
	GetList = soup.find_all(href=re.compile(".html"))
	#这里只需要链接
	UrlList = []
	for item in GetList:
		UrlList.append("http://www.dajiadu.net/files/article/html/34/34749/" + item["href"])
	if UrlList[-1] == "http://www.dajiadu.net/files/article/html/34/34749/index.html":
		del UrlList[-1]
	return UrlList

def ParseDetailPage(page):

	soup = BeautifulSoup(page,"html.parser")
	Title = soup.find_all(id="title")[0].get_text()
	Content = soup.find_all(id=re.compile("content"))[0].get_text()
	return Title,Content
def WriteDataToFile(data):
	with open('难道我是神','a+') as f:
		f.write(data)


def main():
	url = "http://www.dajiadu.net/files/article/html/34/34749/index.html"
	page = OpenPage(url)
	urllist =  ParseMainPage(page)
	print "clone do"
	for url in urllist:
		page = OpenPage(url)
		title,content = ParseDetailPage(page)
		print title
		data = "\n\n" + title + "\n\n" + content
		WriteDataToFile(data.encode("utf-8"))
	print "done"

#main()
def TEXT():
	url = "http://www.dajiadu.net/files/article/html/34/34749/index.html"
	page = OpenPage(url)
	urllist = ParseMainPage(page)
	for url in urllist:
		print url


TEXT()

#main()



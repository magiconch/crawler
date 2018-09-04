#coding=utf-8
'''
爬取百度文库
'''
import urllib2
import re
import sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding("utf-8")

def OpenPage(url):
	myhead = {}
	req = urllib2.Request(url,headers=myhead)
	f = urllib2.urlopen(req)
	data = f.read()
	return data.decode("GBK").encode("utf-8")

def ParseDetailPage(page):
	soup = BeautifulSoup(page,"html.parser")
	Content = soup.find_all(class_=re.compile("reader-word-layer reader-word-s1-10"))[0].get_text()
	print Content
page = OpenPage("https://wenku.baidu.com/view/baf190e30875f46527d3240c844769eae009a325.html")
#f = open("wenku")
#page = f.read()
print page
ParseDetailPage(page)

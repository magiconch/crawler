#coding=utf-8
import re
import urllib2
import sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding("utf-8")
head_url = 'http://adnmb1.com'
#获取网址
def OpenPage(url):
	myhead = {}
	req = urllib2.Request(url,headers=myhead)
	f= urllib2.urlopen(req)
	data = f.read()
	return data

#获取所有版块的URL
def ParseMainPage(page):
	soup = BeautifulSoup(page,"html.parser")
	GetList = soup.find_all(href=re.compile("/f/"))
	UrlList = []
	for item in GetList:
		UrlList.append("http://adnmb1.com/"+ item["href"])
	del UrlList[0]
	return UrlList

#获取当前版块内所有的串信息
def ParseBoardPage():
	pass
#获取串内容
'''
需要获取的内容包括 po主留言，用户留言，用户id，poid
用字典储存，这里的po主留言编号就是url
'''
def ParseDetailPage(page):
    #reply_content = soup.find_all(class_=re.compile("")
    soup = BeautifulSoup(page,"html.parser")
	#for item in head_content:
	#	print item.get_text()
    '''
    在这里需要考虑到有的串可能有多个页面，所以在这里获取每个页面的URL
    这里的pages_list是处理前包含上页，下页，空行的列表
    这里只需要有页码的列表，需要过滤掉其他信息
    pages_url是HTML格式的url列表，需要使用正则表达式处理成可直接使用的url
    '''
    pages_list = soup.find_all(class_=re.compile("uk-pagination uk-pagination-left h-pagination"))[0]
    pages_tag = []
    for child in pages_list.children:
        print type(child)
        if type(pages_list) is type(child):
            pages_tag.append(child)
    pages_url = []

    for index in range(1,len(pages_tag)-1):
        pages_url.append(str((pages_tag[index]).contents[0]))

    for index in range(len(pages_url)):
        pages_url[index] = ''.join(re.findall(r'href="(.*)"', pages_url[index]))
    print pages_url
    head_id = soup.find_all(class_=re.compile("h-threads-info-id"))[0].get_text()
    head_content = []
    for url in pages_url:
        page = OpenPage(head_url+url)
        soup = BeautifulSoup(page,"html.parser")
        head_content =head_content + soup.find_all(class_=re.compile("h-threads-content"))
    head_content = list(set(head_content))
    return [str(value) for value in head_content] , head_id

def TEST():
	page = OpenPage("http://adnmb1.com")
	print ParseMainPage(page)

def TEST2():
	page = OpenPage("http://adnmb1.com/t/14937269")
	ParseDetailPage(page)
TEST2()

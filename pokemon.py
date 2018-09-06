# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome("/usr/bin/chromedriver")     # 打开 Chrome 浏览器

# 将刚刚复制的帖在这
driver.get("https://www.bilibili.com/bangumi/media/md5707/?from=search&seid=16694422454236132120")
driver.find_element_by_class_name("misl-ep-item simple").click()

# 得到网页 html, 还能截图
# current_url
print driver
print driver.current_url()
html = driver.page_source

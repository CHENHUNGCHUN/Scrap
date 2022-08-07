# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:54:28 2019

@author: UserPc
"""

from selenium import webdriver
import selenium
import time
from bs4 import BeautifulSoup
import requests
import re
import codecs
import csv


gg,dd = eval(input('请输入页面滚动次数和查询的日期(范例：2,"2019-01-01")\n:'))
title=[]
contant=[]
time_=[]
http=[]
#华尔街见闻
browser = webdriver.Chrome()
browser.get('https://wallstreetcn.com/news/global?from=home')
#browser.minimize_window() 
print('华尔街见闻')
time.sleep(10)

for i in range(gg):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    print('等2秒')
    time.sleep(2)

soup = BeautifulSoup(browser.page_source,'html.parser')
divs = soup.find('div',class_='article-list').find_all('div',class_='article-entry list-item')
browser.close()

#金石
browser1 = webdriver.Chrome()
browser1.get('https://xnews.jin10.com/#/')
#browser1.minimize_window() 
print('金石数据')
time.sleep(10)

for i in range(gg):
    browser1.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    print('等2秒')
    time.sleep(2)
    
soup1 = BeautifulSoup(browser1.page_source,'html.parser')
divs1 = soup1.find('ul',class_='newsList').find_all('li',class_='news-item')
browser1.close()
#资料整理
#华尔街见闻

for i in range(len(divs)):
    title.append(divs[i].find('span').text)
    contant.append(divs[i].find('div',class_='content').text)
    time_.append(divs[i].find('time')['datetime'][0:10])
    http.append('https://wallstreetcn.com'+divs[i].find('a')['href'])
#金石数据

for i in range(len(divs1)):
    title.append(divs1[i].find('div',class_='news-i-title').text.strip('\n '))
    time_.append(divs1[i].find('ul',class_='news-i-other clear').find('span').text[0:10])
    if re.search('^//xnews.jin10.com',divs1[i].a['href']) != None:
        http.append('https:'+divs1[i].a['href'])
    else:
        http.append(divs1[i].a['href'])


key_words=['.*美联储.*','.*美国.*','.*欧洲.*','.*美元.*','.*黄金.*','.*瑞郎.*','.*瑞士.*'\
           ,'.*欧元.*','.*央行.*','.*鲍威尔.*','.*首相.*','.*特朗普.*','.*升息.*'\
           ,'.*降息.*','.*华尔街.*','.*欧元区.*','.*债.*','.*油.*','.*利率.*','.*倒挂.*'\
           ,'.*英国.*','.*德国.*','.*德拉吉.*','.*议息.*']
old=[] #记忆之前的
a=['TIME',dd] #时间
with open('wallstreet.csv','r',encoding='utf_8_sig') as file2:
    csvReader = csv.reader(file2)
    for i in csvReader:
        old.append(i)

with open('wallstreet.csv','w',encoding='utf_8_sig',newline='') as file:
    csvWriter = csv.writer(file)
    csvWriter.writerow(a)
    for i in range(len(title)):
            for j in key_words:
                if time_[i] == dd:
                    if re.search(j,title[i]) != None:
                        print(title[i])
                        csvWriter.writerow(['***標題***',title[i]])
                        print(time_[i])
                        print(http[i])
                        csvWriter.writerow(['網址',http[i]])
                        break
    for j in old:
        csvWriter.writerow(j)
print('寫入完成')
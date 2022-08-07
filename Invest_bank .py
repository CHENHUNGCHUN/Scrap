# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:05:36 2019

@author: UserPc
"""
import time
import csv
from bs4 import BeautifulSoup
import requests
import selenium
from selenium import webdriver
import codecs
import gspread
from oauth2client.service_account import ServiceAccountCredentials 

browser = webdriver.Chrome()
browser.get('https://datacenter.jin10.com/banks_orders')
a = browser.find_element_by_xpath("//*[@type='checkbox']")
a.click()
print('wait 10 sec')
time.sleep(10)
soup = BeautifulSoup(browser.page_source,'html.parser')
row = soup.find('ul',class_='banks-list clearfixed').find_all('li',class_='banks-list-item banks-curli clearfixed')
a=[]
for i in row:
    a.append(i)
#print(len(a))
#print(a)
#print(len(a))
#for i in range(0,len(a)):
#    print('name =', row[i].find('span',class_='namedesc').text)
#    print('category =', row[i].find('a',{'target':'_blank'}).text)
#    print('direction =', row[i].find('span',class_='type').text)
#    print('position =', row[i].find('div',class_='open').text)
#    print('target =', row[i].find('div',class_='target').text)
#    print('stoploss =', row[i].find('div',class_='stoploss').text)
#    print('spot =', row[i].find('div',class_='currentPrice').text)

b=['name']
c=['category']
d=['direction']
e=['position']
f=['target']
g=['stoploss']
h=['spot']
T=[time.strftime('%m/%d %H:%M:%S')]

for i in range(0,len(a)):
    b.append(row[i].find('span',class_='namedesc').text)
    c.append(row[i].find('a',{'target':'_blank'}).text)
    d.append(row[i].find('span',class_='type').text)
    e.append(row[i].find('div',class_='open').text)
    f.append(row[i].find('div',class_='target').text)
    g.append(row[i].find('div',class_='stoploss').text)
    h.append(row[i].find('div',class_='currentPrice').text)
    
with open('data.csv','w',encoding='utf_8_sig',newline='') as file:
    #file.write(codecs.BOM_UTF8)
    csvWriter = csv.writer(file)
    csvWriter.writerow(b)
    csvWriter.writerow(c)
    csvWriter.writerow(d)
    csvWriter.writerow(e)
    csvWriter.writerow(f)
    csvWriter.writerow(g)
    csvWriter.writerow(h)
    
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('123.json',scope)
gc = gspread.authorize(credentials)    
wk = gc.open('EmotionUpdate')
wks = wk.worksheet('sheet2')
wks.append_row(T)
wks.append_row(b)
wks.append_row(c)
wks.append_row(d)
wks.append_row(e)
wks.append_row(f)
wks.append_row(g)
wks.append_row(h)
print('寫入完成')
browser.close()
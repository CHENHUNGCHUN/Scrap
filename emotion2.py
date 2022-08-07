# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:03:01 2019

@author: USER
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv
import time
from time import sleep
import gspread
from oauth2client.service_account import ServiceAccountCredentials 


while True:
    try:
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('123.json',scope)
        gc = gspread.authorize(credentials)
        
        req = requests.get('http://www.stockq.org/')
        soup = BeautifulSoup(req.text,'html.parser')
        
        EUR = soup.find_all('table','marketdatatable')[7].find_all('tr')[2] #歐元
        GBP = soup.find_all('table','marketdatatable')[7].find_all('tr')[3] #英鎊
        JPY = soup.find_all('table','marketdatatable')[7].find_all('tr')[14] #日幣
        CHF = soup.find_all('table','marketdatatable')[7].find_all('tr')[4] #瑞郎
        NUD = soup.find_all('table','marketdatatable')[7].find_all('tr')[13] #紐幣
        AUD = soup.find_all('table','marketdatatable')[7].find_all('tr')[12] #澳幣
        US_dallor = soup.find_all('table','marketdatatable')[3].find_all('tr')[21] #美元
        GOLD = soup.find_all('table','marketdatatable')[6].find_all('tr')[2] #黃金
        
        browser = webdriver.Chrome()
        browser.get('https://datacenter.jin10.com/reportType/dc_ssi_trends')
        #print(browser.page_source)
        row = browser.find_elements_by_class_name('buy-data')
        c=[]
        for i in row:
            c.append(i.text)
        d=['buy',time.strftime('%m/%d %H:%M:%S')]
        for i in range(0,13):
            g=float(c[i].replace('%',''))
            d.append(g)
            #print(d)           
        row2 = browser.find_elements_by_class_name('sell-data')
        e=[]
        f=['sell',time.strftime('%m/%d %H:%M:%S')]
        for i in row2:
            e.append(i.text)
        for i in range(0,13):
            x=float(e[i].replace('%',''))
            f.append(x)
            #print(f)
        g=['spot',time.strftime('%m/%d %H:%M:%S'),\
           EUR.find_all('td')[1].text,GBP.find_all('td')[1].text,\
           JPY.find_all('td')[1].text,CHF.find_all('td')[1].text,\
           NUD.find_all('td')[1].text,AUD.find_all('td')[1].text,\
           '','','','','',GOLD.find_all('td')[1].text,US_dallor.find_all('td')[1].text]
        
        with open('emotion_data.csv','a',newline='') as file:
            csvwriter = csv.writer(file)
            #csvwriter.writerow(['','EUR','GBP','JPY','CHF','NUD','AUD','EUR/JPY','GBP/JPY',\
                                #'GBP/JPY','AUD/JPY','EUR/AUD','GOLD','USDDOLLAR'])
            csvwriter.writerow(d)
            csvwriter.writerow(f)
            
        wks = gc.open('EmotionUpdate').sheet1
        wks.append_row(d)
        wks.append_row(f)
        wks.append_row(g)
        browser.close()
        print('糾咪 寫入完成時間：',time.strftime('%m/%d %H:%M:%S'))
        sleep(3600)
    except Exception as e:
        browser.close()
        print('現在時間:',time.strftime('%m/%d %H:%M:%S'),'讀寫錯誤 等待10秒')
        print('e')
        time.sleep(10)
        pass
    continue
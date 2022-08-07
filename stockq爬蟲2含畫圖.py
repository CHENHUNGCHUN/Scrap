# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:48:04 2019

@author: USER
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import time

req = requests.get('http://www.stockq.org/')
soup = BeautifulSoup(req.text,'html.parser')
TWI = soup.find_all('table','marketdatatable')[0].find_all('tr')[9] #台灣
TWI_OTC = soup.find_all('table','marketdatatable')[0].find_all('tr')[10] #台櫃買
CHINA = soup.find_all('table','marketdatatable')[0].find_all('tr')[11] #上證
C_399001 = soup.find_all('table','marketdatatable')[0].find_all('tr')[17] #深證
C_399006 = soup.find_all('table','marketdatatable')[0].find_all('tr')[19] #創業板
NIKKEI_225 = soup.find_all('table','marketdatatable')[0].find_all('tr')[4] #日經
HS = soup.find_all('table','marketdatatable')[0].find_all('tr')[20]
KOSPI = soup.find_all('table','marketdatatable')[0].find_all('tr')[8] #韓股
UK = soup.find_all('table','marketdatatable')[1].find_all('tr')[3] #英國
DAX = soup.find_all('table','marketdatatable')[1].find_all('tr')[5] #德國
FRN = soup.find_all('table','marketdatatable')[1].find_all('tr')[4] #法國
DJ = soup.find_all('table','marketdatatable')[2].find_all('tr')[2] #道瓊
SP500 = soup.find_all('table','marketdatatable')[2].find_all('tr')[4] #標普
RaSO2000 = soup.find_all('table','marketdatatable')[2].find_all('tr')[9] #羅素2000
NASDAQ = soup.find_all('table','marketdatatable')[2].find_all('tr')[10] #NASDAQ
Micro = soup.find_all('table','marketdatatable')[2].find_all('tr')[11] #費半
US_dollar = soup.find_all('table','marketdatatable')[3].find_all('tr')[21] #美指
GOLD = soup.find_all('table','marketdatatable')[6].find_all('tr')[2] #黃金
SIlver = soup.find_all('table','marketdatatable')[6].find_all('tr')[3] #白銀
BAR = soup.find_all('table','marketdatatable')[6].find_all('tr')[5] #鈀金
BOIL = soup.find_all('table','marketdatatable')[6].find_all('tr')[17] #布蘭特原油
WIT = soup.find_all('table','marketdatatable')[6].find_all('tr')[18] #德州輕原油
VIX = soup.find_all('table','marketdatatable')[3].find_all('tr')[7] # VIX
#外汇
EUR = soup.find_all('table','marketdatatable')[7].find_all('tr')[2] #欧元
GBP = soup.find_all('table','marketdatatable')[7].find_all('tr')[3] #英镑
CHF = soup.find_all('table','marketdatatable')[7].find_all('tr')[4] #瑞郎
AUD = soup.find_all('table','marketdatatable')[7].find_all('tr')[12] #澳币
NUD = soup.find_all('table','marketdatatable')[7].find_all('tr')[13] #纽币
JPY = soup.find_all('table','marketdatatable')[7].find_all('tr')[14] #日币
CAD = soup.find_all('table','marketdatatable')[7].find_all('tr')[25] #加币

#美债
req = requests.get('https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield')
soup = BeautifulSoup(req.text,'html.parser')
bond = soup.find('table','t-chart').find_all('tr')[-1] #美债
#泛欧600
req = requests.get('https://www.marketwatch.com/investing/index/sxxp?countrycode=xx')
soup = BeautifulSoup(req.text,'html.parser')
#stock_600 = soup.find('div','element element--intraday').find('div','intraday__data')#泛歐600



print('*****************')
print(time.strftime('%H:%M:%S'))
print('-----------------')
print('***亞洲***')
print('台灣櫃買：',TWI_OTC.find_all('td')[1].text,TWI_OTC.find_all('td')[3].text)
print('台灣加權：',TWI.find_all('td')[1].text,TWI.find_all('td')[3].text)
print('上證指數：',CHINA.find_all('td')[1].text,CHINA.find_all('td')[3].text)
print('深證成指：',C_399001.find_all('td')[1].text,C_399001.find_all('td')[3].text)
print('創業板：',C_399006.find_all('td')[1].text,C_399006.find_all('td')[3].text)
print('NIKKEI 225：',NIKKEI_225.find_all('td')[1].text,NIKKEI_225.find_all('td')[3].text)
print('香港恒生：',HS.find_all('td')[1].text,HS.find_all('td')[3].text)
print('KOSPI：',KOSPI.find_all('td')[1].text,KOSPI.find_all('td')[3].text)
print('***歐洲各國***')
print('英國股市：',UK.find_all('td')[1].text,UK.find_all('td')[3].text)
print('德國股市：',DAX.find_all('td')[1].text,DAX.find_all('td')[3].text)
print('法國股市：',FRN.find_all('td')[1].text,FRN.find_all('td')[3].text)
#print('泛歐600:',stock_600.find('span').text,stock_600.find('span','change--percent--q').text)
print('***美國***')
print('道瓊工業：',DJ.find_all('td')[1].text,DJ.find_all('td')[3].text)
print('標普 500：',SP500.find_all('td')[1].text,SP500.find_all('td')[3].text)
print('Nasdaq：',NASDAQ.find_all('td')[1].text,NASDAQ.find_all('td')[3].text)
print('費城半導體：',Micro.find_all('td')[1].text,Micro.find_all('td')[3].text)
print('羅素2000：',RaSO2000.find_all('td')[1].text,RaSO2000.find_all('td')[3].text)
print('***美债***')
print('美10年债:',bond.find_all('td')[-3].text)
print('美30年债:',bond.find_all('td')[-1].text)
print('***外汇***')
print('欧元:',EUR.find_all('td')[1].text,EUR.find_all('td')[3].text) #欧元
print('英镑:',GBP.find_all('td')[1].text,GBP.find_all('td')[3].text) #英镑
print('瑞郎:',CHF.find_all('td')[1].text,CHF.find_all('td')[3].text) #瑞郎
print('澳币:',AUD.find_all('td')[1].text,AUD.find_all('td')[3].text) #澳币
print('纽币:',NUD.find_all('td')[1].text,NUD.find_all('td')[3].text) #纽币
print('日币:',JPY.find_all('td')[1].text,JPY.find_all('td')[3].text) #日币
print('加币:',CAD.find_all('td')[1].text,CAD.find_all('td')[3].text) #加币
print('***原物料、金屬***')
print('美元指数 :',US_dollar.find_all('td')[1].text,US_dollar.find_all('td')[3].text)
print('VIX指数 ：',VIX.find_all('td')[1].text,VIX.find_all('td')[3].text)
print('黃金    ：',GOLD.find_all('td')[1].text,GOLD.find_all('td')[3].text)
print('白銀    ：',SIlver.find_all('td')[1].text,SIlver.find_all('td')[3].text)
print('鈀金    ：',BAR.find_all('td')[1].text,BAR.find_all('td')[3].text)
print('布蘭特原油：',BOIL.find_all('td')[1].text,BOIL.find_all('td')[3].text)
print('德州輕原油：',WIT.find_all('td')[1].text,WIT.find_all('td')[3].text)
print('-----------------')
print('*****************')
print('\n')

#亚股图

b=[]
Asia_stockpct=[TWI_OTC.find_all('td')[3].text,TWI.find_all('td')[3].text,CHINA.find_all('td')[3].text,C_399001.find_all('td')[3].text,C_399006.find_all('td')[3].text,NIKKEI_225.find_all('td')[3].text,HS.find_all('td')[3].text,KOSPI.find_all('td')[3].text]
for i in Asia_stockpct:
    a=float(i.replace('%',''))
    b.append(a)
x=['TWI_OTC','TWI','SHA0001','399001','399006','NIKKEI 225','HONKON','KOSPI']

plt.style.use('classic')  #ggplot
plt.figure(figsize=(12,12),facecolor='lightblue')
plt.grid(True)  #网格
plt.bar(x,b,alpha=0.5,color='black',align='center',hatch='o',lw=3)
#plt.legend()
for j,i in zip(b,x):
    if j>=0:
        plt.text(i,j+0.4,'%.2f' %j+"%" ,va='bottom',ha='center',fontsize = 15) #fontsize 字的大小
    else:
        plt.text(i,j-0.4,'%.2f' %j+"%" ,va='bottom',ha='center',fontsize = 15) #fontsize 字的大小
plt.xlabel('Market')
plt.ylabel('Retrun(%)')
plt.title('Asia stock market')
plt.savefig('asia_stock.png')
plt.ylim(-1,3)   #y轴上下限
plt.show()

##欧股
#g=[]
#EURO_stock = [UK.find_all('td')[3].tex,DAX.find_all('td')[3].text,FRN.find_all('td')[3].text,stock_600.find('span','change--percent--q').text]
#for i in EURO_stock:
#    a=float(i.replace('%',''))
#    c.append(a)
#t = ['UK','DAX','FRA','STOXX 600']
#plt.style.use('classic')
#plt.figure(figsize=(10,10),facecolor='lightblue')
#plt.grid(True)
#plt.bar(y,c,alpha=0.5,width=0.8,align='center',color='black',hatch='o',lw=3)#align='center' 可以将条状图显示在中间
#plt.xlabel('Market')
#plt.ylabel('Return (%)')
#plt.title('Europe Stock Market')
#for j,i in zip(g,t):
#    if j>=0:
#        plt.text(i,j+0.4,'%.2f' %j+"%" ,fontsize = 15,va='bottom',ha='center')
#    else:
#        plt.text(i,j-0.4,'%.2f' %j+"%" ,fontsize = 15,va='bottom',ha='center')#fontsize 字的大小
#plt.ylim(-1.5,0.5)   #y轴上下限
#plt.savefig('EUROPE_stock.png')
#plt.show()


#美股图

c=[]
Amarica_stock = [DJ.find_all('td')[3].text,SP500.find_all('td')[3].text,NASDAQ.find_all('td')[3].text,Micro.find_all('td')[3].text,RaSO2000.find_all('td')[3].text]
for i in Amarica_stock:
    a=float(i.replace('%',''))
    c.append(a)
y = ['Dow','S&P500','Nasdaq','SOX','Raso2000']
plt.style.use('classic')
plt.figure(figsize=(12,12),facecolor='lightblue')
plt.grid(True)
plt.bar(y,c,alpha=0.5,width=0.8,align='center',color='black',hatch='o',lw=3)#align='center' 可以将条状图显示在中间
plt.xlabel('Market')
plt.ylabel('Return (%)')
plt.title('US Stock Market')
for j,i in zip(c,y):
    if j>=0:
        plt.text(i,j+0.4,'%.2f' %j+"%" ,fontsize = 15,va='bottom',ha='center')
    else:
        plt.text(i,j-0.4,'%.2f' %j+"%" ,fontsize = 15,va='bottom',ha='center')#fontsize 字的大小
plt.ylim(0,4.5)   #y轴上下限
plt.savefig('US_stock.png')
plt.show()

#避险资产图

d=[]
z = ['DollarIndex','Gold','JPY','Silver']
Hedge = [US_dollar.find_all('td')[3].text,GOLD.find_all('td')[3].text,JPY.find_all('td')[3].text,\
        SIlver.find_all('td')[3].text ]
for i in Hedge:
    d.append(float(i.replace('%','')))
    
plt.style.use('classic')
plt.figure(figsize=(12,12),facecolor='lightblue')
plt.grid(True)
plt.bar(z,d,alpha=0.5,width=0.5,align='center',color='black',hatch='o')#align='center'可以将条状图显示在中间
plt.xlabel('Market')
plt.ylabel('Return (%)')
plt.title('Hedge')
for j,i in zip(d,z):
    if j>=0:
        plt.text(i,j+0.4,'%.2f' %j+"%" ,fontsize = 15,ha='center')
    else:
        plt.text(i,j-0.4,'%.2f' %j+"%" ,fontsize = 15,ha='center')#fontsize 字的大小
plt.ylim(-1.5,1.5)   #y轴上下限
plt.savefig('Hedge.png')
plt.show()

#外汇图

e=[]
a=['DXY','EUR','GBP','CHF','AUD','NUD','JPY','CAD']
FX=[US_dollar.find_all('td')[3].text,EUR.find_all('td')[3].text,GBP.find_all('td')[3].text,\
    CHF.find_all('td')[3].text,AUD.find_all('td')[3].text,NUD.find_all('td')[3].text,\
    JPY.find_all('td')[3].text,CAD.find_all('td')[3].text]
for i in FX:
    e.append(float(i.replace('%','')))

plt.style.use('classic')
plt.figure(figsize=(12,12),facecolor='lightblue')
plt.grid(True)
plt.bar(a,e,alpha=0.5,width=0.9,align='center',color='black',hatch='o',lw=3)
plt.xlabel('Market')
plt.ylabel('Return(%)')
plt.title('FX Market')
for j,i in zip(e,a):
    if j>=0:
        plt.text(i,j+0.3,'%.2f' %j+"%" ,fontsize = 15,va='bottom',ha='center')
    else:
        plt.text(i,j-0.3,'%.2f' %j+"%" ,fontsize = 15,va='bottom',ha='center')
        #ha =>文字靠中间(center) 靠右(right) 靠左(left)
plt.ylim(-1.5,2)   #y轴上下限
plt.savefig('FX.png')
plt.show()
from cgi import print_form
from heapq import merge
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import bs4
import time
import re

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from textwrap import indent

import json
cred = credentials.Certificate('supcar-85c0a-firebase-adminsdk-o10rd-e6722e0084.json')
firebase_admin.initialize_app(cred)
firebase_admin.get_app(name='[DEFAULT]')
db = firestore.client()
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\Users\Admin\Desktop\scrapping\geckodriver.exe', options=options)
page = 1
record = []
brand = ''
Brand = []
name =''
price = ''
url = ''
img =''
while page <= 9:
    driver.get('https://www.checkraka.com/car/?cartype=2372&quicksearch_order=306%2CDESC-326%2CASC&page=' + str(page))
    data = driver.page_source
    soup = bs4.BeautifulSoup(data)
    el = soup.find_all('div',{'class':'content c158'})
    for e in el:
        brand = e.find('div',{'class':'data'}).find('a').text
        brand = brand.split(" ")[0]
        if(brand == "BMW"):
            brand = "Bmw"
        elif(brand == "McLaren"):
            brand = "Mclaren"
        elif(brand == "Mercedes-benz"):
            brand = "Benz"
        name = e.find('div',{'class':'data'}).find('a').text
        p = e.find('div',{'class':'price'}).text.split()[0].replace(',','')
        if p == "call":
            price = p

        else:
            price = int(p)

        img = e.find('div',{'class':'logo'}).find('img')
        img = img['src']
        url = e.find('div',{'class':'logo'}).find('a')
        url = url['href']
        id = url[-8:]
        id = id.split("/")[0]
        url = 'https://www.checkraka.com'+url
        record = {'Brand': brand, 'Name': name, 'Price': price, 'Url': url, 'Img': img}
        data1 = {
            id: record

        }
        db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
        db.collection(u'Spyder').document(brand).set(data1,merge=True)
    page += 1
    
driver.quit()
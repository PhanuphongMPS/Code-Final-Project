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
cred = credentials.Certificate(
    'supcar-85c0a-firebase-adminsdk-o10rd-e6722e0084.json')

firebase_admin.initialize_app(cred)
firebase_admin.get_app(name='[DEFAULT]')
db = firestore.client()

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\Users\Admin\Desktop\scrapping\geckodriver.exe', options=options)
page = 1
Brand = []
brand = ''
el = []
soup = []
data = []
while page <= 21:
    if page == 6:
        page += 1
    elif page ==16:
        page += 1
    driver.get('http://www.spyderautoimport.com/car_brand/' + str(page))
    data = driver.page_source
    soup = bs4.BeautifulSoup(data)
    el = soup.find_all('li', {'class': 'col-md-3'})
    web = ('http://www.spyderautoimport.com/car_brand/' + str(page))
    for e in el:
        brand = e.select_one(
            "li.col-md-3 > a:nth-child(1) > span:nth-child(2) > p:nth-child(1)").text.strip()
        if brand == "BMW":
            brand = "Bmw"
        elif brand =="Maclaren":
            brand = "Mclaren"
        elif(brand == "Mercedes-Benz"):
            brand = "Benz"
        name = e.select_one(
            "li.col-md-3> a:nth-child(1) > span:nth-child(2) > p:nth-child(2)").text.strip()
        color = e.select_one(
            "li.col-md-3 > a:nth-child(1) > span:nth-child(2) > p:nth-child(3)").text.strip()
        Brand.append(brand)
        link = e.find('a')
        url = link['href']
        img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
        id = url.split(
            'http://www.spyderautoimport.com/car_detail/')[1].split("/")[0]
        record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
        data1 = {
            id: record,
        }
        db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
        db.collection(u'Spyder').document(brand).set(data1,merge=True)
    page += 1
driver.quit()


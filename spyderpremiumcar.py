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
driver.get('http://www.spyderautoimport.com/premium-used-car/')
data = driver.page_source
soup = bs4.BeautifulSoup(data)
el=soup.select(".photos>div")
record=[]
Brand=[]
for e in el:
    name =''
    color = ''
    url = ''
    brand = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(1)").text.strip()
    if brand == "Sold Out": 
        brand = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(2)").text.strip()
        if brand == "BMW":
            brand = "Bmw"
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(4)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Bentley":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(4)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Mercedes-Benz":
            brand = "Benz"
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(4)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Ferrari":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(4)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Porsche":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(4)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Lamborghini":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(4)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Ford":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(4)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Nissan":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(4)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Volkswagen":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(4)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Audi":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(4)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Maclaren":
            brand = "Mclaren"
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(4)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Maserati":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(4)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
    else:
        if brand == "BMW":
            brand = "Bmw"
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(2)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Bentley":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(2)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Mercedes-Benz":
            brand = "Benz"
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(2)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Ferrari":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(2)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Porsche":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(2)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Lamborghini":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(2)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Ford":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(2)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Nissan":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(2)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Volkswagen":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(2)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Audi":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(2)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Maclaren":
            brand = "Mclaren"
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(2)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)
        elif brand == "Maserati":
            Brand.append(brand)
            name = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(2)").text.strip()
            color = e.select_one("div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(3)").text.strip()
            soup.find_all('div',{'class':'photo'})
            link = e.find('a',{'class':'gall'})
            url = link['href']
            id = url.split('http://www.spyderautoimport.com/premium-used-car-detail/')[1].split("/")[0]
            img = 'https://cars.ksl.com/images/no-image-defaults/cars-noimage_hatchback-lrg.png'
            record = {'Brand': brand, 'Name': name, 'Color': color, 'Url': url, 'Img': img}
            data1 = {
                id: record

            }
            db.collection(u'Spyder').document(str(brand).lower()).set(data1,merge=True)
            db.collection(u'Spyder').document(brand).set(data1,merge=True)

driver.quit()

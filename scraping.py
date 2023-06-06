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

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\Users\Admin\Desktop\scrapping\geckodriver.exe', options=options)
driver.get('http://www.spyderautoimport.com/premium-used-car/')
data = driver.page_source
soup = bs4.BeautifulSoup(data)
all_product = soup.find_all('div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(1)')
if (all_product == "Sold Out"):
    all_product = soup.find_all('div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(2)')
else:
    all_product = soup.find_all('div.photo > a:nth-child(1) > div:nth-child(3) > p:nth-child(1)')
for product in all_product:
    print(product.txt)
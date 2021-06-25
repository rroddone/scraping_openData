# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 12:28:46 2021

@author: ricar
"""
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import requests
"""para eliminar InsecureRequestWarning"""
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://datos.mec.gov.py/app/dataMateriaTituloCompatibleDepartamento.txt'
page = requests.get(url, verify = False)
html = response.read()

soup =BeautifulSoup(page.content, 'lxml')
teach = soup.find('pre').find(text = True)
print(teach)



#print(page)


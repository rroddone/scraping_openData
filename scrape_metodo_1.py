# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 18:42:47 2021

@author: ricar
"""

import pandas as pd
from bs4 import BeautifulSoup
import urllib.request

adress = 'https://datos.mec.gov.py/app/dataMateriaTituloCompatibleDepartamento.txt'
response = urllib.request.urlopen(adress)
html = response.read()

soup = BeautifulSoup(html, 'lxml')
pre = soup.find_all('pre').contents[0]
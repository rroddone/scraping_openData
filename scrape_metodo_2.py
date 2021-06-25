# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:55:52 2021

@author: ricar
"""

from requests_html import HTMLSession
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



def getLista(url):
    s = HTMLSession()
    r = s.get(url, verify = False)
    r.html.render(sleep = 1)
    
    lista = {'lista': r.html.xpath('/html/body/pre', first = True).text}
    
    
    
    print(lista)
    return lista

getLista('https://datos.mec.gov.py/app/dataMateriaTituloCompatibleDepartamento.txt')
    
    
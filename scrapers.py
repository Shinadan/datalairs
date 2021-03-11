# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 16:24:01 2021

@author: Adegboyega
"""

import time
from datetime import date
#import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import numpy as np

options = Options()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options = options, 
                          executable_path=chromedriver_autoinstaller.install()
                          )
                          #executable_path='D:\\Anaconda3\\lib\\site-packages\\chromedriver_autoinstaller\\89\\chromedriver.exe'

#time for delays in the web scraping
timeouts = np.linspace(1,5)

url_tds = 'https://towardsdatascience.com'
driver.get(url_tds)
page_tds = driver.page_source

def tds():    
    #parse html with bs
    site = bs(page_tds,'html.parser')
    homepage_content = site.find_all('div', 
                                 class_='v hc')
    contents = []
    for content in homepage_content:
        try:
            title = content.find('a', class_='ex ca')
            author = content.find('p', class_='be b bf bg fy')
            href = content.find('a', {'class':'ex ca'})['href'].split('?')[0]
            link = url_tds+href
            #delay
            time.sleep(np.random.choice(timeouts))
            #append info to list
            contents.append('%s by %s %s' % (title.text, author.text, link))
            
        except AttributeError:
            continue      
    return contents 

url_mds = 'https://medium.com/topic/data-science'
driver.get(url_mds)
page_mds = driver.page_source

def mds():
    #parse html with bs
    site = bs(page_mds,'html.parser')
    homepage_content = site.find_all('div', 
                                 class_='aj fm')
    contents = []
    for content in homepage_content:
        try: 
            if str(content.find('div', class_="n cs")) == 'None':
                pass
            
            elif content.find('div', class_="n cs").text.split('·')[0] == date.today().strftime("%b %#d"):
                title = content.find('h3', class_='bi fy ge bk aw en eo at ep av eq gj aq')
                href = title.find('a')['href'].split('?')[0]
                contents.append('%s \n %s' % (title.text, href))   
            #delay
            time.sleep(np.random.choice(timeouts))      
        except AttributeError:
            continue
    return contents

url_mml = 'https://medium.com/topic/machine-learning'
driver.get(url_mml)
page_mml = driver.page_source

def mml():
    #parse html with bs
    site = bs(page_mml,'html.parser')
    homepage_content = site.find_all('div', 
                                 class_='aj fm')
    contents = []
    for content in homepage_content:
        try:
            if str(content.find('div', class_="n cs")) == 'None':
                pass
            elif content.find('div', class_="n cs").text.split('·')[0] == date.today().strftime("%b %#d"):
                title = content.find('h3', class_='bi fy ge bk aw en eo at ep av eq gj aq')
                href = title.find('a')['href'].split('?')[0]
                contents.append('%s \n %s' % (title.text, href))
            #delay
            time.sleep(np.random.choice(timeouts))
        except AttributeError:
            continue
    return contents

url_mai = 'https://medium.com/topic/artificial-intelligence'
driver.get(url_mai)
page_mai = driver.page_source

def mai():
    #parse html with bs
    site = bs(page_mai,'html.parser')
    homepage_content = site.find_all('div', 
                                 class_='aj fm')
    contents = []
    for content in homepage_content:
        try:
            if str(content.find('div', class_="n cs")) == 'None':
                pass
            elif content.find('div', class_="n cs").text.split('·')[0] == date.today().strftime("%b %#d"):
                title = content.find('h3', class_='bi fy ge bk aw en eo at ep av eq gj aq')
                href = title.find('a')['href'].split('?')[0]
                contents.append('%s \n %s' % (title.text, href))
            #delay
            time.sleep(np.random.choice(timeouts))
        except AttributeError:
            continue
    return contents

driver.quit()
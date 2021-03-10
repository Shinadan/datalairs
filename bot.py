# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:01:31 2021

@author: Adegboyega
"""
import time
from datetime import date
#import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#import chromedriver_autoinstaller

options = Options()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options = options,
                          executable_path='D:\\Anaconda3\\lib\\site-packages\\chromedriver_autoinstaller\\89\\chromedriver.exe'
                          )
                          #executable_path=chromedriver_autoinstaller.install())
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
        title = content.find('a', class_='ex ca')
        author = content.find('p', class_='be b bf bg fy')
        href = content.find('a', {'class':'ex ca'})['href'].split('?')[0]
        link = url_tds+href
        
        contents.append('%s by %s %s' % (title.text, author.text, link))
       
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
        if str(content.find('div', class_="n cs")) == 'None':
            pass
        
        elif content.find('div', class_="n cs").text.split('·')[0] == date.today().strftime("%b %#d"):
            title = content.find('h3', class_='bi fy ge bk aw en eo at ep av eq gj aq')
            href = title.find('a')['href'].split('?')[0]
            contents.append('%s \n %s' % (title.text, href))
       
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
        if str(content.find('div', class_="n cs")) == 'None':
            pass
        
        elif content.find('div', class_="n cs").text.split('·')[0] == date.today().strftime("%b %#d"):
            title = content.find('h3', class_='bi fy ge bk aw en eo at ep av eq gj aq')
            href = title.find('a')['href'].split('?')[0]
            contents.append('%s \n %s' % (title.text, href))
       
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
        if str(content.find('div', class_="n cs")) == 'None':
            pass
        
        elif content.find('div', class_="n cs").text.split('·')[0] == date.today().strftime("%b %#d"):
            title = content.find('h3', class_='bi fy ge bk aw en eo at ep av eq gj aq')
            href = title.find('a')['href'].split('?')[0]
            contents.append('%s \n %s' % (title.text, href))
       
    return contents

driver.quit()

def data_articles():
    print('Bot starting')
    webpages = ['tds', 'mds', 'mml', 'mai']
    for webpage in webpages:
        for article in globals()[webpage]():
            tweet = article
            print(tweet , '\n')
            time.sleep(0)
            
if __name__ == '__main__':
    data_articles()
    


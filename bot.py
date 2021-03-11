# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:01:31 2021

@author: Adegboyega
"""
import time
from scrapers import tds, mds, mml, mai

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
    


# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:01:31 2021

@author: Adegboyega
"""
import time
from scrapers import tds, mds, mml, mai
from twitter import Twitter, OAuth, TwitterHTTPError
import credentials

oauth = OAuth(
        credentials.ACCESS_TOKEN,
        credentials.ACCESS_SECRET,
        credentials.CONSUMER_KEY,
        credentials.CONSUMER_SECRET)
twit = Twitter(auth=oauth)

def data_articles():
    print('Bot starting')
    webpages = ['tds', 'mds', 'mml', 'mai']
    for webpage in webpages:
        for article in globals()[webpage]():
            try:
                tweet = article
                twit.statuses.update(status=tweet)
                #print(tweet , '\n')
                time.sleep(60)
            except TwitterHTTPError:
                continue
            
if __name__ == '__main__':
    try:
        data_articles()
    except Exception as e:
        print(e)
    


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:22:46 2019

@author: Linna
"""

import pandas as pd

import requests

from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time


############ 
############ USE BOILER ROOM SITE
############



chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)                                   
   
    
all_comments=[]
all_video_titles = []     




driver.get('https://boilerroom.tv/genre/house/')


driver.execute_script("window.scrollTo(" + str(300) + ", " + str(300 + 100) + ")")
time.sleep(1.5)

driver.execute_script("window.scrollTo(" + str(1000) + ", " + str(1000 + 100) + ")")
time.sleep(1.5)

driver.execute_script("window.scrollTo(" + str(2000) + ", " + str(2000 + 100) + ")")

driver.execute_script("window.scrollTo(" + str(3000) + ", " + str(3000 + 100) + ")")

button = driver.find_element_by_css_selector('.-GenericList-LoadMore-k49rZa')

button.click()


b2 = driver.find_element_by_css_selector('.-Grid-Column-3-extraLarge-z2-uAK:nth-child(2)')

b2.click()




b3 = driver.find_element_by_class_name('-Player-PlayerIframe-3E4cg1')


b3 = driver.find_element_by_class_name('-Player-PlayerIframe-3E4cg1').get_src()

b4_url = driver.find_element_by_class_name('-Player-PlayerIframe-3E4cg1').get_attribute('src')

b4_split = str.split(b4_url, sep = '/')

b5_split = str.split(b4_split[4], sep = '?')

b6_url = 'https://www.youtube.com/watch?v=' + b5_split[0]

driver.get(b6_url)

## then get the comments


#####3 LOOP IT

hi = 0

chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)                                   
   
    
all_comments=[]
all_video_titles = []     

driver.get('https://boilerroom.tv/genre/house/')


driver.execute_script("window.scrollTo(" + str(300) + ", " + str(300 + 100) + ")")
time.sleep(1.5)

for i in range(2, 30): #should be 1000
    try:
        b2 = driver.find_element_by_css_selector('.-Grid-Column-3-extraLarge-z2-uAK:nth-child(' + str(i) + ')')
        b2.click()
        time.sleep(1)
    except:
        print(i)
        print('error 1')
    try:
        b4_url = driver.find_element_by_class_name('-Player-PlayerIframe-3E4cg1').get_attribute('src')
        b4_split = str.split(b4_url, sep = '/')
        b5_split = str.split(b4_split[4], sep = '?')
        b6_url = 'https://www.youtube.com/watch?v=' + b5_split[0]
    except:
        print(i)
        print('error 2')
    try:
        time.sleep(1.5)
        driver.get(b6_url)
        time.sleep(1.5)
    except:
        print(i)
        print('error 3')
    try:
        video_title = driver.find_element_by_css_selector('.ytd-video-primary-info-renderer').text
        print(video_title) 
        # get comments
        # go back to boiler room
        driver.get('https://boilerroom.tv/genre/house/')
        driver.execute_script("window.scrollTo(" + str(300) + ", " + str(300 + 100) + ")")
        if(i >= 5):
            driver.execute_script("window.scrollTo(" + str(600) + ", " + str(600 + 100) + ")")  
        if(i >= 9):
            driver.execute_script("window.scrollTo(" + str(900) + ", " + str(900 + 100) + ")")
        if(i >= 13):
            driver.execute_script("window.scrollTo(" + str(1200) + ", " + str(1200 + 100) + ")")
        if(i >= 17):
            driver.execute_script("window.scrollTo(" + str(1500) + ", " + str(1500 + 100) + ")")
        if(i >= 21):
            driver.execute_script("window.scrollTo(" + str(1800) + ", " + str(1800 + 100) + ")")
        if(i >= 25):
            b7 = driver.find_element_by_css_selector('.-GenericList-LoadMore-k49rZa')
            b7.click()
        ## 24 videos before a "load more" -- 4 vids in 1 row
        # load more '.-GenericList-LoadMore-k49rZa'
        ## 8 vids loaded at a time
        time.sleep(1.5)
    except:
        print(i)
        print('error 4')
        hi = hi + 1
 





       
out_dat = pd.DataFrame()
out_dat['video_titles'] = all_video_titles
out_dat['comments'] = all_comments

out_dat.to_csv('/Users/Linna/Documents/boilerroom_data/comments7.csv')
















       

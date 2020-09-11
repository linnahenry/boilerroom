#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 16:08:40 2018

@author: Linna
"""

import pandas as pd

import requests

from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

import os

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.options import Options

from time import strptime

import copy

from datetime import datetime

import re

import random

import uuid

import urllib.request

from newspaper import Config, Article, Source

from joblib import Parallel, delayed

from tqdm import tqdm, trange

from nltk import tokenize

from nltk.sentiment.vader import SentimentIntensityAnalyzer

import subprocess

import nltk



#driver = webdriver.Chrome()

chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)                                   

 

driver.get('https://www.youtube.com/user/brtvofficial/videos')

button = driver.find_element_by_css_selector('.ytd-grid-renderer:nth-child(4)') #video-title

button.click()

#driver.find_element_by_css_selector('#comments').get_attribute("innerHTML")

comments = driver.find_element_by_css_selector('#comments').text

comments.split('\n')

#driver.get('https://www.google.com/search?q=' + str(uuid.uuid4()))

#vwc.split('\n')[0].replace(',', '')

all_comments=[]
all_video_titles = []

for i in range(2, 1000):
    driver.get('https://www.youtube.com/user/brtvofficial/videos')
    button = driver.find_element_by_css_selector('.ytd-grid-renderer:nth-child(' + str(i) + ')') 
    time.sleep(3) # wait to load
    #vid_title = button.text
    #links = button.get_attribute('href')
    button.click()
    video_title = driver.find_element_by_css_selector('.ytd-video-primary-info-renderer').text
    SCROLL_PAUSE_TIME = 0.5
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #driver.execute_script("window.scrollTo(5, 10)")
        driver.execute_script("window.scrollTo(900, 1000)")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    comments = driver.find_element_by_css_selector('#comments').text
    comments = comments.split('\n')
    all_video_titles.append(video_title)
    all_comments.append(comments)

#container .ytd-video-primary-info-renderer .ytd-video-primary-info-renderer



#driver.execute_script("window.scrollTo(0, Y)")


for i in range(2, 1000):
    driver.get('https://www.youtube.com/user/brtvofficial/videos')
    button = driver.find_element_by_css_selector('.ytd-grid-renderer:nth-child(' + str(i) + ')') 
    time.sleep(3) # wait to load
    button.click()
    time.sleep(3)
    video_title = driver.find_element_by_css_selector('.ytd-video-primary-info-renderer').text
    print(video_title)
    

#scroll_iter = 9000 #up it by 10000 each time    
#for i in range(84, 1000):
#    if(i/28>=1):
#        #scroll
#        scroll_iter = 9000
#        #scroll_iter = scroll_iter + 10000*int(i/29)
#        driver.get('https://www.youtube.com/user/brtvofficial/videos')
#        j = 0
#        while j < int(i/28):
#            driver.execute_script("window.scrollTo(" + str(scroll_iter) + ", " + str(scroll_iter + 1000) + ")")
#            time.sleep(1.5)
#            #scroll_iter = scroll_iter + 10000*int(i/29)
#            j = j+1
#        #time.sleep(3)
#        button = driver.find_element_by_css_selector('.ytd-grid-renderer:nth-child(' + str(i) + ')') 
#        time.sleep(3) # wait to load
#        button.click()
#        time.sleep(3)
#        video_title = driver.find_element_by_css_selector('.ytd-video-primary-info-renderer').text
#        print(video_title) 
#    else: #beginning of the videos
#        driver.get('https://www.youtube.com/user/brtvofficial/videos')
#        button = driver.find_element_by_css_selector('.ytd-grid-renderer:nth-child(' + str(i) + ')') 
#        time.sleep(3) # wait to load
#        button.click()
#        time.sleep(3)
#        video_title = driver.find_element_by_css_selector('.ytd-video-primary-info-renderer').text
#        print(video_title)    
    
    
    
#using try except
    
scroll_iter = 9000 #up it by 10000 each time    
for i in range(84, 1000):
    if(i/28>=1):
        #scroll
        scroll_iter = 9000
        #scroll_iter = scroll_iter + 10000*int(i/29)
        driver.get('https://www.youtube.com/user/brtvofficial/videos')
        j = True
        while j:
            try:
                button = driver.find_element_by_css_selector('.ytd-grid-renderer:nth-child(' + str(i) + ')')
                j = False
            except:
                driver.execute_script("window.scrollTo(" + str(scroll_iter) + ", " + str(scroll_iter + 1000) + ")")
                time.sleep(1.5)
        time.sleep(3) # wait to load
        button.click()
        time.sleep(3)
        video_title = driver.find_element_by_css_selector('.ytd-video-primary-info-renderer').text
        print(video_title) 
    else: #beginning of the videos
        driver.get('https://www.youtube.com/user/brtvofficial/videos')
        button = driver.find_element_by_css_selector('.ytd-grid-renderer:nth-child(' + str(i) + ')') 
        time.sleep(3) # wait to load
        button.click()
        time.sleep(3)
        video_title = driver.find_element_by_css_selector('.ytd-video-primary-info-renderer').text
        print(video_title)    
 
    
 
    
chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)                                   
   
    
all_comments=[]
all_video_titles = []         
     
 # some edits and adding in comments       
scroll_iter = 10000 #up it by 10000 each time    
for i in range(2, 7000): #have to start on i = 4
    scroll_iter = 10000
    #scroll_iter = scroll_iter + 10000*int(i/29)
    #driver.get('https://www.youtube.com/user/brtvofficial/videos')
    driver.get('https://www.youtube.com/user/brtvofficial/videos?flow=grid&sort=p&view=0') #sort by most popular
    #driver.get('https://www.youtube.com/user/brtvofficial/videos?sort=da&flow=grid&view=0') #sort by oldest
    time.sleep(1.5)
    j = True
    jiter = 0 
    while j and jiter < 100:
        try:
            button = driver.find_element_by_css_selector('.ytd-grid-renderer:nth-child(' + str(i) + ')')
            #print(j)
            j = False
        except:
            driver.execute_script("window.scrollTo(" + str(scroll_iter) + ", " + str(scroll_iter + 1000) + ")")
            time.sleep(1.5)
            jiter = jiter + 1
    if(jiter == 100):
        next
    else:
        time.sleep(1.5) # wait to load
        button.click()
        time.sleep(1.5)
        video_title = driver.find_element_by_css_selector('.ytd-video-primary-info-renderer').text
        print(video_title) 
        jj = True
        driver.execute_script("window.scrollTo(" + str(500) + ", " + str(500 + 100) + ")")
        time.sleep(1.5)
        driver.execute_script("window.scrollTo(" + str(500) + ", " + str(500 + 100) + ")")
        time.sleep(1.5)
        while jj:
            try:
                comments = driver.find_element_by_css_selector('#comments').text
                jj = False
            except:
                driver.execute_script("window.scrollTo(" + str(scroll_iter) + ", " + str(scroll_iter + 1000) + ")")
                time.sleep(1.5)
        #reply_iter = sum([x == 'View reply' for x in comments.split('\n')]) #like View like repl
        reply_iter = sum(['View' in x and 'repl' in x for x in comments.split('\n')])
        read_mores = sum([x == 'Read more' for x in comments.split('\n')])
        current_comments = comments.split('\n')
        current_comments = [x for x in current_comments if 'View' not in x and 'repl' not in x]
        read_more_ind = [y for y,x in zip(list(range(0, len(current_comments))),current_comments) if x == 'Read more']
        read_more_ind = [int((x - 3)/5) + 1 for x in read_more_ind]
        sc_iter2 = 700 
        for k in range(0, len(read_more_ind)):
            if(read_more_ind[k] == 1):
                try:
                    button3 = driver.find_element_by_css_selector('#more .ytd-comment-renderer') 
                    button3.click()
                    comments = driver.find_element_by_css_selector('#comments').text
                    driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 100) + ")")
                    sc_iter2 = sc_iter2 + 300
                except:
                    driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + (sc_iter2 + 100) + ")")
                    sc_iter2 = sc_iter2 + 300
                    time.sleep(1.5)
            else:
                try:
                    button4 = driver.find_element_by_css_selector('#content , .ytd-item-section-renderer:nth-child(' + str(read_more_ind[k]) + ')')
                    button4.click()
                    comments = driver.find_element_by_css_selector('#comments').text
                    driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 100) + ")")
                    sc_iter2 = sc_iter2 + 300
                except:
                    driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 100) + ")")
                    sc_iter2 = sc_iter2 + 300
                    time.sleep(1.5)
        try:
            total_comments = int(comments.split('\n')[0].split(' ')[0].replace(',', ''))
        except:
            total_comments = 0
        reply_iter = sum(['View' in x and 'repl' in x for x in comments.split('\n')])
        comments_found = sum([x == 'REPLY' for x in comments.split('\n')]) + reply_iter
        replies = []
        start_comments = comments_found
        prev_comments = 0
        niter = 0
        while comments_found < total_comments:
            #driver.execute_script("window.scrollTo(" + str(scroll_iter) + ", " + str(scroll_iter + 1000) + ")")
            #driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 1000) + ")")
            #sc_iter2 = sc_iter2 + 1300
            time.sleep(3)
            comments = driver.find_element_by_css_selector('#comments').text
            #reply_iter = sum([x == 'View reply' for x in comments.split('\n')])
            reply_iter = sum(['View' in x and 'repl' in x for x in comments.split('\n')])
            read_mores = sum([x == 'Read more' for x in comments.split('\n')])
            current_comments = comments.split('\n')
            current_comments = [x for x in current_comments if 'View' not in x and 'repl' not in x]
            read_more_ind = [y for y,x in zip(list(range(0, len(current_comments))),current_comments) if x == 'Read more']
            read_more_ind = [int((x - 3)/5) + 1 for x in read_more_ind]
            if(len(read_more_ind) > k+1):
                for k in range(0, len(read_more_ind)):
                    if(read_more_ind[k] == 1):
                        try:
                            button3 = driver.find_element_by_css_selector('#more .ytd-comment-renderer') 
                            button3.click()
                            comments = driver.find_element_by_css_selector('#comments').text
                            driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 100) + ")")
                            sc_iter2 = sc_iter2 + 300
                        except:
                            driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 100) + ")")
                            sc_iter2 = sc_iter2 + 300
                            time.sleep(1.5)
                    else:
                        try:
                            button4 = driver.find_element_by_css_selector('#content , .ytd-item-section-renderer:nth-child(' + str(read_more_ind[k]) + ')')
                            button4.click()
                            comments = driver.find_element_by_css_selector('#comments').text
                        except:
                            driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 100) + ")")
                            sc_iter2 = sc_iter2 + 300
                            time.sleep(1.5)
            else:
                nnnnnnnnnnnnnnnnnnnnnnnnnn = 1 #trash line for no reason
                driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 100) + ")")
                sc_iter2 = sc_iter2 + 300
            driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 100) + ")")
            sc_iter2 = sc_iter2 + 3300
            time.sleep(1)
            total_comments = int(comments.split('\n')[0].split(' ')[0].replace(',', ''))
            comments = driver.find_element_by_css_selector('#comments').text
            reply_iter = sum(['View' in x and 'repl' in x for x in comments.split('\n')])
            comments_found = sum([x == 'REPLY' for x in comments.split('\n')]) + reply_iter
            if(comments_found == prev_comments and niter >= 3):
                break
                comments_found = total_comments
            else:
                prev_comments = comments_found
                niter = niter + 1
            #if(comments_found == start_comments):
             #   break
              #  comments_found = total_comments
            #start_comments = comments_found  
        all_video_titles.append(video_title)
        all_comments.append(comments)
        



        
    if(reply_iter > 0):
        j = 0
        while j < reply_iter:
            try:
                button2 = driver.find_element_by_css_selector('#more-text')
                button2.click()
                reps = driver.find_element_by_css_selector('#loaded-replies').text
                replies = replies.append(reps)
                read_mores = sum([x == 'Read more' for x in reps.split('\n')])
                try:
                    button3 = driver.find_element_by_css_selector('#more .ytd-comment-renderer')
                    button3.click()
                except:
                    nnnnnnnnnn = 1 #trash line
                j = j + 1
                driver.execute_script("window.scrollTo(" + str(500) + ", " + str(500 + 100) + ")")
            except:
                driver.execute_script("window.scrollTo(" + str(500) + ", " + str(500 + 100) + ")")
                time.sleep(1.5)
        comments = [comments, replies]
        
        
        
        all_video_titles.append(video_title)
        all_comments.append(comments)
    
#        while read_mores > 0:
#            try:
#                button3 = driver.find_element_by_css_selector('#more .ytd-comment-renderer')
#                #button4 = driver.find_element_by_css_selector('#content , .ytd-item-section-renderer:nth-child(18)')
#                button3.click()
#                comments = driver.find_element_by_css_selector('#comments').text
#                read_mores = sum([x == 'Read more' for x in comments.split('\n')])
#            except:
#                driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2+100) + ")")
#                sc_iter2 = sc_iter2 + 300
#                time.sleep(1.5) 
    
    
    
    
    
    
    #.ytd-comment-replies-renderer
    
#content , .ytd-item-section-renderer:nth-child(11) #content-text , #more .ytd-comment-renderer

# this as a use case: Cadency | Boiler Room x Herrensauna

out_dat = pd.DataFrame()
out_dat['video_titles'] = all_video_titles
out_dat['comments'] = all_comments

out_dat.to_csv('/Users/Linna/Documents/boilerroom_data/comments9.csv')

#i = 86    
button2 = driver.find_element_by_css_selector('#more-text')
button2.click()
driver.find_element_by_css_selector('#loaded-replies').text
    
# if n comments = n 'REPLY' then have all comments
# iterate through the number of times there is a 'View reply'

reply_iter = sum([x == 'View reply' for x in comments.split('\n')])

total_comments = int(comments.split('\n')[0].split(' ')[0])

comments_found = sum([x == 'REPLY' for x in comments.split('\n')]) + reply_iter


driver.find_element_by_css_selector('#.ytd-comment-replies-renderer')  
    
    
    
 
#times out after i = 29
j = True
while j:
    try:
        button.click()
        j = False
    except:
        driver.execute_script("window.scrollTo(" + str(scroll_iter) + ", " + str(scroll_iter + 1000) + ")")
        time.sleep(1.5)  
    
    
#get replies
#.ytd-comment-replies-renderer
##more-text
    
    
    
############ 
############ RE DO BY PLAY ALL
############



chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)                                   
   
    
all_comments=[]
all_video_titles = []     



driver.get('https://www.youtube.com/watch?v=ta9i08iUqWg&list=UUGBpxWJr9FNOcFYA5GkKrMg')   

overall_iter = 0
current_iter = 4
#for i in range(4, 7000):
while overall_iter < 7000:
    time.sleep(1.5)
    video_title = driver.find_element_by_css_selector('.ytd-video-primary-info-renderer').text
    print(video_title) 
    jj = True
    driver.execute_script("window.scrollTo(" + str(500) + ", " + str(500 + 100) + ")")
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(" + str(500) + ", " + str(500 + 100) + ")")
    time.sleep(1.5)
    while jj:
        try:
            comments = driver.find_element_by_css_selector('#comments').text
            jj = False
        except:
            driver.execute_script("window.scrollTo(" + str(scroll_iter) + ", " + str(scroll_iter + 1000) + ")")
            time.sleep(1.5)
    reply_iter = sum(['View' in x and 'repl' in x for x in comments.split('\n')])
    comments_found = sum([x == 'REPLY' for x in comments.split('\n')]) + reply_iter
    replies = []
    try:
        total_comments = int(comments.split('\n')[0].split(' ')[0].replace(',', ''))
    except:
        nnnnn= 1 # trash
    all_video_titles.append(video_title)
    all_comments.append(comments)
    ### need to scroll back up...
    driver.execute_script("window.scrollTo(" + str(5) + ", " + str(10) + ")")
    #button = driver.find_element_by_css_selector('.ytd-playlist-panel-renderer:nth-child(' + str(i) + ')')
    try:
        button = driver.find_element_by_css_selector('.ytd-playlist-panel-renderer:nth-child(' + str(current_iter) + ')')
        button.click()
    except:
        current_iter = 4
        button = driver.find_element_by_css_selector('.ytd-playlist-panel-renderer:nth-child(' + str(current_iter) + ')')
        button.click()
    overall_iter = overall_iter + 1
    current_iter = current_iter + 1
    
    
    
    
    
    

i = 6

button = driver.find_element_by_css_selector('.ytd-playlist-panel-renderer:nth-child(' + str(i) + ')')

driver.find_element_by_css_selector('.ytd-playlist-panel-renderer:nth-child(' + str(i) + ')').get_attribute('href')
 
button.click()



out_dat = pd.DataFrame()
out_dat['video_titles'] = all_video_titles
out_dat['comments'] = all_comments

out_dat.to_csv('/Users/Linna/Documents/boilerroom_data/comments7.csv')






    
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

for i in range(2, 1000):
    try:
        b2 = driver.find_element_by_css_selector('.-Grid-Column-3-extraLarge-z2-uAK:nth-child(' + str(i) + ')')
        b2.click()
        time.sleep()
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
        time.sleep(1.5)
    except:
        print(i)
        print('error 4')
        hi = hi + 1









i = 6

driver.get('https://www.youtube.com/watch?v=XdHSpNTKjCY&index=' + str(i) + '&list=UUGBpxWJr9FNOcFYA5GkKrMg')



   
 # some edits and adding in comments       
scroll_iter = 10000 #up it by 10000 each time    
for i in range(2, 7000): #have to start on i = 4
    scroll_iter = 10000
    #scroll_iter = scroll_iter + 10000*int(i/29)
    #driver.get('https://www.youtube.com/user/brtvofficial/videos')
    driver.get('https://www.youtube.com/user/brtvofficial/videos?flow=grid&sort=p&view=0') #sort by most popular
    #driver.get('https://www.youtube.com/user/brtvofficial/videos?sort=da&flow=grid&view=0') #sort by oldest
    time.sleep(1.5)
    j = True
    jiter = 0 
    while j and jiter < 100:
        try:
            button = driver.find_element_by_css_selector('.ytd-grid-renderer:nth-child(' + str(i) + ')')
            #print(j)
            j = False
        except:
            driver.execute_script("window.scrollTo(" + str(scroll_iter) + ", " + str(scroll_iter + 1000) + ")")
            time.sleep(1.5)
            jiter = jiter + 1
    if(jiter == 100):
        next
    else:
        time.sleep(1.5) # wait to load
        button.click()
        time.sleep(1.5)
        video_title = driver.find_element_by_css_selector('.ytd-video-primary-info-renderer').text
        print(video_title) 
        jj = True
        driver.execute_script("window.scrollTo(" + str(500) + ", " + str(500 + 100) + ")")
        time.sleep(1.5)
        driver.execute_script("window.scrollTo(" + str(500) + ", " + str(500 + 100) + ")")
        time.sleep(1.5)
        while jj:
            try:
                comments = driver.find_element_by_css_selector('#comments').text
                jj = False
            except:
                driver.execute_script("window.scrollTo(" + str(scroll_iter) + ", " + str(scroll_iter + 1000) + ")")
                time.sleep(1.5)
        #reply_iter = sum([x == 'View reply' for x in comments.split('\n')]) #like View like repl
        reply_iter = sum(['View' in x and 'repl' in x for x in comments.split('\n')])
        read_mores = sum([x == 'Read more' for x in comments.split('\n')])
        current_comments = comments.split('\n')
        current_comments = [x for x in current_comments if 'View' not in x and 'repl' not in x]
        read_more_ind = [y for y,x in zip(list(range(0, len(current_comments))),current_comments) if x == 'Read more']
        read_more_ind = [int((x - 3)/5) + 1 for x in read_more_ind]
        sc_iter2 = 700 
        for k in range(0, len(read_more_ind)):
            if(read_more_ind[k] == 1):
                try:
                    button3 = driver.find_element_by_css_selector('#more .ytd-comment-renderer') 
                    button3.click()
                    comments = driver.find_element_by_css_selector('#comments').text
                    driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 100) + ")")
                    sc_iter2 = sc_iter2 + 300
                except:
                    driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + (sc_iter2 + 100) + ")")
                    sc_iter2 = sc_iter2 + 300
                    time.sleep(1.5)
            else:
                try:
                    button4 = driver.find_element_by_css_selector('#content , .ytd-item-section-renderer:nth-child(' + str(read_more_ind[k]) + ')')
                    button4.click()
                    comments = driver.find_element_by_css_selector('#comments').text
                    driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 100) + ")")
                    sc_iter2 = sc_iter2 + 300
                except:
                    driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 100) + ")")
                    sc_iter2 = sc_iter2 + 300
                    time.sleep(1.5)
        try:
            total_comments = int(comments.split('\n')[0].split(' ')[0].replace(',', ''))
        except:
            total_comments = 0
        reply_iter = sum(['View' in x and 'repl' in x for x in comments.split('\n')])
        comments_found = sum([x == 'REPLY' for x in comments.split('\n')]) + reply_iter
        replies = []
        start_comments = comments_found
        prev_comments = 0
        niter = 0
        while comments_found < total_comments:
            #driver.execute_script("window.scrollTo(" + str(scroll_iter) + ", " + str(scroll_iter + 1000) + ")")
            #driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 1000) + ")")
            #sc_iter2 = sc_iter2 + 1300
            time.sleep(3)
            comments = driver.find_element_by_css_selector('#comments').text
            #reply_iter = sum([x == 'View reply' for x in comments.split('\n')])
            reply_iter = sum(['View' in x and 'repl' in x for x in comments.split('\n')])
            read_mores = sum([x == 'Read more' for x in comments.split('\n')])
            current_comments = comments.split('\n')
            current_comments = [x for x in current_comments if 'View' not in x and 'repl' not in x]
            read_more_ind = [y for y,x in zip(list(range(0, len(current_comments))),current_comments) if x == 'Read more']
            read_more_ind = [int((x - 3)/5) + 1 for x in read_more_ind]
            if(len(read_more_ind) > k+1):
                for k in range(0, len(read_more_ind)):
                    if(read_more_ind[k] == 1):
                        try:
                            button3 = driver.find_element_by_css_selector('#more .ytd-comment-renderer') 
                            button3.click()
                            comments = driver.find_element_by_css_selector('#comments').text
                            driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 100) + ")")
                            sc_iter2 = sc_iter2 + 300
                        except:
                            driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 100) + ")")
                            sc_iter2 = sc_iter2 + 300
                            time.sleep(1.5)
                    else:
                        try:
                            button4 = driver.find_element_by_css_selector('#content , .ytd-item-section-renderer:nth-child(' + str(read_more_ind[k]) + ')')
                            button4.click()
                            comments = driver.find_element_by_css_selector('#comments').text
                        except:
                            driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 100) + ")")
                            sc_iter2 = sc_iter2 + 300
                            time.sleep(1.5)
            else:
                nnnnnnnnnnnnnnnnnnnnnnnnnn = 1 #trash line for no reason
                driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 100) + ")")
                sc_iter2 = sc_iter2 + 300
            driver.execute_script("window.scrollTo(" + str(sc_iter2) + ", " + str(sc_iter2 + 100) + ")")
            sc_iter2 = sc_iter2 + 3300
            time.sleep(1)
            total_comments = int(comments.split('\n')[0].split(' ')[0].replace(',', ''))
            comments = driver.find_element_by_css_selector('#comments').text
            reply_iter = sum(['View' in x and 'repl' in x for x in comments.split('\n')])
            comments_found = sum([x == 'REPLY' for x in comments.split('\n')]) + reply_iter
            if(comments_found == prev_comments and niter >= 3):
                break
                comments_found = total_comments
            else:
                prev_comments = comments_found
                niter = niter + 1
            #if(comments_found == start_comments):
             #   break
              #  comments_found = total_comments
            #start_comments = comments_found  
        all_video_titles.append(video_title)
        all_comments.append(comments)














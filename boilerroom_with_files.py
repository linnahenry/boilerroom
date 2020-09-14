#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 12:59:12 2020

@author: Linna
"""




# watch this video on how to find all URLs associated with a youtube channel
# https://www.youtube.com/watch?v=cwttM41xVBY




import pandas as pd

import requests

from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

import re


# set up a chrome driver to use for web scraping
chromedriver = '/Users/Linna/Downloads/chromedriver 2'
driver = webdriver.Chrome(chromedriver)                                   
   

# from the above youtube video, here are the saved youtube URLs in a csv
all_br = pd.read_csv('/Users/Linna/Downloads/BoilerRoom Videos - Sheet1.csv', header = None)

# test navigating to a URL
driver.get(all_br.iloc[12,1])


# test clicking on the "show more"
button = driver.find_element_by_css_selector('#more .ytd-video-secondary-info-renderer') #video-title

button.click()



# test collecting the description 
description =  driver.find_element_by_css_selector('#collapsible').text

description.split('\n')



driver.get('https://www.youtube.com/watch?v=BMtfZNMFMG4')


## loop through all URLs, and save the video descriptions

all_desc = []

for i in range(0, all_br.shape[0]):
    driver.get(all_br.iloc[i,1])
    try:
        button = driver.find_element_by_css_selector('#more .ytd-video-secondary-info-renderer') #video-title
        button.click()
        description = driver.find_element_by_css_selector('#collapsible').text
        d2 = description.split('\n')    
        all_desc.append(d2)
    except:
        all_desc.append('')



# save it just in case
ad = pd.DataFrame(all_desc)



all_br['description'] = ad

all_br.to_csv('/Users/Linna/Documents/BoilerRoom_desc.csv')


# test collecting the songs & artists for a single DJ

[x == 'Song' for x in all_br['description'][41]]

[x == 'Artist' for x in all_br['description'][41]]


sind = [y for x,y in zip(all_br['description'][41], list(range(0, len(all_br['description'][41])))) if x == 'Song']

aind = [y for x,y in zip(all_br['description'][41], list(range(0, len(all_br['description'][41])))) if x == 'Artist']

sind = [x+1 for x in sind]

aind = [x+1 for x in aind]


songs = [x for x,y in zip(all_br['description'][41], list(range(0, len(all_br['description'][41])))) if y in sind]

artists = [x for x,y in zip(all_br['description'][41], list(range(0, len(all_br['description'][41])))) if y in aind]


# iterate through all the video descriptions, separating out the songs and artists

all_songs = []
all_artists = []
all_conjoined = []
all_index = []
for i in range(0, all_br.shape[0]):
    sind = [y for x,y in zip(all_br['description'][i], list(range(0, len(all_br['description'][i])))) if x == 'Song']
    aind = [y for x,y in zip(all_br['description'][i], list(range(0, len(all_br['description'][i])))) if x == 'Artist']
    sind = [x+1 for x in sind]
    aind = [x+1 for x in aind]
    songs = [x for x,y in zip(all_br['description'][i], list(range(0, len(all_br['description'][i])))) if y in sind]
    artists = [x for x,y in zip(all_br['description'][i], list(range(0, len(all_br['description'][i])))) if y in aind]
    all_songs.append(songs)
    all_artists.append(artists)
    all_conjoined.append([[x,y] for x,y in zip(songs, artists)])
    all_index.append([i for x in list(range(0, len(artists)))])



#flat_list = [item for sublist in all_conjoined for item in sublist] ## need to take out current 

#flat_list = [item for sublist in all_conjoined[0:i] + all_conjoined[i+1:len(all_conjoined)] for item in sublist] ## need to take out current 



#i = 41
#c_set = all_conjoined[i]
#flat_conjoined = [item for sublist in all_conjoined[0:i] + all_conjoined[i+1:len(all_conjoined)] for item in sublist] ## need to take out current 
#flat_index = [item for sublist in all_index[0:i] + all_index[i+1:len(all_conjoined)] for item in sublist]


# for every youtube video, find music in common with other videos

similar_artists = []
similar_songs = []
for i in range(0, all_br.shape[0]):
    c_set = all_conjoined[i]
    flat_conjoined = [item for sublist in all_conjoined[0:i] + all_conjoined[i+1:len(all_conjoined)] for item in sublist] ## need to take out current 
    flat_index = [item for sublist in all_index[0:i] + all_index[i+1:len(all_conjoined)] for item in sublist]
    a_match = []
    song_match = []
    for j in range(0, len(c_set)):
        if c_set[j] in flat_conjoined:
            match_ind = [x for x,y in zip(flat_index, flat_conjoined) if y == c_set[j]]
            a_match.append(list(all_br[0][match_ind]))
            song_match.append(c_set[j])
    similar_artists.append(a_match)    
    similar_songs.append(song_match)
            


# given an artist, return other artists that played the same song + the song that links them


def find_rec(artist):
    art_match = [re.search(artist, x) for x in all_br[0]]
    mind = [x for x,y in zip(list(range(0,all_br.shape[0])), art_match) if y != None]
    sa = [x for x,y in zip(similar_artists, list(range(0, len(similar_artists)))) if y in mind]
    ss = [x for x,y in zip(similar_songs, list(range(0, len(similar_songs)))) if y in mind]
    return([sa, ss])


find_rec('Peggy Gou')

find_rec('James Murphy') 

find_rec('Holy Ghost') # returns nothing
        
    
#len(flat_conjoined)
#len(flat_index)    
#flat_conjoined = [item for sublist in all_conjoined for item in sublist] ## need to take out current 
#flat_index = [item for sublist in all_index for item in sublist]












































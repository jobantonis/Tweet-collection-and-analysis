#!/usr/bin/env python
# coding: utf-8

#  # Version 1
#   
# **This version can login to twitter automatically and navigate to the search bar, where it automatically chooses the "latest" tab for all historical tweet data. A snippet of javascript is used for automatic scrolling in order to load the next set of tweets. Also included is a way in order to tell  the page position and compare it each scroll, as to judge wether or not the end of all tweets is reached, much like in the advanced web scraping tutorial. In order to mitigate potential issues caused by a connection interruption / lag, a maximum number of 3 scroll attempts is allowed if current scroll position on the page = the last known scroll position.
# 
# **With this version,a single keyword "coronavaccin" is being searched upon. Through use of the csv library it is then exported to a csv file.
# 
# **Entities captured in this version so far are: 
#     Tweet Text 
#     User Name
#     Twitter Handle
#     Retweet Count
#     Like Count
#         

# In[ ]:


#VERSION 1


import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from msedge.selenium_tools import Edge, EdgeOptions 

#Function for getting multiple tweets

def get_tweet_data(card):
    username = card.find_element_by_xpath('.//span').text
    try:
        handle = card.find_element_by_xpath('.//span[contains(text(), "@")]').text
    except NoSuchElementException:
        return
    
    try:
        postdate = card.find_element_by_xpath('.//time').get_attribute('datetime')
    except NoSuchElementException:
        return
    
    comment = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
    responding = card.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
    text = comment + responding
    reply_cnt = card.find_element_by_xpath('.//div[@data-testid="reply"]').text
    retweet_cnt = card.find_element_by_xpath('.//div[@data-testid="retweet"]').text
    like_cnt = card.find_element_by_xpath('.//div[@data-testid="like"]').text
    
    tweet = (username, handle, postdate, text, reply_cnt, retweet_cnt, like_cnt)
    return tweet

#Starting webdriver (using microsoft Edge)
options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)

#Logging into Twitter
driver.get('https://twitter.com/login') 
driver.maximize_window()

username = driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
username.send_keys('Job_A98')

my_password = getpass() 

password = driver.find_element_by_xpath('//input[@name = "session[password]"]')
password.send_keys(my_password)
password.send_keys(Keys.RETURN) 
sleep(1) 

#Finding search input

search_input = driver.find_element_by_xpath('//input[@aria-label="Search query"]')
search_input.send_keys('#coronavaccin')
search_input.send_keys(Keys.RETURN)

#Going to "Latest" tab for historical data 

driver.find_element_by_link_text('Latest').click()  

#Get tweets on page 
data = []
tweet_ids = set() #Used in order to mitigate scraping duplicate tweets caused by possible increasing number of tweets per scroll 
last_position = driver.execute_script("return window.pageYOffset;") #For tracking scroll position, breaking out of loop if end is reached
scrolling = True

while scrolling:
    page_cards = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
    for card in page_cards[-15:]:
        tweet = get_tweet_data(card)
        if tweet:
            tweet_id = ''.join(tweet)
            if tweet_id not in tweet_ids:
                tweet_ids.add(tweet_id)    
                data.append(tweet)
            
            
    scroll_attempt = 0 #used as sometimes due to lag scrolling will not register, so we allow for number of scroll attempts
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1) #giving program time to load before scraping
        curr_position = driver.execute_script("return window.pageYOffset;")
        if last_position == curr_position: #breaks out of loop if current and last scroll positions are the same
            scroll_attempt += 1 
            if scroll_attempt >= 3:
                scrolling = False
                break
            else: 
                sleep(2) 
        else:
            last_position = curr_position
            break


# In[2]:


with open('coronavaccin_tweets.csv', 'w', newline='', encoding='utf-8') as f:
    header = ['UserName', 'Handle', 'Timestamp', 'Text', 'Reply count', 'Retweets', 'Like count']
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)


# # Version 2 
# 
# **This version is a slightly altered version to version 1. As we attempt to eventually analyze sentiment towards a coronavirus vaccin during a certain time window around each covid pressconference (also for feasability, as the total number of tweets from the start of covid till now would mean a large number of data entries), we require searching around specific dates. In order to achieve this, this version starts the browser through selenium and navigates to a custom made URL (as in the adv web scraping tutorial) which contains specific time windows, enables capturing Dutch tweets only and yields tweets that include a multitude of ways in which people could misspell "coronavaccin" in order to get an as complete picture as possible. None of these things are taken into account in Version 1.  
# 
# **The downside (?) to this approach is that we do need to re-run the scraper with a custom URL that captures the time windows around all previous press conferences. This would mean manually changing that URL for each time period and rerunning the scraper. 
# 
# **Entities captured in this version so far are: 
#     Tweet Text 
#     User Name
#     Twitter Handle
#     Retweet Count
#     Like Count

# In[6]:


#VERSION 2

# Testing the scraper without automatic login. Here we made a custom search URL and inserted it into driver.get
# The result should take into account specific dates posted (around the last persconferentie, Feb 22-24th 2021) and only contain Dutch tweets

import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from msedge.selenium_tools import Edge, EdgeOptions 

#Function for getting multiple tweets

def get_tweet_data(card):
    username = card.find_element_by_xpath('.//span').text
    try:
        handle = card.find_element_by_xpath('.//span[contains(text(), "@")]').text
    except NoSuchElementException:
        return
    
    try:
        postdate = card.find_element_by_xpath('.//time').get_attribute('datetime')
    except NoSuchElementException:
        return
    
    comment = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
    responding = card.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
    text = comment + responding
    reply_cnt = card.find_element_by_xpath('.//div[@data-testid="reply"]').text
    retweet_cnt = card.find_element_by_xpath('.//div[@data-testid="retweet"]').text
    like_cnt = card.find_element_by_xpath('.//div[@data-testid="like"]').text
    
    tweet = (username, handle, postdate, text, reply_cnt, retweet_cnt, like_cnt)
    return tweet

#Starting webdriver with Microsoft Edge
options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)

#Logging into Twitter
driver.get('https://twitter.com/search?q=(coronavaccin%20OR%20corona_vaccin%20OR%20covidvaccin%20OR%20covid_vaccin%20OR%20corona_vaccine%20OR%20coronavaccine%20OR%20covidvaccine%20OR%20covid_vaccine)%20lang%3Anl%20until%3A2021-02-24%20since%3A2021-02-22&src=typed_query&f=live') 
driver.maximize_window() 

#Get tweets on page 
data = []
tweet_ids = set() #Used in order to mitigate scraping duplicate tweets caused by possible increasing number of tweets per scroll 
last_position = driver.execute_script("return window.pageYOffset;") #For tracking scroll position, breaking out of loop if end is reached
scrolling = True

while scrolling:
    page_cards = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
    for card in page_cards[-15:]:
        tweet = get_tweet_data(card)
        if tweet:
            tweet_id = ''.join(tweet)
            if tweet_id not in tweet_ids:
                tweet_ids.add(tweet_id)    
                data.append(tweet)
            
            
    scroll_attempt = 0 #used as sometimes due to lag scrolling will not register, so we allow for number of scroll attempts
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1) #giving program time to load before scraping
        curr_position = driver.execute_script("return window.pageYOffset;")
        if last_position == curr_position: #breaks out of loop if current and last scroll positions are the same
            scroll_attempt += 1 
            if scroll_attempt >= 3:
                scrolling = False
                break
            else: 
                sleep(2) 
        else:
            last_position = curr_position
            break


# In[7]:


with open('coronavaccin_tweets.csv', 'w', newline='', encoding='utf-8') as f:
    header = ['UserName', 'Handle', 'Timestamp', 'Text', 'Reply count', 'Retweets', 'Like count']
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)


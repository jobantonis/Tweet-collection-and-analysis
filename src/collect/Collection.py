#!/usr/bin/env python
# coding: utf-8

# # Twitter scraper COVID vaccine press conferences within the Netherlands

# We built a Twitter scraper in order to find out the sentiment towards to COVID-19 vaccine in the Netherlands, within the time frames surrounding the Dutch governments' Press Conferences. Herewith we want to measure the influence of the regulations regarding COVID-19 on the attitude people have towards COVID-19 vaccines. 
# 
# Our scraper results in a CSV file, containing the following entities:
# - Dutch tweets containing the following keywords: *coronavaccin, corona_vaccin, covidvaccin, covid_vaccin, covid_vaccine, covidvaccine, coronavaccine, covid_vaccine*   
# - Specific dates the tweets were posted (around the persconferences (3 days before and 3 days after), *datums + timeframe n.t.b. https://www.rijksoverheid.nl/onderwerpen/coronavirus-covid-19/coronavirus-beeld-en-video/videos-persconferenties*) 
# - Content of the tweets
# - User ID *anoniem gemaakt d.m.v. ...*
# 
# ##Datum nog veranderen!!!

# For our code, we decided to use Selenium because Twitter is a dynamic webpage where we need to mimic scrolling like a Twitter user.
# Therefore, we first have to download and import some drivers and prerequisites.

# In[1]:


import csv
import selenium.webdriver   
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


# Then, we wrote a function in order to get multiple tweets. We used the .find()-function in order to find specific elements in the source code of the website. Below, we inserted 2 pictures, showing examples of how we found the specific elements (for username and comment). The '.text'-function makes sure we copy the text belonging to the element we were looking for.

# <img src="https://raw.githubusercontent.com/jobantonis/Tremendously-awesome-repository/main/Screenshot%202021-03-11%20at%2017.17.12.png" align="center" width=60%/>

# In[2]:


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
    #text = comment + responding
    reply_cnt = card.find_element_by_xpath('.//div[@data-testid="reply"]').text
    retweet_cnt = card.find_element_by_xpath('.//div[@data-testid="retweet"]').text
    like_cnt = card.find_element_by_xpath('.//div[@data-testid="like"]').text
    
    tweet = {'UserName':username, 
             'Handle':handle, 
             'Timestamp': postdate,
             'Comment': comment, 
             'Responding': responding, 
             'Reply count':reply_cnt, 
             'Retweets': retweet_cnt, 
             'Like count': like_cnt}
    return(tweet)


# We use Selenium, and therefore have to choose a browser in which we are going to open Twitter. We decided to use Chrome, so we set our Driver to Chrome.

# In[3]:


driver = selenium.webdriver.Chrome()


# First, we navigate to the login page, after which our credentials are put in. 

# In[4]:


driver.get('https://twitter.com/login') 
driver.maximize_window()

username = driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
username.send_keys('Job_A98')

my_password = getpass() 

password = driver.find_element_by_xpath('//input[@name = "session[password]"]')
password.send_keys(my_password)
password.send_keys(Keys.RETURN) 
sleep(1) 


# Then, we navigate to the search bar in the top right. There we fill in all relevant keywords, the time window selected (which is altered for a number of days aorund past COVID related press conferences) and specify to search for Dutch tweets only. 

# In[5]:


search_input = driver.find_element_by_xpath('//input[@aria-label="Search query"]')
search_input.send_keys('(vaccin OR vaccine OR coronavaccin OR corona_vaccin OR covidvaccin OR covid_vaccin OR corona_vaccine OR coronavaccine OR covidvaccine OR covid_vaccine) lang:nl until:2021-01-05 since:2021-01-03')
search_input.send_keys(Keys.RETURN)


# Following the input of our query, we head to the "latest" tab in order to capture all historical tweets instead of just the popular ones.

# In[6]:


driver.find_element_by_link_text('Latest').click()


# Next, we want to fill the data with our input. Therefore, we create a list called 'data'. Furthermore, since it is a dynamic website which is accessed through scrolling through the site, we want to make sure we do not add the same tweets twice, therefore the function set(), called tweet_ids is added. Lastly, we added a function that executes the script and stops when we are at the last page. 

# In[7]:


data = [] #needed to fill a string with data
tweet_ids = set() #Used in order to mitigate scraping duplicate tweets caused by possible increasing number of tweets per scroll 
last_position = driver.execute_script("return window.pageYOffset;") #For tracking scroll position, breaking out of loop if end is reached
scrolling = True


# While scrolling, we want to make sure to capture our data from the tweets we encounter. After that, we actually begin to scroll down the pages. Since we are aware that there is a possibility that our internet laggs in between because of poor internet connection, we made sure our scraper tries to scroll twice before it is disregarded.

# In[8]:


while scrolling:
    
    page_cards = driver.find_elements_by_xpath('//div[@data-testid="tweet"]') #First div with which the scraper encounters a tweet
    for card in page_cards[-15:]: # used -15, since we assume there are 15 tweets loaded each time
        tweet = get_tweet_data(card) #get 15 tweets per reload
        if tweet not in data:
            data.append(tweet)    
        
 #       if tweet:
 #           tweet_id = tweet #make 1 tweet of the separate words used in the tweet
 #           if tweet_id not in tweet_ids: #Make sure you do not capture the same tweet twice, by only appending tweets that you haven't added before. 
 #               tweet_ids.add(tweet_id) #to the set() function we add tweet_ids
 #               data.append(tweet) #add tweets to data list

    scroll_attempt = 0 #used as sometimes due to lag scrolling will not register, so we allow for number of scroll attempts
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1) #giving program time to load before scraping
        curr_position = driver.execute_script("return window.pageYOffset;")
        if last_position == curr_position: #breaks out of loop if current and last scroll positions are the same
            scroll_attempt += 1 
            #2 attempts to check if it is the end of the page, since it is also possible that the scraper laggs because of poor internet connection.
            if scroll_attempt >= 3: 
                scrolling = False
                break
            else: 
                sleep(2) 
        else:
            last_position = curr_position #makes sure the loop ends
            break


# Copy the data to a CSV file, creating headers and writing data towards the file using the following code:

# In[9]:


data


# In[12]:


len(data)


# In[11]:


with open("DataCollection_Twitter.csv", "w", newline="", encoding='utf-8') as csv_file:
  cols = ['UserName', 
             'Handle', 
             'Timestamp',
             'Comment', 
             'Responding', 
             'Reply count', 
             'Retweets', 
             'Like count'] 
  writer = csv.DictWriter(csv_file, fieldnames=cols, restval='MISSING')
  writer.writeheader()
  writer.writerows(data)


# In[ ]:





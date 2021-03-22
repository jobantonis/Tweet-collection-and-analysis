#!/usr/bin/env python
# coding: utf-8

# # Twitter scraper COVID vaccine press conferences within the Netherlands¶

# We built a Twitter scraper in order to find out the sentiment towards to COVID-19 vaccine in the Netherlands, within the time frames surrounding the Dutch governments' Press Conferences. Herewith we want to measure the influence of the regulations regarding COVID-19 on the attitude people have towards COVID-19 vaccines.
# 
# Our scraper results in a CSV file, containing the following entities:
# 
# - Dutch tweets containing the following keywords: coronavaccin, corona_vaccin, covidvaccin, covid_vaccin, covid_vaccine, covidvaccine, coronavaccine, covid_vaccine, vaccin and vaccine.
# - Specific dates the tweets were posted (around the persconferences (3 days before and 3 days after), datums + timeframe n.t.b. https://www.rijksoverheid.nl/onderwerpen/coronavirus-covid-19/coronavirus-beeld-en-video/videos-persconferenties)
# - Content of the tweets
# - User information
# 

# For our code, we decided to use Selenium because Twitter is a dynamic webpage where we need to mimic scrolling like a Twitter user. Therefore, we first have to download and import some drivers and prerequisites. The prerequisite "custom_urls" is another python file that stores all custom URLS that our scraper uses to include tweets over specific periods of time and searched on certain keywords.

# In[1]:


import csv
import selenium.webdriver 
import custom_urls
from tqdm import tqdm
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


# Then, we wrote a function in order to get multiple tweets. We used the .find()-function in order to find specific elements in the source code of the website. Below, we inserted 2 pictures, showing examples of how we found the specific elements (for username and comment). The '.text'-function makes sure we copy the text belonging to the element we were looking for.

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

# In[18]:


driver = selenium.webdriver.Chrome()


# Below, we navigate Twitter to the page we want to scrape. We built in the dates we want to scrape and the keywords we are looking for. After this, we maximize the window to make sure we capture the whole page. Because loading the browser might take some time, we insert sleep(5).

# In[19]:


driver.get('https://twitter.com/explore') 
driver.maximize_window() 
sleep(5)


# To actually capture the tweets from the page, we wrote the following code. This code searches for all the tweets on the loaded page. It also uses the previously written code 'get_tweet_data(card)', which makes sure the data captured in the tweet is captured.

# In[20]:


#function getting tweet data from page
data = []
def get_tweets():
    page_cards = driver.find_elements_by_xpath('//div[@data-testid="tweet"]') #First div with which the scraper encounters a tweet
    for card in page_cards[:len(page_cards)]:
        tweet = get_tweet_data(card) 
        if tweet:
            data.append(tweet)  


# Because Twitter is a dynamic website, we have to build a function which scrolls down the page automatically. 'driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')' makes sure the page is scrolled down until the site has to load again. Then we inserted sleep again, because it might take some time to load the page again. This makes sure our code will not continue while the page isn't fully loaded yet. Furthermore, we use 'last_position' and 'curr_position' to make sure a loop is build which scrolls down the page until the end. However, we are well aware that internet might lag and this could cause us to run out of the loop prematurily. Therefore, we allow a few scroll attempts before the code breaks (see: end of scroll region). Also, we have incorporated the previously written function 'get_tweets' into the code. Doing this makes sure the tweets are captured while scrolling. After this we also inserted some sleep time. Finally, we close the browser.

# In[21]:


#Function scroll code
def auto_scroll():
    scrolling = True
    scroll_attempt = 0
    last_position = driver.execute_script("return window.pageYOffset;")
    
    for query in tqdm(custom_urls.dates):
        search_input = driver.find_element_by_xpath('//input[@aria-label="Search query"]')
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)
        driver.find_element_by_link_text('Latest').click()
        sleep(5)
    
        while True:
            #check scroll position
            get_tweets() #getting tweets while we scroll
	    sleep(2)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(5) #giving program time to load before scraping
            curr_position = driver.execute_script("return window.pageYOffset;")
            if last_position == curr_position: #breaks out of loop if current and last scroll positions are the same
                scroll_attempt += 1 
           
                #end of scroll region
                if scroll_attempt >= 3: 
                    scrolling = False
                    break #Here: it makes sure the loop is ended
                else:
                    sleep(2) # attempt another scroll
            else:
                last_position = curr_position 
                continue
        print("Onto the next set of dates")
        driver.back()
    print("Done!")
    


# In[22]:


auto_scroll() # Run the scroll function


# In[23]:


len(data)


# In[9]:


data


# After the above code has run fully, we want to store the data into a CSV-file. Therefore we use the following code, which writes the data captured into a nicely structured CSV-file. 

# In[24]:


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


# The final step is to upload the data captured to a cloud. This is important, because this makes sure it is available, even if your computer crashes for example. For this code, Google Sheets is chosen. 

# In[95]:


# Important!! Need to have the client file for this!


# In[25]:


import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open('CSV-to-Google-Sheet')

with open('DataCollection_Twitter.csv', 'r', encoding='latin-1') as file_obj:
    content = file_obj.read()
    client.import_csv(spreadsheet.id, data=content)


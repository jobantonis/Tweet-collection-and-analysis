#!/usr/bin/env python
# coding: utf-8

# In[42]:


pip install tweepy


# In[33]:


####Twitter Test eigen timeline ####

import tweepy
import csv 
auth = tweepy.OAuthHandler("CN3wSkXrRLbDxfRN6tUxe7CWt", "oQ18k2fmHZjiiBUVljv3aVlroZXlKkPLXx1N6myTDI8XiVrTCF")
auth.set_access_token("286242148-T1eyfgST9y5SXMEY9BDySAS4QwlJjp5lLT9Y4dhO", "iUc5WKuqUY3iE6njrMp2WDpgwecrZRmUWTVBDiDG8nQep")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


# In[82]:


#### Collecting tweets met hashtag coronavaccine" ####
search_words = "vaccin"
search_noretweets = search_words + " -filter:retweets "
date_since = "2021-01-01"

tweets =tweepy.Cursor(api.search, 
                           q=search_noretweets,
                           lang= "nl",
                           since = date_since).items(10)

[tweet.text for tweet in tweets]
    
       


# In[ ]:


##### Collecting tweets met hashtag coronavaccine - test met csv bestand ####
search_words = "vaccin"
search_noretweets = search_words + " -filter:retweets "
date_since = "2021-01-01"
tweets = []

#Open csv bestand
with open("Tweepy_Output.csv", mode = "w", encoding="utf-8") as tweepy_file:

#Csv writer
    tweepy_writer = csv.writer(tweepy_file, delimiter=',')



    for tweet in tweepy.Cursor(api.search, 
                           q=search_noretweets,
                           lang= "nl",
                           since = date_since).items(10):
        tweets.append(tweet)
    
       
#Rij toevoegen aan bestand
        tweepy_writer.writerow(tweets)


# In[92]:


####Test met meerdere entities ####

# Collecting tweets met hashtag coronavaccine"
search_words = "vaccin"
search_noretweets = search_words + " -filter:retweets "
date_since = "2021-02-14"

tweets = tweepy.Cursor(api.search, 
                           q=search_noretweets,
                           lang= "nl",
                           since = date_since).items(10)

for tweet in tweets:
    print("Posted on:", tweet.created_at) 
    print("Text:", tweet.text)
    print("Liked:", tweet.favorited)
    print("Retweet count:", tweet.retweet_count)
    print("Twitter user ID:", tweet.id)
    


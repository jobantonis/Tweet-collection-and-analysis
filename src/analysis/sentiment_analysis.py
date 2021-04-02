#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os.path


#
path = os.path.abspath(os.path.join(os.getcwd(),'gen/data-preparation/output/tweet_data_cleaned.csv'))
tweets = pd.read_csv(path, encoding= 'unicode_escape')
#print(tweets)

date = tweets[['Timestamp']]
users = tweets[['UserName']]
comments = tweets.Comment_clean


# In[ ]:


# add comments to dictionary
comments.to_dict()


# Import Dutch sentiment-analysis
from pattern.nl import sentiment as sentiment_nl


# In[6]:


# Creating an empty list, then running a sentiment analysis on tweets in a particular range
new_comments = list()

counter = 0
while counter < len(comments):
    for comment in comments:
        if comment:
            polarity_nl, subjectivity_nl = sentiment_nl(comment)
            new_comments.append(comment)
            new_comments.append(polarity_nl)
        counter += 1


# In[7]:


# convert the new_comments list to a dictionary
import itertools
new_comments_iter = iter(new_comments)
new_comments_dict_object = itertools.zip_longest(new_comments_iter, new_comments_iter, fillvalue=None)
new_comments_dict = dict(new_comments_dict_object)


# In[8]:


new_comments_sub = list()

counter = 0
while counter < len(comments):
    for comment in comments:
        if comment:
            polarity_nl, subjectivity_nl = sentiment_nl(comment)
            new_comments_sub.append(comment)
            new_comments_sub.append(subjectivity_nl)
        counter += 1


# In[9]:


# convert the new_comments list to a dictionary
new_comments_iters = iter(new_comments_sub)
new_comments_dict_objects = itertools.zip_longest(new_comments_iters, new_comments_iters, fillvalue=None)
new_comments_dicts = dict(new_comments_dict_objects)


# In[ ]:


# Creation of final tweet file with all necessary components
tweets2 = pd.DataFrame(list(new_comments_dict.items()),columns = ['Comment','Polarity'])
tweets3 = pd.DataFrame(list(new_comments_dicts.items()),columns = ['Comment','Subjectivity'])
tweets_final = tweets2.join(date)
final_tweets = tweets_final.join(users)
final_tweets = final_tweets.merge(tweets3)

# In[13]:


#TIMESTAMP ADDED, writes to csv
final_tweets = final_tweets[["UserName", "Timestamp", "Comment", "Polarity", "Subjectivity"]]
path2 = os.path.abspath(os.path.join(os.getcwd(),'gen/analysis/output/sentiment_tweets.csv'))
final_tweets.to_csv (path2, index = False, header=True)


# In[ ]:





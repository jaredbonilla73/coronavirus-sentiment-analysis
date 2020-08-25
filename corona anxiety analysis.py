#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tweepy
from textblob import TextBlob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

consumer_key = 'FkfYnS5rj9J2W7Ri5qhqZIsXn'
consumer_secret = 'BhyKgm97vQRHYVJyG8hBlfeAgJQBnzISYqabXtfdbgfOZmXZRp'
access_token='421390178-e7O1PGG0DIOrCVNv0LWIpbCs6XZ93sgSzzjWNT6a'
access_token_secret ='Ry71JBO5RW3sLpW7TEakKOX8aXFMTOjB8vjJjZzsSN4D2'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


# In[4]:


anxiety_tweets = 'anxiety'
date = '2020-01-20'
tweets = tweepy.Cursor(api.search,
                      q=anxiety_tweets,
                      since=date).items()

new_list = []
for tweet in tweets:
    print(tweet.text)
    new_list.append(tweet.text)
    print('\n')    


# In[5]:


print(len(new_list))
print(new_list[0])


# In[6]:


#create df out of list of tweets
df= pd.DataFrame(new_list,columns=['Tweets'])
df.head()


# In[17]:


df = dfc.copy()


# In[18]:


#import regular expressions
#use regulaer expression to replace @ RT and hyperlinks
import re
def cleantxt(text):
    text = re.sub(r'@[A-za-z0-9]+','',text)
    text = re.sub(r'RT[\s]+','',text)
    text = re.sub(r'https?:\/\/\S+','',text)
    
    return text


# In[19]:


df['Tweets'] = df['Tweets'].apply(cleantxt)


# In[20]:


#create functions to assess subjectivity and polarity of tweets
def get_subjev(text):
    return TextBlob(text).sentiment.subjectivity

def get_polar(text):
    return TextBlob(text).sentiment.polarity


# In[21]:


df['Subjectivity']= df['Tweets'].apply(get_subjev)
df['Polarity']=df['Tweets'].apply(get_polar)
df.head()


# In[22]:


#for each word in tweets join on the white space
#create wordcloud
all_words = ''.join([twts for twts in df['Tweets']])
word_cloud = WordCloud(width=500,height=300,random_state=21,max_font_size=119).generate(all_words)

plt.imshow(word_cloud,interpolation='bilinear')
plt.axis('off')
plt.show()


# In[23]:


def analyze(score):
    if score<0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'
    
df['Analysis']=df['Polarity'].apply(analyze)
df.head()


# In[24]:


sorted_df = df.sort_values(by=['Polarity'],ascending=False)
sorted_df.head()


# In[27]:


#create df on only positive so sentiment analysis look for shape
positive_sentiment = df[df['Analysis'] == 'Positive']
positive_sentiment.shape


# In[ ]:





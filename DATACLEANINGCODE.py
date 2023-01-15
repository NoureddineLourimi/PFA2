#!/usr/bin/env python
# coding: utf-8

# Pandas, to open data files and to apply certain operations to the data.
# Html, to decode HTML entities into regular characters.
# Re, to filter and delete unnecessary links, hash, username, punctuations or whatever you wish.
# Nltk, to clean stopwords.

# In[1]:


import pandas as pd
import html
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# we need to import the Twitter data. in this case, I use CSV Twitter data

# In[2]:


pd.set_option(‘display.max_colwidth’, None)
data = pd.read_csv(‘your_sample.csv’)
data.head()


# Once we have imported the data, we’re now ready for the data cleaning process. The first things that we’re going to clean are data duplicates. Most of the time, we don’t need the data duplicates, because in further use (i.e. analysis) these data duplicates could mess up the result by messing up the measurement.

# In[3]:


new_data = data.drop_duplicates(‘Tweet Content’,keep=’first’) #delete the duplicates by dropping them and store the result value to a new variable
new_data.head()


# If your dataframe have indices included on it, once you drop those data duplicates, you need to store the new dataframe in a new file. Don’t forget to store the new dataframe to a new file without including the index on it, so that we could explore the data more freely later on.
# 
# We’re here assuming that we’re only going to use the tweets data, so we’re going to extract the tweets data out of the file.

# In[4]:


new_data.to_csv(r’your_new_sample.csv’, index = False)
new_sample = pd.read_csv(‘your_new_sample.csv’)
new_sample.head()
tweets = new_sample[‘Tweet Content’]
tweets.head()


# Once we extracted tweet data, we’ll notice things that need to be cleaned. Most of the time, the tweets returned by Twitter JSON data contain HTML entities and they need to be decoded into characters. So, we’re cleaning them using html library. Apart from that, we also need to clean up newlines since they make the data messy.

# In[5]:


for i in range (len(tweets)):
x = tweets[i].replace(“\n”,” “) #cleaning newline “\n” from the tweets
tweets[i] = html.unescape(x)
tweets.head()


# Sometimes when tweeting, Twitter users attach media like pictures, videos, etc. Those media will be converted into links on the JSON data. Since we’re only going to be using the text data, which is the tweets, so we need to clean up the links. Also, we will clean up hash characters (only the hash characters not the whole hashtags) and username. All those things will be cleaned using the regex Python library.

# In[6]:


for i in range (len(tweets)):
tweets[i] = re.sub(r”(@[A-Za-z0–9_]+)|[^\w\s]|#|http\S+”, “”, tweets[i])
tweets.head()


# Up till now, we already got much cleaner data, but there is one more thing that we need to do to make it even cleaner. In text-data, mostly it contains insignificant words that are not used for the analysis process because they could mess up the analysis score. So, we’re about to clean them now using the nltk Python library. There are several steps you need to do to remove the stopwords:

# - Preparing stopwords

# In[7]:


tweets_to_token = tweets
sw = stopwords.words(‘english’) #you can adjust the language as you desire
sw.remove(‘not’) #we exclude not from the stopwords corpus since removing not from the text will change the context of the text


# - Tokenize the tweets

# In[9]:


for i in range(len(tweets_to_token)):
tweets_to_token[i] = word_tokenize(tweets_to_token[i])


# - Remove the Stopwords
# 
# 

# In[10]:


for i in range(len(tweets_to_token)):
tweets_to_token[i] = [word for word in tweets_to_token[i] if not word in sw]
tweets_to_token


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[9]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '67a81f31-f7a1-4073-8b24-a4c4a87ccafc',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


# In[10]:


type(data)


# In[11]:


import pandas as pd


pd.set_option('display.max_columns', None)


# In[38]:


df = pd.json_normalize(data['data'])
df['timestamp'] = pd.to_datetime('now')
df


# In[45]:


# Automating the Above process

# creating a automative function

def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 
    #Original Sandbox Environment: 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'15',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '67a81f31-f7a1-4073-8b24-a4c4a87ccafc',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

#NOTE:
# I had to go in and put "jupyter notebook --NotebookApp.iopub_data_rate_limit=1e10"
# Into the Anaconda Prompt to change this to allow to pull data
    
    # Use this if you just want to keep it in a dataframe
    df = pd.json_normalize(data['data'])
    df['Timestamp'] = pd.to_datetime('now')
    df 

    if not os.path.isfile(r'/Users/sahildabgotra/Desktop/api/api.csv'):
        df.to_csv(r'/Users/sahildabgotra/Desktop/api/api.csv', header='column_names')
    else:
        df.to_csv(r'/Users/sahildabgotra/Desktop/api/api.csv', mode='a', header=False)
        



# In[46]:


import os 
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print('API Runner completed')
    sleep(60) #sleep for 1 minute
exit()


# In[35]:


df


# In[48]:


pd.set_option('display.float_format', lambda x:'%.5f' % x)


# In[49]:


df


# In[53]:


df3 = df.groupby('name', sort=False)[['quote.USD.percent_change_1h', 'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d']].mean()

df4 = df3.stack()
df4


# In[54]:


type(df4)


# In[57]:


df5 = df4.to_frame(name= 'values')
df5


# In[58]:


df5.count()


# In[62]:


index = pd.Index(range(90))

df6 = df5.reset_index()
df6


# In[76]:


df7 = df6.rename(columns={'level_1': 'percent_change'})
df7


# In[84]:


df7['percent_change'] = df7['percent_change'].replace(['quote.USD.percent_change_1h', 'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d'],['1hr', '24hr', '7d', '30d', '60d', '90d'])


# In[80]:


# creating visualizations

import seaborn as sns
import matplotlib.pyplot as plt



# In[85]:


sns.catplot(x = 'percent_change', y = 'values', hue='name', data = df7, kind = 'point')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





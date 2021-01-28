#!/usr/bin/env python
# coding: utf-8

# In[11]:


url1='https://timesofindia.indiatimes.com/india'
url2='https://timesofindia.indiatimes.com/world'
url3='https://timesofindia.indiatimes.com/world'
url4='https://timesofindia.indiatimes.com/' 



# In[31]:


import requests
from bs4 import BeautifulSoup
reqs=requests.get(url1)
soup=BeautifulSoup(reqs.text,'html.parser')
print('Title:')
for title in soup.find_all('title'):
    print(title.get_text())
print('Link:')
print(url1)
print('Date and time:')
print(soup.date   , soup.time)
print('Text:')
print(soup.text)


# In[33]:


import requests
from bs4 import BeautifulSoup
reqs=requests.get(url2)
soup=BeautifulSoup(reqs.text,'html.parser')
print('Title:')
for title in soup.find_all('title'):
    print(title.get_text())
print('Link:')
print(url2)
print('Date and time:')
print(soup.date   , soup.time)
print('Text:')
print(soup.text)


# In[34]:


import requests
from bs4 import BeautifulSoup
reqs=requests.get(url3)
soup=BeautifulSoup(reqs.text,'html.parser')
print('Title:')
for title in soup.find_all('title'):
    print(title.get_text())
print('Link:')
print(url3)
print('Date and time:')
print(soup.date   , soup.time)
print('Text:')
print(soup.text)


# In[32]:


import requests
from bs4 import BeautifulSoup
reqs=requests.get(url4)
soup=BeautifulSoup(reqs.text,'html.parser')
print('Title:')
for title in soup.find_all('title'):
    print(title.get_text())
print('Link:')
print(url4)
print('Date and time:')
print(soup.date   , soup.time)
print('Text:')
print(soup.text)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


from zipfile import ZipFile


# In[9]:


#Create a ZipFile Object and load sample.zip in it
with ZipFile('Appearances.csv.zip', 'r') as zipping:
   # Extract all the contents of zip file in current directory
   zipping.extract('Appearances.csv', 'Unzipped.csv')


# In[10]:


#Create a ZipFile Object and load sample.zip in it
with ZipFile('Batting.csv.zip', 'r') as zipping:
   # Extract all the contents of zip file in current directory
   zipping.extract('Batting.csv', 'Unzipped.csv')


# In[11]:


#Create a ZipFile Object and load sample.zip in it
with ZipFile('Fielding.csv.zip', 'r') as zipping:
   # Extract all the contents of zip file in current directory
   zipping.extract('Fielding.csv', 'Unzipped.csv')


# In[20]:


import requests
apikey = '6z3fk5cgBQUmGJB2bbg4ImahZBS37fUP'
#https://api.tomtom.com/map/1/tile/basic/main/0/0/0.png?view=Unified&key=6z3fk5cgBQUmGJB2bbg4ImahZBS37fUP
url = 'https://api.tomtom.com/map/1/tile/basic/main/0/0/0.png?view=Unified&key=apikey'
response = requests.get(url)
response


# In[ ]:





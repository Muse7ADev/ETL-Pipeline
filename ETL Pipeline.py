#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install psycopg2-binary


# In[1]:


#import librariesa
import pandas as pd # For data Extraction and Manipulation
import psycopg2 # For connecting Python to postgreSQL database
from sqlalchemy import create_engine # To efficiently manage and reuse the database connections


# In[2]:


# Get the data path and store it in data
data = pd.read_csv(r"C:\Users\Edu\Downloads\BG\BG\dataset\bg.csv")

# view the top five rows
data.head()


# In[3]:


# View the bottom five rows
data.tail()


# In[4]:


# Data Transformation
data.duplicated().sum() # check for duplicate data


# In[5]:


data.drop_duplicates(keep='first' , inplace=True) # remove duplicates if any and keep the first ones


# In[6]:


# check missing data
data.isnull().sum()


# In[16]:


data['brand'].fillna('unknown', inplace=True)
data['category_id'].fillna(0, inplace=True)
data['category_code'].fillna('unknown', inplace=True)
data['price'].fillna(0, inplace=True)
data['user_id'].fillna(0, inplace=True)


# In[12]:


data.isnull().sum()


# In[17]:


# database credentioals
username = 'postgres'
password = 'AmhkbwgA'
host = 'localhost'
port = 5432
db_name = 'postgres'


# In[18]:


# create connection
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{db_name}')


# In[19]:


# load database table
data.to_sql('electronics_Table', engine, if_exists='replace', index=False)

# close the connection
engine.dispose()


# In[ ]:





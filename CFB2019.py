#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


# In[4]:


df = pd.read_csv('CFB2019.csv')
df.head()


# In[5]:


df.info()


# In[11]:


dfn = df['Win-Loss'].str.split('-', expand = True)


# In[12]:


dfn.head()


# In[14]:


df['Win'] = dfn[0]
df['Loss'] = dfn[1]
df.drop(columns = ['Win-Loss'] , inplace = True)


# In[15]:


df.head()


# In[18]:


team = df['Team']
team.head()


# In[19]:


df[['Win']] = df[['Win']].apply(pd.to_numeric, errors = 'coerce')


# In[27]:


df[['Loss']] = df[['Loss']].apply(pd.to_numeric, errors = 'coerce')


# In[29]:


df_corr = df.corr()


# In[30]:


df_corr['Loss']


# In[35]:


plt.figure(figsize = (20,12))
sns.heatmap(df_corr)


# In[38]:


plt.figure(figsize = (20,12))
sns.heatmap(df_corr , cmap = 'YlGnBu' , annot = True)


# In[41]:


df_n =df_corr[df_corr['Win']> 0.7][['Games' , 'Off Rank', 'Off Plays', 'Off Yards']]
plt.figure(figsize = (20,12))
sns.heatmap(df_n , cmap = 'YlGnBu' , annot = True)


# In[42]:


sns.pairplot(df_n)


# In[ ]:





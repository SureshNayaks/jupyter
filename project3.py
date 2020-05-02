#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy
import matplotlib
import sklearn


# In[6]:


import pandas as pd


# In[49]:


import os


# In[50]:


dt = pd.read_excel("pro.xlsx")


# In[51]:


os.chdir("C:\\Users\HP\Desktop") 


# In[52]:


dt = pd.read_excel("pro.xlsx")


# In[54]:


dt


# In[47]:


import matplotlib.pyplot as plt
import numpy as np


# In[57]:


dt['AgeGroup'][1]


# In[ ]:





# In[58]:


dt['AgeGroup'][1]


# In[62]:


plt.bar(dt['AgeGroup'], dt['Percentage'])
plt.ylabel('some numbers')
plt.show()


# In[64]:


dt = pd.read_excel("covid_19_india.xlsx")


# In[65]:


dt


# In[66]:


group = dt.groupby('State/UnionTerritory')


# In[68]:


group.groups


# In[72]:



def group_by_date(dt)
    grouped = dt.groupby('Date')
    conformed_cases=0
    deaths=0
    cured=0
    for name,group in grouped:
       
    


# In[ ]:


def count(dt):
    conformed = 0
    death = 0
    cure = 0
    for 


# In[73]:


group


# In[74]:


plt.plot(group['State/UnionTerritory'], group['Confirmed'], 'r--', group['State/UnionTerritory'], group['Deaths'], 'bs', group['State/UnionTerritory'], group['Cured'], 'g^')
plt.show()


# In[ ]:


def group_by_date(dt):
    


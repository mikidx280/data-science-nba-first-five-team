#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
mpl.rcParams['figure.dpi'] = 500
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("df_the_org.csv")


# In[8]:


df = pd.read_csv("df_the_org.csv")


# In[9]:


df


# In[10]:


df[df.won > 0]


# In[6]:


sns.relplot(x=df["points"],y=df["minutes"], data=df,hue=df['position'],size=df['position'], sizes=(20, 100),style=df['won'])


# In[6]:


sns.violinplot(x=df['position'], y=df['games started'], data=df, hue=df['won'])


# In[7]:


df1 = pd.DataFrame(df, columns = ['age', 'games', 'minutes', 'points', 'Assists', 'R.total'])
sns.heatmap(df1.corr(), annot=True)


# In[8]:


ct1 = pd.crosstab(df['team name'],df['won'])
ct1


# In[9]:


ct2 = pd.crosstab(df['team name'], df['won'], normalize='index')
ct2


# In[10]:


ct2.plot(kind = 'bar', figsize=(10,4))
plt.title('team name vs. won', fontsize=12)
plt.xlabel('team name')
plt.ylabel('won')


# In[11]:


sns.barplot(x=df['position'], y=df['points'], hue=df['won'],data=df,ci=0,estimator=np.mean)


# In[12]:


sns.barplot(x=df['position'], y=df['R.total'], hue=df['won'],data=df,ci=0,estimator=np.mean)


# In[ ]:





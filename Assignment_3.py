#!/usr/bin/env python
# coding: utf-8

# # Assignment 3
# ## Data Merging and Exploratory Analysis

# In[4]:


import pandas as pd


# Loading all the csv files

# In[9]:


df1 = pd.read_csv('Sheet1.csv')


# In[11]:


df2 = pd.read_csv('Sheet2.csv')


# In[12]:


df3 = pd.read_csv('Sheet3.csv')


# In[13]:


df4 = pd.read_csv('Sheet4.csv')


# In[14]:


main_df = pd.read_csv('US_Accidents_Dec20_Updated_sheet1.csv')


# Checking the info of all the csv files.

# In[15]:


df1.info


# In[16]:


df2.info


# In[17]:


df3.info


# In[18]:


df4.info


# In[19]:


main_df.info


# All the columns in the datasets are same. Hence we can merge all the datasets in one for further analysis.

# In[20]:


df = pd.concat([df1,df2,df3,df4,main_df])


# In[21]:


df.info


# In[23]:


df.describe()


# In[27]:


df.columns


# #### Question1: Which city had the most amount of accidents?

# In[28]:


city_counts = df.City.value_counts()


# In[35]:


city_counts.head(10).index


# In[31]:


import seaborn as sns
import matplotlib 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[38]:


plt.figure(figsize=(12,8))
plt.xticks(rotation = 75)
plt.title("Number of Accidents in Cities")
sns.barplot(x = city_counts.head(20).index,y = city_counts.head(20));


# #### Ans1: From the above plot we can see that most amount of accidents happend in Houston city of Texes.

# ### Question2: Identify if there was any time of the year or day that had more reported accidents? Try to infer why?

# In[39]:


df.Start_Time


# In[48]:


df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')


# In[50]:


df['Year']= pd.DatetimeIndex(df.Start_Time).year


# In[83]:


df.Year.unique()


# In[52]:


df['Day']= pd.DatetimeIndex(df.Start_Time).day


# In[53]:


df.Day


# In[56]:


df['Date'] = pd.to_datetime(df['Start_Time']).dt.date
df['Time'] = pd.to_datetime(df['Start_Time']).dt.time


# In[66]:


def hr_func(ts):
    return ts.hour
df['Hour'] = df['Time'].apply(hr_func)


# In[77]:


df_Acci = df.value_counts(['Hour','Year']).reset_index(name='No_of_Accidents')


# In[126]:


df_Acci


# In[111]:


plt.figure(figsize = (19,9))
plt.title('Number of Accidents of Different years at all times')
sns.barplot(x = df_Acci.Hour, y = df_Acci.No_of_Accidents, hue = df_Acci.Year);


# #### Ans2: From the above plot we can see that most of the accidents happend between 6 to 8 and 15 to 17 i.e. most of the accidents happend during rush hour. Drivers who are running late to work in the morning or who are eager to get home in the evening, which can lead to unsafe driving.   

# In[113]:


df.columns


# ### Question3: Pick anyone of the factor(weather_condition, Sunrise_Sunset etc.) and Predict what effect it migh have had on the number of accidents. Comfirm with a visualization. Were you right and wrong?

# #### For the analysis I had choosen Sunrise_Sunset as factor. From the above result i predict that most of the accidents happened during day time.

# In[133]:


df_counts = df.groupby('Sunrise_Sunset').size().reset_index(name ='counts')


# In[134]:


df_counts


# In[170]:


colors = sns.color_palette('pastel')[1:5]
plt.pie(df_counts.counts , labels = df_counts.Sunrise_Sunset ,radius = 1.7, colors = colors , autopct = '%0.3f%%');


# #### Ans3: As per my prediction the most of the accidents happend during day time. The piechart comfirmed that my prediction is right. 
# End
#!/usr/bin/env python
# coding: utf-8

# #                     Assignment_1
# ##               Exploratory Data Analysis
# 

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


sales_df = pd.read_csv('sales_full_data.csv')


# #### Loading the provided dataset in Jupytor Notebook

# In[4]:


sales_df


# In[5]:


sales_df.info


# In[6]:


sales_df.describe()


# In[7]:


sales_df.columns = sales_df.columns.str.replace(' ','_')


# Replacing the spacing in the name of columns with the underscore for accessing the columns with their name.

# In[8]:


sales_df.columns


# In[9]:


df = sales_df.copy()


# Copying the Dataset to a another dataframe (df) before making changes to dataframe.

# In[10]:


df.info


# In[11]:


df.Order_Date


# In[12]:


df['Date'] = pd.to_datetime(df.Order_Date, errors ='coerce')


# Changing the dtype of Order_Date to datetime and making a new column name Date.

# In[13]:


df.Date


# In[14]:


df['month']=pd.DatetimeIndex(df.Date).month


# Creating the month columns from Date.

# In[15]:


df.month


# In[16]:


df


# In[17]:


df.Price_Each


# In[18]:


df['price'] = pd.to_numeric(df.Price_Each , errors = 'coerce')


# Changing the price dtype from object to numeric(float).

# In[19]:


df.price


# In[20]:


df['quantity']=pd.to_numeric(df.Quantity_Ordered, errors = 'coerce')


# Changing the Quantity_Ordered dtype from object to numeric(float).

# In[21]:


df.quantity


# In[22]:


df.drop(['Quantity_Ordered'],axis = 'columns',inplace = True)


# Droping the Columns which is of no use.

# In[23]:


df


# In[24]:


df['total_price'] = df.price*df.quantity


# Calculating the total price by multiplying the price and quantity.

# In[25]:


df.total_price


# In[26]:


month_df = df.groupby('month')[['price']].sum()


# Taking monthwise sum of sales.

# In[27]:


month_df


# ### Question1: Which month had the highest and lowest sales? What do you think the reason for this was? 

# In[28]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[29]:


plt.figure(figsize = (9,8))
plt.title("Months vs Total Sales in that Month")
x = month_df.index
y = month_df.price
sns.barplot(x=x,y=y);


# #### Ans1: From the above plot we can see that December has the highest sales. The reason would be the NewYear and Chrismas. People likes to buy Gift for their friends and new things for upcoming year.

# In[30]:


df


# In[31]:


df['date'] = pd.to_datetime(df['Date']).dt.date
df['time'] = pd.to_datetime(df['Date']).dt.time


# Seperating date and time for furthur analysis.

# In[32]:


df


# In[33]:


def hr_func(ts):
    return ts.hour
df['hour'] = df['time'].apply(hr_func)


# Converting the time in hour.

# In[34]:


df


# ### Question2: At what time of day would you put advertisements so that sales incre

# In[35]:


hour_df =df.hour.value_counts().rename_axis('hour').reset_index(name='No_of_Purchases')


# Counting the total number of purchases in that perticular hour.

# In[36]:


hour_df


# In[37]:


plt.figure(figsize = (12,8)) 
plt.title('Hourwise No of Purchases')
plt.xticks(rotation = 75)
sns.barplot(x =hour_df.hour,y = hour_df.No_of_Purchases);


# #### Ans2: From the above graph we can observe that most of the sales are between 8:00 to 23:00 . If we show ads between those hours more people will watch the advertisement and sales will increase.

# In[38]:


df['quantity'] = df['quantity'].fillna(0).astype(int)


# In[39]:


df.Product.unique()


# In[40]:


Max_df = df[['quantity','Product']]


# Making another dataframe with just quantity and Product columns.

# In[41]:


Max_df_copy = Max_df.copy()


# In[42]:


Max_df_copy


# In[43]:


Max_df_copy.value_counts()


# ## Question3: What products were sold the most?

# In[44]:


plt.figure(figsize = (15,8))
Max_df_copy.value_counts().plot(kind = 'bar')


# #### Ans3: From above plot we can observe that products:
#           Lightning Charging Cable      
#           USB-C Charging Cable          
#           Wired Headphones              
#           Apple Airpods Headphones      
#           AA Batteries (4-pack)         
#           AAA Batteries (4-pack)        
#           Bose SoundSport Headphones    
#           27in FHD Monitor               
#           iPhone                         
#           27in 4K Gaming Monitor         
#           34in Ultrawide Monitor         
#           Google Phone                   
#           Flatscreen TV                  
#           Macbook Pro Laptop
# #### Sold the most.

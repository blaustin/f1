#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd
import csv


# In[2]:


# functions

def get_sec(time_str):
    """Get seconds from time."""
    m, s = time_str.split(':')
    time = float(m) * 60 + float(s)
    return time


# In[3]:


#initialize driver classes

class Driver():
    def _init__(self, cum_time,retired):
        self.driver_rating = driver_rating
        self.total_time = None #INITIALIZE 0:00:00.00
        self.tire_wear = 0
        self.current_pos = 0
        
    def get_race(self,races):
        


# In[ ]:


# assign dataset names
race_names = ['Bahrian 2021','Emilia Romagna 2021','Portugal 2021','Espana 2021','Monaco 2021','Azerbaijan 2021','France 2021','Styria 2021','Austria 2021','Britain 2021','Hungary 2021','Dutch 2021','Italy 2021','Russia 2021','Turkey 2021','United States 2021','Mexico 2021','Sao Paolo 2021','Qatar 2021','Saudi Arabia 2021','Abu Dhabi 2021']
  
# create empty list
races = []
  
# append datasets into teh list
for i in range(len(race_names)):
    temp_df = pd.read_csv("races/"+race_names[i]+".csv")
    races.append(temp_df)
    


# In[21]:


x = races[0].loc[0,'3']

exec('%s = %d' % (name,))


# In[34]:


daniel = {}
hamilton = {}

for name in race_names:
    daniel[name] = {
        'cum_time' : list(),
        'position' : list()
    }


    hamilton[name] = {
        'cum_time' : list(),
        'position' : list()
    }  


# In[35]:


#x = float(races[0].loc[1,'3'])
    
#get cum_time for Daniel Ricciardo

temp_cum_time = []
num_laps = 57
cum_time = 0
for i in range(1,num_laps):
    cum_time += get_sec(races[0].loc[i,'3'])
    daniel[race_names[0]]['cum_time'].append(round(cum_time,3))
    
for i in range(1,num_laps):
    cum_time += get_sec(races[0].loc[i,'77'])
    hamilton[race_names[0]]['cum_time'].append(round(cum_time,3))
    


# In[39]:


first = np.array(daniel['Bahrian 2021']['cum_time'])
second = np.array(hamilton['Bahrian 2021']['cum_time'])
first - second


# In[28]:


lap_data = open("races/bahrian 2021.csv")
reader = csv.DictReader(lap_data)
for col in reader:
    print(type(col['3']))


# In[ ]:


def load_data():
    """
    Load data from CSV files into `people` and `movies` dictionaries
    """

    # Load people
    with open(f"lap_data.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            id = int(row["id"])
            people[id] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set(),
                "visited": False
            }


#!/usr/bin/env python
# coding: utf-8

# In[1]:


#IMPORTANT - Daniel
from zipfile import ZipFile


#Create a ZipFile Object and load sample.zip in it
with ZipFile('Appearances.csv.zip', 'r') as zipping:
   # Extract all the contents of zip file in current directory
   zipping.extract('Appearances.csv', 'Unzipped.csv')


#Create a ZipFile Object and load sample.zip in it
with ZipFile('Batting.csv.zip', 'r') as zipping:
   # Extract all the contents of zip file in current directory
   zipping.extract('Batting.csv', 'Unzipped.csv')


#Create a ZipFile Object and load sample.zip in it
with ZipFile('Fielding.csv.zip', 'r') as zipping:
   # Extract all the contents of zip file in current directory
   zipping.extract('Fielding.csv', 'Unzipped.csv')


# In[2]:


# In[2]: - Dylan


#IMPORTANT
import pandas as pd
import numpy as np

import warnings 
warnings.filterwarnings('ignore')

##Import all of the csv files needed and convert them to dataframes
pitching = pd.read_csv('Pitching.csv')
people = pd.read_csv('People.csv')
batting = pd.read_csv('Unzipped.csv/Batting.csv')
batting_df = pd.DataFrame(batting)
people_df = pd.DataFrame(people)
pitching_df = pd.DataFrame(pitching)


people_batting_df = pd.merge(people_df, batting_df, how='inner', on='playerID')

people_pitching_df = pd.merge(people_df, pitching_df, how='inner', on='playerID')

##Creates a list of countries and states
countries = people['birthCountry'].drop_duplicates().to_list()
states = people['birthState'].drop_duplicates().to_list()


# In[3]:


# In[4]: - Dylan


#IMPORTANT

#creates dataframe for country pitching stats
pitching_country_df = people_pitching_df.iloc[0:0]
pitching_country_df['country'] = people['birthCountry'].drop_duplicates()
pitching_country_df = pitching_country_df.reset_index(drop=True)
pitching_country_df = pitching_country_df.drop(columns=['playerID', 'birthYear', 'birthMonth', 'birthDay', 'birthCountry', 'birthState', 'birthCity', 'deathYear', 'deathMonth', 'deathDay', 'deathCountry', 'deathState', 'deathCity', 'nameFirst', 'nameLast', 'nameGiven', 'weight', 'height', 'bats', 'throws', 'debut', 'finalGame', 'retroID', 'bbrefID', 'yearID', 'stint', 'teamID', 'lgID'])
pitching_country_df = pitching_country_df.set_index('country')

#create a list of pitching stats we want to record
pitching_stats = list(pitching_country_df.columns)

#complete country pitcher dataframe
for country in countries:
    data = people_pitching_df.loc[people_pitching_df['birthCountry'] == country]
    for stat in pitching_stats:
        stat_total = str(data[stat].sum())
        pitching_country_df.loc[country, stat] = stat_total


# In[4]:


#Gets ERA - Dylan
for country in countries:
    IPouts = int(pitching_country_df.loc[country, 'IPouts'])
    ER = int(pitching_country_df.loc[country, 'ER'])
    try:
        ERA = (ER*9)/(IPouts/3)
    except ZeroDivisionError:
        ERA = 0
    pitching_country_df.loc[country,'ERA'] = ERA


# In[5]:


#Gets WHIP - Daniel
for country in countries:
    IPouts = int(pitching_country_df.loc[country, 'IPouts'])
    hits = int(pitching_country_df.loc[country, 'H'])
    walks = int(pitching_country_df.loc[country, 'BB'])
    try:
        WHIP = (walks + hits) / (IPouts/3)
    except ZeroDivisionError:
        ERA = 0
    pitching_country_df.loc[country,'WHIP'] = WHIP


# In[6]:


pitching_country_df


# In[7]:


#creates dataframe for country batting stats - Dylan
batting_country_df = people_batting_df.iloc[0:0]
batting_country_df['country'] = people['birthCountry'].drop_duplicates()
batting_country_df = batting_country_df.reset_index(drop=True)
batting_country_df = batting_country_df.drop(columns=['playerID','birthYear','birthMonth','birthDay','birthCountry','birthState','birthCity','deathYear','deathMonth','deathDay','deathCountry','deathState','deathCity','nameFirst','nameLast','nameGiven','weight','height','bats','throws','debut','finalGame','retroID','bbrefID','yearID','stint','teamID','lgID'])
batting_country_df = batting_country_df.set_index('country')

#create a list of batting stats we want to record
batting_stats = list(batting_country_df.columns)

#complete country batting dataframe
for country in countries:
    data = people_batting_df.loc[people_batting_df['birthCountry'] == country]
    for stat in batting_stats:
        stat_total = str(data[stat].sum())
        batting_country_df.loc[country, stat] = stat_total


# In[8]:


#Gets batting avg - Daniel
for country in countries:
    hits = int(batting_country_df.loc[country, 'H'])
    ab = int(batting_country_df.loc[country, 'AB'])
    try:
        AVG = hits/ab
    except ZeroDivisionError:
        AVG = 0
    batting_country_df.loc[country, 'AVG'] = AVG


# In[9]:


#Gets OBP - Daniel
for country in countries:
    hits = int(batting_country_df.loc[country, 'H'])
    walks = int(batting_country_df.loc[country, 'BB'])
    hbp = float(batting_country_df.loc[country, 'HBP'])
    ab = int(batting_country_df.loc[country, 'AB'])
    sacfly = float(batting_country_df.loc[country, 'SF'])
    try:
        OBP = (hits + walks + hbp) / (ab + walks + hbp + sacfly)
    except ZeroDivisionError:
        AVG = 0
    batting_country_df.loc[country, 'OBP'] = OBP


# In[10]:


#Gets SLG - Daniel
for country in countries:
    hits = int(batting_country_df.loc[country, 'H'])
    double = int(batting_country_df.loc[country, '2B'])
    triple = int(batting_country_df.loc[country, '3B'])
    hr = int(batting_country_df.loc[country, 'HR'])
    single = int(hits - (double + triple + hr))
    ab = int(batting_country_df.loc[country, 'AB'])
    total_bases = int(single + (2 * double) + (3 * triple) + (4 * hr))
    try:
        SLG = total_bases / ab
    except ZeroDivisionError:
        SLG = 0
    batting_country_df.loc[country, 'SLG'] = SLG


# In[11]:


#Gets OPS - Daniel
for country in countries:
    #OBP data
    hits = int(batting_country_df.loc[country, 'H'])
    walks = int(batting_country_df.loc[country, 'BB'])
    hbp = float(batting_country_df.loc[country, 'HBP'])
    ab = int(batting_country_df.loc[country, 'AB'])
    sacfly = float(batting_country_df.loc[country, 'SF'])
    try:
        OBP = (hits + walks + hbp) / (ab + walks + hbp + sacfly)
    except ZeroDivisionError:
        AVG = 0
    batting_country_df.loc[country, 'OBP'] = OBP
    #SLG data
    hits = int(batting_country_df.loc[country, 'H'])
    double = int(batting_country_df.loc[country, '2B'])
    triple = int(batting_country_df.loc[country, '3B'])
    hr = int(batting_country_df.loc[country, 'HR'])
    single = int(hits - (double + triple + hr))
    ab = int(batting_country_df.loc[country, 'AB'])
    total_bases = int(single + (2 * double) + (3 * triple) + (4 * hr))
    try:
        SLG = total_bases / ab
    except ZeroDivisionError:
        SLG = 0
    batting_country_df.loc[country, 'SLG'] = SLG
    
    OPS = OBP + SLG
    batting_country_df.loc[country, 'OPS'] = OPS


# In[12]:


batting_country_df


# In[13]:


import folium
import json


# In[19]:


CENTER_US = (39.8333333,-98.585522)
state_geojson = 'custom.geo.json'
map = folium.Map(location=CENTER_US, zoom_start=4, tiles='Open Street Map') #blank map format

folium.Choropleth(geo_data=state_geojson, 
                  data=batting_country_df,
                  columns=['country', 'HR'],
                  key_on ='feature.id',
                  fill_color='YlOrRd',
                  legend_name='Country Home Run Total').add_to(map)

for row in batting_country_df.to_records(): # loop for each row(state)
    pos = (row['Latitude'], row['Longitude'])
    message = f"{row['HR']}%"
    fill_color = 'YlOrRd'
    marker = folium.Marker(location=pos, popup=message)
    map.add_child(marker)
map #finding map of pop change


# In[ ]:





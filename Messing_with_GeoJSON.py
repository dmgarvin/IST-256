#!/usr/bin/env python
# coding: utf-8

# In[1]:


#IMPORTANT
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


#creates dataframe for country pitching stats
pitching_country_df = people_pitching_df.iloc[0:0]
pitching_country_df['country'] = people['birthCountry'].drop_duplicates()
pitching_country_df = pitching_country_df.reset_index(drop=True)
pitching_country_df = pitching_country_df.drop(columns=['playerID', 'birthYear', 'birthMonth', 'birthDay', 'birthCountry', 'birthState', 'birthCity', 'deathYear', 'deathMonth', 'deathDay', 'deathCountry', 'deathState', 'deathCity', 'nameFirst', 'nameLast', 'nameGiven', 'weight', 'height', 'bats', 'throws', 'debut', 'finalGame', 'retroID', 'bbrefID', 'yearID', 'stint', 'teamID', 'lgID'])
pitching_country_df = pitching_country_df.set_index('country')


# In[35]:


#create a list of pitching stats we want to record
pitching_stats = list(pitching_country_df.columns)


# In[5]:


#complete country pitcher dataframe
for country in countries:
    data = people_pitching_df.loc[people_pitching_df['birthCountry'] == country]
    for stat in pitching_stats:
        stat_total = str(data[stat].sum())
        pitching_country_df.loc[country, stat] = stat_total


# In[6]:


#Gets ERA
for country in countries:
    IPouts = int(pitching_country_df.loc[country, 'IPouts'])
    ER = int(pitching_country_df.loc[country, 'ER'])
    try:
        ERA = (ER*9)/(IPouts/3)
    except ZeroDivisionError:
        ERA = 0
    pitching_country_df.loc[country,'ERA'] = ERA


# In[7]:


#creates dataframe for country batting stats
batting_country_df = people_batting_df.iloc[0:0]
batting_country_df['country'] = people['birthCountry'].drop_duplicates()
batting_country_df = batting_country_df.reset_index(drop=True)
batting_country_df = batting_country_df.drop(columns=['playerID','birthYear','birthMonth','birthDay','birthCountry','birthState','birthCity','deathYear','deathMonth','deathDay','deathCountry','deathState','deathCity','nameFirst','nameLast','nameGiven','weight','height','bats','throws','debut','finalGame','retroID','bbrefID','yearID','stint','teamID','lgID'])
batting_country_df = batting_country_df.set_index('country')


# In[8]:


#create a list of batting stats we want to record
batting_stats = list(batting_country_df.columns)


# In[9]:


#complete country batting dataframe
for country in countries:
    data = people_batting_df.loc[people_batting_df['birthCountry'] == country]
    for stat in batting_stats:
        stat_total = str(data[stat].sum())
        batting_country_df.loc[country, stat] = stat_total


# In[36]:


#creates dataframe for country pitching stats
pitching_state_df = people_pitching_df.iloc[0:0]
pitching_state_df['state'] = people['birthState'].drop_duplicates()
pitching_state_df = pitching_state_df.reset_index(drop=True)
pitching_state_df = pitching_state_df.drop(columns=['playerID', 'birthYear', 'birthMonth', 'birthDay', 'birthCountry', 'birthState', 'birthCity', 'deathYear', 'deathMonth', 'deathDay', 'deathCountry', 'deathState', 'deathCity', 'nameFirst', 'nameLast', 'nameGiven', 'weight', 'height', 'bats', 'throws', 'debut', 'finalGame', 'retroID', 'bbrefID', 'yearID', 'stint', 'teamID', 'lgID'])
pitching_state_df['State'] = pitching_state_df['state']
pitching_state_df = pitching_state_df.set_index('state')


# In[38]:


pitching_state_df


# In[39]:


batting_state_df


# In[40]:


#create a list of pitching stats we want to record
pitching_stats = list(pitching_country_df.columns)


# In[41]:


#complete state pitcher dataframe
for state in states:
    data = people_pitching_df.loc[people_pitching_df['birthState'] == state]
    for stat in pitching_stats:
        stat_total = str(data[stat].sum())
        pitching_state_df.loc[state, stat] = stat_total


# In[42]:


#Gets ERA
for state in states:
    IPouts = int(pitching_state_df.loc[state, 'IPouts'])
    ER = int(pitching_state_df.loc[state, 'ER'])
    try:
        ERA = (ER*9)/(IPouts/3)
    except ZeroDivisionError:
        ERA = 0
    pitching_state_df.loc[state,'ERA'] = ERA


# In[43]:


#creates dataframe for country batting stats
batting_state_df = people_batting_df.iloc[0:0]
batting_state_df['state'] = people['birthState'].drop_duplicates()
batting_state_df = batting_state_df.reset_index(drop=True)
batting_state_df = batting_state_df.drop(columns=['playerID','birthYear','birthMonth','birthDay','birthCountry','birthState','birthCity','deathYear','deathMonth','deathDay','deathCountry','deathState','deathCity','nameFirst','nameLast','nameGiven','weight','height','bats','throws','debut','finalGame','retroID','bbrefID','yearID','stint','teamID','lgID'])
batting_state_df['State'] = batting_state_df['state']
batting_state_df = batting_state_df.set_index('state')


# In[44]:


#create a list of batting stats we want to record
batting_stats = list(batting_country_df.columns)


# In[45]:


#complete state batting dataframe
for state in states:
    data = people_batting_df.loc[people_batting_df['birthState'] == state]
    for stat in batting_stats:
        stat_total = str(data[stat].sum())
        batting_state_df.loc[state, stat] = stat_total


# In[46]:


#complete state pitching dataframe
for state in states:
    data = people_pitching_df.loc[people_pitching_df['birthState'] == state]
    for stat in pitching_stats:
        stat_total = str(data[stat].sum())
        pitching_state_df.loc[state, stat] = stat_total


# In[20]:


#Gets batting avg
for state in states:
    hits = int(batting_state_df.loc[state, 'H'])
    ab = int(batting_state_df.loc[state, 'AB'])
    try:
        AVG = hits/ab
    except ZeroDivisionError:
        AVG = 0
    batting_state_df.loc[state, 'AVG'] = AVG


# In[21]:


#Gets OBP - Daniel
for state in states:
    hits = int(batting_state_df.loc[state, 'H'])
    walks = int(batting_state_df.loc[state, 'BB'])
    hbp = float(batting_state_df.loc[state, 'HBP'])
    ab = int(batting_state_df.loc[state, 'AB'])
    sacfly = float(batting_state_df.loc[state, 'SF'])
    try:
        OBP = (hits + walks + hbp) / (ab + walks + hbp + sacfly)
    except ZeroDivisionError:
        AVG = 0
    batting_state_df.loc[state, 'OBP'] = OBP


# In[22]:


#Gets SLG - Daniel
for state in states:
    hits = int(batting_state_df.loc[state, 'H'])
    double = int(batting_state_df.loc[state, '2B'])
    triple = int(batting_state_df.loc[state, '3B'])
    hr = int(batting_state_df.loc[state, 'HR'])
    single = int(hits - (double + triple + hr))
    ab = int(batting_state_df.loc[state, 'AB'])
    total_bases = int(single + (2 * double) + (3 * triple) + (4 * hr))
    try:
        SLG = total_bases / ab
    except ZeroDivisionError:
        SLG = 0
    batting_state_df.loc[state, 'SLG'] = SLG


# In[23]:


#Gets OPS - Daniel
for state in states:
    #OBP data
    hits = int(batting_state_df.loc[state, 'H'])
    walks = int(batting_state_df.loc[state, 'BB'])
    hbp = float(batting_state_df.loc[state, 'HBP'])
    ab = int(batting_state_df.loc[state, 'AB'])
    sacfly = float(batting_state_df.loc[state, 'SF'])
    try:
        OBP = (hits + walks + hbp) / (ab + walks + hbp + sacfly)
    except ZeroDivisionError:
        AVG = 0
    batting_state_df.loc[state, 'OBP'] = OBP
    #SLG data
    hits = int(batting_state_df.loc[state, 'H'])
    double = int(batting_state_df.loc[state, '2B'])
    triple = int(batting_state_df.loc[state, '3B'])
    hr = int(batting_state_df.loc[state, 'HR'])
    single = int(hits - (double + triple + hr))
    ab = int(batting_state_df.loc[state, 'AB'])
    total_bases = int(single + (2 * double) + (3 * triple) + (4 * hr))
    try:
        SLG = total_bases / ab
    except ZeroDivisionError:
        SLG = 0
    batting_state_df.loc[state, 'SLG'] = SLG
    
    OPS = OBP + SLG
    batting_state_df.loc[state, 'OPS'] = OPS


# In[52]:


pitching_state_df


# In[24]:


us_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

us_states_df = batting_state_df.iloc[0:0]

for state in us_states:
    data = batting_state_df[batting_state_df['State'] == state]
    us_states_df = us_states_df.append(data)


# In[57]:


import pandas as pd
import numpy as np
import folium
import warnings
import json

#map for hitting statistics
statistic = input('Input the statistic you want graphed: ')

us_states_df['Code'] = us_states_df['State']

geo = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/usa/geographic-centers.csv')

new_us_states_df = pd.merge(us_states_df, geo, on='Code')

  
#import map of the states
CENTER_US = (39.8333333,-98.585522)
london = (51.5074, -0.1278)
map = folium.Map(location=CENTER_US, zoom_start=4)

#Insert the markers onto the map
for row in new_us_states_df.to_records():
    pos = (int(row['Latitude']), int(row['Longitude']))
    message = f"{row['Code']} {statistic}: {row[statistic]}"
    marker = folium.Marker(location = pos, popup=message)
    new_map = map.add_child(marker)    
    
    
    
with open("NYC4-us-states.json") as file:
    state_geo = json.load(file)

choropleth = folium.Choropleth(
    geo_data=state_geo,
    data = new_us_states_df,
    fill_color = 'YlOrRd',
    key_on = 'feature.id',
    fill_opacity=0.7,
    line_opacity=0.2,
    columns= ["Code", statistic]
).add_to(map)

map


# In[48]:


p_us_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

p_us_states_df = pitching_state_df.iloc[0:0]

for state in us_states:
    data = pitching_state_df[pitching_state_df['State'] == state]
    p_us_states_df = p_us_states_df.append(data)


# In[53]:


#map for pitching stats
p_statistic = input('Input the statistic you want graphed: ')

p_us_states_df['Code'] = p_us_states_df['State']

geo = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/usa/geographic-centers.csv')

p_new_us_states_df = pd.merge(p_us_states_df, geo, on='Code')

  
#import map of the states
CENTER_US = (39.8333333,-98.585522)
london = (51.5074, -0.1278)
map = folium.Map(location=CENTER_US, zoom_start=4)

#Insert the markers onto the map
for row in p_new_us_states_df.to_records():
    pos = (int(row['Latitude']), int(row['Longitude']))
    message = f"{row['Code']} {p_statistic}: {row[p_statistic]}"
    marker = folium.Marker(location = pos, popup=message)
    new_map = map.add_child(marker)    
    
    
    
with open("NYC4-us-states.json") as file:
    state_geo = json.load(file)

choropleth = folium.Choropleth(
    geo_data=state_geo,
    data = p_new_us_states_df,
    fill_color = 'YlOrRd',
    key_on = 'feature.id',
    fill_opacity=0.7,
    line_opacity=0.2,
    columns= ["Code", p_statistic]
).add_to(map)

map


# In[1]:


#worked on a global geojson map, had issues with the map appearing so we stuck with US only


# In[ ]:


import folium
import pandas as pd
import json
filename = 'custom.geo.json'
f = open(filename,)
borders = json.loads(f)
borders
# Step 2: Write your code here
population_data = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/usa/us-pop-estimates-2010-2016.csv', dtype = {'2010': int, '2016': int} )
geography_data = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/usa/geographic-centers.csv')
merged_data = population_data.merge(geography_data, how='inner', on='Code') #used help for format
merged_data['pop_change_pct'] = (100 * (merged_data['2016'] - merged_data['2010']) / merged_data['2010'])
merged_df = pd.DataFrame(merged_data)
merged_df #finds pct change and adds to dataframe
#creating map of data
CENTER_US = (39.8333333,-98.585522)
state_geojson = 'custom.geo.json'
map = folium.Map(location=CENTER_US, zoom_start=4, tiles='Open Street Map') #blank map format

folium.Choropleth(geo_data=state_geojson, data=merged_df,
                 columns=['Code', 'pop_change_pct'], key_on ='feature.id', fill_color='YlOrRd',
                 legend_name='2010 to 2016 Population Pct. Change').add_to(map)

for row in merged_df.to_records(): # loop for each row(state)
    pos = (row['Latitude'], row['Longitude'])
    message = f"{row['pop_change_pct']}%"
    fill_color = 'YlOrRd'
    marker = folium.Marker(location=pos, popup=message)
    map.add_child(marker)
map #finding map of pop change
pip install datapackage
from datapackage import Package

package = Package('https://datahub.io/core/geo-countries/datapackage.json')

# print list of all resources:
print(package.resource_names)

# print processed tabular data (if exists any)
for resource in package.resources:
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        print(resource.read())

data = json.load('geo-countries_zip')
data


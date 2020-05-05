#!/usr/bin/env python
# coding: utf-8

# In[110]:


#imports for the code
import pandas as pd
import numpy as np
import folium
import warnings
import json


# In[37]:


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


# In[38]:


#Retrieve Data
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

#Combines a player's statistics with their personal information
people_batting_df = pd.merge(people_df, batting_df, how='inner', on='playerID')

people_pitching_df = pd.merge(people_df, pitching_df, how='inner', on='playerID')

##Creates a list of countries and states
countries = people['birthCountry'].drop_duplicates().to_list()
states = people['birthState'].drop_duplicates().to_list()
us_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

##Imports the geodata that will be used later for the chloropleth
geo = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/usa/geographic-centers.csv')


# In[103]:


#State Pitching Stats

#creates dataframe for state pitching stats
pitching_state_df = people_pitching_df.iloc[0:0]
pitching_state_df['state'] = people['birthState'].drop_duplicates()
pitching_state_df = pitching_state_df.reset_index(drop=True)
pitching_state_df = pitching_state_df.drop(columns=['playerID', 'birthYear', 'birthMonth', 'birthDay', 'birthCountry', 'birthState', 'birthCity', 'deathYear', 'deathMonth', 'deathDay', 'deathCountry', 'deathState', 'deathCity', 'nameFirst', 'nameLast', 'nameGiven', 'weight', 'height', 'bats', 'throws', 'debut', 'finalGame', 'retroID', 'bbrefID', 'yearID', 'stint', 'teamID', 'lgID', 'BAOpp'])
pitching_state_df = pitching_state_df.set_index('state')

#create a list of pitching stats we want to record
pitching_stats = list(pitching_state_df.columns)



#complete state pitcher dataframe
for state in states:
    data = people_pitching_df.loc[people_pitching_df['birthState'] == state]
    for stat in pitching_stats:
        stat_total = int(data[stat].sum())
        pitching_state_df.loc[state, stat] = stat_total
#Gets ERA
for state in states:
    IPouts = int(pitching_state_df.loc[state, 'IPouts'])
    ER = int(pitching_state_df.loc[state, 'ER'])
    try:
        ERA = (ER*9)/(IPouts/3)
    except ZeroDivisionError:
        ERA = 0
    pitching_state_df.loc[state,'ERA'] = ERA

    
#Creates a column to merge the geodata and baseball stats on
pitching_state_df = pitching_state_df.reset_index()
pitching_state_df['Code'] = pitching_state_df['state']
pitching_state_df = pitching_state_df.set_index('state')

#Creates a new dataframe that only includes the US states
us_states_pitching_df = pitching_state_df.iloc[0:0]

for state in us_states:
    data = pitching_state_df[pitching_state_df['Code'] == state]
    us_states_pitching_df = us_states_pitching_df.append(data)
    
    
#Merges the geo data with the US states pitching data
new_us_states_pitching_df = pd.merge(us_states_pitching_df, geo, on='Code')

#Creates new columns that contain the rank of each state in regards to a particular stat
for stat in pitching_stats:
    stat_name = stat + 'Rank'
    new_us_states_pitching_df[stat_name] = new_us_states_pitching_df[stat].rank(method='average',ascending=False)


# In[107]:


#State Batting Stats

batting_state_df = people_batting_df.iloc[0:0]
batting_state_df['state'] = people['birthState'].drop_duplicates()
batting_state_df = batting_state_df.reset_index(drop=True)
batting_state_df = batting_state_df.drop(columns=['playerID','birthYear','birthMonth','birthDay','birthCountry','birthState','birthCity','deathYear','deathMonth','deathDay','deathCountry','deathState','deathCity','nameFirst','nameLast','nameGiven','weight','height','bats','throws','debut','finalGame','retroID','bbrefID','yearID','stint','teamID','lgID'])
batting_state_df = batting_state_df.set_index('state')

#create a list of batting stats we want to record
batting_stats = list(batting_state_df.columns)

#complete state batting dataframe
for state in states:
    data = people_batting_df.loc[people_batting_df['birthState'] == state]
    for stat in batting_stats:
        stat_total = int(data[stat].sum())
        batting_state_df.loc[state, stat] = stat_total

#Gets batting avg
for state in states:
    hits = int(batting_state_df.loc[state, 'H'])
    ab = int(batting_state_df.loc[state, 'AB'])
    try:
        AVG = hits/ab
    except ZeroDivisionError:
        AVG = 0
    batting_state_df.loc[state, 'AVG'] = AVG


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

#Gets OPS - Daniel
for state in states:
    OBP = batting_state_df.loc[state, 'OBP']
    SLG = batting_state_df.loc[state, 'OBP']
    OPS = OBP + SLG
    batting_state_df.loc[state, 'OPS'] = OPS
    
#Adds the additional batting statistics that weren't part of the original list   
batting_stats.append('OBP')
batting_stats.append('OPS')
batting_stats.append('AVG')
batting_stats.append('SLG')

#Creates a column to merge the geodata and baseball stats on
batting_state_df = batting_state_df.reset_index()
batting_state_df['Code'] = batting_state_df['state']
batting_state_df = batting_state_df.set_index('state')

#Creates a new dataframe that only includes the US states
us_states_batting_df = batting_state_df.iloc[0:0]

for state in us_states:
    data = batting_state_df[batting_state_df['Code'] == state]
    us_states_batting_df = us_states_batting_df.append(data)
    
    
#Merges the geo data with the US states batting data
new_us_states_batting_df = pd.merge(us_states_batting_df, geo, on='Code')

#Creates new columns that contain the rank of each state in regards to a particular stat
for stat in batting_state_df:
    stat_name = stat + 'Rank'
    new_us_states_batting_df[stat_name] = new_us_states_batting_df[stat].rank(method='average',ascending=False)
    


# In[123]:


#Function that will take the data, create the choropleth, and display it on the US states

def graph_data(dataset, statistic):
    #Insert the markers onto the map
                for row in dataset.to_records():
                    pos = (int(row['Latitude']), int(row['Longitude']))
                    message = f"{row['Code']} {statistic}: {row[statistic]}"
                    marker = folium.Marker(location = pos, popup=message)
                    new_map = map.add_child(marker) 
                    
    #Display the data using a choropleth
                statisticRank = statistic + 'Rank'
                choropleth = folium.Choropleth(
                    geo_data=state_geo,
                    data = dataset,
                    fill_color = 'RdYlGn',
                    key_on = 'feature.id',
                    fill_opacity=0.7,
                    line_opacity=0.2,
                    columns= ["Code", statisticRank],
                    legend_name = f'Ranked by Total {statistic}'
                ).add_to(map)

                return map


# In[124]:


#Mapping Code


#import map of the states
CENTER_US = (39.8333333,-98.585522)
london = (51.5074, -0.1278)
map = folium.Map(location=CENTER_US, zoom_start=4)
with open("NYC4-us-states.json") as file:
            state_geo = json.load(file)

#A variety of loops to ask the user which statistic they want to have graphed
while True:
    while True:
        b_or_p = input("Would you like to look at batting or pitching stats? (B for batting, P for pitching, or Q to quit): ").upper()
        if b_or_p == 'B':
            dataset = new_us_states_batting_df
            graphable_stats = batting_stats
            break
        elif b_or_p == 'P':
            dataset = new_us_states_pitching_df
            graphable_stats = pitching_stats
            break
        elif b_or_p == 'Q':
            break
        else:
            print("please enter B or P")
            
    if b_or_p == 'Q':
        break
        
    else:
        statistic = input('Input the statistic you want graphed: ').upper()
        
        while True:
            if statistic in graphable_stats:
                
                #Call the function that generates the choropleth
                graph_data(dataset, statistic)
                #display the map
                display(map)
            
                break

            else:
                print(f"That is not a valid statistic, please choose from the list provided: {graphable_stats}")
                statistic = input('Input the statistic you want graphed: ').upper()


# In[ ]:





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


# In[4]:


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
#Gets ERA
for country in countries:
    IPouts = int(pitching_country_df.loc[country, 'IPouts'])
    ER = int(pitching_country_df.loc[country, 'ER'])
    try:
        ERA = (ER*9)/(IPouts/3)
    except ZeroDivisionError:
        ERA = 0
    pitching_country_df.loc[country,'ERA'] = ERA



#creates dataframe for country batting stats
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


# In[ ]:





import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import os
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#.....קריאה לנתונים

df1 = pd.read_csv("2011.csv")
df2 = pd.read_csv("2012.csv")
df3 = pd.read_csv("2013.csv")
df4 = pd.read_csv("2014.csv")
df5 = pd.read_csv("2015.csv")
df6 = pd.read_csv("2016.csv")
df7 = pd.read_csv("2017.csv")
df8 = pd.read_csv("2018.csv")
df9 = pd.read_csv("2019.csv")
df10 = pd.read_csv("2020.csv")
df11 = pd.read_csv("2021.csv")

#..איחוד הנתנונים
frames = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11]
final_df = pd.concat(frames)
final_df['won']=0

#final_df.to_csv("all_nba_players.csv",index=False)
#print(final_df.dtypes)
# print(final_df.head())

#....... מילוי התאים החסרים
#print(final_df.isna().sum())
final_df['2FG'].fillna(0.0,inplace=True)
final_df['3FG'].fillna(0.0,inplace=True)
final_df['FT'].fillna(0.0,inplace=True)
final_df['Field goals'].fillna(-0.1,inplace=True)



df_cleaning = final_df.copy()

#.....          עדכון שמות הקבוצה הישנות בשמות הקבוצה החדשות וכן שמות השחקנים
names_of_the_teams_past=['NJN','NOH','CHA']
names_of_the_teams_now=['BRK','NOP','CHO']

position_of_the_players_past=['PG-SG','SG-PG','SG-SF','SF-SG','SF-PF','PF-SF','PF-C','C-PF','SG-PF',
                               'PG','SG','SF','PF','C']

position_of_the_players_now=['Guard','Guard','Guard','Forward','Forward','Forward','Forward','Center','Guard','Guard'
     ,'Guard','Forward','Forward','Center']



df_cleaning.replace(to_replace=names_of_the_teams_past,value=names_of_the_teams_now,inplace=True)
df_cleaning.replace(to_replace=position_of_the_players_past,value=position_of_the_players_now,inplace=True)


list_names=df_cleaning.Player_name

new_list_names=list()

for name in list_names:
    if ('ć' in name or 'č' in name or '*' in name):
        name=name.replace('č','c')
        name=name.replace('ć','c')
        name=name.replace('*','')
    new_list_names.append(name)

df_new_name=pd.DataFrame({'player_name':new_list_names})
print(df_new_name)
df_cleaning['Player_name']=df_new_name['player_name'].values



#                  ....ניקוי נתונים לא רצויים

#..#סף נקודות + סף כמות משחקים + שם הקבוצה

points_mean=df_cleaning.points.mean()
games_min=82/3

df_cleaning.loc[df_cleaning.games<=games_min,'games']=np.nan
df_cleaning.loc[df_cleaning.points<=points_mean,'points']=np.nan


df_cleaning.dropna(inplace=True)


df_cleaning.to_csv("df_cleaning.csv",index=False)






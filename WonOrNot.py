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


df1_1 = pd.read_csv("df_cleaning.csv")
df2_2 = pd.read_csv("all_nba_first_team.csv")


df2_2.rename(columns={'player': 'Player_name'}, inplace=True)

df1=df1_1.copy()
df2=df2_2.copy()

players_R_data=df1.Player_name
players_five_data=df2.Player_name

years_R_data=df1['year played']
years_five_data=df2.year


for i in range (0,len(years_five_data)):
    for j in range (0,len(years_R_data)):
        if(years_five_data[i]==2022):
            break
        if ((players_R_data[j].lower()==players_five_data[i].lower()) and (years_R_data[j]==years_five_data[i])):
            index_won=(df1.loc[(df1['Player_name'] == players_R_data[j]) & (df1['year played'] == years_R_data[j])].index)
            df1.loc[index_won,'won']=1





df1.to_csv("df_the_org.csv",index=False)


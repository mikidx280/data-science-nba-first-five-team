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

url="http://www.espn.com/nba/history/awards/_/id/44"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")
tbl = soup("table", attrs={"class": "tablehead"})[0]

pl_name_odd=list()

pl_name_even=list()

years_even= list()
years_odd=list()

for row in tbl('tr',attrs={"class": "oddrow"}):
    cells=row('td')
    if(cells[0].get_text()=='2010'):
        break
    if (cells[0].get_text() != "" or cells[0].get_text() !=''):
        for i in range(5):
         years_even.append(cells[0].get_text())
    pl_name_even.append(cells[1].get_text())


for row in tbl('tr',attrs={"class": "evenrow"}):
    cells=row('td')
    if(cells[0].get_text()=='2009'):
        break
    if (cells[0].get_text() != "" or cells[0].get_text() !=''):
        for i in range(5):
         years_odd.append(cells[0].get_text())
    pl_name_odd.append(cells[1].get_text())

df_even_years=pd.DataFrame({"year": years_even, "player":pl_name_even})

df_odd_years=pd.DataFrame({"year": years_odd, "player":pl_name_odd})

frames=[df_odd_years,df_even_years]
df_all_nba_first_team=pd.concat(frames)

df_all_nba_first_team.sort_values('year',ascending=False,inplace=True)
print(df_all_nba_first_team)
df_all_nba_first_team.to_csv('all_nba_first_team.csv',index=False)

















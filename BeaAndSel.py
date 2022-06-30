
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

PATH="C:\Program Files\chromedriver.exe"

driver=webdriver.Chrome(PATH)

url="https://www.basketball-reference.com/leagues/NBA_2021_per_game.html"

driver.get(url)

#.......עזרה לסלניום על מנת ללחוץ על הקישורים המבוקשים
list_season=["2019-20 Player Stats: Per Game","2018-19 Player Stats: Per Game","2017-18 Player Stats: Per Game",
             "2016-17 Player Stats: Per Game","2015-16 Player Stats: Per Game","2014-15 Player Stats: Per Game",
             "2013-14 Player Stats: Per Game","2012-13 Player Stats: Per Game","2011-12 Player Stats: Per Game",
             "2010-11 Player Stats: Per Game"]

#....השנים עם הסיומות לשמירה כקובץ csv
years_to_csv = ['2021.csv', '2020.csv', '2019.csv', '2018.csv', '2017.csv',
                '2016.csv', '2015.csv', '2014.csv', '2013.csv', '2012.csv'
    , '2011.csv']

#........שאיבת הנתונים בעזרת ביוטיפול סופ
def get_players_data(url,x_year,csv_name_helper):
    html=requests.get(url)
    soup=BeautifulSoup(html.content,"html.parser")
    tbl=soup("table",attrs={"class":"sortable"})[0]
#// כמות התאים בשורה
    pl_name=list()
    pl_age=list()
    pl_position=list()
    pl_team_name=list()
    pl_games=list()
    pl_games_started=list()
    pl_minutes=list()
    pl_points=list()
    pl_fg=list()
    pl_2fg=list()
    pl_3fg=list()
    pl_free_throw=list()
    pl_of_reb=list()
    pl_def_reb=list()
    pl_tot_reb=list()
    pl_ast=list()
    pl_stl=list()
    pl_tov=list()
    pl_blk=list()
    pl_personal_fouls=list()



    for row in tbl ("tr",attrs={"class":"full_table"}):
        cells=row("td")
        pl_name.append(cells[0].get_text())
        pl_position.append(cells[1].get_text())
        pl_age.append(cells[2].get_text())
        pl_team_name.append(cells[3].get_text())
        pl_games.append(cells[4].get_text())
        pl_games_started.append(cells[5].get_text())
        pl_minutes.append(cells[6].get_text())
        pl_fg.append(cells[9].get_text())
        pl_3fg.append(cells[12].get_text())
        pl_2fg.append(cells[15].get_text())
        pl_free_throw.append(cells[19].get_text())
        pl_of_reb.append(cells[20].get_text())
        pl_def_reb.append(cells[21].get_text())
        pl_tot_reb.append(cells[22].get_text())
        pl_ast.append(cells[23].get_text())
        pl_stl.append(cells[24].get_text())
        pl_blk.append(cells[25].get_text())
        pl_tov.append(cells[26].get_text())
        pl_personal_fouls.append(cells[27].get_text())
        pl_points.append(cells[28].get_text())

    #...סיום הלולאה
    year_size=len(pl_fg)
    print(year_size)

    df=pd.DataFrame({"Player_name":pl_name,"age":pl_age,"position":pl_position,"team name":pl_team_name,
                     "games":pl_games,"games started":pl_games_started,"minutes":pl_minutes,"points":pl_points,"Field goals":pl_fg,
                     "2FG":pl_2fg,"3FG":pl_3fg,"FT":pl_free_throw,"R.offensive":pl_of_reb,
                     "R.defensive":pl_def_reb,"R.total":pl_tot_reb,"Assists":pl_ast,"Steals":pl_stl,"BLK":pl_blk,
                     "Turnover":pl_tov,"Persona fouls":pl_personal_fouls,"year played":x_year})


    df.to_csv(csv_name_helper,index=False)

#......סלניום על מנת לשותת בין השנים + ביוטיפול סופ על מנת לשאוב את הנתונים
def runingOnPages( list_season, driver,csv_helper):
 x=2021
 i=0
 for year in list_season:
     try:
         link = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.LINK_TEXT, year))
         )
         correct_urls = driver.current_url
         get_players_data(correct_urls, x, csv_helper[i])
         x=x-1
         i=i+1
         print(i,x)
         link.click()
     except:
         driver.quit()


#הרצת הקוד
runingOnPages(list_season,driver,years_to_csv)


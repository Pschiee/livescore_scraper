import requests
import codecs
from HTMLParser import *
from selenium import webdriver

url = 'https://www.livescore.com/soccer/2020-06-01/'

driver = webdriver.Chrome('F:/ChromeDriver/chromedriver.exe')
driver.get(url)

my_parse = HTMLParser(driver.page_source)
temp_home_teams = my_parse.find_all('div',clas = 'ply tright name')
temp_away_teams = my_parse.find_all('div',clas = 'ply name')
home_scores = my_parse.find_all('span',clas = 'hom')
away_scores = my_parse.find_all('span',clas = 'awy')
home_teams = []
away_teams = []
for i in range(len(temp_home_teams)):
    home_teams.append(my_parse.clean(temp_home_teams[i]))
    away_teams.append(my_parse.clean(temp_away_teams[i]))
    print(f"{home_teams[i]} {home_scores[i]} - {away_scores[i]} {away_teams[i]}")


driver.quit()
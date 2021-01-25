import requests
from bs4 import BeautifulSoup
import pandas as pd
page=requests.get("https://en.wikipedia.org/wiki/List_of_India_ODI_cricketers").text
#page
soup = BeautifulSoup(page,"lxml")
a = print(soup.prettify())

#print(player_names)
dataframe=pd.DataFrame(a)
# dataframe['player_names']= Players
#dataframe.head()
dataframe.to_csv("Cricket_players.csv")
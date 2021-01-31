import requests
import time
import lxml

from selenium import webdriver
from bs4 import BeautifulSoup

from sys import argv

#open page
driver = webdriver.Chrome(executable_path="/Users/chocolee/git/Map-for-Lumpie/src/crawlers/chromedriver")

#load page with input model
driver.get("https://www.ubereats.com/au/location")
source = driver.page_source

#find cities
soup = BeautifulSoup(source, 'html.parser')
cities = soup.find_all("span", class_="bt") #scrap cities

for city in cities:
    print(city.get_text()) #print cities




#send csv, column A = "au", B = "cities"
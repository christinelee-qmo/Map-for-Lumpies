#Foodpanda
import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://www.foodpanda.co.jp/restaurants/new?lat=35.4659811&lng=139.622062&vertical=restaurants")
    
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify()) 
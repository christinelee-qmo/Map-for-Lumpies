#出前間 https://demae-can.com/search/address/zip/?genreNm=youshoku
import requests
from bs4 import BeautifulSoup

response = requests.get(
    "")
    
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify()) 
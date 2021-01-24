import requests
import time

from selenium import webdriver
from bs4 import BeautifulSoup

from sys import argv

ppcodes = ['9011201','1680065','9011414']

driver = webdriver.Chrome(executable_path="/Users/chocolee/git/Map-for-Lumpies.git/src/crawlers/chromedriver")

for ppcode in ppcodes:
    #load page with input model
    driver.get("https://www.ubereats.com/jp/feed?mod=locationManager&modctx=feed&next=%2Fjp%2Ffeed%3Fpl%3DJTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFMyU4MCU5MiUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpRWDctU3BCdTVUUVIzb25uMGIyS21ZVSUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EyNi4xOTQzNzQlMkMlMjJsb25naXR1ZGUlMjIlM0ExMjcuNzUxNjcwNCU3RA%253D%253D%26ps%3D1&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFMyU4MCU5MiUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpRWDctU3BCdTVUUVIzb25uMGIyS21ZVSUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EyNi4xOTQzNzQlMkMlMjJsb25naXR1ZGUlMjIlM0ExMjcuNzUxNjcwNCU3RA%3D%3D&ps=1")
    #click "edit"
    postcode = driver.find_element_by_id("location-typeahead-location-manager-input")

    #type postcode
    postcode.send_keys(ppcode)
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//UL[@id="location-typeahead-location-manager-menu"]/LI[1]').click()

    #load content
    time.sleep(1.6)

    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    #soup = BeautifulSoup(response.text, "html.parser")
    noservice = soup.find_all(string="入力された住所は配達エリア外です")
    notime = soup.find_all(string="時間をおいて再度お試しください")
    
    if print(noservice) == '入力された住所は配達エリア外です':
        print("true")
    else:
        print("false")




    #入力された住所は配達エリア外です
    #時間をおいて再度お試しください

    #Tokyo 1680065
    #https://www.ubereats.com/jp/feed?ps=1&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFMyU4MCU5MiUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUp5eVRYRXBmdEdHQVJKcnNxSUxQVElKVSUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EzNS43MjQ0MTgyJTJDJTIybG9uZ2l0dWRlJTIyJTNBMTM5LjYzNjI4MjklN0Q%3D

    #Okinawa 9011201 時間をおいて再度お試しください cq gw hp ba hn
    #https://www.ubereats.com/jp/feed?ps=1&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFMyU4MCU5MiUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpSMU1JWUZadjVUUVIzc1RDaHQtU0ZXOCUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EyNi4xMzU1MDM3JTJDJTIybG9uZ2l0dWRlJTIyJTNBMTI3LjcyNjQyNTclN0Q%3D

    #9011414 入力された住所は配達エリア外です hj hk cc

    # data 
    #JP 00000000 out-of-service

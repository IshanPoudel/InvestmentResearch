import re
import time
import logging
import csv
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import mysql.connector
import traceback



chrome_options = Options()  # Instantiate an options class for the selenium webdriver
# chrome_options.add_argument("--headless")  # So that a chrome window does not pop up
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


def get_news_from_google(key):
    print("I am here")



    # change space to a + sign as used by google url
    key = key.lower().replace(" ", "-")
    # url = "https://www.google.com/search?q=" + key + "&source=lmns&tbm=nws&bih=717&biw=1309&rlz=1C5CHFA_enNP906NP906&hl=en-US&sa=X&ved=2ahUKEwjzs8Wsnpz3AhUM0FMKHUsmADsQ_AUoAXoECAEQAQ"
    url = "https://www.google.com/search?q="+key+"++stock+news&biw=1309&bih=746&tbs=qdr%3Aw%2Csbd%3A1&tbm=nws&ei=HhQFY4_xEdKjqtsP5bmAkAY&ved=0ahUKEwiP-Ozxw935AhXSkWoFHeUcAGIQ4dUDCA4&uact=5&oq=UAA++stock+news&gs_lcp=Cgxnd3Mtd2l6LW5ld3MQAzIFCAAQkQIyBAgAEB4yBQgAEIYDMgUIABCGAzIFCAAQhgMyBQgAEIYDOgUIABCABDoGCAAQHhAHUABYlQNg5QVoAHAAeACAAVqIAb8CkgEBNJgBAKABAcABAQ&sclient=gws-wiz-news"
    driver.get(url)

    time.sleep(10)

    #declare array and string for the news.
    google_news_title_text= []
    google_news_link = []

    #Get the html page
    html_text = driver.page_source

    soup = BeautifulSoup(html_text, 'html.parser')




    XPATH_TUPLE_FOR_NEWS_TITLE  = (By.XPATH ,  "//*[@id='rso']/div/div/div[1]")
    XPATH_TUPLE_FOR_NEWS_SUMMARY = (By.XPATH , "//*[@id='rso']/div/div/div[1]/div/a/div/div[2]/div[3]")
    XPATH_TUPLE_FOR_NEWS_COMPANY = (By.XPATH , "//*[@id='rso']/div/div/div[1]/div/a/div/div[2]/div[1]/span")
    XPATH_TUPLE_FOR_NEWS_LINK = (By.XPATH , "//*[@id='rso']/div/div/div[3]/div/a/div/div[1]/div/div")

    data = driver.find_element(*XPATH_TUPLE_FOR_NEWS_CARD)
    print(data.text)
    html_for_house_cards = data.get_attribute('innnerHTML')
    print(html_for_house_cards)

    # // *[ @ id = "rso"] / div / div / div[1] / div / a / div / div[2] / div[2]

    # for news in us_news_blob:
    #
    #     news_class = news.find("div", {"class": "v7W49e"})
    #     # Iterate through <div id="search">
    #     #                      <div class="v7W49e" >
    #     #                           <div hase="i" >
    #     news_hve_id = news_class.find_all("g-card")
    #     print(news_hve_id)
    #
    #     for actual_news in news_hve_id:
    #
    #
    #         try:
    #
    #             news_text = actual_news.find("div", {"role": "heading"}).text
    #             google_news_title_text.append(news_text)
    #             news_title = actual_news.a['href']
    #             google_news_link.append(news_title)
    #             print("i added" + news_title)
    #             driver.close()
    #         except Exception as e:
    #             print("Error")
    #             driver.close()
    return  google_news_title_text , google_news_link





title , link = get_news_from_google("AAPL")
print("I am outside the function")
for i in range(len(title)) :

    print("I am here")

driver.close()
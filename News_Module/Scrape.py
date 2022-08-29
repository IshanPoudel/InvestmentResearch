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


def parse_news_link(html):
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.find('a', href=True)
    return (soup['href'])

def parse_image_link(html):

    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.find('img')
    return (soup['src'])

def get_news_from_google(key):

    chrome_options = Options()  # Instantiate an options class for the selenium webdriver
    chrome_options.add_argument("--headless")  # So that a chrome window does not pop up
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.implicitly_wait(20)



    try:

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

        driver.implicitly_wait(20)

        soup = BeautifulSoup(html_text, 'html.parser')

        News_Tuple=[]

    except:
        print("Could not get source")
        return  "Error"
        driver.close()
        quit()

    for i in range(1, 6):

        try:

            Value_Tuple = []
            Value_Tuple.append(key)




            XPATH_TUPLE_FOR_NEWS_TITLE  = (By.XPATH ,  "// *[ @ id = 'rso'] / div / div / div["+str(i)+"] / div / a / div / div[2] / div[2]")
            XPATH_TUPLE_FOR_NEWS_SUMMARY = (By.XPATH , "//*[@id='rso']/div/div/div["+str(i)+"]/div/a/div/div[2]/div[3]")
            XPATH_TUPLE_FOR_NEWS_COMPANY = (By.XPATH , "//*[@id='rso']/div/div/div["+str(i)+"]/div/a/div/div[2]/div[1]/span")

            XPATH_TUPLE_FOR_NEWS_LINK = (By.XPATH , " // *[ @ id = 'rso'] / div / div / div["+str(i)+"] / div ")
            XPATH_TUPLE_FOR_IMAGE_LINK = (By.XPATH , "//*[@id='rso']/div/div/div["+str(i)+"]/div/a/div/div[1]/div/div")



            data = driver.find_element(*XPATH_TUPLE_FOR_NEWS_TITLE)
            # print(data.text)
            Value_Tuple.append(data.text)

            data = driver.find_element(*XPATH_TUPLE_FOR_NEWS_SUMMARY)
            # print(data.text)
            Value_Tuple.append(data.text)

            data = driver.find_element(*XPATH_TUPLE_FOR_NEWS_COMPANY)
            # print(data.text)
            Value_Tuple.append(data.text)
            #
            data = driver.find_element(*XPATH_TUPLE_FOR_NEWS_LINK)
            # print(data.get_attribute('innerHTML'))
            # print(parse_news_link(data.get_attribute('innerHTML')))
            Value_Tuple.append(parse_news_link(data.get_attribute('innerHTML')))

            data = driver.find_element(*XPATH_TUPLE_FOR_IMAGE_LINK)
            # print(data.get_attribute('innerHTML'))
            # print(parse_image_link(data.get_attribute('innerHTML')))
            Value_Tuple.append(parse_image_link(data.get_attribute('innerHTML')))

            News_Tuple.append(Value_Tuple)

            print('\n')

        except:
            print('Could not get link for ' + key)
            driver.close()

            pass

    return  News_Tuple






import time
import logging
import csv
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



chrome_options = Options()  # Instantiate an options class for the selenium webdriver
# chrome_options.add_argument("--headless")  # So that a chrome window does not pop up
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


def get_news_from_google(key):
    print("I am here")



    # change space to a + sign as used by google url
    key = key.lower().replace(" ", "-")
    url = "https://www.google.com/search?q=" + key + "&source=lmns&tbm=nws&bih=717&biw=1309&rlz=1C5CHFA_enNP906NP906&hl=en-US&sa=X&ved=2ahUKEwjzs8Wsnpz3AhUM0FMKHUsmADsQ_AUoAXoECAEQAQ"
    driver.get(url)

    time.sleep(10)

    #declare array and string for the news.
    google_news_title_text= []
    google_news_link = []

    #Get the html page
    html_text = driver.page_source

    soup = BeautifulSoup(html_text, 'html.parser')

    us_news_blob = soup.find_all("div", {"id": "search"})


    for news in us_news_blob:

        news_class = news.find("div", {"class": "v7W49e"})
        # Iterate through <div id="search">
        #                      <div class="v7W49e" >
        #                           <div hase="i" >
        news_hve_id = news_class.find_all("g-card")
        print(news_hve_id)

        for actual_news in news_hve_id:


            try:

                news_text = actual_news.find("div", {"role": "heading"}).text
                google_news_title_text.append(news_text)
                news_title = actual_news.a['href']
                google_news_link.append(news_title)
                print("i added" + news_title)
                driver.close()
            except Exception as e:
                print("Error")
                driver.close()
    return  google_news_title_text , google_news_link





title , link = get_news_from_google("AAPL")
print("I am outside the function")
for i in range(len(title)) :

    print("I am here")
    print( title[i] , link[i])
    print('\n')



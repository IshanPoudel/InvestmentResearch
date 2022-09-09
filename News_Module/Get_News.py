import sys
sys.path.append("..")
from Scrape import get_news_from_google
import json
import mysql.connector

import mysql.connector


with open('../config.json') as config_file:
    data = json.load(config_file)

with open('../website.json') as website_link:
    web_link = json.load(website_link)

db = mysql.connector.connect(host=data['host'],
                             user=data['username'],
                             passwd=data['password'] ,
                             db='stock_news'
                            )

mycursor = db.cursor()


stocks = ['GOOG', 'AAPL', 'MSFT' , 'TSLA' , 'META'  , 'JNJ' , 'V' , 'XOM' , 'WMT' , 'BABA', 'AMZN', 'GE', 'AMD', 'WMT', 'BAC', 'GM',
'T', 'UAA', 'SHLD','DIS' , 'AVGO' , 'ORCL' , 'DHR', 'XOM', 'RRC', 'BBY', 'MA', 'PFE', 'JPM', 'SBUX' , 'NVDA' , 'PG' , 'MA' , 'CVX' , 'LLY' , 'BAC' , 'KO' , 'PFE' , 'ABBV' , 'PEP' , 'COST' , 'MRK' , 'TMO']

# //Cre




for stock in stocks:
    tuple = get_news_from_google(stock)

    if tuple != 'Error':






        query = "INSERT INTO news (stock_ticker , news_headline , news_summary , news_provider , news_link , news_image_link) VALUES (%s , %s , %s , %s , %s , %s)"

        for values in tuple:
            # new_value = list(values)
            # new_values = list(values)
            # try:
            #     new_values[5] = web_link[new_values[0]]
            # except:
            #     print("No value in jon file")

             mycursor.execute(query , values)
             db.commit()
             print("Added news from " + values[0])


    

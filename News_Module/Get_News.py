import sys
sys.path.append("..")
from Scrape import get_news_from_google
import json
import mysql.connector

import mysql.connector


with open('../config.json') as config_file:
    data = json.load(config_file)

db = mysql.connector.connect(host=data['host'],
                             user=data['username'],
                             passwd=data['password'] ,
                             db='stock_news'
                            )

mycursor = db.cursor()


stocks = ['GOOG', 'AAPL', 'FB', 'BABA', 'AMZN', 'GE', 'AMD', 'WMT', 'BAC', 'GM',
'T', 'UAA', 'SHLD', 'XOM', 'RRC', 'BBY', 'MA', 'PFE', 'JPM', 'SBUX']




for stock in stocks:
    tuple = get_news_from_google(stock)

    if tuple != 'Error':



        query = "INSERT INTO news (stock_ticker , news_headline , news_summary , news_provider , news_link , news_image_link) VALUES (%s , %s , %s , %s , %s , %s)"

        for values in tuple:
             mycursor.execute(query , values)
             db.commit()
             print("Added news from " + values[0])


    

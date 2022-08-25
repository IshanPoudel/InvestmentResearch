#Sample script to run to a virtual private instance
import mysql.connector
import  json

with open('config.json') as config_file:
    data = json.load(config_file)

db = mysql.connector.connect(host=data['host'],
                             user=data['username'],
                             passwd=data['password']
                            )

mycursor = db.cursor()

mycursor.execute("DROP DATABASE IF EXISTS stock_news")
mycursor.execute("CREATE DATABASE stock_news")

db = mysql.connector.connect(host=data['host'],
                             user=data['username'],
                             passwd=data['password'],
                             db='stock_news'
                            )


mycursor = db.cursor()


mycursor.execute("CREATE TABLE news (stock_ticker VARCHAR(20) , news_headline VARCHAR(500) , news_summary VARCHAR(2000) , news_provider VARCHAR(100)  , news_link VARCHAR (1000) , news_image_link VARCHAR (5000) , AddedDate datetime default now() ) ")


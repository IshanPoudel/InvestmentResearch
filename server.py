

import mysql.connector
import json
from utils import get_negative_neutral_positive
from  utils import load_artifacts
from utils import use_finbert_model

from flask import Flask , request , jsonify
import random

app = Flask(__name__)

with open('config.json') as config_file:
    data = json.load(config_file)

db = mysql.connector.connect(host=data['host'],
                             user=data['username'],
                             passwd=data['password'],
                             db='stock_news'
                            )


mycursor = db.cursor()


@app.route('/get_news' )
def get_news():
    # stock_ticker
    # VARCHAR(20), news_headline
    # VARCHAR(500), news_summary
    # VARCHAR(2000), news_provider
    # VARCHAR(100), news_link
    # VARCHAR(1000), news_image_link
    # VARCHAR(5000), AddedDate
    # datetime
    # default
    # now()
    query = 'select stock_ticker , news_headline , news_summary , news_provider , news_link , news_image_link from news ORDER BY RAND() LIMIT 10 '
    mycursor.execute(query)
    rows = mycursor.fetchall()




    news_array = []
    for key , value , summary , provider , link , image_link in rows:
        prediciton = use_finbert_model(value)
        news_array.append((key , value ,prediciton , summary , provider , link , image_link))

    # for each news shuffle it .
    random.shuffle(news_array)




    return {"data": news_array}


@app.route('/get_specific_news/<string:ticker>' , methods=['GET'] )
def get_specific_news(ticker):

    # stock_ticker = request.form['stock_ticker']

    # query = "select stock_ticker , news_headline , news_summary , news_provider , news_link , news_image_link from news where stock_ticker = '"+ticker+"'"
    query = "select stock_ticker , news_headline ,news_summary , news_provider , news_link , news_image_link from news where stock_ticker = '" + ticker + "' ORDER BY AddedDate DESC"
    mycursor.execute(query)
    rows = mycursor.fetchall()

    news_array = []
    sentiment_prediction=[]


    for key , value , summary , provider , link , image_link in rows:

        news_array.append( (value  , use_finbert_model(value) , summary , provider , link , image_link))






    return { "data" : news_array}

# @app.route('request/<string:ticker>' , methods = ['GET'])
# def add_stock(ticker):
#     query = "insert into stock_ticker_to_add values(%s)"
#     mycursor.execute(query)
# sql query does not work . Need to add more.






if __name__ == "__main__":
    load_artifacts()

    # app.run(debug=True, host="10.219.155.18")

    # app.run(  debug=True , host="0.0.0.0")
    app.run(host="0.0.0.0", port=5000, debug=True)
    # app.run(host="10.219.155.18" , port=5000 , debug=True)










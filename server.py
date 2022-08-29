

import mysql.connector
import json

from flask import Flask , request , jsonify

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

    query = 'select stock_ticker , news_headline from news '
    mycursor.execute(query)
    rows = mycursor.fetchall()

    news_array = []

    for key , value in rows:
        news_array.append(value)


    return {"data": news_array}


@app.route('/get_specific_news/<string:ticker>' , methods=['GET'] )
def get_specific_news(ticker):

    # stock_ticker = request.form['stock_ticker']

    query = "select stock_ticker , news_headline from news where stock_ticker = '"+ticker+"'"
    mycursor.execute(query)
    rows = mycursor.fetchall()

    news_array = []


    for key , value in rows:

        news_array.append(value)





    return {ticker: news_array}







if __name__ == "__main__":
    app.run(  debug=True , host="0.0.0.0")








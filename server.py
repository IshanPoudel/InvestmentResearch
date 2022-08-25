

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

    query = 'select stock_ticker , news_headline , AddedDate from news '
    mycursor.execute(query)
    rows = mycursor.fetchall()

    return {"data": rows}


@app.route('/get_specific_news' )
def get_specific_news():

    # stock_ticker = request.form['stock_ticker']
    stock_ticker = 'goog'
    query = "select stock_ticker , news_headline from news where stock_ticker = '"+stock_ticker+"'"
    mycursor.execute(query)
    rows = mycursor.fetchall()

    return {"data": rows}





if __name__ == "__main__":
    app.run(debug=True)








import mysql.connector
import  json

with open('config.json') as config_file:
    data = json.load(config_file)

db = mysql.connector.connect(host=data['host'],
                             user=data['username'],
                             passwd=data['password']
                            )


mycursor = db.cursor()

mycursor.execute("DROP DATABASE IF EXISTS user_table")
mycursor.execute("CREATE DATABASE user_table")

db = mysql.connector.connect(host=data['host'],
                             user=data['username'],
                             passwd=data['password'],
                             db='user_table'
                            )


mycursor = db.cursor("CREATE TABLE user_id (user_id int , FirstName varchar(255), UserEmail varchar(500) , UserPassword varchar(500) )")


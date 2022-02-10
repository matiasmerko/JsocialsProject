from flask import Flask, redirect, url_for, render_template, request
import mysql.connector
import requests
import json
from datetime import datetime
from mysql.connector import Error
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        connection = mysql.connector.connect(host='localhost',
                                             database='group3',
                                             user='group3',
                                             password='cSHhKD')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
        mySql_insert_query = """ SELECT lat,user_long FROM request_user_data; """
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        connection.commit()
        cursor.close()
        return render_template("leaflet.html",data=myresult)
    else:
        return render_template("loc.html")


@app.route("/accepted")
def user():
    return render_template("loc.html")


if __name__ == "__main__":
    app.run(host="10.72.1.14", port=8088, debug=True)

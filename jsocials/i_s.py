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
        user = "bering"
        sport_n = request.form["activity_name"]
        ph_nr = request.form["phone_name"]
        pl_ti = request.form["time_name"]
        sp_loc = request.form["location_name"]
        print("@@@@@@@@@@@@@@@@")
        print(sport_n)
        print("@@@@@@@@@@@@@@@@")
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
        ip_address=request.remote_addr
        time_var=datetime.now()
        browser_name=request.headers.get('User-Agent')
        print("============")
        print(ip_address)
        print(country)
        print(time_var)
        print(browser_name)
        mySql_insert_query_0 = """INSERT INTO request_user_data_2 (ipaddress, r_time, browser) VALUES (%s,%s,%s) """
        print("============")
        mySql_insert_query = """INSERT INTO INFO_BOX_SPORTS (userName, phoneNumber, play_time, destination, sportname) VALUES (%s,%s,%s,%s,%s) """
        record_0 = (ip_address,time_var,browser_name)
        record = (user, ph_nr, pl_ti, sp_loc, sport_n)
        cursor_0 = connection.cursor()
        cursor = connection.cursor()
        cursor_0.execute(mySql_insert_query_0, record_0)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into User table")
        cursor_0.close()
        cursor.close()
        return redirect(url_for("user"))
    else:
        return render_template("request.html")


@app.route("/accepted")
def user():
    return render_template("request_accepted.html")


if __name__ == "__main__":
    app.run(host="10.72.1.14", port=8088, debug=True)

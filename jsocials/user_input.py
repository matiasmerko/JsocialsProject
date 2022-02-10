from flask import Flask, redirect, url_for, render_template, request
import mysql.connector
import requests
from datetime import datetime
from mysql.connector import Error
app = Flask(__name__)
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        user = request.form["user"]
        passw = request.form["pass"]
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
        res = requests.get('https://ipinfo.io/')
        data = res.json()
        city = data['city']
        location = data['loc'].split(',')
        latitude = location[0]
        longitude = location[1]
        print("============")
        print(ip_address)
        print(time_var)
        print(browser_name)
        print("Latitude : ", latitude)
        print("Longitude : ", longitude)
        print("City : ", city)
        mySql_insert_query_0 = """INSERT INTO request_user_data (user_email, ipaddress, r_time, browser, lat, user_long, user_city) VALUES (%s,%s,%s,%s,%s,%s,%s) """
        print("============")
        mySql_insert_query = """INSERT INTO User (user_email, phone_number) 
                                VALUES 
                                (%s,%s) """
        record0=(user,ip_address,time_var,browser_name,latitude,longitude,city)
        record=(user,passw)
        cursor = connection.cursor()
        cursor0 = connection.cursor()
        cursor.execute(mySql_insert_query,record)       
        cursor0.execute(mySql_insert_query_0,record0)
        connection.commit()                                                                      
        print(cursor.rowcount, "Record inserted successfully into User table")
        cursor.close()
        cursor0.close()
        return redirect(url_for("user"))
    else:
        return render_template("log_in.html")
@app.route("/accepted")
def user():
    return render_template("accepted.html")
if __name__ == "__main__":
    app.run(host="10.72.1.14", port=8080, debug=True)

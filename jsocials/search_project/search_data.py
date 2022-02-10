from flask import Flask, redirect, url_for, render_template, request
import mysql.connector
from mysql.connector import Error
app = Flask(__name__)
@app.route("/", methods=["POST", "GET"])
def home():
    print("bering is ind")
    if request.method == "POST":
        print("here")
        ph_nr =request.form["loc_place"]
        box_3 =request.form["choices_section"]
        box_4 =request.form["choices_start_time"]
        pl_ti =request.form["user_name"]
        print(ph_nr)
        print(box_3)
        print(box_4)
        print(pl_ti)
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
        else:
            print("not connected")
        if box_3=="Sports":
            mySql_insert_query = "SELECT INFO_BOX_SPORTS.userName, INFO_BOX_SPORTS.play_time, INFO_BOX_SPORTS.sport_location FROM   INFO_BOX_SPORTS WHERE  INFO_BOX_SPORTS.userName=%s AND INFO_BOX_SPORTS.play_time=%s AND INFO_BOX_SPORTS.sport_location=%s;"
        elif box_3=="Study":
            mySql_insert_query = "SELECT INFO_BOX_STUDY.study_time, INFO_BOX_STUDY.study_time, INFO_BOX_STUDY.study_place FROM   INFO_BOX_STUDY WHERE  INFO_BOX_STUDY.userName=%s AND INFO_BOX_STUDY.study_time=%s AND INFO_BOX_STUDY.study_place=%s;"
        else:
            mySql_insert_query = "SELECT INFO_BOX_GATHERINGS.userName, INFO_BOX_GATHERINGS.gathering_time, INFO_BOX_GATHERINGS.gathering_location FROM   INFO_BOX_GATHERINGS WHERE  INFO_BOX_GATHERINGS.userName=%s AND INFO_BOX_GATHERINGS.gathering_time=%s AND INFO_BOX_GATHERINGS.gathering_location=%s;"
        record=(pl_ti,box_4,ph_nr)
        cursor = connection.cursor()                                  
        cursor.execute(mySql_insert_query,record)                                                   
        myresult = cursor.fetchall()
        for x in myresult:
              print(x)
        connection.commit()                                                                      
        temp=[["SORRY!","NOTHING FOUND","TRY AGAIN"]]
        print(cursor.rowcount, "Record inserted successfully into User table")
        return render_template("priv.html",data="bering")
        if cursor.rowcount==0:
            cursor.close()
            print("jam ktu")
            return render_template("request_accepted.html",data=temp)
        cursor.close()
        return render_template("request_accepted.html",data=myresult)
    else:
        return render_template("search.html")
@app.route("/accepted")
def user():
    return render_template("request_accepted.html")
if __name__ == "__main__":
    app.run(host="10.72.1.14", port=8088, debug=True)

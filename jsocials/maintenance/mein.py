from flask import Flask, redirect, url_for, render_template, request
import mysql.connector
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
        mySql_insert_query = """INSERT INTO User (user_email, phone_number) 
                                VALUES 
                                (%s,%s) """
        record=(user,passw)
        cursor = connection.cursor()                                  
        cursor.execute(mySql_insert_query,record)                                                                  
        connection.commit()                                                                      
        print(cursor.rowcount, "Record inserted successfully into User table")
        cursor.close()
        if user_email=="kebiana":
            return redirect(url_for("user"))
        else:
            return render_template("accepted.html");
    else:
        return render_template("mein_2.html")
@app.route("/accepted")
def user():
    return render_template("accepted.html")
if __name__ == "__main__":
    app.run(host="10.72.1.14", port=8080, debug=True)

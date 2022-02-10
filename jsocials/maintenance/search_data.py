from flask import Flask, redirect, url_for, render_template, request
import mysql.connector
from mysql.connector import Error
app = Flask(__name__)
@app.route("/", methods=["POST", "GET"])
def home():
    print("bering is ind")
    if request.method == "POST":
        print("here")
        pl_ti =request.form["user_name"]
        print(pl_ti)
        print("jam ktu")
        return render_template("denied.html")
    else:
        return render_template("meintance.html")
@app.route("/accepted")
def user():
    return render_template("denied.html")
if __name__ == "__main__":
    app.run(host="10.72.1.14", port=8088, debug=True)

from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os

# Configuration

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_randlejo'
app.config['MYSQL_PASSWORD'] = '5633' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_RandleJo' ###check this please****
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

# Routes 

@app.route('/')
def root():
    return render_template("Index.j2")

@app.route("/Boxes.j2")
def boxes():
    return render_template("Boxes.j2")

@app.route("/Distributors.j2")
def distributor():
    return render_template("Distributors.j2")

@app.route("/Distributor_Products.j2")
def dist_prod():
    return render_template("Distributor_Products.j2")

@app.route("/Products.j2")
def products():
    return render_template("Products.j2")

@app.route("/Purchases.j2")
def purchases():
    return render_template("Purchases.j2")
# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1989)) 
 
    app.run(port=port, debug=True) 

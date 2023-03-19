from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os

# Configuration

app = Flask(__name__)

# database connection
# Template:
# app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
# app.config["MYSQL_USER"] = "cs340_OSUusername"
# app.config["MYSQL_PASSWORD"] = "XXXX" | last 4 digits of OSU id
# app.config["MYSQL_DB"] = "cs340_OSUusername"
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_randlejo'
app.config['MYSQL_PASSWORD'] = '5633' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_randlejo' 
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

# Routes 

@app.route("/")
def index():
    return render_template("Index.j2")

@app.route("/Index")
def home():
    return render_template("Index.j2")

# Customer Routes

@app.route("/Customers", methods=["POST", "GET"])
def customers():

    if request.method == "POST":
        if request.form.get("Add_Customer"):
            customerName = request.form["customerName"]
            customerEmail = request.form["customerEmail"]
            customerPhone = request.form["customerPhone"]
            customerAddress = request.form["customerAddress"]
            customerCity = request.form["customerCity"]
            customerState = request.form["customerState"]
            customerZipcode = request.form["customerZipcode"]
            query = "INSERT INTO Customers(customerName, customerEmail, customerPhone, customerAddress, customerCity, customerState, customerZipcode) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (customerName, customerEmail, customerPhone, customerAddress, customerCity, customerState, customerZipcode))
            mysql.connection.commit()
        return redirect("/Customers")
    # Populates Customers table
    if request.method == "GET":
        query = "SELECT customerID, customerName, customerEmail, customerPhone, customerAddress, customerCity, customerState, customerZipcode FROM Customers;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return render_template("Customers.j2", data=data)


@app.route("/delete_customer/<int:customerID>")
def delete_customer(customerID):
    # mySQL query to delete the planet with our passed id
    query = "DELETE FROM Customers WHERE customerID = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query, (customerID,))
    mysql.connection.commit()

    # redirect back to customers page
    return redirect("/Customers")

@app.route("/edit_Customers/<int:customerID>", methods=["POST", "GET"])
def edit_Customers(customerID):
    if request.method == "GET":
        query = "SELECT * FROM Customers WHERE customerID = %s" % (customerID)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return render_template("edit_Customers.j2", data=data)
    
    if request.method == "POST":
        if request.form.get("Edit_Customer"):
            
            customerName = request.form["customerName"]
            customerEmail = request.form["customerEmail"]
            customerPhone = request.form["customerPhone"]
            customerAddress = request.form["customerAddress"]
            customerCity = request.form["customerCity"]
            customerState = request.form["customerState"]
            customerZipcode = request.form["customerZipcode"]
            query = "UPDATE Customers SET Customers.customerName = %s, Customers.customerEmail = %s, Customers.customerPhone = %s, Customers.customerAddress = %s, Customers.customerCity = %s, Customers.customerState = %s, Customers.customerZipcode = %s WHERE Customers.customerID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (customerName, customerEmail, customerPhone, customerAddress, customerCity, customerState, customerZipcode, customerID))
            mysql.connection.commit()
            return redirect("/Customers")

# Boxes routes

@app.route("/Boxes", methods=["POST", "GET"])
def boxes():

    if request.method == "POST":
        if request.form.get("Add_Box"):
            boxType = request.form["boxType"]
            boxPrice = request.form["boxPrice"]
            query = "INSERT INTO Boxes(boxType, boxPrice) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (boxType,boxPrice))
            mysql.connection.commit()
        return redirect("/Boxes")
    # Populates Boxes table
    if request.method == "GET":
        query = "SELECT boxID, boxType, boxPrice FROM Boxes;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return render_template("Boxes.j2", data=data)


@app.route("/delete_box/<int:boxID>")
def delete_box(boxID):
    # mySQL query to delete the planet with our passed id
    query = "DELETE FROM Boxes WHERE boxID = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query, (boxID,))
    mysql.connection.commit()

    # redirect back to Boxes page
    return redirect("/Boxes")

# Distributor routes

# Distributor_Boxes routes

# Purchase routes
# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1919)) 
 
    app.run(port=port, debug=True)

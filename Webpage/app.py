# -gkochera(March 2020) flask-starter-app(Version 1.0) [Github Repo Source Code] https://github.com/osu-cs340-ecampus/flask-  starter-app.git
# - citation scope: bsg_people_app module
#  - Originality: Based on the CS 340 bsg_people_app starter code with exception of contents of the bsg_people_app
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
            # Account for null Email, Phone, and Zipcode
            if customerEmail == "" and customerPhone == "" and customerZipcode == "":
                query = "INSERT INTO Customers(customerName, customerAddress, customerCity, customerState) VALUES (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, customerAddress, customerCity, customerState))
                mysql.connection.commit()
            # Account for null Email, Phone
            elif customerEmail == "" and customerPhone == "":
                query = "INSERT INTO Customers(customerName, customerAddress, customerCity, customerState, customerZipcode) VALUES (%s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, customerAddress, customerCity, customerState, customerZipcode))
                mysql.connection.commit()
            # Account for null Email, Zipcode
            elif customerEmail == "" and customerZipcode == "":
                query = "INSERT INTO Customers(customerName, customerPhone, customerAddress, customerCity, customerState) VALUES (%s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, customerPhone, customerAddress, customerCity, customerState))
                mysql.connection.commit()
            # Account for null Phone, Zipcode
            elif customerPhone == "" and customerZipcode == "":
                query = "INSERT INTO Customers(customerName, customerEmail, customerAddress, customerCity, customerState) VALUES (%s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, customerEmail, customerAddress, customerCity, customerState))
                mysql.connection.commit()
            # Account for null Email
            elif customerEmail == "":
                query = "INSERT INTO Customers(customerName, customerPhone, customerAddress, customerCity, customerState, customerZipcode) VALUES (%s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, customerPhone, customerAddress, customerCity, customerState, customerZipcode))
                mysql.connection.commit()
            # Account for null Phone
            elif customerPhone == "":
                query = "INSERT INTO Customers(customerName, customerEmail, customerAddress, customerCity, customerState, customerZipcode) VALUES (%s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, customerEmail, customerAddress, customerCity, customerState, customerZipcode))
                mysql.connection.commit()
            # Account for null Zipcode
            elif customerZipcode == "":
                query = "INSERT INTO Customers(customerName, customerEmail, customerPhone, customerAddress, customerCity, customerState) VALUES (%s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, customerAddress, customerCity, customerState))
                mysql.connection.commit()
            # no null inputs
            else:
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
    # mySQL query to delete the customers with our passed id
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
            # Account for null Email, Phone, and Zipcode
            if (customerEmail == "" or customerEmail == "None") and (customerPhone == "" or customerPhone == "None") and (customerZipcode == "" or customerZipcode == "None"):
                query = "UPDATE Customers SET Customers.customerName = %s, Customers.customerEmail = NULL, Customers.customerPhone = NULL, Customers.customerAddress = %s, Customers.customerCity = %s, Customers.customerState = %s, Customers.customerZipcode = NULL WHERE Customers.customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, customerEmail, customerPhone, customerAddress, customerCity, customerState, customerZipcode, customerID))
                mysql.connection.commit()
            # Account for null Email, Phone
            elif (customerEmail == "" or customerEmail == "None") and (customerPhone == "" or customerPhone == "None"):
                query = "UPDATE Customers SET Customers.customerName = %s, Customers.customerEmail = NULL, Customers.customerPhone = NULL, Customers.customerAddress = %s, Customers.customerCity = %s, Customers.customerState = %s, Customers.customerZipcode = %s WHERE Customers.customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, customerEmail, customerPhone, customerAddress, customerCity, customerState, customerZipcode, customerID))
                mysql.connection.commit()
            # Account for null Email, Zipcode
            elif (customerEmail == "" or customerEmail == "None") and (customerZipcode == "" or customerZipcode == "None"):
                query = "UPDATE Customers SET Customers.customerName = %s, Customers.customerEmail = NULL, Customers.customerPhone = %s, Customers.customerAddress = %s, Customers.customerCity = %s, Customers.customerState = %s, Customers.customerZipcode = NULL WHERE Customers.customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, customerEmail, customerPhone, customerAddress, customerCity, customerState, customerZipcode, customerID))
                mysql.connection.commit()
            # Account for null Phone, Zipcode
            elif (customerPhone == "" or customerPhone == "None") and (customerZipcode == "" or customerZipcode == "None"):
                query = "UPDATE Customers SET Customers.customerName = %s, Customers.customerEmail = %s, Customers.customerPhone = NULL, Customers.customerAddress = %s, Customers.customerCity = %s, Customers.customerState = %s, Customers.customerZipcode = NULL WHERE Customers.customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, customerEmail, customerPhone, customerAddress, customerCity, customerState, customerZipcode, customerID))
                mysql.connection.commit()
            # Account for null Email
            elif customerEmail == "" or customerEmail == "None":
                query = "UPDATE Customers SET Customers.customerName = %s, Customers.customerEmail = NULL, Customers.customerPhone = %s, Customers.customerAddress = %s, Customers.customerCity = %s, Customers.customerState = %s, Customers.customerZipcode = %s WHERE Customers.customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, customerEmail, customerPhone, customerAddress, customerCity, customerState, customerZipcode, customerID))
                mysql.connection.commit()
            # Account for null Phone
            elif customerPhone == "" or customerPhone == "None":
                query = "UPDATE Customers SET Customers.customerName = %s, Customers.customerEmail = %s, Customers.customerPhone = NULL, Customers.customerAddress = %s, Customers.customerCity = %s, Customers.customerState = %s, Customers.customerZipcode = %s WHERE Customers.customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, customerEmail, customerPhone, customerAddress, customerCity, customerState, customerZipcode, customerID))
                mysql.connection.commit()
            # Account for null Zipcode
            elif customerZipcode == "" or customerZipcode == "None":
                query = "UPDATE Customers SET Customers.customerName = %s, Customers.customerEmail = %s, Customers.customerPhone = %s, Customers.customerAddress = %s, Customers.customerCity = %s, Customers.customerState = %s, Customers.customerZipcode = NULL WHERE Customers.customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, customerEmail, customerPhone, customerAddress, customerCity, customerState, customerZipcode, customerID))
                mysql.connection.commit()
            # No null inputs
            else:
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
    # mySQL query to delete the purchase with our passed id
    query = "DELETE FROM Boxes WHERE boxID = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query, (boxID,))
    mysql.connection.commit()

    # redirect back to Boxes page
    return redirect("/Boxes")

# Distributor_Boxes routes

@app.route("/Distributor_Boxes", methods=["POST", "GET"])
def distributor_boxes():
    if request.method == "POST":
        if request.form.get("Add_Distributor_Box"):
            distributorName = request.form["distributorName"]
            boxType = request.form["boxType"]
            if distributorName == "":
                query = "INSERT INTO Distributor_Boxes(boxID) VALUES(%s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (boxType))
                mysql.connection.commit()
            elif boxType == "":
                query = "INSERT INTO Distributor_Boxes(distributorID) VALUES(%s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (distributorName))
                mysql.connection.commit()
            else:
                query = "INSERT INTO Distributor_Boxes(distributorID, boxID) VALUES (%s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (distributorName, boxType))
                mysql.connection.commit()
            return redirect("/Distributor_Boxes")

    # Populates Distributor_Boxes table
    if request.method == "GET":
        query = "SELECT Distributor_Boxes.dandbID, Distributors.distributorName AS Distributor, Boxes.boxType AS boxType FROM Distributor_Boxes INNER JOIN Distributors ON Distributor_Boxes.distributorID = Distributors.distributorID INNER JOIN Boxes ON Distributor_Boxes.boxID = Boxes.boxID;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT boxID, boxType FROM Boxes"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        boxType_data = cur.fetchall()

        query2 = "SELECT distributorID, distributorName FROM Distributors"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        distributorName_data = cur.fetchall()
        return render_template("Distributor_Boxes.j2", data=data, boxTypes=boxType_data, distributorNames=distributorName_data)


@app.route("/delete_distributor_box/<int:dandbID>")
def delete_distributor_box(dandbID):
    # mySQL query to delete the distributor with our passed id
    query = "DELETE FROM Distributor_Boxes WHERE dandbID = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query, (dandbID,))
    mysql.connection.commit()

    # redirect back to Distributor_Boxes page
    return redirect("/Distributor_Boxes")

# Distributor routes

@app.route("/Distributors", methods=["POST", "GET"])
def distributors():

    if request.method == "POST":
        if request.form.get("Add_Distributor"):
            boxType = request.form["boxType"]
            distributorName = request.form["distributorName"]
            distributorEmail = request.form["distributorEmail"]
            distributorPhone = request.form["distributorPhone"]
            distributorAddress = request.form["distributorAddress"]
            distributorCity = request.form["distributorCity"]
            distributorState = request.form["distributorState"]
            distributorZipcode = request.form["distributorZipcode"]
            distributorPrice = request.form["distributorPrice"]
            # Account for null Email, Phone, and Zipcode
            if distributorEmail == "" and distributorPhone == "" and distributorZipcode == "":
                query = "INSERT INTO Distributors(boxID, distributorName, distributorAddress, distributorCity, distributorState, distributorPrice) VALUES (%s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (boxType, distributorName, distributorAddress, distributorCity, distributorState, distributorPrice))
                mysql.connection.commit()
            # Account for null Email, Phone
            elif distributorEmail == "" and distributorPhone == "":
                query = "INSERT INTO Distributors(boxID, distributorName, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorPrice) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (boxType, distributorName, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorPrice))
                mysql.connection.commit()
            # Account for null Email, Zipcode
            elif distributorEmail == "" and distributorZipcode == "":
                query = "INSERT INTO Distributors(boxID, distributorName, distributorPhone, distributorAddress, distributorCity, distributorState, distributorPrice) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (boxType, distributorName, distributorPhone, distributorAddress, distributorCity, distributorState, distributorPrice))
                mysql.connection.commit()
            # Account for null Phone, Zipcode
            elif distributorPhone == "" and distributorZipcode == "":
                query = "INSERT INTO Distributors(boxID, distributorName, distributorEmail, distributorAddress, distributorCity, distributorState, distributorPrice) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (boxType, distributorName, distributorEmail, distributorAddress, distributorCity, distributorState, distributorPrice))
                mysql.connection.commit()
            # Account for null Email
            elif distributorEmail == "":
                query = "INSERT INTO Distributors(boxID, distributorName, distributorPhone, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorPrice) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (boxType, distributorName, distributorPhone, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorPrice))
                mysql.connection.commit()
            # Account for null Phone
            elif distributorPhone == "":
                query = "INSERT INTO Distributors(boxID, distributorName, distributorEmail, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorPrice) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (boxType, distributorName, distributorEmail, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorPrice))
                mysql.connection.commit()
            # Account for null Zipcode
            elif distributorZipcode == "":
                query = "INSERT INTO Distributors(boxID, distributorName, distributorEmail, distributorPhone, distributorAddress, distributorCity, distributorState, distributorPrice) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (boxType, distributorName, distributorEmail, distributorPhone, distributorAddress, distributorCity, distributorState, distributorPrice))
                mysql.connection.commit()
            # no null inputs
            else:
                query = "INSERT INTO Distributors(boxID, distributorName, distributorEmail, distributorPhone, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorPrice) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (boxType, distributorName, distributorEmail, distributorPhone, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorPrice))
                mysql.connection.commit()
            return redirect("/Distributors")
            
    # Populates Distributors table
    if request.method == "GET":
        query = "SELECT Distributors.distributorID, Boxes.boxType AS boxType, distributorName, distributorEmail, DistributorPhone, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorPrice FROM Distributors INNER JOIN Boxes ON Distributors.boxID = Boxes.boxID;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT boxID, boxType FROM Boxes"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        boxType_data = cur.fetchall()
        return render_template("Distributors.j2", data=data, boxTypes=boxType_data)


@app.route("/delete_distributor/<int:distributorID>")
def delete_distributor(distributorID):
    # mySQL query to delete the distributor with our passed id
    query = "DELETE FROM Distributors WHERE distributorID = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query, (distributorID,))
    mysql.connection.commit()

    # redirect back to Distributors page
    return redirect("/Distributors")

# Purchase routes

@app.route("/Purchases", methods=["POST", "GET"])
def purchases():

    if request.method == "POST":
        if request.form.get("Add_Purchase"):
            customerName = request.form["customerName"]
            boxType = request.form["boxType"]
            purchaseDate = request.form["purchaseDate"]
            purchaseRevenue = request.form["purchaseRevenue"]
            query = "INSERT INTO Purchases(customerID, boxID, purchaseDate, purchaseRevenue) VALUES (%s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (customerName, boxType, purchaseDate, purchaseRevenue))
            mysql.connection.commit()
        return redirect("/Purchases")
    # Populates Purchases table
    if request.method == "GET":
        query = "SELECT Purchases.purchaseID, Customers.customerName AS customerName, Boxes.boxType AS boxType, purchaseDate, purchaseRevenue FROM Purchases INNER JOIN Customers ON Purchases.customerID = Customers.customerID INNER JOIN Boxes ON Purchases.boxID = Boxes.boxID;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT boxID, boxType FROM Boxes;"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        boxType_data = cur.fetchall()

        query2 = "SELECT customerID, customerName FROM Customers;"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        customerName_data = cur.fetchall()
        return render_template("Purchases.j2", data = data, boxTypes=boxType_data, customerNames=customerName_data)


@app.route("/delete_purchase/<int:purchaseID>")
def delete_purchase(purchaseID):
    # mySQL query to delete the purchase with our passed id
    query = "DELETE FROM Purchases WHERE purchaseID = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query, (purchaseID,))
    mysql.connection.commit()

    # redirect back to Purchases page
    return redirect("/Purchases")

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1990)) 
 
    app.run(port=port, debug=True)
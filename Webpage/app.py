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
app.config['MYSQL_DB'] = 'cs340_randlejo' ###check this please****
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

# Routes 

@app.route('/', methods=["POST","GET"])
def root():
    return render_template("Index.j2")

@app.route("/Boxes.j2", methods=["POST","GET"])
def boxes():
    return render_template("Boxes.j2")

@app.route("/Distributors.j2", methods=["POST","GET"])
def distributor():
    if request.method == 'POST':
        distributor_name = request.form['distributorName']
        distributor_email = request.form['distributorEmail']
        distributor_phone = request.form['distributorPhone']
        distributor_address = request.form['distributorAddress']
        distributor_city = request.form['distributorCity']
        distributor_state = request.form['distributorState']
        distributor_zipcode = request.form['distributorZipcode']
        distributor_product = request.form['distributorProduct']
        distributor_price = request.form['distributorPrice']

        query = f"""
                INSERT INTO Distributors (boxID, distributorName, distributorEmail, distributorPhone, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorProduct, distributorPrice)
                VALUES (1, '{distributor_name}', '{distributor_email}', '{distributor_phone}', '{distributor_address}', '{distributor_city}', '{distributor_state}', '{distributor_zipcode}', '{distributor_product}', '{distributor_price}')
                """
        cur = mysql.connection.cursor()
        cur.execute(query)
        mysql.connection.commit()
        cur.close()

        return redirect('/Distributors.j2')
    
    if request.method == 'GET':
        search_query = request.args.get('search')

        if search_query:
            query = f"""
                    SELECT distributorID,
                            distributorName,
                            distributorEmail,
                            distributorPhone,
                            distributorAddress,
                            distributorCity,
                            distributorState,
                            distributorZipcode,
                            distributorProduct,
                            distributorPrice
                    FROM Distributors
                    WHERE UPPER(distributorName) LIKE UPPER('%{search_query}%')
                    """
        else:
            query = """
                    SELECT distributorID,
                            distributorName,
                            distributorEmail,
                            distributorPhone,
                            distributorAddress,
                            distributorCity,
                            distributorState,
                            distributorZipcode,
                            distributorProduct,
                            distributorPrice
                    FROM Distributors
                    ORDER BY distributorID
                    """

        cur = mysql.connection.cursor()
        cur.execute(query)
        db_distributors = cur.fetchall()
        cur.close()

        return render_template("Distributors.j2", distributors=db_distributors)
    
@app.route('/delete_distributors/<string:distributor_id>')
def delete_distributor(distributor_id):
    query = f"DELETE FROM Distributors WHERE distributorID = '{distributor_id}'"
    cur = mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()
    cur.close()

    return redirect('/Distributors.j2')
    
@app.route('/update_distributors/<int:distributor_id>', methods=['POST', 'GET'])
def update_distributors(distributor_id):
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM Distributors WHERE distributorID = %s', [distributor_id])
        distributor = cur.fetchone()
        cur.close()
        return render_template('update_distributors.j2', distributor=distributor)

    elif request.method == 'POST':
        name = request.form['distributorName']
        email = request.form['distributorEmail']
        phone = request.form['distributorPhone']
        address = request.form['distributorAddress']
        city = request.form['distributorCity']
        state = request.form['distributorState']
        zipcode = request.form['distributorZipcode']
        product = request.form['distributorProduct']
        price = request.form['distributorPrice']

        cur = mysql.connection.cursor()
        cur.execute(
            """
            UPDATE Distributors
            SET distributorName = %s, distributorEmail = %s, distributorPhone = %s,
                distributorAddress = %s, distributorCity = %s, distributorState = %s,
                distributorZipcode = %s, distributorProduct = %s, distributorPrice = %s
            WHERE distributorID = %s
            """,
            (name, email, phone, address, city, state, zipcode, product, price, distributor_id)
        )
        mysql.connection.commit()
        cur.close()

        return redirect('/distributors')

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

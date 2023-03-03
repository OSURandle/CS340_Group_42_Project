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
        input_distributor_id = request.form['input-distributor-id']
        input_distributor_name = request.form['input-distributor-name']

        query = """
                INSERT INTO distributors (distributor_id, name)
                VALUES ('%s', '%s')""" % (input_distributor_id, input_distributor_name)

        cur = mysql.connection.cursor()
        cur.execute(query)
        mysql.connection.commit()

        cur.close()

        return redirect('/distributors')
    
    if request.method == 'GET':

        search_query = request.args

        if search_query:
            search_query = search_query['search']
            query = """SELECT distributor_id,
                                name
                        FROM distributors
                        WHERE UPPER(distributor_id) LIKE UPPER(CONCAT('%%', '%s',
                            '%%'))
                           OR UPPER(name) LIKE UPPER(CONCAT('%%', '%s', '%%'))
                    """ % (search_query, search_query)
        else:
            query = "SELECT distributor_id, name FROM distributors ORDER BY distributor_id"

        cur = mysql.connection.cursor()
        cur.execute(query)
        db_distributors = cur.fetchall()
        
        return render_template("Distributors.j2", distributors=db_distributors)
    
@app.route('/delete_distributors/<string:distributor_id>')
def delete_distributor(distributor_id):
    query = "DELETE FROM distributors WHERE distributor_id = '%s'" % (distributor_id)
    cur = mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()

    cur.close()

    return redirect('/distributor')
    
@app.route('/update_distributors/<string:distributors_id>', methods=['POST', 'GET'])
def update_distributors(distributor_id):

    if request.method == 'GET':
        query = """
                SELECT distributor_id,
                        name
                FROM distributors WHERE distributor_id = '%s'
                """ % (distributor_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        db_distributors = cur.fetchone()
        cur.close()

        return render_template(
            "forms/update_distributors.j2",
            distributors=db_distributors)

    if request.method == 'POST':
        input_distributor_name = request.form['distributor-name']

        query = """
                UPDATE distributors
                SET name = '%s'
                WHERE distributor_id = '%s'""" % (input_distributor_name, distributor_id)

        cur = mysql.connection.cursor()
        cur.execute(query)
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

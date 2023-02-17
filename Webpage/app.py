from flask import Flask, render_template
import os

# Configuration

app = Flask(__name__)

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
 
    app.run(port=port) 
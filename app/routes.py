from app import app, db
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

import os

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///" + os.path.join(basedir, "database.db")
#db.init_app(app)

import app.models as models


@app.route("/")
def home():
    return render_template("home.html", page_title="HOME")

@app.route("/about")
def about():
    return render_template("about.html", page_title="ABOUT")

@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="CONTACT")

@app.route("/all_products")
def all_products():
    results = models.Product.query.all()
    print(results)
    return render_template("all_products.html", page_title="ALL PRODUCTS")

@app.route("/men")
def men():
    return render_template("men.html", page_title="MEN")

@app.route("/women")
def women():
    return render_template("women.html", page_title="WOMEN")

@app.route("/kids")
def kids():
    return render_template("kids.html", page_title="KIDS")

@app.route("/product/<int:id>")
def product(id):
    product = models.Product.query.filter_by(id=id).first()
    return render_template("product.html", product=product)
    
if __name__ == "__main__":
    app.run(debug=True)

import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clothes.db"
db.init_app(app)

#db.create_all()

from app import routes, models
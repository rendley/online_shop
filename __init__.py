from flask import Flask
from flask_sqlalchemy import SQLAlchemy






app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SECRET_KEY']='hfouewhfoiwefoquw'

db = SQLAlchemy(app)





from shop.admin import views


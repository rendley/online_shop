from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_test.db'
app.config['SECRET_KEY']='hfouewhfoiwefoquw'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)




from shop.admin import views


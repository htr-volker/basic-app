'''
Main flask file to be run to start the app
'''
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.static_folder = 'static'

user = getenv('MYSQL_USER')
password = getenv('MYSQL_PASSWORD')
url = getenv('MYSQL_URL')
db = getenv('MYSQL_DATABASE')
secret = getenv('MYSQL_SECRETKEY')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + user + ':' + password + '@' + url + '/' + db
app.config['SECRET_KEY'] = secret

db = SQLAlchemy(app)

from application import routes

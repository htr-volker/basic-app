from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

# Set login details from environment variables
user = getenv('MYSQL_USER')
password = getenv('MYSQL_PASSWORD')
url = getenv('MYSQL_URL')
db = getenv('MYSQL_DATABASE')
secret = getenv('MYSQL_SECRETKEY')

# Connect to database via URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + user + ':' + password + '@' + url + '/' + db

# Secret key for verification
app.config['SECRET_KEY'] = secret

db = SQLAlchemy(app)

from application import routes
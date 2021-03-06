'''
Main flask file to be run to start the app
'''
from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'static'

from application import routes

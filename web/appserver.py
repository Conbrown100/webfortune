# Don't call this flask.py!
# Documentation for Flask can be found at:
# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask, render_template, request, session, redirect, url_for, jsonify, abort, make_response
from flask_sqlalchemy import SQLAlchemy
import os
import subprocess
from subprocess import check_output
import cowsay
import fortune
import time 

app = Flask(__name__)
app.secret_key = b'REPLACE_ME_x#pi*CO0@^z'

sqlite_uri = 'sqlite:///' + os.path.abspath(os.path.curdir) + '/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User

@app.route('/')
def index():
	return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
	
	fortunate_one = make_response(check_output(['fortune', 'outputfortune.dat']))
	fortunate_one.mimetype = "text/plain"
	return fortunate_one

@app.route('/cowsay/<message>/')
def cowsay(message):
	talkative_one = make_response(check_output(['cowsay',  message]))
	talkative_one.mimetype ='text/plain'
	return talkative_one


@app.route('/cowfortune/')
def cowfortune():
	wise_one = make_response(check_output(['python3', 'cowfortune']))
	#pass the output of fortune to the <message> portion of cowsay
	wise_one.mimetype = "text/plain"
	return wise_one



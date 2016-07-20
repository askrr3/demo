from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
mysql = MySQLConnector(app,'validation')
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
	query = "SELECT * FROM users"                       
	users = mysql.query_db(query)
	return render_template('index.html', users=users)

@app.route('/result', methods=['POST'])
def result():
	email = request.form['email']

	forerrors = False
	if len(request.form['email']) < 1:
		flash('Email cannot be blank!')
		return False
	if not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid Email Address!')
		return False
	else:
		query = 'INSERT INTO users (email, created_on) VALUES (:email, NOW())'
		data = {
			'email': request.form['email']
			}
		mysql.query_db(query, data)
		return True
	# return redirect('/')
	return redirect('/')

@app.route('/success')
def result():



	return render_template('index.html')


# @app.route('/success', methods=['GET'])
# def success():

# 	query = 'INSERT INTO validation (email, created_on) VALUES (:email, NOW())'
# 	data = {
# 			'email': request.form['email']
# 			}
# 	mysql.query_db(query, data)
# 	return render_template('final.html')

app.run(debug=True)
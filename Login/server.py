from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
mysql = MySQLConnector(app,'mydb')
app.secret_key = "ThisIsSecret!"


@app.route('/')
def index():
	query = "SELECT * FROM login_regis"
	users = mysql.query_db(query)
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
	firstname = request.form['fname']
	lastname = request.form['lname']
	email = request.form['email']
	password = request.form['password']
	password_con = request.form['password_con']

#input verification

	if len(request.form['fname']) < 2:
		flash("First Name has to be at least 2 characters!")
	if len(request.form['lname']) < 2:
		flash("Last Name has to be at least 2 characters!")
	if len(password) < 3:
		flash("Password should be at least 8 characters!")
	if password != password_con: 
		flash("Password and Password Confirmation should match")
	if len(email) < 1:
		flash('Email cannot be blank!')
	if not EMAIL_REGEX.match(email):
		flash('Invalid Email Address!')

#sql starts here
	else:
		flash('Success!')
		query = 'INSERT INTO login_regis (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)'
		data = {
				'first_name': firstname,
				'last_name': lastname,
				'email': email,
				'password': password
				}
		mysql.query_db(query, data)
	return redirect('/')

@app.route('/login', methods=['GET'])
def login():
	# query = "SELECT * FROM login_regis"
	# users = mysql.query_db(query)
	return render_template('login.html')

@app.route('/loginsubmit', methods=['POST'])
def loginsubmit():

	email = request.form['email']
	password = request.form['password']

	query = "SELECT * FROM login_regis WHERE email = :email and password = :password"
	data = {
			'email' : email,
			'password' : password
			}
	users = mysql.query_db(query, data)

	if len(users) == 0:
		flash('register bro')
	elif users[0]['password'] != password:
		flash('you are wrong')
	else:
		flash('my page doesnt have a logged in page cause i am a loser')


# input should match login_regis db
	return redirect('/')

	# return render_template('login.html')

#password has to equal mydb table password

app.run(debug=True)




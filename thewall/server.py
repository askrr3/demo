from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
mysql = MySQLConnector(app,'thewall')
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
	return render_template('registration.html')

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
		query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)'
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

	return render_template('login.html')

@app.route('/wall')
def wall():
	query = 'SELECT messages.created_at, messages.message, messages.id, messages.users_id, users.first_name, users.last_name FROM users JOIN messages on messages.users_id =  users.id ORDER BY messages.created_at DESC'
	messages = mysql.query_db(query)

	query_comments = 'SELECT comments.created_at, comments.comment, comments.messages_id, comments.id, comments.users_id, users.first_name, users.last_name FROM users JOIN comments on comments.users_id =  users.id'
	# query_comments = 'SELECT * FROM comments'
	
	comments = mysql.query_db(query_comments)


	return render_template('wall.html', comments=comments, messages=messages)


@app.route('/loginsubmit', methods=['POST'])
def loginsubmit():
	email = request.form['email']
	password = request.form['password']

	query = "SELECT * FROM users WHERE email = :email LIMIT 1"
	data = {
			'email' : email,
			}
	users = mysql.query_db(query, data)

	if not 'id' in session.keys():
		session['person'] = users[0]['first_name'] +' '+ users[0]['last_name']
		session['id'] = users[0]['id']
	if len(users) == 0:
		flash('register bro')
	elif users[0]['password'] != password:		
		flash('you are wrong')
	else:
		flash('my page doesnt have a  page')

	return redirect('/wall')

@app.route('/wall/<user_id>', methods=['POST'])
def postmessage(user_id):

	query = 'INSERT INTO messages (message, created_at, updated_at, users_id) VALUES (:message, NOW(), NOW(), :user_id)'
	data = {
			'message' : request.form['messagebox'],	
			'user_id' : user_id
			}
	mysql.query_db(query, data)
	return redirect('/wall')

@app.route('/wallcomment/<messages_id>', methods=['POST'])
def postcomment(messages_id):
#?how to put the newest message on top?

	query = 'INSERT INTO comments (comment, created_at, updated_at, messages_id, users_id) VALUES (:comment, NOW(), NOW(), :messages_id, :users_id)'
	data = {
			'comment' : request.form['commentbox'],
			'users_id' : session['id'],
			'messages_id' : messages_id
			}
	mysql.query_db(query, data)

	return redirect('/wall')


@app.route('/gobackhome')
def gobackhome():
	session.clear()
	return redirect('/')


app.run(debug=True)




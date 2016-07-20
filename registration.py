# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
	return render_template("registration.html")

@app.route('/result', methods=['POST'])
def result():
	email = request.form['email']
	firstname = request.form['firstname']
	lastname = request.form['lastname']
	password = request.form['password']
	confirmpassword = request.form['confirmpassword']

	if len(request.form['firstname']) < 1:
		flash("First Name cannot be empty!")
	if len(request.form['lastname']) < 1:
		flash("Last Name cannot be empty!")
	if len(request.form['password']) < 9:
		flash("Password should be more than 8 characters!")
	if request.form['password'] != request.form['confirmpassword']: 
		flash("Password and Password Confirmation should match")
	# if len(request.form['confirmpassword']) < 9:
	# 	flash("Password should be more than 8 characters!")
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
	return redirect('/')

app.run(debug=True)
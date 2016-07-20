from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index2.html')

@app.route('/show')
def show_user():
	return render_template('user.html', name = 'bill', email = 'kapd@yahoo.com')

@app.route('/users', methods=['POST'])
def create_user():
	name = request.form['name']
	email = request.form['email']
	return redirect('/')
app.run(debug=True)
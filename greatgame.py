import random
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'thisissecret'

@app.route('/')
def game():
	high = 'hidden'
	low = 'hidden'
	correct = 'hidden'

	if not 'guess' in session.keys():
		session['guess'] = int(random.randrange(0, 101))

	if 'userguess' in session.keys():
		print session['guess']
		if int(session['userguess']) > session['guess']:
			high = ''

		if int(session['userguess']) < session['guess']:
			low = ''

		if int(session['userguess'])  == session['guess']:
			correct = ''
			session.pop('userguess')
			session.pop('guess')
	
	return render_template("greatgame.html", high = high, low = low, correct = correct)

@app.route('/result', methods = ['POST'])
def result():

	session['userguess'] = request.form['userguess']
	return redirect('/')


app.run(debug=True) 

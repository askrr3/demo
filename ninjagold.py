import random, datetime
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'thisissecret'

@app.route('/')
def ninja():
	if not 'count' in session.keys():
		session['count'] = 0
	return render_template("ninjagold.html")

	# if not 'finalnum' in session.keys():
	# 	session['finalnum'] = []

@app.route('/result', methods = ['POST']) 
def result():
	if not 'finalnum' in session.keys():
		session['finalnum'] = []

	if (request.form).has_key('farmgold'):
		session['farmgold'] = random.randint(10, 20)
		session['count'] += session['farmgold']
		session['finalnum'] += ('Earned' , session['farmgold'] , 'golds from the farm!' '<br>')

	elif (request.form).has_key('cavegold'):
		session['cavegold'] = random.randint(5, 10)
		session['count'] += session['cavegold']	
		session['finalnum'] += ('Earned' , session['cavegold'] , 'golds from the cave!' '<br>')

	elif (request.form).has_key('housegold'):
		session['housegold'] = random.randint(2, 5)
		session['count'] += session['housegold'] 
		session['finalnum'] += ('Earned' , session['housegold'] , 'golds from the house!' '<br>')

	elif (request.form).has_key('casinogold'):
		session['casinogold'] = random.randint(-50, 50)
		session['count'] += session['casinogold'] 
		session['finalnum'] += ('Entered a casino and won', session['casinogold'], 'gold!' '<br>')
		# if session['casino'] > 0:
		# 	session['finalnum'] += ('Entered a casino and won', session['casinogold'], 'gold!' '<br>')
		# if session['casino'] < 0:
		# 	session['finalnum'] += ('Entered a casino and lost', session['casinogold'], 'gold... Ouch..' '<br>')
		# if session['casinogold'] == 0:
		# 	session['finalnum'] += ('you earned', session['casinogold'] '<br>')



		session['finalnum'] += session['casinogold'], '<br>'

	elif (request.form).has_key('reset'):
		session['count'] = 0
		session.pop('finalnum')

	return redirect('/')


app.run(debug=True) 
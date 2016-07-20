from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'thisissecret'

@app.route('/')
def counter():

	if not 'count' in session.keys():
		session['count'] = 1
	else:
		print type(session ['count'])
	 	session['count'] += 1
	return render_template("counter.html")


app.run(debug=True) 




from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'thisissecret'

@app.route('/')
def game():
	return render_template("turtle.html")

@app.route('/ninja/')
def ninja1():

	return render_template('turtle3.html')

@app.route('/ninja/<color>')
def ninja2(color):
	turtle='turtle'
	turtle2='turtle2'
	turtle3='turtle3'
	turtle4='turtle4'

	if color == 'blue':
		turtle = 'donatello'
	elif color == 'purple':
		turtle2 = 'leonardo2'
	elif color == 'red':
		turtle3 = 'michelangelo2'
	elif color == 'green':
		turtle4 = 'raphael2'

	return render_template('turtle2.html', color=color, turtle=turtle, turtle2=turtle2, turtle3=turtle3, turtle4=turtle4)


# @app.route('/route/with/<vararg>')
# def handler_function(vararg):
# # here you can use the variable "vararg"
# # if you want to see what our argument looks like
# print vararg

app.run(debug=True) 
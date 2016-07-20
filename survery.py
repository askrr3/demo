

from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'thisissecret'


@app.route('/')
def survery():

  return render_template("survery.html")


@app.route('/result', methods=['POST'])
def result():
   name = request.form['name']
   language = request.form['language']
   location = request.form['location']
   comment = request.form['comment']

   if len(request.form['name']) < 1:
      flash("Name cannot be empty!")
      return redirect('/')
   # else:
   # 	  return render_template('result.html', name = name, language = language, location = location, comment = comment)
   if len(request.form['comment']) < 121:
      flash("Comment has to be less than 120!")
      return redirect('/')
   else:
   	  return render_template('result.html', name = name, language = language, location = location, comment = comment)

   return render_template('result.html', name = name, language = language, location = location, comment = comment)



app.run(debug=True) # run our server
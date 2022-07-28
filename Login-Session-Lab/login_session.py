from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

#login_session["quote": "theQuote", "quote's author": "theAuthor", "author's name": "theName"]

@app.route('/', methods = ['GET', 'POST']) # What methods are needed?
def home():
	if request.method == 'POST':
		try:
			login_session['quote'] = request.form['quote']
			login_session["quotes_author"] = request.form["quotes_author"]
			login_session["authors_age"] = request.form["authors_age"]
			if login_session['quote'] == '' or login_session["quotes_author"] == '' or login_session["authors_age"] == '':
				return redirect(url_for('error'))
			else:
				return redirect(url_for('thanks'))
		except:
			return redirect(url_for('error'))
	else:
		return render_template('home.html')


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', login_session = login_session) # What variables are needed?


@app.route('/thanks')
def thanks():
	return render_template('thanks.html', login_session = login_session)


if __name__ == '__main__':
	app.run(debug=True)
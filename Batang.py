from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	error = None
	try:
		if request.method == "POST"

			attempted_username = request.form['username']
			attempted_password = request.form['password']

			flash(attempted_username)
			flash(attempted_password)

	except Exception as e:

		flash(e)
		return render_template("LoginPage.html")

	return render_template("LoginPage.html")

@app.route('/registration/')
def register():
	return render_template("RegistrationPage.html")

@app.route('/studentpage/')
def student_page():
	return render_template("StudentPage.html")

@app.route('/instructorpage/')
def instructor_page():
	return render_template("InstructorPage.html")
from flask import *
from database import *
app = Flask(__name__)

@app.route('/' , methods=['POST', 'GET'])
def home():
	if request.method == 'GET':

		return render_template('home.html' )
	else:
		national_id = request.form['national_id']
		name = request.form['name']
		age = request.form['age']
		subject = request.form['subject']
		print(name)
		print(age)
		print(subject)
		msg1 = "*******###your application submited succesfully "
		create_applicant(national_id , name, age, subject)
		return render_template("home.html" , msg=msg1)

@app.route("/info")
def info():
	list_appilcants = get_appilcants()
	return render_template("applicants.html" , applicants=list_appilcants)


if __name__ == '__main__':
    app.run(debug=True)


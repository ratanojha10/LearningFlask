from flask import Flask, render_template,request
import csv

app=Flask(__name__)

def to_csv(name,_id,email):
	l=[name, _id, email]
	with open('data.csv', 'a') as file:
		p = csv.writer(file)
		p.writerow(l)

@app.route('/', methods=['GET','POST'])
def _form():
	
	if request.method == 'POST':
		name = request.form['name']
		_id = request.form['id']
		email = request.form['email']
		if (name=='' or _id=='' or email==''):
			return "Retry"
		else:
			to_csv(name,_id,email)
			return "Thanks"
	elif request.method == 'GET':
		return render_template('form.html')
if __name__=="__main__":
	app.run(debug=True, host='0.0.0.0', port='5000')
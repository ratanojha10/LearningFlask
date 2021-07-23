from flask import Flask, render_template,request
import csv
import pandas as pd

app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def _form():
	if request.method == 'POST':
		name = request.form['name']
		_id = request.form['id']
		email = request.form['email']
		field = ['name', 'id', 'email']
		with open('data.csv','w') as inFile:
			writer = csv.DictWriter(inFile, fieldnames=field)
			writer.writerow({'name': name, 'id': _id, 'email': email})

	elif request.method=='GET':	
		return render_template('form.html')

if __name__=="__main__":
	app.run(debug=True)

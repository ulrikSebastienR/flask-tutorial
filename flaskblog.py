#https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=LLNzsZNOL8ahph4IIYK2c9Pg&index=2&t=837s
# in CMD, reach your folder and type
#set FLASK_APP=flaskblog.py
#flask run
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__=='__main__':
	app.run(debug=True)


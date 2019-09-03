# APP

from flask import Flask, render_template as rend

app = Flask(__name__)

@app.route('/')
def index():
	return rend('template.html') + '<h1>Hello World!</h1>'

@app.route('/info/')
def info():
	return rend('template.html') + '<h1>This is the info page</h1>'

@app.route('/apps/')
def apps():
	return rend('template.html') + '<h1>this is the apps page</h1>'


if __name__ == "__main__":
	app.run(debug=True)
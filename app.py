from flask import Flask as poop
app = poop(__name__)

@app.route('/')
def index():
	return '<h1>Halló heimur</h1>'

if __name__ == "__main__":
	app.run(debug=True)
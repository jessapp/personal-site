from flask import Flask, flash, redirect, render_template, request, session, abort, url_for


app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello world!"

@app.route("/bio")
def bio():
	return render_template(
		'bio.html',**locals())

if __name__ == "__main__":
	app.run()
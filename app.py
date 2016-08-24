from flask import Flask, flash, redirect, render_template, request, session, abort, url_for


app = Flask(__name__)

@app.route("/")
def hello():
	return render_template(
		'home.html',**locals())

@app.route("/bio")
def bio():
	return render_template(
		'bio.html',**locals())

@app.route("/video")
def video():
	return render_template(
		'video.html',**locals())

@app.route("/programming")
def programming():
	return render_template(
		'programming.html',**locals())

@app.route("/contact")
def contact():
	return render_template(
		'contact.html',**locals())

if __name__ == "__main__":
	app.run()
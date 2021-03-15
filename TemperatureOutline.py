#import flask 
from flask import Flask

#2 create an app
app = Flask(__name__)

#3 define home route
@app.route("/")
def home():
	print("Server received request for")
	return "Welcome to my 'Home' page"

@app.route("/about")
def about():
	name="Ryan Rhino"
	print("yikes there is a rhino")
	return f"This page is about {name}"
#3 define what to do when your user hits the index route
@app.route("/")
def home():
	return "Welcome to my API!!!"

@app.route("/about")
def about():
	name="Ryan the Rhino"
	location= "current location"
	return f" Hi I am {name} at {location}")


#/about in the url to get to the app.route obvy
if __name__=="__main__":
	app.run(debug=True)
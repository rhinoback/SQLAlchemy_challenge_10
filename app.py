

#import flask 
from flask import Flask
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
mes = Base.classes.measurement
sta= Base.classes.station
session = Session(engine)

#2 create an app
app = Flask(__name__)

#3 define home route
@app.route("/")
def home():
	return ("/api/v1.0/precipitation<br>"
	"/api/v1.0/stations<br>"
	"/api/v1.0/tobs<br>"
	"/api/v1.0/start<br>"
	"/api/v1.0/start/end")



# @app.route("/api/v1.0/precipitation")
# def precipitation():
# 	name="Ryan Rhino"
# 	print("yikes there is a rhino")
# 	return f"This page is about {name}"

if __name__=="__main__":
	app.run(debug=True)

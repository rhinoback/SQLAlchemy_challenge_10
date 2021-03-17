

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

# define precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
	return ("/api/v1.0/precipitation")

session = Session(engine)
    # Query most recent 12 months precipitation data
    temp_data_active=session.query(Measurement.date, Measurement.tobs).filter(Measurement.date>='2016-08-18').filter(Measurement.station=='USC00519281').all()
    session.close()
prcp_json = []
    for date, prcp in prcp_data:
       prcp_dict = {}
       prcp_dict["date"] = date
       prcp_dict["prcp"] = prcp
       prcp_json.append(prcp_dict)
    # Convert list of tuples into normal list
    return jsonify(prcp_json)	
# @app.route("/api/v1.0/precipitation")
# def precipitation():

if __name__=="__main__":
	app.run(debug=True)

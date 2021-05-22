import numpy as np
from flask import Flask, request, jsonify, render_template, redirect
import pickle
import requests
import json
import sqlalchemy as db
#from json import JSONEncoder
#from sqlalchemy import create_engine, func
#import psycopg2
#from flask_cors import CORS, cross_origin
import pandas as pd


app = Flask(__name__)
#model=None
model = pickle.load(open('pickle_rf.pkl', 'rb'))

#sample data
# data = [4,2,3,4,3,6]

#route for home
@app.route('/')
def home():
    return render_template('index.html')

#route for visualization details
@app.route('/templates/portfolio-details.html')
def viz():
    return render_template('portfolio-details.html')

#route to send input to model
@app.route('/results',methods=['GET','POST'])
def results():
   
    #below input is from d3/js (json stringify-ed)
    input = request.data
    print(f'this is the input from the dropdown: {input}')
    
    print(f'this is what the input looks like: {input}')

    #un stringify-ed to put in model
    model_input = json.loads(input)
    print(f'this is what is going into the model: {model_input}')
         
    #prediction results hot encoded
    prediction = model.predict(np.array([model_input]))
    print(f'this is the hot encoded prediction: {prediction}')
         

    #go to database to get actual value
    rds_connection_string = "root:WE0ew4F3H2U0@finalproject.cqyw28rarsf4.us-east-1.rds.amazonaws.com:5432/postgres"
    engine = db.create_engine(f'postgresql://{rds_connection_string}')
    connection = engine.connect()
    metadata = db.MetaData()
    beer_style = db.Table('beer_style', metadata, autoload=True, autoload_with=engine)
    predlist = np.where(prediction == 1.0)
    id = int(predlist[1])
    query = db.select([beer_style.columns.beer_style]).where(beer_style.columns.beer_style_id == id)
    result = pd.DataFrame(connection.execute(query).fetchall())
    beer = result.iloc[0, 0]
    print(f'this is the prediction: {beer}')
    
    #result correctly prints in terminal but does not print to html (render_template below doesn't work)
    return render_template('index.html',value=beer)
    


if __name__ == "__main__":
    app.run(debug=True)

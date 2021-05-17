import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import requests
import json
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

#route to send input to model
@app.route('/results',methods=['GET', 'POST'])
def results():
   
    #below input is from d3/js (json stringify-ed)
    input = request.data
    print(f'this is the input from the dropdown: {input}')

    #un stringify-ed to put in model
    model_input = json.loads(input)
    print(f'this is what is going into the model: {model_input}')
         
    #prediction results hot encoded
    prediction = model.predict(np.array([model_input]))
    print(f'this is the hot encoded prediction: {prediction}')

    #go to database to get actual value
    # rds_connection_string = "root:WE0ew4F3H2U0@finalproject.cqyw28rarsf4.us-east-1.rds.amazonaws.com:5432/postgres"
    # engine = create_engine(f'postgresql://{rds_connection_string}')
    # connection = engine.connect()
    # metadata = db.MetaData()
    # beer_style = db.Table('beer_style', metadata, autoload=True, autoload_with=engine)
    # predlist = np.where(prediction == 1.0)
    # id = int(predlist[1])
    # query = db.select([beer_style.columns.beer_style]).where(beer_style.columns.beer_style_id == id)
    # result = pd.DataFrame(connection.execute(query).fetchall())
    # beer = result.iloc[0, 0]
    #print(f'this is the prediction: {beer}')
    
    prediction_list = list(prediction)
    prediction_json = json.dumps(prediction_list)
    print(prediction_json)
    #post prediction result to js/html
    return render_template('index.html', prediction=prediction_json)


#route to put model results into js/html
# @app.route('/test', methods=['GET', 'POST'])
# def testfn():
#     # GET request
#     if request.method == 'GET':
#         message = {'greeting':'Hello from Flask!'}
#         return jsonify(message)  # serialize and use JSON headers
#     # POST request
#     if request.method == 'POST':
#         print(request.get_json())  # parse as JSON
#         return 'Sucesss', 200

if __name__ == "__main__":
    app.run(debug=True)
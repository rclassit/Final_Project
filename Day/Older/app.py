import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import requests
import json

app = Flask(__name__)
#model=None
model = pickle.load(open('pickle_rf.pkl', 'rb'))

#sample data
# data = [4,2,3,4,3,6]

#route for home
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/results',methods=['POST'])
def results():
    
    # data = request.get_json(force=True)
    # prediction = model.predict([np.array(data)])
    # print(request.data)
    
    #response_dict=json.loads(request.data)
    
    #below response_dict is input for model
    input = request.data
    data = [input[0],input[1],input[2],input[3],input[4],input[5]]
   
    #print(response_dict["overall"])

    prediction = model.predict(np.array([data]))
    print(f'this is the prediction: {prediction}')

    #eventually put model output below 

    return render_template(prediction_text=prediction)
    #return jsonify("successfully connected to web api")


if __name__ == "__main__":
    app.run(debug=True)
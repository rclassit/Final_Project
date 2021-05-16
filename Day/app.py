import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import requests
import json
from sklearn import *


app = Flask(__name__)

model = pickle.load(open('pickle_rf.pkl', 'rb'))

# sample data
data = [4,2,3,4,3,6]
prediction = model.predict(np.array([data]))
    
print(prediction)

#route for home
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/results',methods=['POST'])
def results():
    response_dict=json.loads(request.data)
    int_features = [int(x) for x in request.data]
    final_features = [np.array(int_features)]
    prediction= model.predict(final_features)
    print(request.data)
    
    

    # below response_dict is input for model
    print(response_dict["overall"])

    
    # eventually put model output below (in jsonify)
    return jsonify("successfully connected to web api")
    return render_template('index.html', prediction_text='Sales should be $ {}'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)
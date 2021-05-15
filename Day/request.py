import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


#this does something but it's not all working (5/14 10pm)


app = Flask(__name__)
model = pickle.load(open('pickle_rf.pkl', 'rb'))

#sample data
# data = [4,2,3,4,3,6]
# prediction = model.predict(np.array([data]))
    
#print(prediction)

#route for home
@app.route('/')
def home():
    return render_template('/template/index.html')

#API receives details through html; needs to be connected somehow to submit button/js getparams function
#little bit of code in get params function may work?

@app.route('/predict',methods=['POST'])
def predict():

    data = request.get_json(force=True)
    prediction = model.predict(data)

    #here is where we can rewrite the prediction from an array to the beer style
    output = prediction

    return render_template('/template/index.html', prediction_text='{}'.format(output))

#results makes another POST request to /results; recieves JSON inputs, uses model to make prediction
#returns prediction in JSON which can be accessed through API endpoint
#not sure how this is different from /predict ¯\_(ツ)_/¯
@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)

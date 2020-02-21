# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
import flask
import numpy as np
from flask import Flask, request, jsonify
import pickle

path = "//192.168.2.32/Group/Data Team/Abul/1. Code/O2_P12_RecommendationEngine/RecomAPI/flask-salary-predictor-master"

app = Flask(__name__)

# Load the model
model = pickle.load(open(path+'model.pkl','rb'))

@app.route('/api',methods=['POST'])

def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[np.array(data['exp'])]])

    # Take the first value of prediction
    output = prediction[0]

    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    try:
    	app.run(port=5000, debug=True)
    except:
    	print("Server is exited unexpectedly. Please contact server admin.")

app = flask.Flask(__name__)
app.config["DEBUG"] = True
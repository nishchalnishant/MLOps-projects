Developing a web service
The next step is to package this model into a web service that, when given the data through a POST request, returns the MPG (Miles per Gallon) predictions as a response.

I am using the Flask web framework, a commonly used lightweight framework for developing web services in Python. In my opinion, it is probably the easiest way to implement a web service.

Flask gets you started with very little code and you don’t need to worry about the complexity of handling with HTTP requests and responses.

Here are the steps:

Create a new directory for your flask application.
Set up a dedicated environment with dependencies installed using pip.
Install the following packages:
pandas
numpy
sklearn
flask
gunicorn
seaborn
The next step is to activate this environment and start developing a simple endpoint to test the application:

Create a new file, main.py and import the flask module:

from flask import Flask
Create a Flask app by instantiating the Flask class:

##creating a flask app and naming it "app"
app = Flask('app')
Create a route and a function corresponding to it that will return a simple string:

@app.route('/test', methods=['GET'])
def test():
return 'Pinging Model Application!!'
The above code makes use of decorators — an advanced Python feature. You can read more about decorators here.

We don’t need a deep understanding of decorators, just that adding a decorator @app.route on top of the test() function assigns that web service address to that function.

Now, to run the application we need this last piece of code:

if **name** == ‘**main**’:
app.run(debug=True, host=’0.0.0.0', port=9696)
The run method starts our flask application service. The 3 parameters specify:

debug=True — restarts the application automatically when it encounters any change in the code
host=’0.0.0.0' — makes the web service public
port=9696 — the port that we use to access the application
Now, in your terminal run the main.py:

python main.py

Opening the URL http://0.0.0.0:9696/test in your browser will print the response string on the webpage:

With the application now running, let’s run the model.

Create a new directory model_files to store all the model-related code.

In this directory, create a ml_model.py file which will contain the data preparation code and the predict function we wrote here.

Copy and paste the libraries you imported earlier in the article and the preprocessing/transformation functions. The file should look like this:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer

##functions

def preprocess_origin_cols(df):
df["Origin"] = df["Origin"].map({1: "India", 2: "USA", 3: "Germany"})
return df

acc_ix, hpower_ix, cyl_ix = 3, 5, 1

class CustomAttrAdder(BaseEstimator, TransformerMixin):
def **init**(self, acc*on_power=True): # no \*args or \*\*kargs
self.acc_on_power = acc_on_power
def fit(self, X, y=None):
return self # nothing else to do
def transform(self, X):
acc_on_cyl = X[:, acc_ix] / X[:, cyl_ix]
if self.acc_on_power:
acc_on_power = X[:, acc_ix] / X[:, hpower_ix]
return np.c*[X, acc_on_power, acc_on_cyl]

        return np.c_[X, acc_on_cyl]

def num_pipeline_transformer(data):
numerics = ['float64', 'int64']

    num_attrs = data.select_dtypes(include=numerics)

    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('attrs_adder', CustomAttrAdder()),
        ('std_scaler', StandardScaler()),
        ])
    return num_attrs, num_pipeline

def pipeline_transformer(data):

    cat_attrs = ["Origin"]
    num_attrs, num_pipeline = num_pipeline_transformer(data)

    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, list(num_attrs)),
        ("cat", OneHotEncoder(), cat_attrs),
        ])
    full_pipeline.fit_transform(data)
    return full_pipeline

def predict_mpg(config, model):

    if type(config) == dict:
        df = pd.DataFrame(config)
    else:
        df = config

    preproc_df = preprocess_origin_cols(df)
    print(preproc_df)
    pipeline = pipeline_transformer(preproc_df)
    prepared_df = pipeline.transform(preproc_df)
    print(len(prepared_df[0]))
    y_pred = model.predict(prepared_df)
    return y_pred

In the same directory add your saved model.bin file as well.

Now, in the main.py we are going to import the predict_mpg function to make predictions. But to do that we are required to create an empty **init**.py file to tell Python that the directory is a package.

Your directory should have this tree:

Next up, define the predict/ route that will accept the vehicle_config from an HTTP POST request and return the predictions using the model and predict_mpg() method.

In your main.py, first import:

import pickle
from flask import Flask, request, jsonify
from model_files.ml_model import predict_mpg
Then add the predict route and the corresponding function:

@app.route('/predict', methods=['POST'])
def predict():
vehicle = request.get_json()
print(vehicle)
with open('./model_files/model.bin', 'rb') as f_in:
model = pickle.load(f_in)
f_in.close()
predictions = predict_mpg(vehicle, model)

    result = {
        'mpg_prediction': list(predictions)
    }
    return jsonify(result)

Here, we’ll only be accepting POST request for our function and thus we have methods=[‘POST’] in the decorator.

First, we capture the data( vehicle_config) from our request using the get_json() method and store it in the variable vehicle.
Then we load the trained model into the model variable from the file we have in the model_files folder.
Now, we make the predictions by calling the predict_mpg function and passing the vehicle and model.
We create a JSON response of this array returned in the predictions variable and return this JSON as the method response.
We can test this route using Postman or the requests package and then start the server running the main.py. Then in your notebook, add this code to send a POST request with the vehicle_config:

import requests

url = “http://localhost:9696/predict"
r = requests.post(url, json = vehicle_config)
r.text.strip()

##output: '{"mpg_predictions":[34.60333333333333,19.32333333333333,14.893333333333333]}'
Great! Now, comes the last part: this same functionality should work when deployed on a remote server.

https://www.freecodecamp.org/news/end-to-end-machine-learning-project-turorial/

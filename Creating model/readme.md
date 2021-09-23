- In this section our goal is to create the model we are going to use through out this repo.

- We would start with a bad model then after some iteration we wolud improve our model performance and deploy the improved model.

- Here we have use Tensorflow to create this NLP model but there are many other packages we can use to create ml models , such as SKlearn , Pytorch etc.

- In addition to above packages we are also going to use the data analysis packages such as pandas , numpy and seaborn.

Cheat sheet for -

- Sklearn - https://whimsical.com/sklearn-LcpNYZXMZzGrDvVhyhDNCn

#######################################
#######################################
#######################################
#######################################

Saving the Trained Model
Once you’re confident enough to take your trained and tested model into the production-ready environment, the first step is to save it into a .h5 or .bin file using a library like pickle .

Make sure you have pickle installed in your environment.

Next, let’s import the module and dump the model into a .bin file:

import pickle

##dump the model into a file
with open("model.bin", 'wb') as f_out:
pickle.dump(final_model, f_out) # write final_model in .bin file
f_out.close() # close the file
This will save your model in your present working directory unless you specify some other path.

It’s time to test if we are able to use this file to load our model and make predictions. We are going to use the same vehicle config as we defined above:

##vehicle config
vehicle_config = {
'Cylinders': [4, 6, 8],
'Displacement': [155.0, 160.0, 165.5],
'Horsepower': [93.0, 130.0, 98.0],
'Weight': [2500.0, 3150.0, 2600.0],
'Acceleration': [15.0, 14.0, 16.0],
'Model Year': [81, 80, 78],
'Origin': [3, 2, 1]
}
Let’s load the model from the file:

##loading the model from the saved file
with open('model.bin', 'rb') as f_in:
model = pickle.load(f_in)
Make predictions on the vehicle_config:

##defined in prev_blog
predict_mpg(vehicle_config, model)

##output: array([34.83333333, 18.50666667, 20.56333333])
The output is the same as we predicted earlier using final_model.

# End to End ML deployment

When it comes to ML deployment we have many options.

In order to deploy any trained model, you need the following:

- A trained model ready to deploy — save the model into a file to be further loaded and used by the web service.

- A web service — that gives a purpose for your model to be used in practice. For our fuel consumption model, it can be using the vehicle configuration to predict its efficiency. We’ll use Flask to develop this service.

- A cloud service provider — you need special cloud servers to deploy the application. For simplicity, we are going to use Heroku for this (I'll cover AWS and GCP in other articles).

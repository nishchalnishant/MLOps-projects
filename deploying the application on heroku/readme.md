In this section we are going to discuss ways to deploy our ml model into production.

https://www.freecodecamp.org/news/deploy-your-machine-learning-models-for-free/

# Model Deployment and challenges

Unique for each specific case, we will go over the most common cases pertaining to deployment.

Machine learning applications differ in nature compared to other typical
software applications such as mobile applications in two main ways.
• Underlying model
• Underlying data

In simple terms we are exposing the ml models as REST API endpoints to serve the reuqests.

Model deployment can be seen as the last step in ML project lifecycle but is the begining of the model management phase where we continously check for better performing model , retraining the model if there is data drift .

Dependig on the use case the model deployment practices varies a lot.

In this repository we will see deployment from smaller scale to larger scale .

- we would start from deploying ml models using flask api on any PAAS provider . In ths case we are using heroku

- Then we will contanarize the same flask web but dockerize the entire application and run it on any PAAS provider here we are using heroku.

- Then we will use the Container orchestrator to manage our containers . Athough there are many orchestrators we are going to use the Kuber netes and deploy it .

Different PAAS providers we can use --

Algorithmia

- Algorithmia is a MLOps (machine learning operations) tool founded by Diego Oppenheimer and Kenny Daniel that provides a simple and faster way to deploy your machine learning model into production.

-Algorithmia specializes in "algorithms as a service". It allows users to create code snippets that run the ML model and then host them on Algorithmia. Then you can call your code as an API.

PythonAnywhere

- platform as a service based on the Python programming language.

Heroku

Google Cloud Platform

Microsoft Azure Functions

AWS Lambda

Now your model can be used for different applications of your choice, such as web apps, mobile apps, or e-commerce, by a simple API call from Algorithmia.

To deploy this flask application on Heroku, you need to follow these very simple steps:

Create a Procfile in the main directory — this contains the command to get the run the application on the server.
Add the following in your Procfile:
web: gunicorn wsgi:app
We are using gunicorn (installed earlier) to deploy the application:

Gunicorn is a pure-Python HTTP server for WSGI applications. It allows you to run any Python application concurrently by running multiple Python processes within a single dyno. It provides a perfect balance of performance, flexibility, and configuration simplicity.
Now, create a wsgi.py file and add:

##importing the app from main file
from main import app

if **name** == “**main**”:
app.run()
Make sure you delete the run code from the main.py .

Write all the python dependencies into requirements.txt.

You can use pip freeze > requirements.txt or simply put the above-mentioned list of packages + any other package that your application is using.

Now, using the terminal,

initialize an empty git repository,
add the files to the staging area,
and commit files to the local repository:
$ git init
$ git add .
$ git commit -m "Initial Commit"
Next, create a Heroku account if you haven’t already. Then login to the Heroku CLI:

heroku login
Approve the login from the browser as the page pops up.

Now create a flask app:

heroku create <name of your app>
I named it mpg-flask-app. It will create a flask app and will give us a URL on which the app will be deployed.

Finally, push all your code to Heroku remote:

$ git push heroku master

And Voilà! Your web service is now deployed on https://mpg-flask-app.herokuapp.com/predict.

Again, test the endpoint using the request package by sending the same vehicle config:

With that, you have all the major skills you need to start building more complex ML applications.

You can refer to my GitHub repository for this project.

And you can develop this entire project along with me:

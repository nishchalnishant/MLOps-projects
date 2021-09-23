from predictionFile import Prediction
from trainQnAModel import ModelTraining

from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin

#predict(text)
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    user_story = request.json["user_story"].split(' ')
    user_query = request.json["user_query"].split(' ')
    predctnObj = Prediction()
    prediction = predctnObj.executeProcessing(user_story, user_query)
    print(prediction)
    print(type(prediction))
    return { ' '.join(user_story), ' '.join(user_query), '| Prediction:', prediction }


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0', port=7000, debug=True)
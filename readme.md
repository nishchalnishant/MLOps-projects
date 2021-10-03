# How to Run this project in your system

clone into this repository git clone https://github.com/nishchalnishant/MLOps-projects.git

install required packages !pip install requirements.txt

# End to End ML deployment using DVC and CML

- Continous integeration using CML and github actions

- Continous deployment using GitHub Pages.

- The deployed model is in the main branch of the repo while the experiments are on other branches.

- Every time something in this repository changes we will rebuild this model and re eavluate the performance of the model and give a repot on the performance of the model.

# Aim of this project --

We are starting with the predictions for the amount of air pollutants for all air quality stations in Patna, if all goes well then we will move onto Delhi.

# Data --

- Data is from CBCB website .

- We are storing the data into the repository intially.

- later we are going to add a link to the data.

# Continous integeration --

- There are two instances where integeration is taking place.

- After each comit

- - These comits can be a new model or a new feture on which we can train the data .

- - The metric for the newly trained model is generated where we see if it is performing better than the previous one .

- Every hour data for the last hour is fetched by the api and added to the initial data.

- - The metric is generated and if the model performcnce crosses a threshold then we retrain the model on recent data to get a better model.

# Timeline

- Starting with getting data for 4 major pollutants in Patna .
  - Got data from the CPCB website from 01/07/2020 to 25/08/2021.
  - As the data is less tan 100 MB we are storing it into our git repository, if the data exceeds then we will store the data on cloud and add a script to download the data data in 'get data.py'
  - At first we are going to just take the avg of the last 5 predictions and predict the estimated [ this is going to be a trial for everything ]

# How to Run this project in your system

clone into this repository git clone https://github.com/nishchalnishant/MLOps-projects.git

install required packages !pip install requirements.txt

# End to End ML deployment using DVC and CML

- Continous integeration using CML

- Continous deployment using GitHub Pages

- Every time something in this repository changes we will rebuild this model and re eavluate the performance of the model and give a repot on the performance of the model.

# Aim of this project --

We are starting with the predictions for the amount of air pollutants for all air quality stations in Patna, if all goes well then we will move onto Delhi.

- Data

# Data --

- Data is from CBCB website .

- We are storing the data into the repository intially.

- later we are going to add a link to the data.

# Timeline

- Starting with getting data for 4 major pollutants in Patna .
  - Got data from the CPCB website from 01/07/2020 to 25/08/2021.
  - As the data is less tan 100 MB we are storing it into our git repository, if the data exceeds then we will store the data on cloud and add a script to download the data data in 'get data.py'
  - At first we are going to just take the avg of the last 5 predictions and predict the estimated [ this is going to be a trial for everything ]

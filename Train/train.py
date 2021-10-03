import pandas as pd
import numpy as np
import os


def univariate_data(dataset, start_index, end_index, history_size, target_size):
  data = []
  labels = []

  start_index = start_index + history_size
  if end_index is None:
    end_index = len(dataset) - target_size

  for i in range(start_index, end_index):
    indices = range(i-history_size, i)
    # Reshape data from (history_size,) to (history_size, 1)
    data.append(np.reshape(dataset[indices], (history_size, 1)))
    labels.append(dataset[i+target_size])
  return np.array(data), np.array(labels)





def create_time_steps(length):
  return list(range(-length, 0))




def baseline(history):
  return np.mean(history)




cities={}   # stores path for all the cities 
cities_result={}

# using the time series split tho chain the cross validation



for i in os.listdir('Data'):
    city_path=os.path.join('Data',i)
    cities[i]={}
    cities_result[i]={}
    
    for j in os.listdir(city_path):
        city_pollutant=os.path.join(city_path,j)
        cities[i][j]={}
        cities_result[i][j]={}

        for k in os.listdir(city_pollutant):
            stations=os.path.join(city_pollutant,k)
            cities[i][j][k]={}
            cities_result[i][j][k]={}

            for l in os.listdir(stations):
                #print(os.path.join(stations,l))
                cities[i][j][k]=str(l)



# looping over each csv file to get the avg of past data and predict the future data 
    
for i in cities.keys():  
    
    for j in cities[i].keys():
        
        for k in cities[i][j].keys():

            print(j)
            
            data_set=pd.read_csv((os.path.join('Data',i,j,k,cities[i][j][k])))

            data_set['From date'] = pd.to_datetime(data_set['From date'])

            temp=cities[i][j][k][:-4]

            data_set=data_set[['From date',temp]]

            data_set=data_set.mask(data_set.eq('None')).dropna()

            # initially we are just dropping na values 
            # Final dataset we are going to train on 

            data_set = data_set.dropna()  

            data_set[temp]=data_set[temp].astype(np.float64)

            ###########################
            
            uni_data = data_set[temp]
            uni_data.index = data_set['From date']

            TRAIN_SPLIT = int(len(uni_data)*0.75)

            uni_data = uni_data.values


            univariate_past_history = 5  # using values from last 5 entries 
            univariate_future_target = 0

            x_train_uni, y_train_uni = univariate_data(uni_data, 0, TRAIN_SPLIT,
                                                    univariate_past_history,
                                                    univariate_future_target)
            x_val_uni, y_val_uni = univariate_data(uni_data, TRAIN_SPLIT, None,
                                                univariate_past_history,
                                                univariate_future_target)
            
            print(temp )
            try:
                print('Prediction for next hour is ', baseline(x_train_uni[0]))
            except IndexError:
                print('Data not available')
   
            print("##################################")
            print("##################################")
            print("##################################")

            print()
            

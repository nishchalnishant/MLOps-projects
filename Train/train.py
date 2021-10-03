import pandas as pd
import numpy as np
import os


cities={}   # stores path for all the cities 
cities_result={}    # stores the predicted result
actual_result={}    # stores the actual resutl
result=pd.DataFrame(columns=['city','pollutant','station','predicted','actual','diffenrece'])

# using the time series split tho chain the cross validation

for i in os.listdir('Data'):
    city_path=os.path.join('Data',i)
    cities[i]={}
    cities_result[i]={}
    actual_result[i]={}
    
    for j in os.listdir(city_path):
        city_pollutant=os.path.join(city_path,j)
        cities[i][j]={}
        cities_result[i][j]={}
        actual_result[i][j]={}

        for k in os.listdir(city_pollutant):
            stations=os.path.join(city_pollutant,k)
            cities[i][j][k]={}
            cities_result[i][j][k]={}
            actual_result[i][j][k]={}

            for l in os.listdir(stations):
                #print(os.path.join(stations,l))
                cities[i][j][k]=str(l)

# looping over each csv file to get the avg of past data and predict the future data 
    
for i in cities.keys():  
    
    for j in cities[i].keys():
        
        for k in cities[i][j].keys():
            
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

            # avg of last 10 data 
            
            cities_result[i][j][k]=data_set.iloc[-10:-1][temp].mean()

            actual_result[i][j][k]=data_set.iloc[-1:][temp].mean()


            #storing the result into a dataframe 
            result=result.append({
            'city':i,
            'pollutant':j,
            'station':k,
            'predicted':cities_result[i][j][k],
            'actual':actual_result[i][j][k],
            'diffenrece':cities_result[i][j][k]-actual_result[i][j][k]},ignore_index=True)

result.to_csv('metrics.csv')

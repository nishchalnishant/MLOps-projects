# getting and appending data 

from datagovindia import DataGovIndia
import pandas
import numpy
from time import gmtime, strftime
# Import writer class from csv module
from csv import writer
import os
from dotenv import load_dotenv
load_dotenv()



YOUR_API_KEY = os.getenv('API_KEY')

datagovin = DataGovIndia(YOUR_API_KEY)

# getting data for all stations for no2 , pm2.5 and pm10
data = datagovin.get_data("3b01bcb80b144abfb6f2c1bfd384ba69",
                          num_results='all',
                           filters={'id':[76,77,78,83,84,85,90,91,92,97,98,99,104,105,106]})

cities={}

for i in os.listdir('Data'):
    city_path=os.path.join('Data',i)
    cities[i]={}
    
    for j in os.listdir(city_path):
        city_pollutant=os.path.join(city_path,j)
        cities[i][j]={}

        for k in os.listdir(city_pollutant):
            stations=os.path.join(city_pollutant,k)
            cities[i][j][k]={}

            for l in os.listdir(stations):
                #print(os.path.join(stations,l))
                cities[i][j][k]=str(l)

id_keys = {'Patna': {'no2': {   'DRM Office Danapur  Patna - BSPCB': '78',
   'Govt. High School Shikarpur  Patna - BSPCB': '85',
   'Muradpur  Patna - BSPCB': '92',
   'Rajbansi Nagar  Patna - BSPCB': '99',
   'Samanpura  Patna - BSPCB': '106'},
  'pm10': {   'DRM Office Danapur  Patna - BSPCB': '77',
   'Govt. High School Shikarpur  Patna - BSPCB': '84',
   'Muradpur  Patna - BSPCB': '91',
   'Rajbansi Nagar  Patna - BSPCB': '98',
   'Samanpura  Patna - BSPCB': '105'},
  'pm2.5': {'DRM Office Danapur  Patna - BSPCB': '76',
   'Govt. High School Shikarpur  Patna - BSPCB': '83',
   'Muradpur  Patna - BSPCB': '90',
   'Rajbansi Nagar  Patna - BSPCB': '97',
   'Samanpura  Patna - BSPCB': '104'}}}


for i in cities.keys():  
    
    for j in cities[i].keys():
        
        for k in cities[i][j].keys():
          if k=='.ipynb_checkpoints':
            pass
          else:
            temp=data[data['id']==id_keys[i][j][k]][['last_update','pollutant_avg']]
            List=[temp.iloc[0]['last_update'],strftime("%Y-%m-%d %H:%M:%S", gmtime()),temp.iloc[0]['pollutant_avg']]

            print((os.path.join('Data',i,j,k,cities[i][j][k])))
            # Open our existing CSV file in append mode
            # Create a file object for this file
            with open((os.path.join('Data',i,j,k,cities[i][j][k])), 'a') as f_object:
              
                # Pass this file object to csv.writer()
                # and get a writer object
                writer_object = writer(f_object)
              
                # Pass the list as an argument into
                # the writerow()
                writer_object.writerow(List)
              
                #Close the file object
                f_object.close()



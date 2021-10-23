import pandas as pd
import numpy as np
import os
import seaborn as sns


"""
we will loop through each xlsx file in the Data folder and try to predict the next pollutant value  
"""

files=os.listdir('Data')

result=pd.DataFrame(columns=['Station','co_predicted','co_actual','co_diff',
    'no2_predicted','no2_actual','no2_diff',
    'o3_predicted','o3_actual','o3_differnce',
    'pm10_predicted','pm10_actual','pm10_diff',
    'pm25_predicted','pm25_actual','pm25_diff',
    'so2_predicted','so2_actual','so2_diff'])

#predicting values for next hour



for i in (files):
    path=os.path.join('Data',i)
    df=pd.read_excel(path)
    
    # avg of last 10 data 
    co_predicted=df.iloc[-5:-1]['co'].mean()
    no2_predicted=df.iloc[-5:-1]['no2'].mean()
    o3_predicted=df.iloc[-5:-1]['o3'].mean()
    pm10_predicted=df.iloc[-5:-1]['pm10'].mean()
    pm25_predicted=df.iloc[-5:-1]['pm25'].mean()
    so2_predicted=df.iloc[-5:-1]['so2'].mean()

    co_actual=df.iloc[-1:]['co'].mean()
    no2_actual=df.iloc[-1:]['no2'].mean()
    o3_actual=df.iloc[-1:]['o3'].mean()
    pm10_actual=df.iloc[-1:]['pm10'].mean()
    pm25_actual=df.iloc[-1:]['pm25'].mean()
    so2_actual=df.iloc[-1:]['so2'].mean()

    result=result.append({
            'Station':i[:-5],
            'co_predicted':co_predicted,
            'co_actual':co_actual,
            'co_diff':(co_predicted-co_actual),
            'no2_predicted':no2_predicted,
            'no2_actual':no2_actual,
            'no2_diff':(no2_predicted-no2_actual),
            'o3_predicted':o3_predicted,
            'o3_actual':o3_actual,
            'o3_differnce':(o3_predicted-o3_actual),
            'pm10_predicted':pm10_predicted,
            'pm10_actual':pm10_actual,
            'pm10_diff':(pm10_predicted-pm10_actual),
            'pm25_predicted':pm25_predicted,
            'pm25_actual':pm25_actual,
            'pm25_diff':(pm25_predicted-pm25_actual),
            'so2_predicted':so2_predicted,
            'so2_actual':so2_actual,
            'so2_diff':(so2_predicted-so2_actual)},ignore_index=True)



last_hour=result[['Station','co_actual','no2_actual','o3_actual','pm10_actual','pm25_actual','so2_actual']]
    
last_hour = last_hour.melt('Station', var_name='cols', value_name='vals')

last_hour_graph = sns.catplot(x="Station", y="vals", hue='cols', data=last_hour, kind='point',height=5, aspect=11.7/8.27)
    
last_hour_graph.savefig("last_hour.png")

diff_df=result[['Station','co_diff','no2_diff','o3_differnce','pm10_diff','pm25_diff','so2_diff']]

diff_df = diff_df.melt('Station', var_name='cols', value_name='vals')

g = sns.catplot(x="Station", y="vals", hue='cols', data=diff_df, kind='point',height=5, aspect=11.7/8.27)

g.savefig("difference.png")
   

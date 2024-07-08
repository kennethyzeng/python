import numpy as np 
import pandas as pd 
import math

data= pd.read_csv('http://hilpisch.com/tr_eikon_eod_data.csv', index_col=0, parse_dates=True)
#print(data)
data=pd.DataFrame(data['AAPL.O'])
#print(data)
print(data.shift(6))   #mean the data shift one down one position  
#Calculates the log returns over the complete history.
data['Returns'] = np.log(data/data.shift())    #log(today's value/nextDay's value  ); if it is NaN, result is NaN
#print(data)
data.dropna(inplace=True)

lags=6
cols=[]
for lag in range(1, lags +1):
    col='lag_{}'.format(lag)
    print(col)
    data[col]= np.sign(data['Returns']).shift(lag)
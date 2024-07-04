"""
S&P 500 index values.

analyze historical index levels for a few years to see how the volatility of the index has fluctuated over time and hope to find
evidence that volatility

• Retrieve index level data from the web
• Calculate the annualized rolling standard deviation of the log returns (volatility)
• Plot the index level data and the volatility results

"""
import numpy as np 
import pandas as pd 
from pylab import plt, mpl 

plt.sytle.use('seaborn')
mpl.rcParams['font.family']='serif'

data=pd.read_csv('../../file.csv', index_col=0, parse_data=True)
data=pd.dataFrame(data['.SPX'])
data.dropna(inplace=True)
data.info()

data['rets'] = np.log(data/data.shift(1))
data['vola'] = data['rets'].rolling(252).std()* np.sqrt(252)
data['.SPX','vola'] = data['rets'].rolling(252).std() * np.sqrt(252)
data[['.SPX', 'vola']].plot(subplots=True, figsize=(10,6))


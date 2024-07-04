"""
"""
import numpy as np 
import math 

S0 = 100
K = 105 
T=1.0
r = 0.05
sigma = 0.2

I =10000
np.random.seed(1000)
z= np.random.standard_normal(I)
ST = S0 * np.exp((r-sigma **2 /2) * T + sigma * math.sqrt(T)*z)
hT=np.maximum(ST -K, 0)
print(hT)


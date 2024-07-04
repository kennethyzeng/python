"""
Algorithmic desciption of the Monte Carlo Valuation procedure. 4 Step 
#1 Draw I pseduo -random numbers z(i) from the standard normal distribution 

#2 Calculate all resulting index levels at maturity ST(i) for given z(i)
note: seem index levels at matuirty mean stock price at maturity 

#3 Calculate all inner values of the option at maturity as hT(i) = max(ST(i) – K, 0).
note: some values are higher than K, others aren't. K is strike price. find the difference; also it will be 0 if below strike price 

#4  Estimate the option present value via the Monte Carlo estimator
note: estimate option present value  

So Monte Carlo estimator is to tell investor the option present value for 1 year option call?
"""

import math
import numpy as np

# Parameter Values
S0 = 100.  # initial index level
K = 105.  # strike price
T = 1.0  # time-to-maturity (unit: year)
r = 0.05  # riskless short rate
sigma = 0.2  # volatility

I = 10000  # number of simulations

# Valuation Algorithm produce 
#step 1:
z = np.random.standard_normal(I)  # pseudo-random numbers  #sunykate the estimate function how many times

#step 2 : index values at maturity
ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * math.sqrt(T) * z)  #numpy array
#print(ST)
#step 3:
hT = np.maximum(ST - K, 0)  # Option payoff at maturity;
#print(np.mean(hT))   #mean is sum of elements divide of size of elements; it is single value, not numpy array

#step 4: # Monte Carlo estimator
C0 = math.exp(-r * T) * np.mean(hT)   #option present value estimation


# Result Output
print('Value of the European call option %5.3f.' % C0)
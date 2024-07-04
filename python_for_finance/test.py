import numpy as np 
loops=2500000
a = np.arange(1, loops )
r = 3* np.log(a) + np.cos(a) **2
print(r)
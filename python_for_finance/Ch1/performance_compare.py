import math 
loops = 2500000
a = range(1, loops)
def f(x):
    return 3 * math.log(x) + math.cos(x) **2 

r = [f(x) for x in a]
print(r)

#######################

import numpy as np 
loops=2500000
a = np.arange(1, loops )
r = 3* np.log(a) + np.cos(a) **2
print(r)

####################faster. with multiple thread
import numexpr as ne 
import numpy as np 
loops = 2500000
a = np.arange(1, loops)
ne.set_num_threads(1)
f = '3*log(a) + cos(a) **2'
r = ne.evaluate(f)
print(r)

###faster when set the multiple thread 
ne.set_num_threads(4)  #set 4 thread 
r=ne.evaluate(f)
print(r)
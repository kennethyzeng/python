########method 1: kind of slow
import math
import timeit

loops = 10
a = range(1, loops)
def f(x):
    return 3 * math.log(x) + math.cos(x) ** 2

r = [f(x) for x in a]

###################Method 2: faster 
import math 
loops = 2500000
a = range(1, loops)
def f(x):
    return 3 * math.log(x) + math.cos(x) **2 

r = [f(x) for x in a]
print(r)

#####################Method 3: 
import numexpr as ne 
import numpy as np 
loops = 2500000
a = np.arange(1, loops)
ne.set_num_threads(1)
f = '3*log(a) + cos(a) **2'
r = ne.evaluate(f)
print(r)
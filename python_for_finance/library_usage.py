###################  1 Math  ###################
#math.log(x, base)   #default for base is 'e'
import math 
print(math.log(1))   
print(math.log(8,2))  #4

res=math.exp(1)   #e^1
math.cos(9) **2 

####################   2 nummpy ###################
import numpy as np 
"""
np.random.see(value)   #input seed value to generate repeated random number 
np.random.see(0) #generate pseudo-random number based on see. seed can be any number
https://www.analyticsvidhya.com/blog/2021/12/what-does-numpy-random-seed-do/
                 
"""

#
I =20
print(np.random.seed(0))
z = np.random.standard_normal(I)  #output is the list; positive or negative float value
for i in range(len(z)):
    print(z[i])

#
I =20
np.random.seed(1000)
z = np.random.permutation(I)  #output is the numpy array of integer between 0-20
for i in range(len(z)):
    print(z[i])

#
s =np.randome.choice(5, 10)  #numpy array with random number between 0 and 5 with the size 10

#
np.exp(1)   #e^1

#
hT=[1,2,5,10]
np.mean(hT)   #(1+2+5+10)/4

#
ST=[100,-97, 113,140,105]
K=100
np.maximum(ST - K, 0)

#
import numpy as np 
loops=2500000
a = np.arange(1, loops )
r = 3* np.log(a) + np.cos(a) **2
print(r)


####################  3  sys   ###################
#output python version and clang version
import sys
print(sys.version)

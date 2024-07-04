import sys
import numpy as np
import math

#print(sys.version)

I =30
np.random.seed(1000)
z = np.random.permutation(I)
#for i in range(len(z)):
#    print(z[i])

hT = np.maximum(10,0)
print(hT)

res=math.exp(1)
print(res)

print(np.exp(0))

hT=[1,2,5,10]
res1=np.mean(hT) 
print(res1)



indx = np.random.randint(0,61,12) 
print(indx)
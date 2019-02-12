import numpy as np


array=np.random.rand(3,3)
print(array)
print("******************************************************************")
print(array.max(axis=1))




#Alternatively


arr=[[1,2,3],[4,5,6],[7,8,9]]
print(list(map(max,arr)))


#to print maximum element

print(max(map(max,arr)))

#using numpy
print(array.max())

import numpy as np
#MATRIX don vi.
""" a = np.identity(5)
print(a)

#ma tran lap. 
arr = np.array([[1,2,3]])
r1  = np.repeat(arr,3,axis=0)
print(r1) """

# long 2 ma tran. vao nhau
output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1] = 9
print(z)

output[1:4, 1:4] = z
print(output)

#Becareful when copying arrays
a = np.array([1,2,3])
b = a
b[0] = 100 
print(a)


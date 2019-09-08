import numpy as np
#Linear Algebra
a = np.full((2,3),2)
print(a)

b = np.ones((3,2))
print(b)

print(np.matmul(a,b))

#Check again with the identity matrix 
c = np.identity(3)
print(np.linalg.det(c))


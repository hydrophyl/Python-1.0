import numpy as np
a = np.array([[1,2,3,4,5,6,7],[2,5,3,6,2,7,7],[4,4,6,8,3,5,1]])
print(a)
#Get a specific element [r, c]
print(a[1,3])

#Get a specific row
print(a[0, :])
print(a[:, 2])

#Getting a little more fancy [startindex:endindex:stepsize]
print(a[0, 1:6:2])

#Change something
a[1,6] = 10
print(a[1,:])
print(a)

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
print(b[1,:,1])
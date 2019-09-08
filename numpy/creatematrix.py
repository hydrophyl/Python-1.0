import numpy as np
#all  0s matrix
a = np.zeros((2,3))
print(a)

#all 1s matrix
b = np.ones((4,2,2), dtype='int32')
print(b)

#all any number matrix
c = np.full((2,2), 12)
print(c)

#full matrix
d = np.full(a.shape, 4)
print(d)

e = np.random.random_sample(a.shape)
print(e)

f = np.random.rand(4,2)
print(f)

g = np.random.randint(-5,7, size=(3,3))
print(g)

h = np.random.randint(2,10, size=a.shape)
print(h)
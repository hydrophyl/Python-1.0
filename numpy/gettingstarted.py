#Numpy lesson - Crash course of freecodecamp.org
#Why Numpy faster? - Fixed Type
#Faster to read less bytes of memory
import numpy as np
import matplotlib.pyplot as plt
a = np.array([1.,3.,5.])
b = np.array([1.,2.,3.])

e  = np.linspace(1,5,10)

x = np.arange(0,3*np.pi, 0.1)

y = np.tan(x)

plt.plot(x,y)
plt.show()
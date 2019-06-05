import matplotlib.pyplot as plt
import numpy as np

#Prepare the data
x = np.linspace(0,20)

#Plot the data
plt.plot(x, x, label='linear')
plt.plot(x, x, label='')
# Add a legend
plt.legend()

#Show the plot
plt.show()

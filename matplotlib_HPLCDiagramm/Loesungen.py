import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#koordinates annehmen
#Theobromin
x = [0,1]
y = [0,40000]
plt.plot(x, y, color='midnightblue', label='Theobromin')
#Coffein
x2 = [0,5]
y2 = [0,160000]
plt.plot(x2, y2,color='lightcoral', label='Coffein')
plt.axhline(y = 12836,color='darkred', label='Power Focus')
plt.axhline(y = 20274,color='darkred', label='Power Focus')
plt.axhline(y = 1845,color='darkorange', label='Earl Grey')
plt.axhline(y = 71183,color='darkorange', label='Earl Grey')
plt.axhline(y = 8667,color='black', label='Kaffee')
plt.axhline(y = 8801,color='black', label='Kaffee')
plt.axhline(y = 9513,color='darkgreen', label='Reistee')
plt.title('Diagramm Theobromin & Coffeingehalt in Kaffee und Tee\nLaura Hielscher & Duy Nguyen 23.04.2019')
plt.xlabel('Konzentration (mg/L)')
plt.ylabel('Area')
plt.legend()
plt.show()

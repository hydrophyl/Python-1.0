import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#koordinates annehmen
#Theobromin
x = [0,1,11]
y = [0,40000,400000]
plt.plot(x, y, color='midnightblue', label='Theobromin')
#Coffein
x2 = [0,5,33,60]
y2 = [0,160000,1100000,2000000]
plt.plot(x2, y2,color='firebrick', label='Coffein')
plt.axhline(y = 61402,color='darkorange', label='Kakao 99%')
plt.axhline(y = 1931119,color='darkorange', label='Kakao 99%')
plt.axhline(y = 21467,color='g', label='Kakao 40%')
plt.axhline(y = 399884,color='g', label='Kakao 40%')
plt.axhline(y = 83894,color='darkviolet', label='Kakao 35%')
plt.axhline(y = 321990,color='darkviolet', label='Kakao 35%')
plt.title('Diagramm Theobromin & Coffeingehalt in Schokolade\nLaura Hielscher & Duy Nguyen 23.04.2019')
plt.xlabel('Konzentration (mg/L)')
plt.ylabel('Area')
plt.legend()
plt.show()

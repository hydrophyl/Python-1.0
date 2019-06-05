import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read files
kurve1 = pd.read_csv('BioP18.Versuch1.Messung.csv', delimiter=',')
kurve2 = pd.read_csv('BioP18.Versuch2.Messung.csv', delimiter=',')
kurve3 = pd.read_csv('BioP18.Versuch3.Messung.csv', delimiter=',')

#specify header PT1,PT2,PT3,PT4,PT5

pt1_list = kurve3["PT1"].tolist()
pt2_list = kurve3["PT2"].tolist()
pt3_list = kurve3["PT3"].tolist()
pt4_list = kurve3["PT4"].tolist()
pt5_list = kurve3["PT5"].tolist()

sollwert = [140] * len(pt1_list)
counter = list(np.arange(0,len(pt1_list),1))
#print(counter)
plt.plot(counter, sollwert, label='Sollwert')
plt.plot(counter, pt1_list, label='PT1')
plt.plot(counter, pt2_list, label='PT2 - in der Mitte gestellte Temperaturfuehler')
plt.plot(counter, pt3_list, label='PT3')
plt.plot(counter, pt4_list, label='PT4')
plt.plot(counter, pt5_list, label='PT5')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Korrektes Beladen des auf 140 Grad C vorgewaermten Sterilisators mit folgenden Komponenten mit Bedienungsfehler')
plt.legend()
plt.show()




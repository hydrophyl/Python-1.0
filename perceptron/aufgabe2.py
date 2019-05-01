#Scikit-learn
#Upgrade version from aufgabe1.py

from sklearn import tree
import pandas as pd

#ANCHOR input dataset:
#Definition



train_data = [list(i) for i in zip(temp,nieder)]
#Output lists input
train_output = []
for i in range(n):
    eingabe = int(input('ist gutes Wetter? 1 wenn ja, 0 wenn nein: '))
    train_output.append(eingabe)
#1 is 'schoen'  0  is 'schlecht'
#ANCHOR Train classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data,train_output)

print('Prognose: [0]-Schlechtes Wetter | [1]-Gutes Wetter')
#TODO test data input
#Counter i
i = 0
temperatur_eingabe = []
niederschlag_eingabe = []
prognose = []
print('Temperatur- und Niederschlag-eingabe. Geben [0,0] zum Abbrechen.')
while(i < 5):
    temperatur = input('Temperatureingabe: ')
    temperatur_eingabe.append(temperatur)
    niederschlag = input('Niederschlageingabe: ')
    niederschlag_eingabe.append(niederschlag)
    print(clf.predict([[temperatur,niederschlag]]))
    prognose.append(clf.predict([[temperatur, niederschlag]]))
    i = i + 1

print("Data \t Temperatur \t Niederschlag \t Prognose")
for data_size in range(4):
    print(f"{data_size} \t {temperatur_eingabe[data_size]} \t\t {niederschlag_eingabe[data_size]} \t\t {prognose[data_size]}")

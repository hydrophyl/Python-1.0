#Scikit-learn
from sklearn import tree
#1 is 'smooth'  0  is 'bumpy'
features = [[140,1], [130, 1], [150,0], [170,0]]
#0 is 'apple, 1 is orange
labels = [0, 0, 1, 1]

#Train classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print(clf.predict([[155,0]]))

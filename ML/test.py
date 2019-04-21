import numpy as np 
from sklearn.datasets import load_iris
from sklearn import tree

flower = load_iris()
test_idx = [0,50,100]

#Training data
train_target = np.delete(flower.target, test_idx)
train_data = np.delete(flower.data, test_idx, axis = 0)

#Testing data
test_target = flower.target[test_idx]
test_data = flower.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print(test_target)
print(clf.predict(test_data))

#viz code
from  sklearn.externals.six import StringIO
import pydot
dot_data = StringIO()
tree.export_graphviz(clf,
                        out_file=dot_data,
                        feature_names=flower.feature_names,
                        class_names=flower.target_names,
                        filled=True, rounded=True,
                        impurity=False)

graph = pydot.graph_from_dot_data(dot_data)
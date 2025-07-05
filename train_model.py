from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib 


iris = load_iris()
x,y = iris.data , iris.target

clf = DecisionTreeClassifier()
clf.fit(x,y)

joblib.dump(clf, 'iris_model.pkl')
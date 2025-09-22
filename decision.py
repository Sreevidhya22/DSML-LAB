from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
iris=load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
c_de=DecisionTreeClassifier()
c_de.fit(x_train,y_train)
y_pred=c_de.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
plt.figure(figsize=(12,8))
plot_tree(c_de, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()


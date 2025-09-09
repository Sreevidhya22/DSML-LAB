import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
data=pd.read_csv('dataset2.csv')
X=data[['sweetness','crunchiness']]
y=data['foodtype']
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.3, random_state=1)
model=KNeighborsClassifier(n_neighbors=2)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Enter the sample data:")
sweetness = int(input("sweetness : "))
crunchiness= int(input("crunchiness : "))
sample = pd.DataFrame([[sweetness, crunchiness]], columns=['sweetness', 'crunchiness'])
pred_label = model.predict(sample)
print("Predicted foodtype:", pred_label[0])


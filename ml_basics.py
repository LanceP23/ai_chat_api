import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv('./data/engineers.csv')
df['level'] = df['years_experience'].apply(lambda x: 1 if x>= 5 else 0)

for experience in df['experience']
    if experience >= 5:
        level  = 1
    else:
        level = 0

X2 = df[['years_experience','age']]
Y2 = df['salary']

X = np.array([[1],[2],[3],[4],[5]])
Y = np.array([35000,40000,50000,60000,72000])

model = LinearRegression()


X_train = X 
Y_train = Y

model.fit(X_train, Y_train)

prediction = model.predict([[6]])
print(f"Predicted salary for 6 years experience: {prediction[0]}")

X_train, X_test , y_train, y_test = train_test_split(X,Y,test_size=0.2, random_state=42)
model2 = LinearRegression()

model2.fit(X_train, y_train)
predictions = model2.predict(X_test)
error = mean_absolute_error(y_test,predictions)
print(f"mean_absolute_error: {error}")

X_class = np.array([[1],[2],[3],[6],[8],[10],[12]])
y_class = np.array([0,0,0,1,1,1,1])

clf = RandomForestClassifier()
clf.fit(X_class, y_class)

years= [[4]]
result=clf.predict(years)
print(f"4 years experience ->{'Senior' if result[0] == 1 else 'Junior'}")


X_train2, X_test2, y_train2, y_test2 = train_test_split(X_class,y_class, test_size=0.3, random_state= 42)
clf2 = RandomForestClassifier()
clf2.fit(X_train2,y_train)

y_pred = clf.predict(X_test2)
print(confusion_matrix(y_test2, y_pred))
print(classification_report(y_test2,y_pred))


X_train3 = X2
y_train3 = Y2

model3 = LinearRegression()

X_train3, X_test3 , y_train3, y_test3 = train_test_split(X2,Y2,test_size=0.2, random_state=42)
model3.fit(X_train3,y_train3)
predictions2 = model3.predict(X_test3)
error2 = mean_absolute_error(y_test3,predictions2)

print(f"{predictions2}")
print(f"MAE:{error2} ")



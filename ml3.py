from sklearn.linear_model import LinearRegression
import pandas
from sklearn import preprocessing
import numpy as np

df = pandas.read_csv('insurance.csv')
#X = np.array(df["age"]).reshape((-1, 1))
X = list(zip(df["age"], df["bmi"]))
y = np.array(df["charges"]) 
#X.reshape(-1, 1)
#y.reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)

X_predict = [[35, 45]]
y_predict = model.predict(X_predict)
print(y_predict)

import pickle
pickle.dump(model, open('model_iris', 'wb'))
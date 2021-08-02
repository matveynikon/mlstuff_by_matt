import pandas
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing


df = pandas.read_csv('IRIS.csv')
model = KNeighborsClassifier(n_neighbors=3)

features = list(zip(df["sepal_length"], df["sepal_width"]))

le = preprocessing.LabelEncoder()
label = le.fit_transform(df["species"])

model.fit(features,df["species"])

"""sns.scatterplot(x='sepal_length', y='sepal_width',
                hue='species', data=df, )
  
# Placing Legend outside the Figure
plt.legend(bbox_to_anchor=(1, 1), loc=1)
  
plt.show()
"""
predicted = model.predict([[4.6,5.8]]) 
print(predicted)
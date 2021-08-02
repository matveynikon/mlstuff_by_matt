import matplotlib.pyplot as plt
import seaborn as sns
import pandas

# data
data = pandas.read_csv('insurance.csv')

# use the scatterplot function to build the bubble map
sns.scatterplot(data=data, x="age", y="charges", size="bmi", legend=False, sizes=(6, 600))

# show the graph
plt.show()
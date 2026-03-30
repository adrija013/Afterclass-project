import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris = pd.read_csv('Iris Dataset.csv')

sns.barplot(x=iris['Species'], y=iris['SepalLengthCm'])
plt.show()

sns.countplot(x=iris['Species'])
plt.show()

sns.boxplot(x=iris['Species'], y=iris['SepalWidthCm'])
plt.show()

sns.swarmplot(x=iris['Species'], y=iris['SepalWidthCm'])
plt.show()

sns.distplot(iris['SepalWidthCm'])
plt.show()

sns.jointplot(iris['SepalWidthCm'])
plt.show()

sns.pairplot(iris[['SepalLengthCm','SepalWidthCm', 'PetalLengthCm','PetalWidthCm']],hue=iris['Species'])
plt.show()
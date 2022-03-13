import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as LR
from sklearn.preprocessing import PolynomialFeatures as PF
dataset = pd.read_csv('dataset.csv')
X= dataset.iloc[:,[0]].values
y= dataset.iloc[:,[1]].values
X_train, X_test , y_train ,y_test = tts(X,y)
polyModel = PF(degree=4)
linearModel = LR()
polyFeatures = polyModel.fit_transform(X)
linearModel.fit(polyFeatures,y)
y_pred = linearModel.predict(polyFeatures)
plt.scatter(X,y)
plt.plot(X,y_pred)
plt.title('Polynomial Regression')
plt.xlabel('Marks')
plt.ylabel('Roll no')
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import matplotlib.pyplot as plt

def MSE_loss(y_predict, y):
    return ((y_predict-y)**2).sum()/len(y)



data = pd.read_csv('dataset1.csv')
x = data['X'].to_numpy().reshape(-1,1)
y = 5*x + 50*np.random.randn(100,1)


#scikit-learn 
x = x.reshape(-1,1)
y = y.reshape(-1,1)
regr = linear_model.LinearRegression()
regr.fit(x,y)
y_pred = regr.predict(x)


print(f'scikit-learn의 loss : { MSE_loss(y_pred,y) }')
plt.plot(x,y_pred,c='r')
plt.scatter(x,y)
plt.text(20,400,"MSE Loss: {:.2f}".format(MSE_loss(y_pred,y)))
plt.show()

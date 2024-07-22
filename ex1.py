# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 11:56:21 2024

@author: USER
"""

#%% 01-1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import matplotlib.pyplot as plt
def MSE_loss(y_predict, y):
    return ((y_predict-y)**2).sum()/len(y)
def function(x,w,b):
    return w*x+b
data = pd.read_csv('linear.csv')
x = data['X'].to_numpy().reshape(-1,1)
y = 5*x + 50*np.random.randn(100,1)
w = [0.5]
b = [0.5]
loss_history = []
epochs = 100
learning_rate = 1e-4
for i in range(epochs):
    prediction = function(x,w[i],b[i])
    loss_history.append(MSE_loss(prediction,y))
    w.append(w[i]-(learning_rate/len(y))*((prediction-y)*x).sum())
    b.append(b[i]-learning_rate*(prediction-y).sum())
loss_history.append(MSE_loss(function(x,w[-1],b[-1]),y)) 
#초기 학습 plot
plt.plot(x,function(x,w[0],b[0]),c='r')
plt.scatter(x,y)
plt.text(20,400,"MSE Loss: {:.2f}".format(MSE_loss(function(x,w[0],b[0]),y)))
plt.show()

#내 학습 plot
plt.plot(x,function(x,w[-1],b[-1]),c='r')
plt.scatter(x,y)
plt.text(20,400,"MSE Loss: {:.2f}".format(MSE_loss(function(x,w[-1],b[-1]),y)))
plt.show()



#scikit-learn 
x = x.reshape(-1,1)
y = y.reshape(-1,1)
regr = linear_model.LinearRegression()
regr.fit(x,y)
y_pred = regr.predict(x)

# print(f"Normal Eq의 w, b : {theta[1],theta[0]} scikit-learn의 w, b : {regr.coef_[0][0],regr.intercept_[0]}")
# print(f'Normal Eq의 loss : { MSE_loss(function(x,theta[1],theta[0]),y) }')
print(f'scikit-learn의 loss : { MSE_loss(y_pred,y) }')
plt.plot(x,y_pred,c='r')
plt.scatter(x,y)
plt.text(20,400,"MSE Loss: {:.2f}".format(MSE_loss(y_pred,y)))
plt.show()



#%% 01-2

import pandas as pd

df = pd.DataFrame({
    'name' : ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'horse power' : [130, 250, 190, 300, 210, 220, 170], 
    'efficiency': [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2] })

vehicle_df = df.set_index('name')
print(vehicle_df)

from sklearn.linear_model import LinearRegression

X = vehicle_df[['horse power']].to_numpy()
y = vehicle_df['efficiency'].to_numpy()

lin_model1 = LinearRegression()
lin_model1.fit(X, y)

print('계수 :', lin_model1.coef_)
print('절편 :', lin_model1.intercept_)
print('예측 점수 :', lin_model1.score(X, y))

print('270 마력 자동차의 예상 연비 :', lin_model1.predict([[270]])[0].round(2),'km/l')


df = pd.DataFrame({
    'name' : ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'horse power' : [130, 250, 190, 300, 210, 220, 170], 
    'weight': [1900, 2600, 2200, 2900, 2400, 2300, 2100],
    'efficiency': [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2] })

vehicle_df = df.set_index('name')
print(vehicle_df)

from sklearn.linear_model import LinearRegression

X = vehicle_df[['horse power', 'weight']].to_numpy()
y = vehicle_df['efficiency'].to_numpy()

lin_model2 = LinearRegression()
lin_model2.fit(X, y)

print('계수 :', lin_model2.coef_)
print('절편 :', lin_model2.intercept_)
print('예측 점수 :', lin_model2.score(X, y))

print('270 마력 자동차의 예상 연비 :', lin_model2.predict([[270, 2500]])[0].round(2),'km/l')




#%% 01-3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


df = pd.read_csv('nonlinear.csv')

# plt.scatter(df['x'], df['y'])

from sklearn.preprocessing import PolynomialFeatures
X = df['x'].to_numpy()
y = df['y'].to_numpy()
X = X.reshape(-1,1) # 입력을 2차원 벡터가 되게 한다. shape = (m, 1)
feature_cubic = PolynomialFeatures(degree = 3)
X_3 = feature_cubic.fit_transform(X)

lin_model = LinearRegression()
domain = np.linspace(0, 1, 100).reshape(-1,1) # 입력은 2차원 벡터로 변형

lin_model.fit(X_3, y)
domain_3 = feature_cubic.fit_transform(domain)
predictions = lin_model.predict(domain_3)
plt.figure(figsize=(16, 4))
plt.subplot(141)
plt.scatter(df['x'], df['y'],label='data')
plt.plot(domain, predictions, color='r',linewidth=3,label='regression')
plt.title('degree=3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
 

# 
feature_cubic2 = PolynomialFeatures(degree = 30)
X_30 = feature_cubic2.fit_transform(X)

lin_model = LinearRegression()
domain = np.linspace(0, 1, 100).reshape(-1,1) # 입력은 2차원 벡터로 변형

lin_model.fit(X_30, y)
domain_30 = feature_cubic2.fit_transform(domain)
predictions30 = lin_model.predict(domain_30)
plt.subplot(142)
plt.scatter(df['x'], df['y'],label='data')
plt.plot(domain, predictions30, color='r',linewidth=3,label='regression')
plt.title('degree=30')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
 

#
feature_cubic3 = PolynomialFeatures(degree = 300)
X_300 = feature_cubic3.fit_transform(X)

lin_model = LinearRegression()
domain = np.linspace(0, 1, 100).reshape(-1,1) # 입력은 2차원 벡터로 변형

lin_model.fit(X_300, y)
domain_300 = feature_cubic3.fit_transform(domain)
predictions300 = lin_model.predict(domain_300)
plt.subplot(143)
plt.scatter(df['x'], df['y'],label='data')
plt.plot(domain, predictions300, color='r',linewidth=3,label='regression')
plt.title('degree=300')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=1)

feature_cubic3 = PolynomialFeatures(degree = 3000)
X_300 = feature_cubic3.fit_transform(X)

lin_model = LinearRegression()
domain = np.linspace(0, 1, 100).reshape(-1,1) # 입력은 2차원 벡터로 변형

lin_model.fit(X_300, y)
domain_300 = feature_cubic3.fit_transform(domain)
predictions300 = lin_model.predict(domain_300)
plt.subplot(144)
plt.scatter(df['x'], df['y'],label='data')
plt.plot(domain, predictions300, color='r',linewidth=3,label='regression')
plt.title('degree=3000')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=1)






#%%  1-3 train test 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('nonlinear.csv')

X = df['x'].to_numpy()
y = df['y'].to_numpy()
X = X.reshape(-1,1) # 입력을 2차원 벡터가 되게 한다. shape = (m, 1)

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3)

poly = PolynomialFeatures(degree = 3)
X3_train = poly.fit_transform(X_train)

lin_model = LinearRegression()
domain = np.linspace(0, 1, 100).reshape(-1,1) # 입력은 2차원 벡터로 변형

lin_model.fit(X3_train, y_train)

domain = np.linspace(0, 1, 100).reshape(-1,1) # 입력은 2차원 벡터로 변형
domain_3 = poly.fit_transform(domain)
predictions = lin_model.predict(domain_3)

plt.figure(figsize=(24,4))
plt.subplot(141)
plt.scatter(X_train, y_train, label='train',color='r')
plt.scatter(X_test, y_test, label='test',color='b')
plt.plot(domain, predictions, color='k',linewidth=3,label='regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('polynomial (degree=3)')

y_hat_train = lin_model.predict(X3_train)
X3_test = poly.fit_transform(X_test)
y_hat_test = lin_model.predict(X3_test)

plt.subplot(142)
plt.scatter(y_train, y_hat_train, color='r',label='train')
plt.xlabel('y')
plt.ylabel('y_hat')
plt.scatter(y_test, y_hat_test, color='b',label='test')
plt.legend()
plt.title('polynomial')
plt.text(-2, 0.5, 'MSE: {0:0.2f}'.format(mean_squared_error(y_test, y_hat_test)))

#
linear = LinearRegression()
linear.fit(X_train, y_train)

pred = linear.predict(domain)
plt.subplot(143)
plt.scatter(X_train, y_train, label='train',color='r')
plt.scatter(X_test, y_test, label='test',color='b')
plt.plot(domain, pred, color='k',linewidth=3,label='regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('linear')

y_hat_train = linear.predict(X_train)
y_hat_test = linear.predict(X_test)
plt.subplot(144)
plt.scatter(y_train, y_hat_train, color='r',label='train')
plt.scatter(y_test, y_hat_test, color='b',label='test')
plt.xlabel('y')
plt.ylabel('y_hat')
plt.legend()
y_pred=linear.predict(X_test)
#plt.plot(X_test, y_pred,linewidth=3)
plt.title('linear')
plt.text(-2, 0.5, 'MSE: {0:0.2f}'.format(mean_squared_error(y_test, y_hat_test)))
# print('Mean squared error:', mean_squared_error(y_test, y_hat_test))

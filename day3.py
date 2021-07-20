#%%  iris dataset

from sklearn import datasets

d = datasets.load_iris() # load IRIS dataset
print(d.DESCR) # print Description
data = d.data # data 
target = d.target

for i in range(0,len(d.data)):
    print(i+1,d.data[i],d.target[i])

#%% svm

from sklearn import svm
s = svm.SVC(gamma=0.1, C=10)
s.fit(d.data,d.target)

new_d = [[6.4, 3.2, 6.0, 2.5],[7.1, 3.1, 4.7, 1.35]]
res = s.predict(new_d)
print("새로운 2개 샘플의 부류는",res)

#%% plot

import plotly.express as px
from plotly.offline import plot
df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',color='species')
plot(fig)

#%% matplotlib 

from sklearn import datasets
import matplotlib.pyplot as plt

digit = datasets.load_digits()

plt.figure(figsize=(5,5))
plt.imshow(digit.images[0],cmap=plt.cm.gray_r,interpolation='nearest')
plt.show()

print(digit.data[0])
print("이 숫자는", digit.target[0],"입니다")

#%% classification 

from sklearn import datasets
from sklearn import svm

digit = datasets.load.digits()

# svm 
s = svm.SVC(gamma=0.1, C=10) 
s.fit(digit.data,digit.target) # modeling

# test with first 3 samples
new_d=[digit.data[0],digit.data[1],digit.data[2]]
res = s.predict(new_d)
print(res)

res = s.predict(digit.data)
correct = [i for i in range(len(res)) if res[i]==digit.target[i]]
acc = len(correct)/len(res)
print("accuracy:",acc*100, "%")

#%% train test

from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np

digit = datasets.load_digits()
x_train, x_test, y_train, y_test = train_test_split(digit.data,digit.target,train_size=0.6)

# svm 
s = svm.SVC(gamma=0.001)
s.fit(x_train,y_train)

res = s.predict(x_test)

# confusion matrix
conf = np.zeros((10,10))
for i in range(len(res)):
    conf[res[i]][y_test[i]] += 1

print(conf)

# accuracy
no_correct = 0
for i in range(10):
    no_correct += conf[i][i]
acc = no_correct/len(res)
print("accuracy:",acc*100)












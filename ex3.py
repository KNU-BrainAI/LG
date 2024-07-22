#%% 3-1

import matplotlib.pyplot as plt
import numpy as np
## 닥스훈트 데이터
d =  [[75, 24], [77, 29], [83, 19], [81, 32], [73, 21], \
      [99, 22], [72, 19], [83, 34]]
### 사모예드 데이터
s = [[76, 55], [78, 58], [82, 53], [88, 54], [76, 61], \
     [83, 52], [81, 57], [89, 64]]
### 말티즈 데이터
m = [[35, 23], [39, 26], [38, 19], [41, 30], [30, 21], \
     [57, 24], [41, 28], [35, 20]]

d_arr = np.array(d)
s_arr = np.array(s)
m_arr = np.array(m)
plt.scatter(d_arr[:,0], d_arr[:,1], c='red', label='Dachshund')
plt.scatter(s_arr[:,0], s_arr[:,1], c='blue', marker = '^', label='Samoyed')
plt.scatter(m_arr[:,0], m_arr[:,1], c='green', marker = 's', label='Maltese')

A = [[58, 30]]
B = [[80, 26]]
C = [[80, 41]]
D = [[75, 55]]

plt.scatter(A[0][0], A[0][1], s=300, c='magenta', label='A')
plt.scatter(B[0][0], B[0][1], s=300, c='gray', label='B')
plt.scatter(C[0][0], C[0][1], s=300, c='cyan', label='C')
plt.scatter(D[0][0], D[0][1], s=300, c='green', label='D')

plt.xlabel('Length')              
plt.ylabel('Height')              
plt.title("Dog size")
plt.legend(loc='upper left')

plt.show()


nolabel_data = d + s + m + A + B + C + D
X = np.array(nolabel_data)
plt.scatter(X[:, 0], X[:, 1], c='blue', label='no labed data')

plt.xlabel('Length')              
plt.ylabel('Height')              
plt.title("Dog data without label")
plt.legend(loc='upper left')

plt.show()


from sklearn import cluster

def kmeans_predict_plot(X, k):
    model = cluster.KMeans(n_clusters=k)
    model.fit(X)
    labels = model.predict(X)    
    colors = np.array(['red', 'green', 'blue', 'magenta'])
    plt.title('k-Means clustering, k={}'.format(k))
    plt.scatter(X[:, 0], X[:, 1], color=colors[labels])

kmeans_predict_plot(X, k = 2)

# k가 3일때의 클러스터링 결과
kmeans_predict_plot(X, k = 3)

# k가 4일때의 클러스터링 결과
kmeans_predict_plot(X, k = 4)


#%%  3-2

from sklearn import cluster
from sklearn.datasets import load_iris 
import numpy as np

import os
os.environ["OMP_NUM_THREADS"] = '1'

import warnings
warnings.filterwarnings('ignore')

iris = load_iris() 
k = len(iris.target_names)  # 몇 개의 군집으로 나눌지를 결정한다

print('kMeans() 군집화 적용...')
model = cluster.KMeans(n_clusters=k)
model.fit(iris.data)
labels = model.predict(iris.data)
print('군집화 결과 labels :', labels)

a_counts = np.bincount(labels[:50])
b_counts = np.bincount(labels[50:100])
c_counts = np.bincount(labels[100:])

d ={ 0: np.argmax(a_counts), 1: np.argmax(b_counts), 2 : np.argmax(c_counts)}
new_labels = np.copy(labels)
for old, new in d.items():
    new_labels[labels == old] = new

print('다시 레이블링을 한 후의 new_labels =', new_labels)

from sklearn.metrics import accuracy_score
print('iris 데이터의 군집화 정확도:    ?  ')
print('iris 데이터의 군집화 정확도:' , accuracy_score(iris.target, new_labels))

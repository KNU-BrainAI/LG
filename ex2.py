#%% 2-1
## 닥스훈트 데이터
d =  [[75, 24], [77, 29], [83, 19], [81, 32], [73, 21], \
      [99, 22], [72, 19], [83, 34]]
### 사모예드 데이터
s = [[76, 55], [78, 58], [82, 53], [88, 54], [76, 61], \
     [83, 52], [81, 57], [89, 64]]
### 말티즈 데이터
m = [[35, 23], [39, 26], [38, 19], [41, 30], [30, 21], \
     [57, 24], [41, 28], [35, 20]]
print('닥스훈트(0) :', d)
print('사모예드(1) :', s)
print('말티즈(2) :', m)
dogs = d + s + m
labels = [0] * len(d) + [1] * len(s) + [2] * len(m)
from sklearn.neighbors import KNeighborsClassifier 
from sklearn import metrics 
dog_classes = {0:'닥스훈트', 1:'사모예드', 2:'말티즈'} 
k = 3
knn = KNeighborsClassifier(n_neighbors = k) 
knn.fit(dogs, labels)
pred = knn.predict(dogs)
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

conf=confusion_matrix(labels, pred)   # 혼동행렬 만들기
print(conf)
plt.imshow(conf)
plt.figure(figsize=(10,4))
plt.subplot(121)
plt.imshow(conf,cmap=plt.cm.jet)
plt.colorbar()
plt.subplot(122)
plt.imshow(conf,cmap=plt.cm.gray)
plt.colorbar()

ConfusionMatrixDisplay(confusion_matrix = conf).plot()


import numpy as np

#True Positive
def true_positive(labels, pred):
    tp = 0
    for gt, pre in zip(labels, pred):
        if gt == 2 and pre == 2:
            tp +=1
    return tp

#True Negative
def true_negative(labels, pred):
    tn = 0
    for gt, pre in zip(labels, pred):
        if gt == 0 and pre == 0:
            tn +=1
    return tn

#False Positive
def false_positive(labels, pred):
    fp = 0
    for gt, pre in zip(labels, pred):
        if gt == 0 and pre == 2:
            fp +=1
    return fp

#False Negative
def false_negative(labels, pred):
    fn = 0
    for gt, pre in zip(labels, pred):
        if gt == 2 and pre == 0:
            fn +=1
    return fn

new_labels = np.append(labels[:8],labels[16:24])
new_pred = np.append(pred[:8],pred[16:24])

TP=true_positive(new_labels, new_pred)
TN=true_negative(new_labels, new_pred)
FP=false_positive(new_labels, new_pred)
FN=false_negative(new_labels, new_pred)

pre=TP/(TP+FP)
print('내가 만든 Precision:',pre)
rec=TP/(FN+TP)
print('내가 만든 Recall:',rec)
print('내가 만든 Accuracy:',(TP+TN)/(FP+FN+TP+TN))
print('내가 만든 F1-score:',2*(pre*rec)/(pre+rec))
print()
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
print('scikit-learn의 Precision:',precision_score(new_labels,new_pred,pos_label=2))
print('scikit-learn의 Recall:',recall_score(new_labels,new_pred,pos_label=2))
print('scikit-learn의 Accuracy:',accuracy_score(new_labels,new_pred))
print('scikit-learn의 F1-score:',f1_score(new_labels,new_pred,pos_label=2))





# 데이터를 어떻게 분류하는가를 보여주는 함수를 만들어 봅니다
def show_classifier_result(data, label):
    for n in [3, 5, 7]:
        knn = KNeighborsClassifier(n_neighbors=n)
        knn.fit(dogs, labels)
        y_pred = knn.predict(data)
        print(label, data, ': k가', n,'일때 :', dog_classes[y_pred[0]])

print('A 데이터 분류결과')
A = [[58, 30]]
show_classifier_result(A, 'A')

B = [[80, 26]]
print()
print('B 데이터 분류결과')
show_classifier_result(B, 'B')

C = [[80, 41]]
print()
print('C 데이터 분류결과')
show_classifier_result(C, 'C')

D = [[75, 55]]
print()
print('D 데이터 분류결과')
show_classifier_result(D, 'D')


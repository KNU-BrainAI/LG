%reset -f
%clear

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 텐서플로우와 케라스를 사용할 수 있도록 준비
import tensorflow as tf
from tensorflow import keras

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

model = keras.models.Sequential( [
    keras.layers.Dense(32, activation= 'tanh'),
    keras.layers.Dense(16, activation= 'tanh'),
    keras.layers.Dense(8, activation= 'tanh'),
    keras.layers.Dense(4, activation= 'tanh'),
    keras.layers.Dense(1, activation= 'tanh'),
])


# model = keras.models.Sequential( [
#     keras.layers.Dense(4, activation= 'tanh'),
#     keras.layers.Dense(4, activation= 'tanh'),
#     keras.layers.Dense(4, activation= 'tanh'),
#     keras.layers.Dense(4, activation= 'tanh'),
#     keras.layers.Dense(4, activation= 'tanh'),
#     keras.layers.Dense(4, activation= 'tanh'),
#     keras.layers.Dense(4, activation= 'tanh'),
#     keras.layers.Dense(4, activation= 'tanh'),
#     keras.layers.Dense(4, activation= 'tanh'),
#     keras.layers.Dense(1, activation= 'tanh'),
# ])

optimizer = keras.optimizers.SGD(learning_rate=0.1)
model.compile(optimizer=optimizer, loss='mse')

data_loc = 'https://github.com/dknife/ML/raw/main/data/'
df = pd.read_csv(data_loc+'nonlinear.csv')
X = df['x'].to_numpy().reshape(-1,1)
y_label = df['y'].to_numpy().reshape(-1,1)


model.fit(X, y_label, epochs=100)

domain = np.linspace(0, 1, 100).reshape(-1,1) # 입력은 2차원 벡터로 변형
y_hat = model.predict(domain)
plt.scatter(df['x'], df['y'])
plt.scatter(domain, y_hat, color='r')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

# 데이터 불러오기
df = pd.read_csv(r'c:\Users\PC00\Downloads\dataset2.csv')
x = df['x'].values
y = df['y'].values

# 입력 데이터 정규화 (0~1)
x_train = x.reshape(-1, 1)

# 모델 정의
model = Sequential([
    Dense(10, activation='tanh', input_shape=(1,)),
    Dense(10, activation='tanh'),
    Dense(1, activation='tanh')
])

# 옵티마이저 및 컴파일
optimizer = SGD(learning_rate=0.1)
model.compile(optimizer=optimizer, loss='mse')

# 학습
model.fit(x_train, y, epochs=100, verbose=0)

# 예측 곡선 생성
x_curve = np.linspace(0, 1, 100).reshape(-1, 1)
y_curve = model.predict(x_curve)

# 그래프 출력
plt.scatter(x, y, label='Data')
plt.plot(x_curve, y_curve, color='red', label='MLP Prediction', linewidth=3)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('MLP with tanh activation')
plt.show()
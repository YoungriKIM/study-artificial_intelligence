#실습 19_1,2,3,4,5, earlystopping까지
#총 6개의 파일을 완성하시오

import numpy as np
from sklearn.datasets import load_diabetes #당뇨병 수준

#데이터 불러오고 , 이건 사이킷런의 데이터 불러오는 방법
dataset = load_diabetes()
x = dataset.data
y = dataset.target

print(x.shape, y.shape) #(442, 10) (442,)

#데이터 전처리 (통으로)
x = x/25.

#트레인 테스트 분리
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, shuffle=True, random_state=66)

#모델 구성
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Dense, Input

model = Sequential()
model.add(Dense(42, input_shape=(10,), activation='relu'))
model.add(Dense(84))
model.add(Dense(84))
model.add(Dense(42))
model.add(Dense(1))

#컴파일, 훈련
model.compile(loss='mse', optimizer='adam', metrics=['mae'])
model.fit(x_train, y_train, epochs=200, batch_size=32, validation_split=0.2, verbose=1)

#평가, 예측
loss, mae = model.evaluate(x_test, y_test, batch_size=1)
print('loss, mae: ', loss, mae)

y_predict = model.predict(x_test)

#RMSE와 R2 구하기
from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
      return np.sqrt(mean_squared_error(y_test, y_predict))
print('RMSE: ', RMSE(y_test, y_predict))

from sklearn.metrics import r2_score
R2 = r2_score(y_test, y_predict)
print('R2: ', R2)

#1번파일
# loss, mae:  3136.7783203125 44.4537353515625
# RMSE:  56.00695024986382
# R2:  0.409904405219381

#2번파일
# loss, mae:  2492.786865234375 40.156646728515625
# RMSE:  49.92781650416666
# R2:  0.5682723462876598
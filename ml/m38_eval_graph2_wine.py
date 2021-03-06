# 그래프로 그려서 확인해보자~

import numpy as np
from xgboost import XGBClassifier, XGBRegressor
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, accuracy_score

#1. 데이터 
x, y = load_wine(return_X_y=True)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True, random_state=311)

#2. 모델
model = XGBClassifier(n_estimators=500, learning_rate=0.01, n_jobs=-1)

#3. 훈련
model.fit(x_train, y_train, verbose=1, eval_metric=['mlogloss', 'merror'] , eval_set=[(x_train, y_train), (x_test, y_test)], early_stopping_rounds=20)

aaa = model.score(x_test, y_test)
print('score: ',aaa)

y_pred = model.predict(x_test)
acc = accuracy_score(y_test, y_pred)
print('r2: ', acc)

print('----------------------------------------')
# 딥러닝 모델처럼(핏을 hist로 반환) evals를 반환해서 그것을 지표로 early stop을 할 수 없을까? > 그래프로도 그려보자
result = model.evals_result()
print(result)

import matplotlib.pyplot as plt

epochs = len(result['validation_0']['mlogloss'])
x_axis = range(0, epochs)

# 첫번째 그래프
fig, ax = plt.subplots()
ax.plot(x_axis, result['validation_0']['mlogloss'], label = 'Train')
ax.plot(x_axis, result['validation_1']['mlogloss'], label = 'Test')
ax.legend()
plt.ylabel('mlogloss')
plt.title('XGBoost mlogloss')
plt.show()

# 두번째 그래프
fig, ax = plt.subplots()
ax.plot(x_axis, result['validation_0']['merror'], label = 'Train')
ax.plot(x_axis, result['validation_1']['merror'], label = 'Test')
ax.legend()
plt.ylabel('merror')
plt.title('XGBoost merror')
plt.show()


# ==================================================
# m35
# score:  0.9722222222222222
# r2:  0.9722222222222222

# ==================================================
# m36 metirc 2개
# [99]    validation_0-mlogloss:0.38320   validation_0-merror:0.00000
#         validation_1-mlogloss:0.48590   validation_1-merror:0.02778
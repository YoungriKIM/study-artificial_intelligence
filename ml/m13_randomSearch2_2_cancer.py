# gridSearch 의 단점: 모든 경우의 수를 다 해서 시간이 오래 걸린다
# randomSearch 의 장점: 랜덤으로 잡아서 하니까 시간이 적게 걸리고, 알아서 파라미터를 잡아주니 덜 감성적인 코딩이 된다.

# 그리드 서치를 랜덤 서치로 바꿔보자


# 제공하는 파라미터
# parameters = [
#     {'n_estimators' : [100,200]},
#     {'max_depth' : [6,8,10,12]},
#     {'min_samples_leaf' : [3,5,7,10]},
#     {'min_samples_split' : [2,3,5,10]},
#     {'n_jobs' : [-1,2,4]}
# ]

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.metrics import accuracy_score
import timeit
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import warnings
warnings.filterwarnings('ignore')

#1. 데이터 불러오기
dataset = load_breast_cancer()
x = dataset.data
y = dataset.target

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=311)

kfold = KFold(n_splits=5, shuffle=True) 

parameters = [
    {'n_estimators' : [50,100,200], 'n_jobs' : [-1,4]},
    {'max_depth' : [6,8,10,12], 'min_samples_split' : [2,3,5,10]},
    {'min_samples_leaf' : [3,5,7,10], 'max_depth' : [6,8,10,12]},
    {'min_samples_leaf' : [3,5,7,10]},
    {'n_jobs' : [-1,2,4,8], 'min_samples_leaf' : [3,5,7,10]}
]

#2. 모델 구성
#--------------------------------------------------------------------------------
start_time = timeit.default_timer()  # 시작한 시각 체크
#--------------------------------------------------------------------------------

model = RandomizedSearchCV(RandomForestClassifier(), parameters, cv = kfold)

#3. 훈련
model.fit(x_train, y_train)

#4. 평가, 예측
print('최적의 매개변수: ', model.best_estimator_)

y_pred = model.predict(x_test)
print('최종정답률: ', accuracy_score(y_pred, y_test))

#--------------------------------------------------------------------------------
end_time = timeit.default_timer()  # 종료한 시각 체크
print('%f초 걸렸습니다.' % (end_time - start_time))
#--------------------------------------------------------------------------------


#===========================================
# DNN 모델
# acc: 0.9736841917037964

# gridsearchCV 일 때 ====================================
# 최적의 매개변수:  RandomForestClassifier(max_depth=10)
# 최종정답률:  0.9473684210526315
# 74.222215초 걸렸습니다.

# RandomizedSearchCV 적용 =============================
# 최적의 매개변수:  RandomForestClassifier(max_depth=6, min_samples_split=5)
# 최종정답률:  0.9385964912280702
# 11.309497초 걸렸습니다.
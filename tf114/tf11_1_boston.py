# 회귀로 데이터 불러와서 만들어라
# 혜지야 고마워

from sklearn.datasets import load_diabetes, load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import tensorflow as tf 

#[실습]
# r2_score로 결론 낼것

#input
x_data, y_data = load_boston(return_X_y=True)
y_data = y_data.reshape(-1,1)
print(x_data.shape, y_data.shape) #(506, 13) (506, 1)

# 전처리 split
x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, train_size = 0.8, shuffle = True, random_state = 66)

# 데이터 종류 지정
x = tf.placeholder(tf.float32, shape=[None, 13])
y = tf.placeholder(tf.float32, shape=[None, 1])

w = tf.Variable(tf.random_normal([13,1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')


hypothesis = tf.matmul(x, w) + b
cost = tf.reduce_mean(tf.square(hypothesis - y))
# train = tf.train.GradientDescentOptimizer(learning_rate = 2.54521e-6).minimize(cost)    #1.54521e-5
train = tf.train.AdamOptimizer(learning_rate=0.8).minimize(cost)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step  in range(100001):
        cost_val, _, hy_val= sess.run([cost, train, hypothesis], feed_dict = {x:x_train, y:y_train})

        pred = sess.run(hypothesis, feed_dict={x: x_test})
        
        if step % 1000 == 0:
            print(step, 'cost : ', cost_val)

    print("r2: ",r2_score(y_test,pred))
    # r2:  0.8112416392568489
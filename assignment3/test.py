'''
Created on Oct 2, 2019

@author: Yang
'''
import pandas as pd
import numpy as np
import random
from matplotlib import pyplot as plt
from time import sleep

mean1 = [-3, 3]
mean2 = [3, 0]
cov = [[2, 0], [0, 3]]

x1 = np.random.multivariate_normal(mean1, cov, 1000)
plt.scatter(x1[:, 0], x1[:, 1], c='c', marker='.')
print("x1: \n",format(x1))
print("x1.shape:{}\n".format(x1.shape))

x2 = np.random.multivariate_normal(mean2, cov, 1000)
plt.scatter(x2[:, 0], x2[:, 1], c='r', marker='.')


xlabels = np.ones(1000)
xlabels = np.concatenate((xlabels, -1*np.ones(1000)))
print("xlabels: \n",format(xlabels))
print("x1.shape:{}\n".format(xlabels.shape))

X = np.concatenate((x1, x2))
print("X : \n",format(X))
print("X.shape:{}\n".format(X.shape))

u1 = np.mean(x1, 0)
u2 = np.mean(x2, 0)

# removing the mena from classes
x1mc = x1 - u1
x2mc = x2 - u2

# covariance matrix for class 1
S1 = np.dot(x1mc.T, x1mc)
print("S1 : \n",format(S1))
print("S1.shape:{}\n".format(S1.shape))

# covariance matrix for class 2
S2 = np.dot(x2mc.T, x2mc)

Sw = S1 + S2
print("Sw : \n",format(Sw))
print("Sw.shape:{}\n".format(Sw.shape))
w = np.dot(np.linalg.inv(Sw), (u1 - u2))
print("w : \n",format(w))
print("w.shape:{}\n".format(w.shape))

plt.plot([-10000*w[0], 10000*w[0]], [-10000*w[1], 10000*w[1]], 'g--')

threshold = -0.001
prediction = np.sign(np.dot(w, X.T) + threshold)

error = np.sum(abs(prediction - xlabels)/2)
error_index= np.argwhere(prediction - xlabels)
print(error)
Q = X[error_index]
print(Q)
plt.scatter(Q[:, 0, 0], Q[:, 0, 1], c='g', marker='.')
### plt.ion()
# plt.show()

print("done")
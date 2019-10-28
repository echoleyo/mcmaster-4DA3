import pandas as pd
import numpy as np
from math import sqrt
from matplotlib import pyplot as plt

""" Question 1

data1x = np.random.uniform(-10, 10, 8000).reshape(1000, 8)
np.savetxt("data1x.txt", data1x, delimiter=',')
 
err_mean = 0
error_var = 9
err_sd = sqrt(error_var)
  
# create error vector
error = np.random.normal(err_mean, err_sd, size=1000)
beta = [-2, 3, 5, 2, 1, 4, 5, 6, -1]
 
# Y =ZB + err
# create Z matrix
data_z = np.insert(data1x, 0, 1, axis=1)
 
# create Y
data_y = np.dot(data_z, beta) + error
# save to datay.txt00
np.savetxt("data1y.txt", data_y)

"""

""" Question 2

cova = np.loadtxt("cova.txt", delimiter=",")
meana = np.loadtxt("meana.txt")
covb = np.loadtxt("cova.txt", delimiter=",")
meanb = np.loadtxt("meana.txt")

x1 = np.random.multivariate_normal(meana, cova, 500)
x2 = np.random.multivariate_normal(meanb, covb, 500)

data2 = np.concatenate((x1, x2))
np.savetxt("data2.txt", data2, delimiter=' ')
"""

""" Question 3
data = np.loadtxt("data1x.txt", delimiter=',')
Z = np.insert(data, 0, 1, axis=1)

Y = np.loadtxt("data1y.txt")
# bata = (Z.T*Z)^(-1) * Z.T * Y
beta = np.dot(np.dot(np.linalg.inv(np.dot(Z.T, Z)), Z.T), Y)

x = [3.1, -1.5, -2, 2.5, 3.5, -3, 2.1, -4]
z = np.insert(x, 0, 1)
y = np.dot(z, beta)
print(y)
"""

""" Question 4
"""
X = np.loadtxt("data2.txt")
print("X: {}\n".format(X))
print("X.shape: {}\n".format(X.shape))

x1, x2 = np.vsplit(X, 2)
# plt.scatter(x1[:, 0], x1[:, 1], c='c', marker='.')
# plt.scatter(x2[:, 0], x2[:, 1], c='r', marker='.')
# print("x2: {}\n".format(x2))
# print("x2.shape: {}\n".format(x2.shape))
mean1 = np.mean(x1, 0)
mean2 = np.mean(x2, 0)

# remove mean from class 1
x1mc = x1 - mean1
x2mc = x2 - mean2

# calculate covariance matrix 
S1 = np.dot(x1mc.T, x1mc)
S2 = np.dot(x2mc.T, x2mc)

# Sw = S1 + S2
Sw = S1 + S2

# w = Sw^(-1)*(u1 - u2)  
w = np.dot(np.linalg.inv(Sw), (mean1 - mean2))
print("w: {}".format(w))
print(w.shape)

plt.plot([-10000*w[0], 10000*w[0]], [-10000*w[1], 10000*w[1]], 'g--')

xlabels = np.ones(500)
xlabels = np.concatenate((xlabels, -1*xlabels))
# print("xlabels: \n",format(xlabels))
# print("x1.shape:{}\n".format(xlabels.shape))

threshold = -0.0001
prediction = np.sign(np.dot(w, X.T) + threshold)
# print(prediction)
error = np.sum(abs(prediction - xlabels) / 2)
print(error)

# plt.show()
print("Done")




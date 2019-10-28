'''
Created on Sep 22, 2019

@author: Yang
'''

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#matplotlib inline


plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12, 8)

# Normal distributed x and y vector with mean 0 and standard deviation 1
x = np.random.normal(0, 1, 500)
y = np.random.normal(0, 1, 500)
X = np.vstack((x, y)).T

plt.scatter(X[:, 0], X[:, 1])
plt.title('Generated Data')
plt.axis('equal');

def cov(x, y):
    xbar, ybar = x.mean(), y.mean()
    return np.sum((x - xbar)*(y - ybar))/(len(x) - 1)


# Covariance matrix
def cov_mat(X):
    return np.array([[cov(X[0], X[0]), cov(X[0], X[1])], \
                     [cov(X[1], X[0]), cov(X[1], X[1])]])



# def get_covariance_matrix(numpy_matrix):
#     return np.cov(numpy_matrix, rowvar=0)
# 
# 
# def show(data):
#     con_matrix = get_covariance_matrix(data)
#     print(con_matrix)
#     print("data shape: {}".format(data.shape))
#     print("covariance shape: {}".format(con_matrix.shape))

if __name__ == '__main__':
    print("x: {}".format(x))
    print("x.shape: {}".format(x.shape))
    print("y: {}".format(y))
    print("y.shape: {}".format(y.shape))
    print("X: {}".format(X))
    print("X.shape: {}".format(X.shape))
#     print("X.T: {}".format(X.T))
#     print("X.T.shape: {}".format(X.T.shape))
    # Calculate covariance matrix 
    print(cov_mat(X.T)) # (or with np.cov(X.T))
    
    
    
#     data = np.array([[1,2], [3,4], [4,5], [5,6]])
#     show(data)
#     
#     data = np.array([[1,2,3], [3,4,3], [4,5,3], [5,6,2],[5,6,2],[5,6,2]])
#     show(data)
#     
#     data = np.array([[1,2,3,5], [3,4,3,2], [4,5,3,3], [5,6,2,3], [4,5,3,3], [4,5,3,3], [4,5,3,3]])
#     show(data)
#     
#     data = np.array([[3,4,3,2,3,4,5,6,2], [3,4,3,2,3,4,5,67,3], [3,4,3,2,3,43,5,2,3]])
#     show(data)
#     
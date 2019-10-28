'''
Created on Sep 25, 2019

@author: Yang
'''

import numpy
import random

# y = b0 + b1X1 + b2X2 + b3X3 +b4X4 + b5X5 + e # beta vakye

b = numpy.array([1,2,3,4,5,6])              # beta value
X = 10 * numpy.random.random((500, 5)) - 5  # 5 attribures as input, 500 data points
Z = numpy.concatenate((numpy.ones((500,1)), X), axis = 1)

e = numpy.random.normal(0, 9, 500)

y = numpy.dot(Z, b) + e

# b = 1 / (Z.T*Z) * Z.T * Y
bhat = numpy.dot(numpy.dot(numpy.linalg.inv(numpy.dot(Z.T, Z)), Z.T), y)

print(bhat)



# print(y)
print("finish")

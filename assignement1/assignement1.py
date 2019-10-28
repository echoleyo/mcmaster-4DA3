'''
Created on Sep 7, 2019

@author: Yang Li
@student_number: 400164509
'''
import pandas as pd
import numpy as np


def get_mean(numpy_matrix):
    return np.mean(numpy_matrix, axis=0)


def get_variance(numpy_matrix):
    return np.var(numpy_matrix, axis=0)


def display_data(data):
    for v in data:
        print("\t{}".format(v))
        

def get_covariance_matrix(numpy_matrix):
    return np.cov(numpy_matrix, rowvar=0)


if __name__ == '__main__':
    print("Question 1:")
    data_a = pd.read_excel(r"dataA.xlsx", header=None)
    data = data_a.to_numpy()
    data_a_mean = get_mean(data)
    print("\ndataA mean:")
    display_data(data_a_mean)
    data_a_variance = get_variance(data)
    print("\ndataA Variance:")
    display_data(data_a_variance)
    print("\ndataA covariance matrix:")
    matrix = get_covariance_matrix(data_a)
    display_data(matrix)
    
    print("\n\n\nQuestion 2:")
    data_b= pd.read_excel(r"dataB.xlsx", header=None)
    data = data_b.to_numpy()
    data_b_mean = get_mean(data)
    print("\ndataB mean:")
    display_data(data_b_mean)
    data_b_variance = get_variance(data)
    print("\ndataB variance:")
    display_data(data_b_variance)
    print("\ndataB covariance matrix:")
    matrix = get_covariance_matrix(data_b)
    display_data(matrix)
    np.savetxt("cova.txt", matrix, delimiter=',')
    np.savetxt("meana.txt", data_b_mean, delimiter=',')
    
    print(matrix.shape)
    print("\n\n\nQuestion 3:")
    print("""
            The reason of the answers are different the parameters used to 
            generate the data is because that data is generated randomly
          """
    )

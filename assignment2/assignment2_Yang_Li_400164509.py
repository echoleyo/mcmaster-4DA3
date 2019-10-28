'''
Created on Sep 19, 2019

@author: Yang
'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from time import sleep


def get_data():
    pd_data = pd.read_excel(r'multNormal.xlsx', header=None)
    _data = pd_data.to_numpy()
    return _data


def get_covariance_matrix(numpy_matrix):
    return np.cov(numpy_matrix, rowvar=0)


def get_variance(numpy_matrix):
    return np.var(numpy_matrix, axis=0)


def question_1(data):
    example_size = int(data.shape[1]/2)
    plot_row = 2
    plot_col = 5
    fig =plt.figure(figsize=(9,6))
    fig.suptitle("Question 1.1")
    
    """
    This for loop is generating 10 plots
    """
    for i in range(example_size):
        ax = plt.subplot(plot_row, plot_col, i + 1)
        ax.set_title("example {}".format(i+1))
        ax.grid(True)
        plt.scatter(data[:,i*2], data[:,i*2+1], c="c", marker=".")
    
    fig2 =plt.figure(figsize=(6,5))
    
    """
    show 10 off-diagnals of covariance matrix
    """
    fig2.suptitle("Question 1.2")
    off_diagnals = []
    for i in range(example_size):
        matrix = get_covariance_matrix(data[:,[i*2, i*2+1]])
        off_diagnal = matrix[0, 1]
        off_diagnals.append(off_diagnal)
        plt.text(i+1, off_diagnal, '[{}, {:.2f}]'.format(i+1, off_diagnal))
     
    plt.plot( range(1, 11), off_diagnals,'g^', 
              range(1, 11), off_diagnals, 'r--',
            c='g')

    plt.show()
    return
    

if __name__ == '__main__':
    data = get_data()
    mean1 = np.mean(data[:,[0,1]], axis=0)
    data1 = data[:,[0,1]]
    print("\nQuestion 1: ")
    question_1(data)
    
    
    
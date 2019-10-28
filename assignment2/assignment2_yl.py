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


def question_1(data):
    example_size = int(data.shape[1]/2)
    """
    generate 2 x 5 figure
    """
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
    
    
    """
    Question 1.2
    show 10 off-diagnals of covariance matrix
    """
    fig2 =plt.figure(figsize=(15,4))
    fig2.suptitle("Question 1.2")
    off_diagnals = []
    variances_1 = []
    variances_2 = []
    for i in range(example_size):
        matrix = np.cov(data[:,[i*2, i*2+1]], rowvar=False)
        off_diagnal = matrix[0, 1]
        v1 = matrix[0, 0]
        v2 = matrix[1, 1]
        off_diagnals.append(off_diagnal)
        variances_1.append(v1)
        variances_2.append(v2)

    plt_variance_1 = plt.subplot(1, 3, 1)
    plt_variance_1.set_title("Variances 1")
    plt.plot( range(1, 11), variances_1,'g^', 
              range(1, 11), variances_1, 'r--', c='g')

    off_diagonal = plt.subplot(1, 3, 2)
    off_diagonal.set_title("Off-diagonals")
    plt.plot( range(1, 11), off_diagnals,'g^', 
              range(1, 11), off_diagnals, 'r--', c='g')
    
    plt_variance_2 = plt.subplot(1, 3, 3)
    plt_variance_2.set_title("Variances 2")
    plt.plot( range(1, 11), variances_2,'g^', 
              range(1, 11), variances_2, 'r--', c='g')

    plt.show()
    return
    

if __name__ == '__main__':
    data = get_data()
    mean1 = np.mean(data[:,[0,1]], axis=0)
    data1 = data[:,[0,1]]
    print("\nQuestion 1: ")
    question_1(data)
    
    
    

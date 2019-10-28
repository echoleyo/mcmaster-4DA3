'''
Created on Oct 15, 2019

@author: Yang
'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from time import sleep

def get_data():
    excel = pd.ExcelFile(r'RegressionData.xlsx',)
    pd_sheet1 = pd.read_excel(excel, header=None, sheet_name='Sheet1')
    pd_sheet2 = pd.read_excel(excel, header=None, sheet_name='Sheet2')
    sheet1 = pd_sheet1.to_numpy()
    sheet2 = pd_sheet2.to_numpy()
    return sheet1, sheet2



if __name__ == '__main__':
    """Get X, and Y 
    """
    data1, Y = get_data()
    
    """ Added 1 in first column
    """
    Z = np.insert(data1, 0, 1.0, axis=1)
    
    """calculate beta
    beta = (Z^T * Z)^-1 * Z^T * Y
    """    
    m_regression = np.dot(np.dot(np.linalg.inv(np.dot(Z.T, Z)), Z.T), Y)
    print(m_regression)

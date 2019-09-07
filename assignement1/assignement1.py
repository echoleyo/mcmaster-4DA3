'''
Created on Sep 7, 2019

@author: Yang
'''
import pandas as pd
import numpy as np

data = pd.read_excel(r"dataA.xlsx")
# print(data)
data_mean = data.mean()
print(data_mean)
print(dir(data))
print(dir(data_mean))

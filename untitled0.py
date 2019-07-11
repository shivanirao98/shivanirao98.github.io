# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:04:28 2019

@author: SHIVANI Y
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('Salary_Data.csv')
x=data.iloc[:,0:1].values
y=data.iloc[:,1].values
plt.scatter(x,y,color='red')
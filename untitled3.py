# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:23:19 2019

@author: SHIVANI Y
"""

#to find the mean using the formulae b1=(xi-mean(x))(yi-ymean)/(xi-xmean)2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('headbrain.csv')
x=data.iloc[:,0:1].values
y=data.iloc[:,1].values#to read the value from the file
c=(x.mean())# formulae for x mean
d=(y.mean())# for y mean
print(c)
print(d)
a=x-c
b=y-d
z=(x-c)**2
for i in range(len(x)):
    beta=(np.sum(a*b))/np.sum(z)#formulae for the mean 
print(beta)
beta1=d-(beta*c)
print(beta1)    

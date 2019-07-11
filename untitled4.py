# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:14:55 2019

@author: SHIVANI Y
"""

#r square algorithm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('headbrain.csv')
x_train=data.iloc[:100,2].values
y_train=data.iloc[:100,2].values
x_test=data.iloc[100:,3].values
y_test=data.iloc[100:,3].values
xmean=x.mean()# formulae for x mean
ymean=y.mean()# for y mean
print(xmean)
print(ymean)


#training
bnum,bdenom=0,0
for i in range(len(y_train)):
    bnum=x[i]-x_train*y[i]-y_train
    bdenom=(x[i]-x_train)**2
b0=bnum/bdenom

b1=y_train-b*x_train



#y=mx+c
y_pred=b1*x_test+b0
plt.scatter(x_train,y_train,color='red',label='training')
plt.scatter(x_test,y_pred,color='blue',label='testing')
plt.scatter(x_test,y_test,color='green',label='actual values')
plt.legend()
plt.show()


#comparing the models
sst,ssr=0,0
for i in range(0,len(y_test)):
    
        sst+=(y_test[i]-y_test.mean())**2
        ssr+=(y_test[i]-y_pred[i])**2
r=1-(ssr/sst)

print('score of the linear model=',r)

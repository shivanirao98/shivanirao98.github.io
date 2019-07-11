# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:37:17 2019

@author: SHIVANI Y
"""

import numpy as np
a=["delhi","banglore","chennai","mumbai"]

from sklearn.preprocessing import LabelEncoder
lEncoder=LabelEncoder()

lEncoder.fit(a)
b=lEncoder.transform(a)
c=["delhi","mumbai"]
lEncoder.fit(c)
lEncoder.transform(c)
lEncoder.inverse_transform([1])


#extracting the data
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('50_Startups.csv')
data.columns
x=data.iloc[:,:4].values
y=data.iloc[:,4].values

#to set the random values in the data set
from sklearn.preprocessing import LabelEncoder
lEncoder=LabelEncoder()

x[:,3]=lEncoder.fit_transform(x[:,3])

from sklearn.preprocessing import OneHotEncoder
ohencoder=OneHotEncoder(categorical_features=[3])

x=ohencoder.fit_transform(x).toarray()
#to delete one column whch is not required
x=x[:,1:]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
mRegressor=LinearRegression()
mRegressor.fit(x_train,y_train)

y_pred=mRegressor.predict(x_test)

from sklearn.metrics import mean_squared_error

mse=mean_squared_error(y_test,y_pred)**(1/2)



# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 11:52:18 2017

@author: kay75
"""
'''
New functions:
-Combine dataframe vertically
-combine dataframe horizontally
-generate dataframe from selected column names
- element-wise +/-/*// manipulation of dataframe
- A few functions on KNN algorithm:
    a. train_test split
    b. train KNN model
     c. test KNN model
     d. using KNN model to do prediction/classification

'''

import pandas as pd
import sklearn.cross_validation as cv
from sklearn import neighbors as nb
from sklearn.metrics import classification_report

#Combine two dataframes horizontally
def combHor(df1, df2):
    return pd.concat([df1, df2], axis=1)

#Combine two dataframes vertically
def combVer(df1, df2):
    return pd.concat([df1, df2])

#Select columns from a dataframe to make a new dataframe
def frameFromCol (listOfNames, df):
    newDf = df[listOfNames]
    return newDf

#Element-wise +/-/*// manipulation
#command is a string of addtion/subtraction/multiplication/division
def basicMan(df, col1, col2, command):
    newDf = df.copy(deep = True)
    
    if command == "addition":
        newDf["{}+{}".format(col1, col2)] = df[col1] + df[col2]
    if command == "subtraction":
        newDf["{}-{}".format(col1, col2)] = df[col1] - df[col2]
    if command == "multiplication":
        newDf["{}*{}".format(col1, col2)] = df[col1] * df[col2]
    if command == "division":
        newDf["{}/{}".format(col1, col2)] = df[col1] / df[col2]
    
    return newDf


'''the following are for K-nerest-neighbor functions'''

#Train-test split
def trainTestSplit (X, y):
    (X_train, X_test, y_train, y_test) = cv.train_test_split(X, y, test_size=.25)
    return (X_train, X_test, y_train, y_test)
'''Can get individual data above by index [0] through [3]'''


#Nearest neighbor
def trainKNN(nbrs, X_train, y_train):
    #First fir the model
    knc = nb.KNeighborsClassifier(n_neighbors=nbrs)
    knc.fit(X_train, y_train)
    return knc

#Test how well the KNN model is
def testKNN(knc, X_test, y_test):
    y_pred = knc.predict(X_test)
    return print(classification_report(y_test, y_pred))

    
#Use the KNN model for prediction
def predKNN(knc, X):
    y_pred = knc.predict(X)
    return y_pred




'''Testing'''
df1 = pd.DataFrame({'col1' : [1.0] * 5, 
                   'col2' : [2.0] * 5, 
                   'col3' : [3.0] * 5 }, index = range(1,6),)
df2 = pd.DataFrame({'col1' : [10.0] * 5, 
                    'col2' : [100.0] * 5, 
                    'col3' : [1000.0] * 5 }, index = range(1,6),)

combHor(df1, df2)

combVer(df1, df2)

frameFromCol(["col1", "col2"], df1)

basicMan(df1, "col1", "col2", "addition")

train_test_data = trainTestSplit(df1, df2["col1"])
train_test_data

knc = trainKNN(2, train_test_data[0], train_test_data[2])

testKNN(knc,train_test_data[1], train_test_data[3] )

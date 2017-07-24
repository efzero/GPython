# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 13:05:21 2017

@author: Jiayin
"""

'''Week June 18th: Basic Regression'''
import pandas as pd

#
# import scikits.statsmodels.api as sm
import numpy as np
# import statsmodels.api as sm

from statsmodels import api as sm

import matplotlib.pyplot as plt


# from sklearn.linear_model import LinearRegression


#Read data from csv file and return a pandas Dataframe to use later
def read_data(csvFile):
    df = pd.read_csv(csvFile)
    return df

#Get column names and return a list of column names
def columnNames (dataframe):
    return list(dataframe)

#Read Column Names and make a data frame
def frameFromCol (listOfNames, dataframe):
    NewDf = dataframe[listOfNames]
    return NewDf


#Summary Statistics for every column in a dataframe
def summary_stat(df):
    return df.describe()

#Regression:
#y is the target data, dependent variable;
#x can be multiple variables, are the festures/independent variables

#x and y are dataframes, contant = True pre-set the intercept != 0; if =0 need to type in False
def regression(y, x, constant = True):
    if constant == True:
        X = sm.add_constant(x)
    else:
        X = x

    results = sm.OLS(y, X).fit()
    return results


def regPlot (y, x, results):
    for i in range(0, len(x.columns)):
        fig = plt.figure()
        plt.subplot()
        plt.scatter(x.ix[:,i], y)
        beta0 = results.params['const']
        beta1 = results.params[x.columns[i]]
        f = lambda x: beta0 + beta1*x
        plt.plot(x.ix[:,i] ,f(x.ix[:,i]),lw=2.5, c="orange",label="regression line")
        plt.title("Scatter & Regression")
        plt.ylabel(y.columns[0])
        plt.xlabel(x.columns[i])
        fig.savefig('scatterRegression_{}.png'.format(i), bbox_inches='tight')
    return None



#Testing Regression functions
# df = read_data('mydata.csv')
#Inspect the first five lines of the data
# df.head()
#Define independent variables and dependent variables and form new dataframes
# x =  df[['COUNT FEMALE', 'COUNT PACIFIC ISLANDER', 'COUNT AMERICAN INDIAN']]
# y = df[['COUNT PUBLIC ASSISTANCE TOTAL']]
# # #Do regression on x and y dataframes
# results = regression(y, x)






# #Look at summary statistics of regression
# print(results.summary())   #Note: many choices to call here
# print(results.rsquared)
'''
If want to use the trained model to predict y using some new dataframe x2, can use
results.predict(x2)
'''

#Testing Summary_stat for columns in a dataframe
# summary_stat(x)

'''Also, maybe make one for dummy variables
    And consider plots with y and x1, x2, x3... etc'''




'''Week June 26th: Defining Input, Output formats(CSV, JSON)'''

'''JSON'''
import json

#parse into a normal dictionary
#json_file is some
#Note json.loads(json_string) is for loading a string
def jsonParse(json_file):
    with open(json_file) as data_file:
        parsed_json = json.load(data_file)
    return parsed_json

'''sample use:
A = jsonParse(jsonFile)
A['key_name'] = ...
'''

#Convert a dictionary to a json file
# Note json.dump writes to a file or file-like object, whereas json.dumps returns a string.
def jsonDump(d, fileName):
    with open('{}.txt'.format(fileName), 'w') as outfile:
        json.dump(d, outfile, sort_keys = True, ensure_ascii=False)
    return None


#Testing
# jsonDump(
# {
#     "maps": [
#         {
#             "id": "blabla",
#             "iscategorical": "0"
#         },
#         {
#             "id": "blabla",
#             "iscategorical": "0"
#         }
#     ],
#     "masks": {
#         "id": "valore"
#     },
#     "om_points": "value",
#     "parameters": {
#         "id": "valore"
#     }
# }, 'testFile')
#
#
# B = jsonParse('testFile.txt')
# print(B)

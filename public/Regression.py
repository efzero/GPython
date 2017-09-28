# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 13:05:21 2017
@author: Jiayin
"""

'''Week June 18th: Basic Regression'''
import pandas as pd
 #import numpy as np
import statsmodels.api as sm

# from sklearn.linear_model import LinearRegression


#Read data from csv file and return a pandas Dataframe to use later
def csvDF(csvFile):
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

#plot 1D scatter & regression plot. I.E. each x variable with y plotting.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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
        fig.savefig('public/images/scatterRegression_{}.png'.format(i), bbox_inches='tight')
    return None


#Correlation of selected data. Value matrix & Heatmap
import numpy as np
#output: m--matrix with values//h--heatmap//mh--heatmap with values annotated
def corr(df, outputForm):
    corr = df.corr()
    if outputForm == 'm':
        return corr
    elif outputForm == 'h':
        fig, ax = plt.subplots()
        ax.imshow(corr, cmap=plt.cm.Oranges, interpolation='nearest', origin='lower', extent=[0,len(df.columns),0,len(df.columns)])
        heatmap = ax.pcolor(corr, cmap=plt.cm.Oranges)
        ax.set_yticks(np.arange(corr.shape[0])+0.5, minor=False)
        ax.set_xticks(np.arange(corr.shape[1])+0.5, minor=False)
        plt.colorbar(heatmap)
        ax.set_yticklabels(df.columns, minor=False)
        ax.set_xticklaabels(df.columns, minor=False, rotation='vertical')
#        fig.savefig('images/corrHeatmap.png', bbox_inches='tight')
#        plt.show()
        return None
    elif outputForm == 'mh':
        fig, ax = plt.subplots()
        ax.imshow(corr, cmap=plt.cm.Oranges, interpolation='nearest', origin='lower', extent=[0,len(df.columns),0,len(df.columns)])
        heatmap = ax.pcolor(corr, cmap=plt.cm.Oranges)
        ax.set_yticks(np.arange(corr.shape[0])+0.5, minor=False)
        ax.set_xticks(np.arange(corr.shape[1])+0.5, minor=False)
        plt.colorbar(heatmap)
        ax.set_yticklabels(df.columns, minor=False)
        ax.set_xticklabels(df.columns, minor=False, rotation='vertical')
        for y in range(corr.shape[0]):
            for x in range(corr.shape[1]):
                plt.text(x + 0.5, y + 0.5, '%.4f' % corr.ix[y, x],
                 horizontalalignment='center',
                 verticalalignment='center',
                 )
 #       fig.savefig('images/corrHeatmap.png', bbox_inches='tight')
 #       plt.show()
        return None
    else:
        return None
# 
#
#
# '''
# plt.figure(2)
# plt.subplot()
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# plt.subplot()
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()
# x.columns[0]
# results.params['const']
# results.params[x.columns[0]]
# #Number of columns of a dataframe
# len(x.columns)
# #Secelect the first column data
# x.ix[:,0]
# '''
#
#
# #Testing Regression functions
# df = csvDF('mydata.csv')
# #Inspect the first five lines of the data
# df.head()
# #Define independent variables and dependent variables and form new dataframes
# x =  df[['COUNT FEMALE', 'COUNT PACIFIC ISLANDER', 'COUNT AMERICAN INDIAN']]
# y = df[['COUNT PUBLIC ASSISTANCE TOTAL']]
# #Do regression on x and y dataframes
# results = regression(y, x)
# #Look at summary statistics of regression
# results.summary()   #Note: many choices to call here
# results.rsquared
# '''
# If want to use the trained model to predict y using some new dataframe x2, can use
# results.predict(x2)
# '''
#
# #Testing Summary_stat for columns in a dataframe
# summary_stat(x)
#
# '''Also, maybe make one for dummy variables
#     And consider plots with y and x1, x2, x3... etc'''
#
# regPlot (y, x, results)
#
#
# #Testing correlation
# newDF = pd.concat([y, x], axis=1)
#
# newDF.head()
# newDF.columns
# len(newDF.columns)
#
#
# '''
# corr = newDF.corr()
# corr.ix[1, 0]
# fig, ax = plt.subplots()
# ax.imshow(corr, cmap=plt.cm.Oranges, interpolation='nearest', origin='lower', extent=[0,len(newDF.columns),0,len(newDF.columns)])
# heatmap = ax.pcolor(corr, cmap=plt.cm.Oranges)
# ax.set_yticks(np.arange(corr.shape[0])+0.5, minor=False)
# ax.set_xticks(np.arange(corr.shape[1])+0.5, minor=False)
# for y in range(corr.shape[0]):
#     for x in range(corr.shape[1]):
#         plt.text(x + 0.5, y + 0.5, '%.4f' % corr.ix[y, x],
#                  horizontalalignment='center',
#                  verticalalignment='center',
#                  )
# plt.colorbar(heatmap)
# ax.set_yticklabels(newDF.columns, minor=False)
# ax.set_xticklabels(newDF.columns, minor=False, rotation='vertical')
# fig.set_size_inches(10, 5)
# plt.show()
# '''
#
# corr(newDF, 'm')
#
# corr(newDF, 'h')
#
# corr(newDF, 'mh')

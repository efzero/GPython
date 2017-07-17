import pandas as pd
import sys, json, numpy as np
import json
import csv
import stats1
from pandas.io.json import json_normalize



def main():
    print("reading data")


    #Testing Regression functions
    df = stats1.read_data('mydata.csv')
    #Inspect the first five lines of the data
    # df.head()
    #Define independent variables and dependent variables and form new dataframes
    x =  df[['COUNT FEMALE', 'COUNT PACIFIC ISLANDER', 'COUNT AMERICAN INDIAN']]
    y = df[['COUNT PUBLIC ASSISTANCE TOTAL']]
    # # #Do regression on x and y dataframes
    results = stats1.regression(y, x)
    stats1.regPlot(y,x, results)
    print("fig saved")


if __name__ == '__main__':
    main()

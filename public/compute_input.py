## compute_input.py
import pandas as pd
import sys, json, numpy as np
import json
import csv
import stats1
from pandas.io.json import json_normalize
#import StasticalCode1.py




#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    data = {"result": { "code": "OK", "msg": "" },
    "report_name":"DAILY",
    "columns":["ad","ad_impressions","cpm_cost_per_ad","cost"],
    "data":[{"row":["CP_CARS10_LR_774470","966","6.002019","5.797950"]}],
    "total":["966","6.002019","5.797950"],
    "row_count":1}

    #Convert the above to a dataframe that matches columns to data

    A = pd.DataFrame()
    A['columns'] = pd.Series(data['columns'])
    A['data'] = json_normalize(data, ['data', 'row'])
    # print("HelloWorld")
    # print(A.T)

    table = pd.read_csv("/home/bowen/GPython/public/mydata.csv")
    mydata = table.as_matrix()
    col_1 = mydata[:,0]
    col_2 = mydata[:,1]
    df = pd.read_csv('mydata.csv')
    x =  df[['COUNT FEMALE', 'COUNT PACIFIC ISLANDER', 'COUNT AMERICAN INDIAN']]
    y = df[['COUNT PUBLIC ASSISTANCE TOTAL']]
    #Do regression on x and y dataframes
    results = stats1.regression(y, x)
    # stats1.rePlot(y, x, results);
    #Look at summary statistics of regression
    print(results.summary())   #Note: many choices to call here
    print(results.rsquared)
    stats1.regPlot(y,x,results)
    #get our data as an array from read_in()
    # lines = read_in()

    #create a numpy array
    # np_lines = np.array(lines)

    #use numpys sum method to find sum of all elements in the array
    # lines_sum = 2*np.sum(np_lines)
    #
    # a = np.zeros(10)


    #return the sum to the output stream
    # print(x)
    # print(y)


#start process
if __name__ == '__main__':




    main()

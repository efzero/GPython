# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:55:18 2017

@author: Jiayin
"""
import sys
# sys.path.append('C:\\Users\\Jiayin\\Desktop\\Kay Lu\\Work & Research\\Python Coding Bowen Project')

from Regression import regression, summary_stat, regPlot, columnNames, frameFromCol, regPlot, corr
from Conversion import csvDF

####Testing with buffer (2) Json (svg buffer (2))
import json

def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])




def main():
    data = csvDF('mydata.csv')
    text = read_in()
    text['cells'][0]['ports']['groups']['out']['attrs']['.port-body']['magnet']="shabi"


    input1 =  data[['COUNT FEMALE', 'COUNT PACIFIC ISLANDER', 'COUNT AMERICAN INDIAN']]
    input2 = data[['COUNT PUBLIC ASSISTANCE TOTAL']]
    # print("success")
    dataDict = {'input1':input1, 'input2':input2}
    singelObj = list(filter(lambda d: d['type'] == 'cell', text['cells']))
    groupedObj = list(filter(lambda d: '.uml-class-box-rect' in d['attrs'], text['cells']))
    pointer = list(filter(lambda d: d['type'] == 'link', text['cells']))
    idDict = {}
    # print(singelObj)
    # print(data)
    def IDmatchOBJ(objName):
        idDict[list(filter(lambda d: d['attrs']['.label']['text'] == objName, singelObj))[0]['id']] = dataDict[objName]


#Match ID with input data (singleObg)
    for i in range(0, len(dataDict)):
        IDmatchOBJ(list(dataDict.keys())[i])

#GroupedObj: Match its own ID to its grouped objects' IDs
    # for i in range(0, len(groupedObj)):
    #     idDict[groupedObj[i]['id']] = groupedObj[i]['embeds']

#Run workflow:
    for i in range(0, len(pointer)):

        if pointer[i]['labels'][0]['attrs']['text']['text'] == 'summary':
            idDict[pointer[i]['target']['id']] = summary_stat(idDict[pointer[i]['source']['id']])
            print (idDict[pointer[i]['target']['id']])



            # if pointer[i]['labels'][0]['attrs']['text']['text'] == 'regression':
            #     if len(idDict[pointer[i]['source']['id']]) == 2:
            #         x = idDict[idDict[pointer[i]['source']['id']][0]]
            #         y = idDict[idDict[pointer[i]['source']['id']][1]]
            #         idDict[pointer[i]['target']['id']] = regression(y, x)
            #         print (idDict[pointer[i]['target']['id']].summary())


#start process
if __name__ == '__main__':
    main()





'''  SOME SCRATCH ----NO USE---USEFUL WORK ARE ABOVE------

funcDict = {"regression":regression, "summary statistics": summary_stat,
            "1Dplot": regPlot, "correlation": corr, "csvDF": csvDF,
            "columnNames":columnNames, "frame from columns": frameFromCol,
            "regression plot":regPlot}

data = 'mydata.csv'
instruction = ['csvDF','frameFromCol','frameFromCol',
               ['summary_stat', 'corr',
                ['regression',"regression plot"]
                ]
                ]

selected_x = ['COUNT FEMALE', 'COUNT PACIFIC ISLANDER', 'COUNT AMERICAN INDIAN']
selected_y = ['COUNT PUBLIC ASSISTANCE TOTAL']


s = ['a','b','c']
input_var = input("enterplease")

def workflow(instList, data):
    iniInput = data;
    for i in range(0, len(instList)):
        if len(instList[i]) == 1:
            output = funcDict[instList[i]](iniInput)


            iniInput = output



df = csvDF(data)

dfy = pd.DataFrame()
dfx = pd.DataFrame()

dfx = frameFromCol(selected_x, df)
dfy = frameFromCol(selected_y, df)





##Need to do below!!!!  :D :D :D

data = 'mydata.csv'

parDict = {"regression":['1', '2'], "summary statistics": ['3'],
            "1Dplot": ['4','5', '6'], "correlation": ['7','8'],
            "csvDF": ['9'],
            "columnNames":['10'],
            "frame from columns": ['11', '12'],
            "regression plot":['13'], 'dfx':['14']}


parDict2 = {'9':data}

selected_x = ['COUNT FEMALE', 'COUNT PACIFIC ISLANDER', 'COUNT AMERICAN INDIAN']
selected_y = ['COUNT PUBLIC ASSISTANCE TOTAL']

parDict2['11'] = selected_x
parDict2['12'] = selected_y



'''
'''
'1':dfy, '2':dfx, '3':df2, '4':dy, '5':dx, '6':result,  }
'''
'''

par = []
for i in range(0, len(parDict["regression"])):
  # parDict2[parDict["regression"][i]] =    #Add new parameters?
    par.append(parDict2[parDict["regression"][i]])


result = funcDict["regression"](*par)
result.summary()






'''

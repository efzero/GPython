# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 01:00:21 2017

@author: kay75
"""

import sys
import json
import matplotlib.pyplot as plt
import re


from Regression import regression, summary_stat, regPlot, columnNames, frameFromCol, regPlot, corr
from Conversion import csvDF
from 100117_100517 import combHor, combVer, frameFromCol, basicMan, trainTestSplit, trainKNN, testKNN, predKNN
#Need to read and Update JSON from website



def main():

 #   with open('test.json') as json_data:
#        text = json.load(json_data)
    # text['cells'][0]['ports']['groups']['out']['attrs']['.port-body']['magnet']="shabi"
    # text['cells'][0]['ports']['groups']['in']['attrs']['.port-body']['magnet']="shabi"
 #   print('nihao')


    obj  = list(filter(lambda d: d['type'] == 'cell', text['cells']))
    # print(list(filter(lambda d: d['attrs']['.label']['text'] == 'input1', obj)))
    # print(list(filter(lambda d: d['attrs']['.label']['text'] == 'input1', obj)))

    in1 = list(filter(lambda d: d['attrs']['.label']['text'] == 'input1', obj))

    in2 = list(filter(lambda d: d['attrs']['.label']['text'] == 'input2', obj))

    # print(in1[0]['data'])
    # print('')
    # print(in2[0]['data'])

    input1 = []
    input2 = []
    dataDict = {}
    data = csvDF('mydata.csv')


    if in1 != []:
        input1 =  data[in1[0]['data']]
        dataDict['input1'] = input1
    if in2 != []:
        input2 = data[in2[0]['data']]
        dataDict['input2'] = input2



    singelObj = list(filter(lambda d: d['type'] == 'cell', text['cells']))
    groupedObj = []  #groupedObj will be a sub-object of singelObj
    pointer = list(filter(lambda d: d['type'] == 'link', text['cells']))
    # print(singelObj)
    # print(pointer)
    idDict = {}

    def IDmatchOBJ(objName):
        idDict[list(filter(lambda d: d['attrs']['.label']['text'] == objName, singelObj))[0]['id']] = dataDict[objName]


    #Match ID with input data (singleObg)
    for i in range(0, len(dataDict)):
        IDmatchOBJ(list(dataDict.keys())[i])


    #Run workflow:
    #With order. I.recursion function
    #running a single pointer
    finishedPointer = []  #to store pointers that was finished to avoid repetition
    def workflow(singlePointer, pointer):
        instName = singlePointer['labels'][0]['attrs']['text']['text']
        inID = singlePointer['source']['id']
        outID = singlePointer['target']['id']

        #pointer's own id. Use it to avoid repetition of finished pointers.
        thisID = singlePointer['id']

        #Recursion if...else...
        if inID in idDict:
            if instName == 'group':
                #categorize output as groupedObj
                groupedObj.append(list(filter(lambda d: d['id'] == outID, singelObj)))
                if outID in idDict:
                    idDict[outID].append(inID)
                else:
                    idDict[outID] = [inID]
                finishedPointer.append(thisID)

            if instName == 'groupAsX':
                #categorize output as groupedObj
                groupedObj.append(list(filter(lambda d: d['id'] == outID, singelObj)))
                if outID in idDict:
                    idDict[outID].insert(0, inID)
                else:
                    idDict[outID] = [inID]
                finishedPointer.append(thisID)

            if instName == 'groupAsY':
                #categorize output as groupedObj
                groupedObj.append(list(filter(lambda d: d['id'] == outID, singelObj)))
                if outID in idDict:
                    idDict[outID].insert(1, inID)
                else:
                    idDict[outID] = [inID]
                finishedPointer.append(thisID)
'''NEW'''
            if instName == 'combHor':
                #Need to group two dataframe first and then use this
                if len(idDict[inID]) >=2:
                    df1 = idDict[idDict[inID][0]]
                    df2 = idDict[idDict[inID][1]]
                    idDict[outID] = combHor(df1, df2)
                    finishedPointer.append(thisID)
                else:
                    backwardPointer = list(filter(lambda d: d['target']['id'] == inID, pointer))
                    for i in range(0, len(backwardPointer)):
                        workflow(backwardPointer[i], pointer)
                    
            if instName == 'combVer':
                #Need to group two dataframe first and then use this
                if len(idDict[inID]) >=2:
                    df1 = idDict[idDict[inID][0]]
                    df2 = idDict[idDict[inID][1]]
                    idDict[outID] = combVer(df1, df2)
                    finishedPointer.append(thisID)
                else:
                    backwardPointer = list(filter(lambda d: d['target']['id'] == inID, pointer))
                    for i in range(0, len(backwardPointer)):
                        workflow(backwardPointer[i], pointer)
             
            pattern = re.compile("^..*[\+\-\*\/]..*$")
            if pattern.match(instName):
                df = idDict[inID]
                
                m = re.search('..*[\+\-\*\/]', instName)
                col1 = m.group(0)[:-2]
                
                n = re.search('[\+\-\*\/]..*', instName)
                col2 = n.group(0)[2:]
                
                t = re.search('[\+\-\*\/]', instName)
                command = t.group(0)
                
                idDict[outID] = basicMan(df, col1, col2, command)
                finishedPointer.append(thisID)
            
            
            if instName == "trainTestSplit":
                if len(idDict[inID]) >= 2:
                    x = idDict[idDict[inID][0]]
                    y = idDict[idDict[inID][1]] 
                    
                    if len(y.columns) == 1:
                        idDict[outID] = trainTestSplit (x, y)
                        finishedPointer.append(thisID)
                        
                else: 
                    backwardPointer = list(filter(lambda d: d['target']['id'] == inID, pointer))
                    for i in range(0, len(backwardPointer)):
                        workflow(backwardPointer[i], pointer)
                        
            if instName == "x train":
                idDict[outID] = idDict[inID][0]
                finishedPointer.append(thisID)
                
            if instName == "y train":
                idDict[outID] = idDict[inID][2]
                finishedPointer.append(thisID)
                
            if instName == "x test":
                idDict[outID] = idDict[inID][1]
                finishedPointer.append(thisID)
                
            if instName == "y test":
                idDict[outID] = idDict[inID][3]
                finishedPointer.append(thisID)
            
            
            
            
            
'''NEW'''          
            if instName == 'summary':
                idDict[outID] = summary_stat(idDict[inID])
                finishedPointer.append(thisID)
                print (idDict[outID])


            if instName == 'regression':
                if len(idDict[inID]) >= 2:
                    #For it to run correctly, need to specify "GroupAsX"
                    #and "GroupAsY" when grouping. As it will take the first two
                    #grouped object as x and y.
                    x = idDict[idDict[inID][0]]
                    y = idDict[idDict[inID][1]] 
                    #check if the y is a single set of data before running:
                    if len(y.columns) == 1:
                        idDict[outID] = regression(y, x)
                        finishedPointer.append(thisID)
                        print (idDict[outID].summary())
                else:
                    backwardPointer = list(filter(lambda d: d['target']['id'] == inID, pointer))
                    for i in range(0, len(backwardPointer)):
                        workflow(backwardPointer[i], pointer)

            if instName == 'regression plot':
                xyGroup = list(filter(lambda d: d['target']['id'] == inID, pointer))
                x = idDict[idDict[xyGroup[0]['source']['id']][0]]
                y = idDict[idDict[xyGroup[0]['source']['id']][1]]
                results = idDict[inID]
                idDict[outID] = regPlot(y, x, results)
                finishedPointer.append(thisID)

            if instName == 'regression summary':
                idDict[outID] = idDict[inID].summary()
                finishedPointer.append(thisID)
                print (idDict[outID].summary())

        else:
            backwardPointer = list(filter(lambda d: d['target']['id'] == inID, pointer))
            for i in range(0, len(backwardPointer)):
                workflow(backwardPointer[i], pointer)



    #Start running
    for i in range(0, len(pointer)):
        if pointer[i]['id'] not in finishedPointer:
            workflow(pointer[i], pointer)





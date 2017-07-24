# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 15:05:00 2017

@author: Jiayin
"""

import sys
import json
import matplotlib.pyplot as plt

from Regression import regression, summary_stat, regPlot, columnNames, frameFromCol, regPlot, corr
from Conversion import csvDF

#Need to read and Update JSON from website



def main():

    with open('test.json') as json_data:
        text = json.load(json_data)
    # text['cells'][0]['ports']['groups']['out']['attrs']['.port-body']['magnet']="shabi"
    # text['cells'][0]['ports']['groups']['in']['attrs']['.port-body']['magnet']="shabi"
    print('nihao')


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






    '''Previousely...From last time... USEFUL ARE ABOVE-----


    for i in range(0, len(pointer)):
        instName = pointer[i]['labels'][0]['attrs']['text']['text']
        inID = pointer[i]['source']['id']
        outID = pointer[i]['target']['id']


        if instName == 'summary':
            idDict[outID] = summary_stat(idDict[inID])
            print (idDict[outID])


        if instName == 'regression':
            if len(idDict[inID]) == 2:
                x = idDict[idDict[inID][0]]
                y = idDict[idDict[inID][1]]
                idDict[outID] = regression(y, x)
                print (idDict[outID].summary())


    '''

if __name__ == '__main__':
    main()

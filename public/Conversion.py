# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 05:07:41 2017
@author: Jiayin
"""
import pandas as pd
import json
import csv
from pandas.io.json import json_normalize



def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

#parse into a normal dictionary
#json_file is some
#Note json.loads(json_string) is for loading a string
def jsonDICT(json_file):
    with open(json_file) as data_file:
        parsed_json = json.load(data_file)
    return parsed_json

'''sample use:
A = jsonDict(jsonFile)
A['key_name'] = ...
'''

#Convert a dictionary to a json file
# Note json.dump writes to a file or file-like object, whereas json.dumps returns a string.
def dictJSON(d, fileName):
    with open('{}.txt'.format(fileName), 'w') as outfile:
        json.dump(d, outfile, sort_keys = True, ensure_ascii=False)
    return None


#Testing
dictJSON(
{
    "maps": [
        {
            "id": "blabla",
            "iscategorical": "0"
        },
        {
            "id": "blabla",
            "iscategorical": "0"
        }
    ],
    "masks": {
        "id": "valore"
    },
    "om_points": "value",
    "parameters": {
        "id": "valore"
    }
}, 'testFile')


B = jsonDICT('testFile.txt')

B   #dictionary


def csvDICT(csvFile):        #csv To a list of dict
    reader = csv.DictReader(open(csvFile, 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list

# C = csvDICT('mydata.csv')
# type(C)



#(List of)dictionaries to a csv file saving locally
def dictCSV(dictString, fileName):
    if type(dictString) is list:      #List of Dict
        keys = dictString[0].keys()
        with open('{}.csv'.format(fileName), 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys, delimiter=',', lineterminator='\n')
            dict_writer.writeheader()
            dict_writer.writerows(dictString)

    else:  #dictionary
        keys = dictString.keys()      #A single Dict
        with open('{}.csv'.format(fileName), 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys, delimiter=',', lineterminator='\n')
            dict_writer.writeheader()
            dict_writer.writerow(dictString)
    return None


# #Testing
# Ldict = [{'name':'bob','age':25,'weight':200},
#          {'name':'jim','age':31,'weight':180}]
# dictSt = {'name':'bob','age':25,'weight':200}
# type(dictSt)
# type(Ldict)

# dictCSV(Ldict, "dictCTest")
# dictCSV(dictSt, "dictCTest2")


#Dataframe to a csv file saving locally
def dfCSV(df, fileName):
    df.to_csv('{}.csv'.format(fileName), index=False)
    return None

#csv to Dataframe
def csvDF(csvFile):
    df = pd.read_csv(csvFile)
    return df

# #Testing
# D = csvDF("dictCTest.csv")
# D

# dfCSV(D, "dfCSVtest")





'''   STILL WORKING ON THIS: JSON & Dataframe conversion
 ***Need JSON samples... What format will they be?? There are some very weird format ones...
    '''

def jsonDF(jsonFile):
    with open(jsonFile) as file:
        text = json.load(file)
    #dict
    if type(text) is dict:
        with open(jsonFile) as file:
            myList = []
            for line in file:
                line = line.replace('\\','')
                myList.append(json.loads(line))
        df = json_normalize(myList)      #Should delve more in "normalize" function. Here, I merely flatten it to one row.

    else: #list of Dict
            df = pd.DataFrame(text)
    return df

# #Testing
# dictJSON([{'created': '2013-02-22', 'data_version': 0.8, 'revision': 1},
#  {'city': 'Southampton',
#   'dates': ['2005-06-13'],
#   'gender': 'male',
#   'match_type': 'T20',
#   'outcome': {'by': {'runs': 100}, 'winner': 'England'},
#   'overs': 20,
#   'player_of_match': ['KP Pietersen'],
#   'teams': ['England', 'Australia'],
#   'toss': {'decision': 'bat', 'winner': 'England'},
#   'umpires': ['NJ Llong', 'JW Lloyds'],
#   'venue': 'The Rose Bowl'},
#  {'1st innings': {'deliveries': [{'0.1': {'batsman': 'ME Trescothick',
#        'bowler': 'B Lee',
#        'non_striker': 'GO Jones',
#        'runs': {'batsman': 0, 'extras': 0, 'total': 0}}},
#      {'19.6': {'batsman': 'PD Collingwood',
#        'bowler': 'GD McGrath',
#        'non_striker': 'J Lewis',
#        'runs': {'batsman': 0, 'extras': 0, 'total': 0},
#        'wicket': {'fielders': ['RT Ponting'],
#         'kind': 'caught',
#         'player_out': 'PD Collingwood'}}}],
#     'team': 'England'}},
#   {'2nd innings': {'deliveries': [{'0.1': {'batsman': 'AC Gilchrist',
#        'bowler': 'D Gough',
#        'non_striker': 'ML Hayden',
#        'runs': {'batsman': 0, 'extras': 0, 'total': 0}}},
#      {'14.3': {'batsman': 'GD McGrath',
#        'bowler': 'SJ Harmison',
#        'non_striker': 'MS Kasprowicz',
#        'runs': {'batsman': 0, 'extras': 0, 'total': 0},
#        'wicket': {'kind': 'bowled', 'player_out': 'GD McGrath'}}}],
#     'team': 'Australia'}}], 'testFile2')


# E = jsonDF('testFile.txt')
# E
# F = jsonDF('testFile2.txt')
# F



# dictJSON({"result": { "code": "OK", "msg": "" },
# "report_name":"DAILY",
# "columns":["ad","ad_impressions","cpm_cost_per_ad","cost"],
# "data":[{"row":["CP_CARS10_LR_774470","966","6.002019","5.797950"]}],
# "total":["966","6.002019","5.797950"],
# "row_count":1}, 'testJSON3')


# jsonDF('testJSON3.txt')

# data = {"result": { "code": "OK", "msg": "" },
#             "report_name":"DAILY",
#             "columns":["ad","ad_impressions","cpm_cost_per_ad","cost"],
#     "data":[{"row":["CP_CARS10_LR_774470","966","6.002019","5.797950"]}],
#     "total":["966","6.002019","5.797950"],
#     "row_count":1}

# #Convert the above to a dataframe that matches columns to data
# A = pd.DataFrame()
# A['columns'] = pd.Series(data['columns'])
# A['data'] = json_normalize(data, ['data', 'row'])
# print(A.T)

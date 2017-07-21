import pandas as pd


def show_summary():
    try:
        myfile = pd.read_csv('/home/bowen/GPython/mydata.csv')
        summary = list(myfile.columns.values)
        datastring = ''
        for i in summary:
            datastring += i
            datastring += ','
        print(datastring)
    except:
        print('error')

show_summary()

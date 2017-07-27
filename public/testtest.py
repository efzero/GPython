import json




with open('test.json') as json_data:
    text = json.load(json_data)


cells = list(filter(lambda d: d['type'] == 'cell', text['cells']))
links = list(filter(lambda d: d['type'] == 'link', text['cells']))



def getName(cells, id):
    cell = list(filter(lambda d: d['id'] == id, cells))
    return cell[0]['attrs']['.label']['text']

# input1 = list(filter(lambda d: d['attrs']['.label']['text'] == 'input1'], cells))
# input2 = list(filter(lambda d: d['attrs']['.label']['text'] == 'input2'], cells))



for i in range(len(links)):
    targetName = getName(cells, links[i]['target']['id'])
    sourceName = getName(cells, links[i]['source']['id'])
    LinkName = links[i]['labels'][0]['attrs']['text']['text']
    print('target', targetName)
    print('linkname', LinkName)
    print('source', sourceName)


# # print(len(links))
# # print(len(cells))



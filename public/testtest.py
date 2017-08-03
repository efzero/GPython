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
# print(len(text['cells']))

def nametoId(name):
    return 0

def Idtoname(id):
    return 0


def process_link(cell, cell2):
    str = cell + cell2
    print(str)

def getBackwardCells(cell):
    return backwardmap[cell]
def getLinkName(link):
    return link['labels'][0]['attrs']['text']['text']

def getForwardCells(cell):
    return forwardmap[cell]




# for i in range(len(links)):
#     targetName = getName(cells, links[i]['target']['id'])
#     sourceName = getName(cells, links[i]['source']['id'])
#     LinkName = links[i]['labels'][0]['attrs']['text']['text']
#     print('target', targetName)
#     print('linkname', LinkName)
#     print('source', sourceName)




visited = []
stored = []

def workflow(cell, direction, cells):
    if direction == 'back':
        #the starting point of the graph
        if len(getBackwardCells(cell)) == 0 and cell not in visited:
            workflow(cell, 'forward', cells)
        else:
        #searching for the backward nodes
            for node in getBackwardCells(cell):
                if node not in visited:
                    workflow(node, 'back', cells)   
    else:
        #only do the traversal when the cell 
        if cell not in visited:
            if len(getForwardCells(cell)) == 0:
                return
            else:
                visited.append(cell)
                for node in getForwardCells(cell):
                    process_link(cell, node)
                    if len(getBackwardCells(node)) > 1:
                        for i in getBackwardCells(node):
                            workflow(i, 'back', cells)                
                    workflow(node, 'forward', cells)

                

cells = ['kuangluo', 'yangtuo', 'xiaoge', 'laogou', 'bowen', 'samantha', 'ayumi', 'amanda']
forwardmap = {'samantha':[], 'amanda':[], 'kuangluo': ['ayumi', 'amanda'], 'ayumi': ['xiaoge'], 'bowen' :['samantha'], 'yangtuo': ['ayumi', 'amanda'], 'xiaoge': ['samantha'], 'laogou': ['xiaoge']}
backwardmap = {'samantha': ['bowen', 'xiaoge'], 'amanda': ['kuangluo', 'yangtuo'], 'ayumi': ['yangtuo', 'kuangluo'], 'kuangluo' :[], 'yangtuo': [], 'xiaoge': ['laogou','ayumi'], 'bowen': [], 'laogou': []}


workflow('kuangluo', 'back', cells)

# print(visited)


# for i in cells:
#     print(visited)
#     if i not in visited:
#         workflow(i, 'back', cells)

   # print(cell, direction)
    # print(visited)
# print(visited)
# print(len(getBackwardCells('samantha')))
# for i in cells:
#     print(getForwardCells(i))


# print('then')

# for i in cells:
#     print(getBackwardCells(i))


# # print(len(links))
# # print(len(cells))



from io import StringIO
from data import getStoptimeData,deleteSpecialText

def stop_timesCheck():
    neededFile = []
    requirefile = ['trip_id','stop_id','stop_sequence']

    read = getStoptimeData()
    header = deleteSpecialText(read[0])
    read.pop(0)
    # print(header)

    for read in read:
        line = deleteSpecialText(read)
        for i,name in enumerate(line):
            # print('name: ',name)
            if name == '':
                if(header[i] in requirefile):
                    neededFile.append(header[i])            
        # print("------------------------------------------")
    neededFile = list(set(neededFile))
    # print(neededFile)
    return neededFile


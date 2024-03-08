import os
import re
from data import getTripData,deleteSpecialText

def tripsCheck():
    
    read = getTripData()

    requirefile = ['route_id','service_id','trip_id','shape_id']

    read = [readed.strip() for readed in read]

    header = deleteSpecialText(read[0])
    
    read.pop(0)
    # print(header)
    neededFile = []

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

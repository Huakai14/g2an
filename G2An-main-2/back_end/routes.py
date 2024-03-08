
import re
from data import getRouteData,deleteSpecialText

def routesCheck():

    read = getRouteData()

    requirefile = ['route_id','agency_id','route_short_name','route_long_name','route_type']
    
    read = [readed.strip() for readed in read]

    header = deleteSpecialText(read[0])
    read.pop(0)
    
    neededFile = []
    a = 1
    for read in read:
        a = a+1
        line = deleteSpecialText(read)
        # print(a,line)
        for i,name in enumerate(line):
            # print(i,'header: ',header[i],'name:',name)
            if name == '':
                if(header[i] in requirefile):
                    neededFile.append(header[i])         
  
        # print("------------------------------------------")
    neededFile = list(set(neededFile))
    # print(neededFile)
    return neededFile

import re
from data import getShapesData,deleteSpecialText

def shapesCheck():

    read = getShapesData()

    requirefile = ['shape_id','shape_pt_lon','shape_pt_lat','shape_pt_sequence']
    
    read = [readed.strip() for readed in read]

    header = deleteSpecialText(read[0])
    read.pop(0)
    # print(header)
    
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

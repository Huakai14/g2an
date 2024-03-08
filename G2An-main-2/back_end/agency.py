import re
from data import deleteSpecialText, getAgencyData

def agencyCheck():
    read = getAgencyData()

    requirefile = ['agency_id','agency_name','agency_url','agency_timezone']

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

    



import re
from data import getCalendarData,deleteSpecialText

def calendarCheck():
    
    read = getCalendarData()

    requirefile = ['service_id','monday','tuesday','wednesday','thursday','friday','saturday','sunday','start_date','end_date']
    
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
    return neededFile


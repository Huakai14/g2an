from zipfile import ZipFile
import os

def unzipfile(path):
    os.chdir(path)
    os.listdir()

    requirefile = ['agency.txt','stops.txt','routes.txt','trips.txt','stop_times.txt','calendar.txt','calendar_dates.txt','shapes.txt']
    correctFileState = False

    with ZipFile("gtfs.zip") as zip_object:
        file_name = zip_object.namelist()
        for file_name in file_name:
            if file_name in requirefile:
                requirefile.remove(file_name)

        if len(requirefile) == 0:
            correctFileState == True
            zip_object.extractall(path)
            return correctFileState

        if len(requirefile) == 1 and (('calendar.txt' in requirefile) or ('calendar_dates.txt' in requirefile)):
            correctFileState == True
            zip_object.extractall(path)
            return correctFileState
        
        else:
            if ('calendar.txt' in requirefile) == ('calendar_dates.txt' in requirefile):
                return requirefile
            else:
                if('calendar.txt' in requirefile):
                    requirefile.remove('calendar.txt')
                if('calendar_dates.txt' in requirefile):
                    requirefile.remove('calendar_dates.txt')
                return requirefile
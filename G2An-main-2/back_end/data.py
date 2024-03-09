import os
from io import StringIO
from datetime import datetime
import pandas as pd

path = r'C:/Users/USER/Desktop/g2an_project/g2an/G2An-main-2/back_end/gtfsFile'
os.chdir(path)
os.listdir()

def deleteSpecialText(text):
    # COMMA_MATCHER = re.compile(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")
    # return COMMA_MATCHER.split(text)
    return text.split(',')

def getStoptimeData():
    file = open("stop_times.txt",'r', encoding="utf-8-sig")
    read = file.readlines()
    read = [readed.strip() for readed in read]
    return read

def getShapesData():
    file = open("shapes.txt",'r', encoding="utf-8-sig")
    read = file.readlines()
    read = [readed.strip() for readed in read]
    return read

def getAgencyData():
    file = open("agency.txt", encoding="utf-8-sig")
    read = file.readlines()
    read = [readed.strip() for readed in read]
    return read

def getRouteData():
    file = open("routes.txt",'r', encoding="utf-8-sig")
    read = file.readlines()
    read = [readed.strip() for readed in read]
    return read

def getStopsData():
    file = open("stops.txt",'r', encoding="utf-8-sig")
    read = file.readlines()
    read = [readed.strip() for readed in read]
    return read

def getCalendarData():
    file = open("calendar.txt",'r', encoding="utf-8-sig")
    read = file.readlines()
    read = [readed.strip() for readed in read]
    return read

def getDateData():
    file = open("calendar_dates.txt",'r', encoding="utf-8-sig")
    read = file.readlines()
    read = [readed.strip() for readed in read]
    return read

def getTripData():
    file = open("trips.txt",'r', encoding="utf-8-sig")
    read = file.readlines()
    read = [readed.strip() for readed in read]
    return read

def getStopPD():
    stop_d = getStopsData()
    header_s = deleteSpecialText(stop_d[0])
    stop_d.pop(0)
    data_string_s = "\n".join(stop_d)
    data_ios = StringIO(data_string_s)
    df_s = pd.read_csv(data_ios, header=None, names=header_s, dtype={'stop_id':str,'stop_code':str,'stop_name':str,'stop_desc':str,'stop_lat':str,'stop_lon':str,'location_type':str})
    return df_s

def getTripsPD(date):
    trip_d = getTripData()
    header_t = deleteSpecialText(trip_d[0])
    trip_d.pop(0)
    data_string_t = "\n".join(trip_d)
    data_iot = StringIO(data_string_t)
    df_t = pd.read_csv(data_iot, header=None, names=header_t, dtype={'route_id':str,'trip_id':str,'service_id':str,'trip_headsign':str,'direction_id':str,'shape_id':str})
    service_on = filter_gtfs_by_date(date).astype(str)
    df_t_filter = df_t[df_t['service_id'].isin(service_on)]

    return df_t_filter

def getAllTripsPD():
    trip_d = getTripData()
    header_t = deleteSpecialText(trip_d[0])
    trip_d.pop(0)
    data_string_t = "\n".join(trip_d)
    data_iot = StringIO(data_string_t)
    df_t = pd.read_csv(data_iot, header=None, names=header_t, dtype={'route_id':str,'trip_id':str,'service_id':str,'trip_headsign':str,'direction_id':str,'shape_id':str})
    return df_t

def getStopTimePD(date):
    stoptime_d = getStoptimeData()
    header_st = deleteSpecialText(stoptime_d[0])
    stoptime_d.pop(0)
    data_string_st = "\n".join(stoptime_d)
    data_iost = StringIO(data_string_st)
    df_st = pd.read_csv(data_iost, header=None, names=header_st, dtype={'trip_id': str, 'arrival_time': str,'departure_time':str,'stop_id':str,'stop_squence':str})
    df_st = df_st[df_st['trip_id'].isin(getTripsPD(date)['trip_id'])]
    return df_st

def getAllStopTimePD():
    stoptime_d = getStoptimeData()
    header_st = deleteSpecialText(stoptime_d[0])
    stoptime_d.pop(0)
    data_string_st = "\n".join(stoptime_d)
    data_iost = StringIO(data_string_st)
    df_st = pd.read_csv(data_iost, header=None, names=header_st, dtype={'trip_id': str, 'arrival_time': str,'departure_time':str,'stop_id':str,'stop_squence':str})
    return df_st

def getCalendarPD():
    data = getCalendarData()
    header_st = deleteSpecialText(data[0])
    data.pop(0)
    data_string_st = "\n".join(data)
    data_ioc = StringIO(data_string_st)
    df_c = pd.read_csv(data_ioc, header=None, names=header_st, dtype={'service_id':str,'monday':str,'tuesday':str,'wednesday':str,'thursday':str,'friday':str,'saturday':str,'sunday':str,'start_date':int,'end_date':int})
    return df_c

def getShapesPD():
    data = getShapesData()
    header_st = deleteSpecialText(data[0])
    data.pop(0)
    data_string_sh = "\n".join(data)
    data_iosh = StringIO(data_string_sh)
    df_sh = pd.read_csv(data_iosh, header=None, names=header_st, dtype={'shape_id':str,'shape_pt_lon':float,'shape_pt_lat':float,'shape_pt_sequence':str,'shape_dist_traveled':str})
    return df_sh

def getCalendarDatePD():
    data = getDateData()
    header_st = deleteSpecialText(data[0])
    data.pop(0)
    data_string_st = "\n".join(data)
    data_ioc = StringIO(data_string_st)
    df_c = pd.read_csv(data_ioc, header=None, names=header_st, dtype={'service_id': str, 'date': str,'exception_type':str})
    return df_c

def getRoutePD():
    data = getRouteData()
    header_r = deleteSpecialText(data[0])
    data.pop(0)
    data_string_r = "\n".join(data)
    data_ior = StringIO(data_string_r)
    df_r = pd.read_csv(data_ior, header=None, names=header_r, dtype={'route_id': str, 'agency_id': str,'route_short_name':str,'route_long_name':str,'route_type':str})
    return df_r

def timeToSec(df,column):
    time_sec = pd.DataFrame()
    time_sec['delta_s'] = pd.to_timedelta(df[column])
    time_sec['delta_s'] = time_sec['delta_s'].dt.total_seconds().astype(int)
    return time_sec['delta_s']

def get_day_of_week_name(date_string):
    # Convert the date string to a datetime object
    date_obj = datetime.strptime(date_string, '%Y-%m-%d')
    # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    day_of_week = date_obj.weekday()
    # Define a dictionary to map day of the week integers to names
    days_of_week = {
        0: "monday",
        1: "tuesday",
        2: "wednesday",
        3: "thursday",
        4: "friday",
        5: "saturday",
        6: "sunday"
    }
    # Return the name of the day of the week
    return days_of_week[day_of_week]

def filter_gtfs_by_date(selected_date):
    # Load calendar.txt and calendar_dates.txt
    calendar = getCalendarPD()
    calendar_dates = getCalendarDatePD()

    # Filter calendar by selected date
    start_date = calendar['start_date']
    end_date = calendar['end_date']
    selected_date_int = int(selected_date.replace('-', ''))
    weeks = get_day_of_week_name(selected_date)
    # print(weeks)
    service_ids_on_date = calendar[(start_date <= selected_date_int) & (end_date >= selected_date_int) & (calendar[weeks] != '0')]['service_id']
    service_ids_on_exception_date = calendar_dates[(calendar_dates['date'] == selected_date_int) & (calendar_dates['exception_type'] == '1')]['service_id']
    service_ids_on_date = pd.concat([service_ids_on_date, service_ids_on_exception_date])
    service_ids_off_date = calendar_dates[(calendar_dates['date'] == selected_date_int) & (calendar_dates['exception_type'] == '2')]['service_id']

    # Remove service_ids_off_date from service_ids_on_date
    service_ids_on_date = service_ids_on_date[~service_ids_on_date.isin(service_ids_off_date)]
    # print('Total_date',service_ids_on_date)
    return service_ids_on_date

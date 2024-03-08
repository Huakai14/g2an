
import pandas as pd
from data import filter_gtfs_by_date, getAllTripsPD, getStopTimePD, timeToSec

def get_start_end_time(date):
    #get start and end time of today
    df_st = getStopTimePD(date)
    df_st['start_time'] = timeToSec(df_st,'arrival_time')
    df_st['end_time'] = timeToSec(df_st,'departure_time')
    return df_st

#get start and end time that exceed 24 hr of yesterday ----------------------
def merge_yesterday_time(date):
    df = get_start_end_time(date)
    #select minimum arrival time time (first stop's arrival time) and maximum departure time(last stop's departure time)
    df = df.groupby('trip_id').agg({'start_time':'min','end_time':'max'}).reset_index()
    df_t = getAllTripsPD()
    df_date = pd.to_datetime(date)
    #minus 1 day so it is yesterday
    datetime_minus_one_day = df_date - pd.Timedelta(days=1)
    datetime_minus_one_day = datetime_minus_one_day.strftime('%Y-%m-%d')
    #Do if yesterday have trip
    if not getStopTimePD(datetime_minus_one_day).empty:
        #get stoptime of yesterday
        df_yesterday = get_start_end_time(datetime_minus_one_day)
        df_yesterday_group = df_yesterday.groupby('trip_id').agg({'start_time':'min','end_time':'max'}).reset_index()
        #select trip that have end time more than 86400
        df_yesterday_selected = df_yesterday_group[(df_yesterday_group['end_time'] > 86400)]
        #if start time less than 86400 mean that trip continuous to today. 
        #start new day with 0.00
        df_yesterday_selected.loc[df_yesterday_selected['start_time'] <= 86400, 'start_time'] = 0
        #if start time more than 86400 mean that trip are in today. 
        #example yesterday start 29:00:00 mean that service start at 5:00:00 of today
        #So minus 86400(24:00:00)
        df_yesterday_selected.loc[df_yesterday_selected['start_time'] > 86400, 'start_time'] -= pd.Timedelta(days=1).total_seconds()
        df_yesterday_selected.loc[:, 'end_time'] -= pd.Timedelta(days=1).total_seconds()
        #merge with trip_id to get service id
        merge_w_trip = pd.merge(df_yesterday_selected,df_t[['trip_id','service_id']],on='trip_id')
        #Combine trip that selected form yesterday that more than 24 hr.
        combined_df = pd.concat([df, merge_w_trip], ignore_index=True)        
        df = combined_df
        # print(df)
    return df

def merge_yesterday(date):
    df = get_start_end_time(date)
    df_t = getAllTripsPD()
    df_date = pd.to_datetime(date)
    df = pd.merge(df,df_t[['trip_id','service_id']],on='trip_id')
    #minus 1 day so it is yesterday
    datetime_minus_one_day = df_date - pd.Timedelta(days=1)
    datetime_minus_one_day = datetime_minus_one_day.strftime('%Y-%m-%d')
    #Do if yesterday have trip
    if not getStopTimePD(datetime_minus_one_day).empty:
        #get stoptime of yesterday
        df_yesterday = get_start_end_time(datetime_minus_one_day)
        #select trip that have end time more than 86400
        df_yesterday_selected = df_yesterday[(df_yesterday['end_time'] > 86400)]
        #if start time less than 86400 mean that trip continuous to today. 
        #start new day with 0.00
        df_yesterday_selected.loc[df_yesterday_selected['start_time'] <= 86400, 'start_time'] = 0
        #if start time more than 86400 mean that trip are in today. 
        #example yesterday start 29:00:00 mean that service start at 5:00:00 of today
        #So minus 86400(24:00:00)
        df_yesterday_selected.loc[df_yesterday_selected['start_time'] > 86400, 'start_time'] -= pd.Timedelta(days=1).total_seconds()
        df_yesterday_selected.loc[:, 'end_time'] -= pd.Timedelta(days=1).total_seconds()
        #merge with trip_id to get service id
        merge_w_trip = pd.merge(df_yesterday_selected,df_t[['trip_id','service_id']],on='trip_id')
        #Combine trip that selected form yesterday that more than 24 hr.
        combined_df = pd.concat([df, merge_w_trip], ignore_index=True)        
        df = combined_df
    return df

def merge_yesterday_time_for_speed(date):
    df = get_start_end_time(date)
    #select minimum arrival time time (first stop's arrival time) and maximum departure time(last stop's departure time)
    df = df.groupby('trip_id').agg({'start_time':'min','end_time':'max'}).reset_index()
    df_t = getAllTripsPD()
    df_date = pd.to_datetime(date)
    df.loc[:, 'time_diff'] =  df['end_time'] -  df['start_time']
    #minus 1 day so it is yesterday
    datetime_minus_one_day = df_date - pd.Timedelta(days=1)
    datetime_minus_one_day = datetime_minus_one_day.strftime('%Y-%m-%d')
    #Do if yesterday have trip
    if not getStopTimePD(datetime_minus_one_day).empty:
        #get stoptime of yesterday
        df_yesterday = get_start_end_time(datetime_minus_one_day)
        df_yesterday_group = df_yesterday.groupby('trip_id').agg({'start_time':'min','end_time':'max'}).reset_index()
        #select trip that have end time more than 86400
        df_yesterday_selected = df_yesterday_group[(df_yesterday_group['end_time'] > 86400)]
        #if start time less than 86400 mean that trip continuous to today. 
        #start new day with 0.00
        df_yesterday_selected.loc[:, 'time_diff'] = df_yesterday_selected['end_time'] - df_yesterday_selected['start_time']
        df_yesterday_selected.loc[df_yesterday_selected['start_time'] <= 86400, 'start_time'] = 0
        #if start time more than 86400 mean that trip are in today. 
        #example yesterday start 29:00:00 mean that service start at 5:00:00 of today
        #So minus 86400(24:00:00)
        df_yesterday_selected.loc[df_yesterday_selected['start_time'] > 86400, 'start_time'] -= pd.Timedelta(days=1).total_seconds()
        df_yesterday_selected.loc[:, 'end_time'] -= pd.Timedelta(days=1).total_seconds()
        #merge with trip_id to get service id
        merge_w_trip = pd.merge(df_yesterday_selected,df_t[['trip_id','service_id']],on='trip_id')
        #Combine trip that selected form yesterday that more than 24 hr.
        combined_df = pd.concat([df, merge_w_trip], ignore_index=True)        
        df = combined_df
        # print(df)
    return df
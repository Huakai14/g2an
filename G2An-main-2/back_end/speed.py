import math

import numpy as np
from start_end_time import merge_yesterday_time, merge_yesterday_time_for_speed

from data import getShapesPD, getAllStopTimePD, getAllTripsPD
import pandas as pd
from geopy.distance import geodesic

def find_speed(date):
    # Load the GTFS data into Pandas DataFrame
    trips_df = getAllTripsPD()
    stop_time_df = getAllStopTimePD()
    df_st = merge_yesterday_time_for_speed(date)
    shapes_df = getShapesPD()

    #get only 'trip_id','stop_sequence' from all stop_time_df
    stop_time_se_id = stop_time_df[['trip_id','stop_sequence']]

    # Merge relevant data
    df_st_merge = pd.merge(df_st,stop_time_se_id , on='trip_id')
    trips_stop_data = pd.merge(df_st_merge,trips_df , on='trip_id')
    trips_stop_data = pd.merge(trips_stop_data , shapes_df, on='shape_id')

    # Sort by trip and sequence
    trips_stop_data.sort_values(by=['trip_id','stop_sequence'], inplace=True)

    # Convert shape_dist_traveled to numeric
    trips_stop_data['shape_dist_traveled'] = pd.to_numeric(trips_stop_data['shape_dist_traveled'], errors='coerce')

    # Calculate distance traveled between consecutive stops
    distant = trips_stop_data.groupby('trip_id')['shape_dist_traveled'].agg({'max'})

    #get time
    df_st_merge = pd.merge(df_st,distant, on='trip_id')
    df_st_merge.rename(columns={'max': 'distant'}, inplace=True)

    # speed = distant(km) / time use (hour)
    df_st_merge['speed'] =  (df_st_merge['distant']/1000)/((df_st_merge['time_diff'])/3600)
    speed = count_speed(df_st_merge)
    print('Speed: ',speed)
    return speed

def speedForAPI(date):
    return find_speed(date).to_dict(orient='records')

def count_speed(df):
    service_rate = pd.DataFrame()
    service_rate['timestamps'] = range(0,86400,60)
    start_at_mask = (service_rate['timestamps'].values[:, np.newaxis] >= df['start_time'].values)
    end_at_mask = (service_rate['timestamps'].values[:, np.newaxis] <= df['end_time'].values)
    within_range_mask = start_at_mask & end_at_mask
    service_rate['count'] = np.sum(within_range_mask, axis=1)

    speed_values = df['speed'].values[:, np.newaxis].T
    service_rate['min_speed'] = np.min(np.where(within_range_mask, speed_values, np.inf), axis=1)
    service_rate['max_speed'] = np.max(np.where(within_range_mask, speed_values, -np.inf), axis=1)
    service_rate['sum_speed'] = np.sum(np.where(within_range_mask, speed_values, 0), axis=1)
    service_rate['speed_mean'] = service_rate['sum_speed'] / service_rate['count']
    service_rate.fillna(0,inplace=True)

    # #find min max mean of service rate in 1 hour
    service_rate_hour = pd.DataFrame()
    service_rate_hour['min_speed'] = service_rate['min_speed']
    service_rate_hour['max_speed'] = service_rate['max_speed']
    service_rate_hour['mean_speed'] = service_rate['speed_mean']
    service_rate_hour['timestamps'] = pd.to_datetime(service_rate['timestamps'], unit='s')
    service_rate_hour['hour'] = service_rate_hour['timestamps'].dt.hour
    service_rate_hour = service_rate_hour.groupby('hour').agg({'min_speed':'min','mean_speed':'max' ,'max_speed':'max'}).reset_index()
    return service_rate_hour
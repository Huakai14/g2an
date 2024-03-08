import numpy as np
import pandas as pd
from start_end_time import merge_yesterday

def headway(date):
    #deploy pandas dataframe with full row
    # pd.set_option('display.max_rows', None)
    headway = pd.DataFrame()
    stop_time_df = merge_yesterday(date)
    headway = findHeadway(stop_time_df)
    print('Headway: ',headway)
    return headway

def headwayForAPI(date):
    return headway(date).to_dict(orient='records')


def findHeadway(df):
    service_rate = pd.DataFrame()
    headway_df = df
    sorted_df = headway_df[['stop_id','trip_id','start_time','end_time']]
    sorted_df = sorted_df.sort_values(by=['stop_id','start_time'], ascending=[False,True])
    sorted_df['prev_end_time'] = sorted_df.groupby('stop_id')['end_time'].shift(1)
    sorted_df['headway'] = sorted_df['start_time'] - sorted_df['prev_end_time']
    # print(sorted_df)
    headway = sorted_df.groupby('stop_id').agg({'headway':'sum','start_time':'min','end_time':'max'})
    # print(headway)
    service_rate['timestamps'] = range(0,86400,60)
    start_at_mask = (service_rate['timestamps'].values[:,np.newaxis] >= headway['start_time'].values)
    end_at_mask = (service_rate['timestamps'].values[:,np.newaxis] <= headway['end_time'].values)
    within_range_mask = start_at_mask & end_at_mask
    # service_rate['count'] = np.sum(within_range_mask, axis=1)

    headway_values = headway['headway'].values[:, np.newaxis].T
    service_rate['min_headway'] = np.min(np.where(within_range_mask, headway_values, np.inf), axis=1)
    service_rate['max_headway'] = np.max(np.where(within_range_mask, headway_values, -np.inf), axis=1)
    # service_rate['sum_headway'] = np.sum(np.where(within_range_mask, headway_values, 0), axis=1)
    # service_rate['mean_headway'] = service_rate['sum_headway'] / service_rate['count']
    
    # #find min max mean of service rate in 1 hour
    service_rate_hour = pd.DataFrame()
    service_rate_hour['min_headway'] = service_rate['min_headway']
    service_rate_hour['max_headway'] = service_rate['max_headway']
    # service_rate_hour['mean_headway'] = service_rate['mean_headway']/3600
    service_rate_hour['timestamps'] = pd.to_datetime(service_rate['timestamps'], unit='s')
    service_rate_hour['hour'] = service_rate_hour['timestamps'].dt.hour
    service_rate_hour = service_rate_hour.groupby('hour').agg({'min_headway':'min' ,'max_headway':'max'}).reset_index()
    return service_rate_hour


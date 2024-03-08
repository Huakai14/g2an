import numpy as np
import pandas as pd
from start_end_time import merge_yesterday_time

def servicesRate(date):
    #deploy pandas dataframe with full row
    service_rate = pd.DataFrame()
    df_st_group = merge_yesterday_time(date)
    #calculate service rate ---------------------------------------------
    service_rate = count_service(df_st_group)
    print('service_rate: ',service_rate)
    return service_rate

def servicesRateForApi(date):
    return servicesRate(date).to_dict(orient='records')


def count_service(df):
    service_rate = pd.DataFrame()
    service_rate['timestamps'] = range(0, 86400, 60)
    start_at_mask = (service_rate['timestamps'].values[:, np.newaxis] >= df['start_time'].values)
    end_at_mask = (service_rate['timestamps'].values[:, np.newaxis] <= df['end_time'].values)
    service_rate['count'] = np.sum(start_at_mask & end_at_mask, axis=1)
    
    # Find min max mean of service rate in 1 hour
    service_rate_hour = pd.DataFrame()
    service_rate_hour['count'] = service_rate['count']
    service_rate_hour['timestamps'] = pd.to_datetime(service_rate['timestamps'], unit='s')
    service_rate_hour['hour'] = service_rate_hour['timestamps'].dt.hour
    service_rate_hour = service_rate_hour.groupby('hour')['count'].agg(['min', 'mean', 'max']).reset_index()
    return service_rate_hour

# servicesRate('2022-08-30')
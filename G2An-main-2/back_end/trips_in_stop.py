import pandas as pd
from data import getStopPD, getStopTimePD, getTripsPD
from io import StringIO
def find_trip_ids_for_stop(date):
    df_s = getStopPD()
    df_t = getTripsPD(date)
    df_st = getStopTimePD(date)

    merged_data = pd.merge(df_st, df_s, on='stop_id')
    merged_data = pd.merge(merged_data, df_t, on='trip_id')
    merged_data = merged_data.drop_duplicates()

    num_trip = merged_data.groupby('stop_id').size().reset_index(name='service')
    result = pd.merge(num_trip,df_s, on ='stop_id')
    result = result[['stop_code','stop_name','service']]
    result = result.sort_values(by='service',ascending=False)
    print('find_trip_ids_for_stop: ',result)
    return result

def find_trip_ids_for_stopForAPI(date):
    return find_trip_ids_for_stop(date).to_dict(orient='records')

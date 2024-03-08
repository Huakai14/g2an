import pandas as pd
from data import getStopPD, getStopTimePD, getTripsPD
from io import StringIO
def stop_in_trip(date):
    # Create a DataFrame
    df_s = getStopPD()
    df_t = getTripsPD(date)
    df_st = getStopTimePD(date)
    
    merged_data = pd.merge(df_st, df_s, on='stop_id')
    merged_data = pd.merge(merged_data, df_t, on='trip_id')
    merged_data = merged_data.drop_duplicates()

    # result = merged_data.groupby('trip_headsign').agg({'stop_id': 'unique','stop_name': 'unique', 'arrival_time': 'unique'})
    result = merged_data.groupby('trip_id').agg({'trip_headsign':'first','stop_id': 'unique','stop_name': 'unique', 'arrival_time': 'unique'})
    print('Stop_in_trip: ',result)
    return result

def stop_in_tripForAPI(date):
    data = stop_in_trip(date)
    records = []
    for trip_headsign, row in data.iterrows():
        record = {
            'trip_headsign': trip_headsign,
            'stop_id': row['stop_id'].tolist(),
            'stop_name': row['stop_name'].tolist(),
            'arrival_time': row['arrival_time'].tolist()
        }
        records.append(record)
    return records

import pandas as pd
from data import  getRoutePD, getStopTimePD, getTripsPD
from io import StringIO
def routes_in_trip(date):
    df_r = getRoutePD()
    df_t = getTripsPD(date)
    merged_data = pd.merge(df_t, df_r, on='route_id')
    merged_data = merged_data.drop_duplicates()
    num_trip = merged_data.groupby('trip_headsign').agg({'route_id': 'unique', 'route_long_name': 'unique'})
    print('routes_in_trip: ',num_trip)
    # for trip_headsigns, data in num_trip.iterrows():
    #     route_id = data['route_id']
    #     route_name = data['route_long_name']
    #     print("Trip Headsigns:", trip_headsigns)
    #     print("Route Name:", route_name)
    #     print("Route ID:",route_id )
    #     print("------------------------------")
    return num_trip

def routes_in_tripForAPI(date):
    data = routes_in_trip(date)
    records = []
    for trip_headsign, row in data.iterrows():
        record = {
            'trip_headsign': trip_headsign,
            'route_id': row['route_id'].tolist(),
            'route_long_name': row['route_long_name'].tolist()
        }
        records.append(record)
    print(records)
    return records

# def routes_in_tripForAPI(date):
#     return routes_in_trip(date).to_dict(orient='records')

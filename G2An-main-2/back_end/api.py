
from fastapi import FastAPI,HTTPException
from relation_stop_trip import stop_in_tripForAPI
from route_in_trip import routes_in_tripForAPI
from headway import headwayForAPI
from service_rate import servicesRateForApi
from speed import speedForAPI
from trips_in_stop import find_trip_ids_for_stopForAPI
from calendars import calendarCheck
from calendar_date import calendar_datesCheck
from routes import routesCheck
from stops import stopsCheck
from stop_times import stop_timesCheck
from trip import tripsCheck
from agency import agencyCheck
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI()

# Allow requests 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

date = '2022-09-30'

@app.get("/")
async def root():
    if calendar_datesCheck() or calendarCheck() or routesCheck() or agencyCheck() or tripsCheck() or stop_timesCheck() or stopsCheck() != []:
        raise HTTPException(status_code=404, detail={"calendar": calendarCheck(),
            "calendar_date": calendar_datesCheck(),
            "route": routesCheck(),
            "agency": agencyCheck(),
            "trip": tripsCheck(),
            "stop": stopsCheck(),
            "stop_time": stop_timesCheck()})
    return {"message": "You have all required files."}

# @app.get("/analyst")
# async def getData():
#     return {"service_rate" : servicesRateForApi(date),
#             "speed":speedForAPI(date),
#             "headway":headwayForAPI(date),
#             "service_in_stop":find_trip_ids_for_stopForAPI(date),
#             "route_in_trip":routes_in_tripForAPI(date),
#             "relation_ST_arrival":stop_in_tripForAPI(date),
#             "relation_ST_headway":"relation_of_stop_and_trips_headway"
#             }

@app.get("/service_rate")
async def getData():
    return {"service_rate" : servicesRateForApi(date)}

@app.get("/speed")
async def getData():
    return {"speed":speedForAPI(date)}

@app.get("/headway")
async def getData():
    return {"headway":headwayForAPI(date)}

@app.get("/service_in_stop")
async def getData():
    return {"service_in_stop":find_trip_ids_for_stopForAPI(date)}

@app.get("/route_in_trip")
async def getData():
    return {"route_in_trip":routes_in_tripForAPI(date)}

@app.get("/relation_ST_arrival")
async def getData():
    return {"relation_ST_arrival":stop_in_tripForAPI(date)}

@app.get("/relation_ST_headway")
async def getData():
    return {"relation_ST_headway":"relation_of_stop_and_trips_headway"}







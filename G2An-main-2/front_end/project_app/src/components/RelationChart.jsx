import React, { useState, useEffect } from 'react';

const RelationChart = () => {
  const [routeInTripData, setRouteInTripData] = useState([]);
  const BASE_URL = process.env.REACT_APP_BASE_URL;

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`${BASE_URL}/route_in_trip`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setRouteInTripData(data.route_in_trip);
      } catch (error) {
        console.error("Fetching data failed", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <table className='table-fixed border-collapse border border-gray-300'>
        <thead>
          <tr>
            <th className="text-left border border-gray-300 p-2">Trip Headsign</th>
            <th className="text-left border border-gray-300 p-2">Number of Trips</th>
            <th className="text-left border border-gray-300 p-2">Route Long Names</th>
          </tr>
        </thead>
        <tbody>
          {routeInTripData.map((item, index) => (
            <tr key={index}>
              <td className="border border-gray-300 p-2">{item.trip_headsign}</td>
              <td className="border border-gray-300 p-2">{item.num_trips}</td>
              <td className="border border-gray-300 p-2">{item.route_long_name.join(', ')}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default RelationChart
import React, { useState, useEffect } from 'react';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
  );
  

const ServiceDataChart = () => {
    const [serviceRateData, setServiceRateData] = useState([]);
    const BASE_URL = process.env.REACT_APP_BASE_URL;
    useEffect(() => {
        // Define the function to fetch data
        const fetchData = async () => {
          try {
            const response = await fetch(`${BASE_URL}/service_rate`);
            if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            setServiceRateData(data.service_rate); // Update state with fetched data
          } catch (error) {
            console.error("Fetching data failed", error);
          }
        };
    
        // Call the fetchData function
        fetchData();
      }, []);
      const serviceData = {
        labels: serviceRateData?.map(entry => entry?.hour.toString()), // Use the 'year' property for labels
        datasets: [
          {
            label: 'min',
            data: serviceRateData?.map(entry => entry?.min), // Use 'mean' for data points
            borderColor: 'rgb(75, 192, 192)',
            backgroundColor: 'rgba(75, 192, 192, 0.5)',
          },
          {
            label: 'avg',
            data: serviceRateData?.map(entry => entry?.mean), // Use 'mean' for data points
            borderColor: 'rgb(255, 0, 0)',
            backgroundColor: 'rgba(255, 0, 0, 0.5)',
          },
          {
            label: 'max',
            data: serviceRateData?.map(entry => entry?.max), // Use 'mean' for data points
            borderColor: 'rgb(255, 255, 0)',
            backgroundColor: 'rgba(255, 255, 0, 0.5)',
          }
        ]
      };
      // Define options for the Line chart
      const options = {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      };    
  return (
    <div className='' style={{ width: '1200px', height: '300px' }}>
        <Bar data={serviceData} options={options} />
    </div>
  )
}

export default ServiceDataChart
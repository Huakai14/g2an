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
  

const Headway = () => {
    const [headwayData, setHeadwayData] = useState([]);
    const BASE_URL = import.meta.env.BASE_URL;
    
    useEffect(() => {
        const fetchData = async () => {
          try {
            const response = await fetch(`${BASE_URL}/analyst`);
            if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            setHeadwayData(data.service_rate); // Update state with fetched data
          } catch (error) {
            console.error("Fetching data failed", error);
          }
        };
    
        // Call the fetchData function
        fetchData();
      }, []);
      const headwaychartData = {
        labels: headwayData?.map(entry => entry?.hour.toString()), // Use the 'year' property for labels
        datasets: [
          {
            label: 'min',
            data: headwayData?.map(entry => entry?.min), // Use 'mean' for data points
            borderColor: 'rgb(75, 192, 192)',
            backgroundColor: 'rgba(75, 192, 192, 0.5)',
          },
          {
            label: 'avg',
            data: headwayData?.map(entry => entry?.mean), // Use 'mean' for data points
            borderColor: 'rgb(255, 0, 0)',
            backgroundColor: 'rgba(255, 0, 0, 0.5)',
          },
          {
            label: 'avg',
            data: headwayData?.map(entry => entry?.max), // Use 'mean' for data points
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
    <>
        <Bar data={headwaychartData} options={options} />
    </>
  )
}

export default Headway
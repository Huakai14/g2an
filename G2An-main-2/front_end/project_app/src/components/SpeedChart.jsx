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
  

const SpeedChart = () => {
    const BASE_URL = process.env.REACT_APP_BASE_URL;
    const [speedData, setSpeedData] = useState([]);
    useEffect(() => {
        // Define the function to fetch data
        const fetchData = async () => {
          try {
            const response = await fetch(`${BASE_URL}/`);
            if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            setSpeedData(data.speed); // Update state with fetched data
          } catch (error) {
            console.error("Fetching data failed", error);
          }
        };
    
        // Call the fetchData function
        fetchData();
      }, []);
      const speedChartData = {
        labels: speedData?.map(entry => entry?.hour.toString()), // Use the 'year' property for labels
        datasets: [
          {
            label: 'min',
            data: speedData?.map(entry => entry?.min_speed), // Use 'mean' for data points
            borderColor: 'rgb(75, 192, 192)',
            backgroundColor: 'rgba(75, 192, 192, 0.5)',
          },
          {
            label: 'avg',
            data: speedData?.map(entry => entry?.mean_speed), // Use 'mean' for data points
            borderColor: 'rgb(255, 0, 0)',
            backgroundColor: 'rgba(255, 0, 0, 0.5)',
          },
          {
            label: 'max',
            data: speedData?.map(entry => entry?.max_speed), // Use 'mean' for data points
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
        <Bar data={speedChartData} options={options} />
    </>
  )
}

export default SpeedChart
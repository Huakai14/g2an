import React, { useState, useEffect } from 'react';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement,PointElement,LineElement, Title, Tooltip, Legend } from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const ServiceInStopChart = () => {
  const [serviceInStopData, setServiceInStopData] = useState([]);
  const BASE_URL = process.env.REACT_APP_BASE_URL;
    

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(`${BASE_URL}/service_in_stop`);
      const data = await response.json();
      setServiceInStopData(data.service_in_stop);
    };

    fetchData();
  }, []);

  const chartData = {
    labels: serviceInStopData.map(item => item.stop_code), // x-axis labels from stop_code
    datasets: [
      {
        type: 'bar',
        label: 'Service in Stop - Bar',
        data: serviceInStopData.map(item => item.service), // y-axis data from service
        backgroundColor: 'rgba(255, 206, 86, 0.5)', // Yellow background
        borderColor: 'rgb(255, 206, 86)', // Yellow border
        borderWidth: 1,
      },
      {
        type: 'line',
        label: 'Service in Stop - Line',
        data: serviceInStopData.map(item => item.service), // y-axis data from service
        backgroundColor: 'rgba(54, 162, 235, 0.5)', // Blue background
        borderColor: 'rgb(54, 162, 235)', // Blue border
        borderWidth: 1,
        fill: false, // Don’t fill under the line
      }
    ]
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        display: false, // Set true if you want to show the legend
      },
      title: {
        display: true,
        text: 'Service in Stop',
      },
    },
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Service',
        },
      },
      x: {
        title: {
          display: true,
          text: 'Stop Code',
        },
      },
    },
  };

  return <Bar options={options} data={chartData} />;
};

export default ServiceInStopChart;

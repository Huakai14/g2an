import React, { useState, useEffect } from 'react';

const Sidebar = ({ isServicerate, onToggleServicerate,isSpeed,onToggleSpeed,isHeadway,onToggleHeadway,isServicein,onToggleServicein,isRelation,onToggleRelation }) => {
    const [selectedDate, setSelectedDate] = useState(''); // State to store the selected date
    const [minDate, setMinDate] = useState('');
    const [maxDate, setMaxDate] = useState('');

    // Function to update the selected date
    const handleDateChange = (event) => {
      setSelectedDate(event.target.value);
      if(isSpeed){
        onToggleSpeed(false);
      }
      if(isServicerate){
        onToggleServicerate(false);
      }
      if(isHeadway){
        onToggleHeadway(false);
      }
      if(isServicein){
        onToggleServicein(false);
      }
      if(isRelation){
        onToggleRelation(false);
      }
    };

    useEffect(() => {
      const fetchDateRange = async () => {
          try {
              const response = await fetch('http://127.0.0.1:8000/range_date');
              if (!response.ok) {
                  throw new Error(`HTTP error! status: ${response.status}`);
              }
              const data = await response.json();
              setMinDate(data.range_date.start_date);
              setMaxDate(data.range_date.end_date);
          } catch (error) {
              console.error("Error fetching date range:", error);
          }
      };

      fetchDateRange();
  }, []);
  
    // useEffect hook to submit the date to your API when selectedDate changes
    useEffect(() => {
      const submitDate = async () => {
        if (selectedDate) { // Check if selectedDate is not empty
          try {
            const response = await fetch('http://127.0.0.1:8000/time', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({ date: selectedDate }),
            });
  
            if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
            }
  
            const data = await response.json();
            alert("Date submitted successfully!");
            console.log(data);
          } catch (error) {
            console.error("Error submitting date:", error);
          }
        }
      };
  
      submitDate();
    }, [selectedDate]);
    return (
    <div className="w-[240px] flex flex-col">
                    <input
                        type="date"
                        value={selectedDate}
                        onChange={handleDateChange}
                        min={minDate}
                        max={maxDate}
                        className="mt-8 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-2 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    />
                    <div className="mt-10 bg-white shadow-2xl rounded-lg pb-40">
                        <div className="bg-green-gradient text-white flex items-center justify-center text-lg font-bold py-5 rounded-tl-lg rounded-tr-lg">
                            <p>- select data -</p>
                        </div>
                        <div className="flex justify-between px-6 py-2">
                            <p>service rate</p>
                            <label className="inline-flex items-center cursor-pointer">
                                <input 
                                    type="checkbox" value="" className="sr-only peer" checked={isServicerate} onChange={onToggleServicerate}/>
                                <div className="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-customGreen"></div>
                            </label>
                        </div>
                        <div className="flex justify-between px-6 py-2">
                            <p>speed</p>
                            <label className="inline-flex items-center cursor-pointer">
                                <input type="checkbox" value="" className="sr-only peer" checked={isSpeed} onChange={onToggleSpeed}/>
                                <div className="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-customGreen"></div>
                            </label>
                        </div>
                        <div className="flex justify-between px-6 py-2">
                            <p>headway</p>
                            <label className="inline-flex items-center cursor-pointer">
                                <input type="checkbox" value="" className="sr-only peer" checked={isHeadway} onChange={onToggleHeadway}/>
                                <div className="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-customGreen"></div>
                            </label>
                        </div>
                        <div className="flex justify-between px-6 py-2">
                            <p>services in stop</p>
                            <label className="inline-flex items-center cursor-pointer">
                                <input type="checkbox" value="" className="sr-only peer" checked={isServicein} onChange={onToggleServicein}/>
                                <div className="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-customGreen"></div>
                            </label>
                        </div>
                        <div className="flex justify-between px-6 py-2">
                            <p>relation between stops and routes</p>
                            <label className="inline-flex items-center cursor-pointer">
                                <input type="checkbox" value="" className="sr-only peer" checked={isRelation} onChange={onToggleRelation}/>
                                <div className="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-customGreen"></div>
                            </label>
                        </div>
                    </div>
                </div>
  )
}

export default Sidebar
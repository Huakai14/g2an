import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import world from './world.svg';
const G2AnUpload = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const navigate = useNavigate(); // Initialize useNavigate hook

    // Function to handle file selection
    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]); // Update the state with the selected file
    };

    useEffect(() => {
        // Function to upload the file
        const uploadFile = async () => {
        if (selectedFile) {
            const formData = new FormData();
            formData.append('file', selectedFile); // Append the selected file to the form data

            try {
            const response = await fetch('http://127.0.0.1:8000/', {
                method: 'POST',
                body: formData, // Send the form data
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            // File uploaded successfully, navigate to /summary
            alert("File uploaded successfully");
            navigate('/summary');
            } catch (error) {
                console.error("Error uploading file:", error);
                alert("Error uploading file: " + error.message);
            }
        }
        };

        uploadFile();
    }, [selectedFile, navigate]);
    
  return (
    <section className='flex h-screen w-screen'>
        <div className="w-1/2 bg-cover bg-center" style={{ backgroundImage: `url('${world}')` }}></div>
        <div className="w-1/2 bg-white">
            <div className="m-4 sm:m-8 md:m-16 lg:m-24">
                <h1 className="text-teal-500 text-8xl font-bold mb-9">G2An</h1>
                <p className="text-cyan-700 text-lg">Online application for transit performance</p>
                <p className="text-cyan-700 text-lg">analysis from GTPS data</p>
                <div className= "flex mt-3">
                    <div className='bg-customBlue text-white px-2 rounded-lg mr-3'>
                        <p>agency.txt</p>
                    </div>
                    <div className='bg-customBlue text-white px-2 rounded-lg mr-3'>
                        <p>stops.txt</p>
                    </div>
                    <div className='bg-customBlue text-white px-2 rounded-lg mr-3'>
                        <p>routes.txt</p>
                    </div>
                    <div className='bg-customBlue text-white px-2 rounded-lg mr-3'>
                        <p>trips.txt</p>
                    </div>
                    <div className='bg-customBlue text-white px-2 rounded-lg mr-3'>
                        <p>stop_times.txt</p>
                    </div>
                </div>
                <div className="flex mt-2">
                    <div className='bg-customBlue text-white px-2 rounded-lg mr-3'>
                        <p>shapes.txt</p>
                    </div>
                    <div className='bg-customBlue text-white px-2 rounded-lg mr-3'>
                        <p>calendar.txt or calendar_dates.txt or both</p>
                    </div>
                </div>
                <p className='my-5 text-gray-500 underline'>more details about GTFS dataset</p>
                <div className="border bg-gray-200 text-center shadow-lg rounded-lg">
                    <p className='mt-8'>Let's get started on G2An</p>
                    <p className='mb-8'>upload your GTFS data</p>
                    <label for="uploadFile1"
                        className="bg-teal-500 hover:bg-teal-700 text-white text-sm px-4 py-2.5 outline-none rounded w-max cursor-pointer mx-auto block font-[sans-serif]">
                        <svg xmlns="http://www.w3.org/2000/svg" className="w-5 mr-2 fill-white inline" viewBox="0 0 32 32">
                            <path
                            d="M23.75 11.044a7.99 7.99 0 0 0-15.5-.009A8 8 0 0 0 9 27h3a1 1 0 0 0 0-2H9a6 6 0 0 1-.035-12 1.038 1.038 0 0 0 1.1-.854 5.991 5.991 0 0 1 11.862 0A1.08 1.08 0 0 0 23 13a6 6 0 0 1 0 12h-3a1 1 0 0 0 0 2h3a8 8 0 0 0 .75-15.956z"
                            data-original="#000000" />
                            <path
                            d="M20.293 19.707a1 1 0 0 0 1.414-1.414l-5-5a1 1 0 0 0-1.414 0l-5 5a1 1 0 0 0 1.414 1.414L15 16.414V29a1 1 0 0 0 2 0V16.414z"
                            data-original="#000000" />
                        </svg>
                            Choose file to Upload
                        <input type="file" id='uploadFile1' className="hidden" accept=".zip" onChange={handleFileChange}/>
                    </label>
                    <div className="flex items-center py-8">
                        <div className="flex-grow flex justify-end">
                            <div className="w-1/2 border-t border-teal-500"></div>
                        </div>
                        <p className="px-4 text-teal-500">or select from our list</p>
                        <div className="flex-grow">
                            <div className="w-1/2 border-t border-teal-500"></div>
                        </div>
                    </div>
                    <select id="countries" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-1/2 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 mx-auto mb-16">
                        <option selected>Select sample GTPS data</option>
                        <option value="1">select 1</option>
                        <option value="2">select 2</option>
                        <option value="3">select 3</option>
                        <option value="4">select 4</option>
                    </select>
                </div>
            </div>
        </div>
    </section>
  )
}

export default G2AnUpload
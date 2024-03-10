import React, { useState, useRef } from 'react';
import html2canvas from 'html2canvas';
import jsPDF from 'jspdf';
import Navbar from '../components/Navbar'
import Sidebar from '../components/sidebar'
import ServiceDataChart from '../components/ServiceDataChart';
import ServiceInStopChart from '../components/ServiceInStopChart';
import SpeedChart from '../components/SpeedChart';
import Headway from '../components/Headway';
import RelationChart from '../components/RelationChart';

const Summary = () => {

  const [isServicerate, setIsServicerate] = useState(false);
  const toggleServicerate = () => {
    setIsServicerate(!isServicerate);
  };
  const [isSpeed, setIsSpeed] = useState(false);
  const toggleSpeed = () => {
    setIsSpeed(!isSpeed);
  };
  const [isHeadway, setIsHeadway] = useState(false);
  const toggleHeadway = () => {
    setIsHeadway(!isHeadway);
  };
  const [isServicein, setIsServicein] = useState(false);
  const toggleServicein = () => {
    setIsServicein(!isServicein);
  };
  const [isRelation, setIsRelation] = useState(false);
  const toggleRelation = () => {
    setIsRelation(!isRelation);
  };
  const [isGeneratingPdf, setIsGeneratingPdf] = useState(false);
  const componentRef = useRef();
  const delay = ms => new Promise(resolve => setTimeout(resolve, ms));
  const downloadPdfDocument = async () => {
    setIsGeneratingPdf(true); // Disable shadow before capturing

    await delay(100);
    const input = componentRef.current; // Reference to the component you want to download as PDF
    html2canvas(input).then((canvas) => {
      const imgData = canvas.toDataURL('image/png');
  
      // Determine the dimensions of the PDF based on the canvas size
      let pdfWidth = canvas.width;
      let pdfHeight = canvas.height;
  
      // Create a PDF with the dimensions of the canvas, converting from pixels to mm
      const pdf = new jsPDF({
        orientation: pdfWidth > pdfHeight ? "landscape" : "portrait",
        unit: "px",
        format: [pdfWidth, pdfHeight]
      });
  
      // Add the canvas image data to the PDF
      pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
  
      // Save the PDF
      pdf.save("download.pdf");

      setIsGeneratingPdf(false); // Re-enable shadow after capturing
    });
  };


  
  return (
    <div style={{ backgroundColor: '#F5F5F5' }}>
        <Navbar />
        <div className="flex flex-col min-h-screen">
            <div className="flex-grow flex min-h-[727px] ml-16">
                <Sidebar 
                  isServicerate={isServicerate} 
                  onToggleServicerate={toggleServicerate} 
                  isSpeed={isSpeed} 
                  onToggleSpeed={toggleSpeed} 
                  isHeadway={isHeadway} 
                  onToggleHeadway={toggleHeadway} 
                  isServicein={isServicein} 
                  onToggleServicein={toggleServicein} 
                  isRelation={isRelation} 
                  onToggleRelation={toggleRelation} 
                />
                <div className="mt-8 mx-16 w-full flex flex-col">
                <div ref={componentRef} className={`bg-white rounded-lg ${!isGeneratingPdf ? 'shadow-2xl' : ''}`}>
                        <div className="m-5">
                        {isServicerate && (
                            <div className="text-base font-bold">
                                <p>Service rate</p>
                                <div className="flex justify-center items-center max-h-[500px]">
                                  <ServiceDataChart />
                                </div>
                            </div>
                        )}
                        {isSpeed && (
                            <div className="text-base font-bold mt-8">
                              <p>Speed</p>
                              <div className="flex justify-center items-center max-h-[500px]">
                                <SpeedChart />
                              </div>
                            </div>
                        )}
                        {isHeadway && (
                            <div className="text-base font-bold mt-8">
                              <p>Headway</p>
                              <div className="flex justify-center items-center min-h-[500px]">
                                <Headway />
                              </div>
                            </div>
                        )}
                        {isServicein && (
                            <div className="text-base font-bold mt-8">
                              <p>services in stop</p>
                              <div className="flex justify-center items-center min-h-[500px]">
                                <ServiceInStopChart />
                              </div>
                            </div>
                        )}
                        {isRelation && (
                            <div>
                              <p className="text-base font-bold mt-8">relation between stops and routes</p>
                              <div className="flex justify-center items-center min-h-[500px]">
                                <RelationChart />
                              </div>
                            </div>
                        )}
                        </div>
                    </div>
                    <div className="flex justify-end">
                        <button onClick={downloadPdfDocument} className="bg-customGreen hover:bg-customGreen text-white font-bold py-2 px-4 text-sm rounded my-5">
                          Export to PDF
                        </button>
                    </div>
                    
                </div>

            </div>
            
        </div>
    </div>
  )
}

export default Summary
import React from 'react'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import G2anUpload from './page/g2an_upload'; // Import HomePage
import Summary from './page/Summary';
function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<G2anUpload />} />
          <Route path="/summary" element={<Summary />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
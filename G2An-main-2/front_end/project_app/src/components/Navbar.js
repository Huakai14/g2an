import React from 'react'
import Logo from './logo.svg'
const Navbar = () => {
  return (
    <nav className='bg-customBlue h-16 text-customGreen flex items-center'>
        <div className='flex items-center text-center ml-5'>
            <img src={Logo} alt="Logo" className="h-8 w-8 mr-2" /> 
            <h2 className='font-bold text-xl'>G2An</h2>
        </div>
    </nav>
  )
}

export default Navbar
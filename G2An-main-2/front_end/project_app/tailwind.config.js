/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        customBlue: '#1B3254',
        customGreen: '#27B3AA',
      },
      backgroundImage: {
        'green-gradient': 'linear-gradient(225deg, #27B3AA 3.26%, #418A69 100%)',
      },
    },
  },
  plugins: [],
}


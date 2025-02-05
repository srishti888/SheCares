// import React from "react"; 
// import { useEffect, useState } from "react";
// import Rectangle from './assets/Rectangle 10.svg'
// import Card from './card'
// import Auth from './Auth'
// import axios from "axios";

// function App() {
//   const [message, setMessage] = useState("");
//   const [email, setEmail] = useState('')
//   const [password, setPassword] = useState('')

//   useEffect(() => {
//     axios.get("http://127.0.0.1:8000/sCApp/hello/")
//       .then(response => setMessage(response.data.message))
//       .catch(error => console.error("Error fetching data:", error));
//   }, []);

//   return (
//     <>
//     <div>
//      <img src={Rectangle} alt="" />
//      <h1>{message}</h1>
//      <Card />
//      <Auth />
//     </div> 
    
//     </>
//   );
// }

// export default App;

// src/App.jsx
import React from 'react';

const App = () => {
  return (
    <div>
      <h1>Hello, World!</h1>
    </div>
  );
};

export default App;

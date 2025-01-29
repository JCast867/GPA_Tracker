// import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/items/') // Replace with your Django API endpoint
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Data from Django Backend</h1>
      <ul>
        {data.map(item => (
          <li key={item.id}>{item.name}</li> // Adjust based on your Django model
        ))}
      </ul>
    </div>
  );
}

export default App;

import './App.css';
import React, { useState } from 'react';
import Products from './products';

function Main() {
  const [search, setSearch] = useState('');
  const [data, setData] = useState([]);
  const YOUR_APP_ID = "539392ab";
  const YOUR_APP_KEY = "ae2b076670edcadb0e551d97049a7b4c";

  const submitHandler = (e) => {
    e.preventDefault();
    fetch(
      `https://api.edamam.com/search?q=${search}&app_id=${YOUR_APP_ID}&app_key=${YOUR_APP_KEY}&from=0&to=12&calories=591-722&health=alcohol-free`
    )
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((responseData) => {
        setData(responseData.hits);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  };
  return (
    
    <div className="Main" > {}

      
      <form onSubmit={submitHandler} className='f1'>
        <input type="text" value={search} placeholder='Enter a Item' onChange={(e) => setSearch(e.target.value)} />
        &nbsp;&nbsp;&nbsp;&nbsp;
        <input type="submit" id="btn" className="btn btn-primary" value="Search" />
        <br />
      </form>
      {data.length >= 1 ? <Products data={data} /> : null}
    </div>
    
  );
}

export default Main;
import './App.css';
import React, { useState, useEffect } from 'react';
import Chatbot from '../components/Chatbot/index.js';
import SourceGraph from '../components/Graph/index.js';
/*
Explore the showGraph and showGraph stuff and why it is reinforced so many times within the code. 
What happens if you remove some of its instances and are they all necessary? Esp showGraph && ( when setShpwGraph is already called
*/
function App() {
  const [isMoved, setIsMoved] = useState(false);  // Default position of text box and button is center of screen
  const [showGraph, setShowGraph] = useState(false);  // Graph is hidden on default
  const [numColumns, setNumColumns] = useState(2); // Default to 5 columns
  const [sources, setSources] =  useState([]);
  const [placeholderText, setPlaceholderText] = useState('Enter your text here'); // Starts w/ indication for user entering text and switches to search bar
  const [isSearch, setIsSearch] = useState(false); // State to track if search button is clicked

  const searchButtonClick = () => {
    setShowGraph(true);
    setNumColumns(5);
    setIsMoved(true);
    setPlaceholderText('Enter your search term here'); // Change the placeholder text
    setIsSearch(true); // Change to search mode

    fetchData();

  };

/*  useEffect(() => {
    fetchData();
  }, [])*/

  const fetchData = async () => {
    try {
      console.log("gi")
      const response = await fetch("http://127.0.0.1:5000/");
      
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      console.log("Data fetched:", data);  // Check if data is fetched correctly
      setSources(data.database);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }
  //return (<SourceGraph sources={sources} />);


  
  return (
    <div className="App">
      <header className="App-header">
        <h1>Research Assistant</h1>
      </header>
      <div className="App-body">
        <div className={`search-container ${isMoved ? 'moved' : ''}`}>
          <p>{placeholderText}</p> {/* Update the placeholder text */}
          {isSearch ? (
            <input type="text" placeholder="Search term..." />
          ) : (
            <textarea placeholder="Input here..." rows="4" cols="50" />
          )}
          <button onClick={searchButtonClick}>SEARCH</button>
        </div>
        {showGraph && (
          <div className="additional-content">
            <div className="table-container">
              <SourceGraph sources={sources} />
            </div>
            <Chatbot placeholder="Ask Chatbot something..." buttonText="SUBMIT" />
          </div>
        )}
      </div>
    </div>
  );

}

export default App;

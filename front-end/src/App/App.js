import './App.css';
import React, { useState } from 'react';
import Chatbot from '../components/Chatbot/index.js';
import Graph from '../components/Graph/index.js';

function App() {
  const [isMoved, setIsMoved] = useState(false);  // Default position of text box and button is center of screen
  const [showGraph, setShowGraph] = useState(false);  // Graph is hidden on default
  const [numColumns, setNumColumns] = useState(2); // Default to 5 columns

  const searchButtonClick = () => {
    setShowGraph(true);
    setNumColumns(5);
    setIsMoved(true);


  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Research Assistant</h1>
      </header>
      <div className="App-body">
        <div className={`search-container ${isMoved ? 'moved' : ''}`}>
          <p>Enter your search term here:</p>
          <input type="text" placeholder="Search term..." />
          <button onClick={searchButtonClick}>SEARCH</button>
        </div>
        {showGraph && (
          <div className="additional-content">
            <Graph num_columns={numColumns} />
            <Chatbot placeholder="Ask Chatbot something..." buttonText="SUBMIT" />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;

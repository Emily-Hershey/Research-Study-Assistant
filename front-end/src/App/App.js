import './App.css';
import React, { useState, useEffect } from 'react';
import Chatbot from '../components/Chatbot/index.js';
import SourceGraph from '../components/Graph/index.js';
import axios from 'axios';
import { useQuery } from 'react-query';
import { QueryClient, QueryClientProvider } from 'react-query';
const queryClient = new QueryClient();

/*
Explore the showGraph and showGraph stuff and why it is reinforced so many times within the code. 
What happens if you remove some of its instances and are they all necessary? Esp showGraph && ( when setShpwGraph is already called
*/
function App() {
  const [search, setSearch] = useState('');
  const [input_box, setInput_box] = useState('')
  const [isMoved, setIsMoved] = useState(false);  // Default position of text box and button is center of screen
  const [showGraph, setShowGraph] = useState(false);  // Graph is hidden on default
  const [numColumns, setNumColumns] = useState(2); // Default to 5 columns
  const [sources, setSources] =  useState([]);
  const [placeholderText, setPlaceholderText] = useState('Enter your text here:'); // Starts w/ indication for user entering text and switches to search bar
  const [isSearch, setIsSearch] = useState(false); // State to track if search button is clicked
  const [isButtonVisible, setIsButtonVisible] = useState(true); // State to track if the next page button is visible

  const nextPageButtonClick = () => {
    setShowGraph(true);
    setNumColumns(5);
    setIsMoved(true);
    setPlaceholderText('Enter your search term here:'); // Change the placeholder text
    setIsSearch(true); // Change to search mode
    setIsButtonVisible(false);

  };

  const searchButtonClick = (e) => {
    if (isSearch == true)
      sendSearch(e);
    else
      sendUserInput(e);
  };

  /*  useEffect(() => {
    fetchData();
  }, [])*/

  const sendUserInput = async (e) => {
    console.log('Sending user input...')
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:9000/", 
        {input_box}, 
        {
          headers: {
            'Content-Type': 'application/json'
          }
        });
      

    } catch (error) {
      console.error('There was an error!', error);
    }
  };

  const sendSearch = async (e) => {
    console.log('Sending search...')
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:9000/", 
        {search}, 
        {
          headers: {
            'Content-Type': 'application/json'
          }
        });
      

    } catch (error) {
      console.error('There was an error!', error);
    }
  };

  
  return (
    <QueryClientProvider client={queryClient}>
      <div className="App">
        <header className="App-header">
          <h1>Research Assistant</h1>
        </header>
        <div className="App-body">
          <div className={`search-container ${isMoved ? 'moved' : ''}`}>
            <p>{placeholderText}</p> {/* Update the placeholder text */}
            {isSearch ? (
              <input type="text" value={search} placeholder="Search term..." onChange={(e)=> setSearch(e.target.value)}/>
            ) : (
              <textarea value={input_box} placeholder="Input here text you want summarized or explained by a chatbot. This can be class notes, a document, a letter...." rows="4" cols="50" onChange={(e)=> setInput_box(e.target.value)}/>
            )}
            <div className="button-container">
              <button onClick={searchButtonClick}>SUBMIT</button> 
              {isButtonVisible && (
                <button onClick={nextPageButtonClick}>NEXT PAGE</button>
              )}
            </div>
          </div>
          {showGraph && (
            <div className="additional-content">
              <div className="table-container">
                <SourceGraph />
              </div>
              <Chatbot placeholder="Ask Chatbot something..." buttonText="SUBMIT" />
            </div>
          )}
        </div>
      </div>
    </QueryClientProvider>

  );

}

export default App;

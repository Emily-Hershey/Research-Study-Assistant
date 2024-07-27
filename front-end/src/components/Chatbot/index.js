import React, {useState} from 'react';
import './index.css';
import axios from 'axios';


function Chatbot({ placeholder, buttonText, onButtonClick }) {
  const [question, setQuestion] = useState('');
  const [textareaValue, setTextareaValue] = useState('');

  
  const submitButtonClick = async (e) => {
    console.log('Sending question...')
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:9000/chatbot", 
        {question}, 
        {
          headers: {
            'Content-Type': 'application/json'
          }
        });
      const response2 = await fetch("http://127.0.0.1:9000/chatbot");
      if (!response2.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response2.json();
      if (data)
        setTextareaValue(data.answer);
      

    } catch (error) {
      console.error('There was an error!', error);
    }
    
  };

  return (
    <div className = "chatbot">
      <div className="input-box">
        <input type="text" value={question} placeholder={placeholder} onChange={(e)=> setQuestion(e.target.value)}/>
        <button onClick={submitButtonClick}>{buttonText}</button>
      </div>
      <textarea readOnly value={textareaValue}></textarea>
    </div>
  );
}

export default Chatbot;
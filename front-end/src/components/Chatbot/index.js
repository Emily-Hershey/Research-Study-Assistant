import React from 'react';
import './index.css';

function Chatbot({ placeholder, buttonText, onButtonClick }) {
  return (
    <div className="input-box">
      <input type="text" placeholder={placeholder} />
      <button onClick={onButtonClick}>{buttonText}</button>
    </div>
  );
}

export default Chatbot;
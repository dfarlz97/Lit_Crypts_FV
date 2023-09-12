import React, { useState } from 'react';
import encryption from '../encryption/Encryption';

const Home = () => {
  const [inputText, setInputText] = useState('');

  const handleInputChange = (event) => {
    const text = event.target.value;
    setInputText(text);
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Enter text"
        value={inputText}
        onChange={handleInputChange}
      />
      <h1>Encrypted Text: {encryption(inputText)}</h1>
    </div>
  );
};

export default Home;

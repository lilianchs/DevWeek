import React from 'react';
import './App.css';
import Searchbar from './searchbar';
import Searchbar2 from './searchbar2';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to the Flyer Generation Website</h1>
        <div style={{ marginBottom: '20px' }}>
          <Searchbar />
        </div>
        <div style={{ marginBottom: '20px' }}>
          <Searchbar2 />
        </div>
      </header>
    </div>
  );
}

export default App;

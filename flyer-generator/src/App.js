import React, { useEffect } from 'react';
import './App.css';
import SearchBar from './searchbar';
import SearchBar2 from './searchbar2';

function App() {
  useEffect(() => {
    const container = document.querySelector('.floating-cubes-container');
    const cubeCount = 20; // Number of cubes to create

    const isOutsideCenter = (left, top) => {
      // Define the central area bounds
      const centerLeftStart = 10;
      const centerLeftEnd = 90;
      const centerTopStart = 10;
      const centerTopEnd = 90;
      return !(left > centerLeftStart && left < centerLeftEnd && top > centerTopStart && top < centerTopEnd);
    };

    for (let i = 0; i < cubeCount; i++) {
      const cube = document.createElement('div');
      cube.classList.add('cube');

      let left, top;
      // Ensure cubes are placed outside the central area
      do {
        left = Math.random() * 100;
        top = Math.random() * 100;
      } while (!isOutsideCenter(left, top));

      cube.style.left = `${left}vw`;
      cube.style.top = `${top}vh`;
      cube.style.animationDuration = `${Math.random() * 10 + 5}s`;
      cube.style.animationDelay = `${Math.random() * 5}s`;
      container.appendChild(cube);
    }
  }, []);

  return (
    <div className="App">
      <div className="floating-cubes-container"></div>
      <header className="App-header">
        <h1>Research Guide</h1>
        <div style={{ marginBottom: '20px' }}>
          <SearchBar />
        </div>
        <div style={{ marginBottom: '20px' }}>
          <SearchBar2 />
        </div>
      </header>
    </div>
  );
}

export default App;

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { BookProvider } from './context/BookContext';
import Home from './pages/Home/Home';
import './App.css';

function App() {
  return (
    <BookProvider>
      <Router>
        <div className="App">
          <header className="app-header">
            <h1>📚 Manajer Buku Saya</h1>
            <nav>
              <a href="/">Beranda</a>
            </nav>
          </header>
          
          <main className="app-main">
            <Routes>
              <Route path="/" element={<Home />} />
            </Routes>
          </main>
        </div>
      </Router>
    </BookProvider>
  );
}

export default App;
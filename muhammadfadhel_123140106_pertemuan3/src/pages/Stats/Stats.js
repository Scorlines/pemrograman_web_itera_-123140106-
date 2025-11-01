import React from 'react';
import { useBook } from '../../context/BookContext';
import { useBookStats } from '../../hooks/useBookStats';
import './Stats.css';

const Stats = () => {
  const { state } = useBook();
  const stats = useBookStats(state.books);

  return (
    <div className="stats">
      <h1>Statistik Buku</h1>
      <div className="stats-grid">
        <div className="stat-card">
          <h3>Total Buku</h3>
          <p className="stat-number">{stats.total}</p>
        </div>
        <div className="stat-card">
          <h3>Dimiliki</h3>
          <p className="stat-number">{stats.owned}</p>
          <p className="stat-percentage">{stats.ownedPercentage}%</p>
        </div>
        <div className="stat-card">
          <h3>Sedang Dibaca</h3>
          <p className="stat-number">{stats.reading}</p>
          <p className="stat-percentage">{stats.readingPercentage}%</p>
        </div>
        <div className="stat-card">
          <h3>Ingin Dibeli</h3>
          <p className="stat-number">{stats.wishlist}</p>
          <p className="stat-percentage">{stats.wishlistPercentage}%</p>
        </div>
      </div>
    </div>
  );
};

export default Stats;
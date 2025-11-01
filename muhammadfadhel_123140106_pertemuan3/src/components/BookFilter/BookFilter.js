import React from 'react';
import './BookFilter.css';

const BookFilter = ({ filter, onFilterChange, searchQuery, onSearchChange }) => {
  return (
    <div className="book-filter">
      <div className="filter-group">
        <label>Filter berdasarkan status:</label>
        <select value={filter} onChange={(e) => onFilterChange(e.target.value)}>
          <option value="all">Semua</option>
          <option value="owned">Dimiliki</option>
          <option value="reading">Sedang Dibaca</option>
          <option value="wishlist">Ingin Dibeli</option>
        </select>
      </div>
      <div className="search-group">
        <label>Cari:</label>
        <input
          type="text"
          placeholder="Cari berdasarkan judul atau penulis"
          value={searchQuery}
          onChange={(e) => onSearchChange(e.target.value)}
        />
      </div>
    </div>
  );
};

export default BookFilter;
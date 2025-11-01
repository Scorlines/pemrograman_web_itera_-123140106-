import React from 'react';
import './BookCard.css';

const BookCard = ({ book, onEdit, onDelete }) => {
  const getStatusText = (status) => {
    switch (status) {
      case 'owned': return 'Dimiliki';
      case 'reading': return 'Sedang Dibaca';
      case 'wishlist': return 'Ingin Dibeli';
      default: return status;
    }
  };

  return (
    <div className="book-card">
      <div className="book-info">
        <h3>{book.title}</h3>
        <p>Oleh: {book.author}</p>
        <span className={`status ${book.status}`}>
          {getStatusText(book.status)}
        </span>
      </div>
      <div className="book-actions">
        <button onClick={() => onEdit(book)} className="btn btn-edit">Edit</button>
        <button onClick={() => onDelete(book.id)} className="btn btn-delete">Hapus</button>
      </div>
    </div>
  );
};

export default BookCard;
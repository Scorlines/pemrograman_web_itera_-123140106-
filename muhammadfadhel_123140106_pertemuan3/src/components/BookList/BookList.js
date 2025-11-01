import React from 'react';
import BookCard from '../BookCard/BookCard';
import './BookList.css';

const BookList = ({ books, onEdit, onDelete }) => {
  if (books.length === 0) {
    return <p className="no-books">Tidak ada buku ditemukan.</p>;
  }

  return (
    <div className="book-list">
      {books.map(book => (
        <BookCard
          key={book.id}
          book={book}
          onEdit={onEdit}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
};

export default BookList;
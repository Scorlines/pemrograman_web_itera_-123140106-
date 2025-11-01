import React, { useState } from 'react';
import { useBook } from '../../context/BookContext';
import BookForm from '../../components/BookForm/BookForm';
import BookList from '../../components/BookList/BookList';
import BookFilter from '../../components/BookFilter/BookFilter';
import './Home.css';

const Home = () => {
  const { state, dispatch } = useBook();
  const [editingBook, setEditingBook] = useState(null);

  const { books, filter, searchQuery } = state;

  const handleAddBook = (book) => {
    dispatch({ type: 'ADD_BOOK', payload: book });
  };

  const handleUpdateBook = (book) => {
    dispatch({ type: 'EDIT_BOOK', payload: book });
    setEditingBook(null);
  };

  const handleDeleteBook = (id) => {
    dispatch({ type: 'DELETE_BOOK', payload: id });
  };

  const handleEditBook = (book) => {
    setEditingBook(book);
  };

  const handleCancelEdit = () => {
    setEditingBook(null);
  };

  const handleFilterChange = (filter) => {
    dispatch({ type: 'SET_FILTER', payload: filter });
  };

  const handleSearchChange = (query) => {
    dispatch({ type: 'SET_SEARCH_QUERY', payload: query });
  };

  const filteredBooks = books.filter(book => {
    const matchesFilter = filter === 'all' || book.status === filter;
    const matchesSearch = book.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         book.author.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesFilter && matchesSearch;
  });

  return (
    <div className="home">
      <div className="home-container">
        <aside className="sidebar">
          <BookForm
            onAddBook={handleAddBook}
            editingBook={editingBook}
            onUpdateBook={handleUpdateBook}
            onCancelEdit={handleCancelEdit}
          />
        </aside>
        <main className="main-content">
          <h1>Koleksi Buku Saya</h1>
          <BookFilter
            filter={filter}
            onFilterChange={handleFilterChange}
            searchQuery={searchQuery}
            onSearchChange={handleSearchChange}
          />
          <BookList
            books={filteredBooks}
            onEdit={handleEditBook}
            onDelete={handleDeleteBook}
          />
        </main>
      </div>
    </div>
  );
};

export default Home;
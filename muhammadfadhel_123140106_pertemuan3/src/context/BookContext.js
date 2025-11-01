import React, { createContext, useContext, useReducer, useEffect } from 'react';
import { bookReducer, initialState } from '../reducers/bookReducer';

const BookContext = createContext();

const initializeState = () => {
  const savedBooks = localStorage.getItem('personalBooks');
  if (savedBooks) {
    try {
      const parsedBooks = JSON.parse(savedBooks);
      return {
        ...initialState,
        books: parsedBooks
      };
    } catch (error) {
      console.error('Error loading books from localStorage:', error);
      return initialState;
    }
  }
  return initialState;
};

export const BookProvider = ({ children }) => {
  const [state, dispatch] = useReducer(bookReducer, initialState, initializeState);

  useEffect(() => {
    try {
      localStorage.setItem('personalBooks', JSON.stringify(state.books));
    } catch (error) {
      console.error('Error saving books to localStorage:', error);
    }
  }, [state.books]);

  return (
    <BookContext.Provider value={{ state, dispatch }}>
      {children}
    </BookContext.Provider>
  );
};

export const useBook = () => {
  const context = useContext(BookContext);
  if (!context) {
    throw new Error('useBook must be used within a BookProvider');
  }
  return context;
};
// src/__tests__/BookForm.test.js
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import BookForm from '../components/BookForm/BookForm';

test('renders BookForm and submits with valid data', () => {
  const mockOnAdd = jest.fn();
  render(<BookForm onAddBook={mockOnAdd} />);

  fireEvent.change(screen.getByLabelText(/title/i), {
    target: { value: 'Test Book' }
  });
  fireEvent.change(screen.getByLabelText(/author/i), {
    target: { value: 'Test Author' }
  });
  fireEvent.click(screen.getByText(/add book/i));

  expect(mockOnAdd).toHaveBeenCalledWith({
    title: 'Test Book',
    author: 'Test Author',
    status: 'owned'
  });
});
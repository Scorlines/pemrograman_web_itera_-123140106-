import React, { useState } from 'react';
import './BookForm.css';

const BookForm = ({ onAddBook, editingBook, onUpdateBook, onCancelEdit }) => {
  const [formData, setFormData] = useState(
    editingBook || { title: '', author: '', status: 'owned' }
  );
  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
    if (errors[name]) {
      setErrors(prev => ({ ...prev, [name]: '' }));
    }
  };

  const validate = () => {
    const newErrors = {};
    if (!formData.title.trim()) newErrors.title = 'Judul wajib diisi';
    if (!formData.author.trim()) newErrors.author = 'Penulis wajib diisi';
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validate()) {
      if (editingBook) {
        onUpdateBook(formData);
      } else {
        onAddBook(formData);
        setFormData({ title: '', author: '', status: 'owned' });
      }
      setErrors({});
    }
  };

  return (
    <form onSubmit={handleSubmit} className="book-form">
      <h2>{editingBook ? 'Edit Buku' : 'Tambah Buku Baru'}</h2>
      <div className="form-group">
        <label htmlFor="title">Judul</label>
        <input
          type="text"
          id="title"
          name="title"
          value={formData.title}
          onChange={handleChange}
          className={errors.title ? 'error' : ''}
        />
        {errors.title && <span className="error-text">{errors.title}</span>}
      </div>
      <div className="form-group">
        <label htmlFor="author">Penulis</label>
        <input
          type="text"
          id="author"
          name="author"
          value={formData.author}
          onChange={handleChange}
          className={errors.author ? 'error' : ''}
        />
        {errors.author && <span className="error-text">{errors.author}</span>}
      </div>
      <div className="form-group">
        <label htmlFor="status">Status</label>
        <select
          id="status"
          name="status"
          value={formData.status}
          onChange={handleChange}
        >
          <option value="owned">Dimiliki</option>
          <option value="reading">Sedang Dibaca</option>
          <option value="wishlist">Ingin Dibeli</option>
        </select>
      </div>
      <div className="form-actions">
        <button type="submit" className="btn btn-primary">
          {editingBook ? 'Perbarui Buku' : 'Tambah Buku'}
        </button>
        {editingBook && (
          <button type="button" className="btn btn-secondary" onClick={onCancelEdit}>
            Batal
          </button>
        )}
      </div>
    </form>
  );
};

export default BookForm;
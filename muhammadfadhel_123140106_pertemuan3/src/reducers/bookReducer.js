export const initialState = {
  books: [],
  filter: 'all',
  searchQuery: ''
};

export const bookReducer = (state, action) => {
  switch (action.type) {
    case 'ADD_BOOK':
      return {
        ...state,
        books: [...state.books, { ...action.payload, id: Date.now() }]
      };
    case 'EDIT_BOOK':
      return {
        ...state,
        books: state.books.map(book =>
          book.id === action.payload.id ? action.payload : book
        )
      };
    case 'DELETE_BOOK':
      return {
        ...state,
        books: state.books.filter(book => book.id !== action.payload)
      };
    case 'SET_FILTER':
      return {
        ...state,
        filter: action.payload
      };
    case 'SET_SEARCH_QUERY':
      return {
        ...state,
        searchQuery: action.payload
      };
    case 'LOAD_BOOKS':
      return {
        ...state,
        books: action.payload
      };
    default:
      return state;
  }
};
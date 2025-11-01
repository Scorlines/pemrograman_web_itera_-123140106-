import { useMemo } from 'react';

export const useBookStats = (books) => {
  const stats = useMemo(() => {
    const total = books.length;
    const owned = books.filter(book => book.status === 'owned').length;
    const reading = books.filter(book => book.status === 'reading').length;
    const wishlist = books.filter(book => book.status === 'wishlist').length;

    return {
      total,
      owned,
      reading,
      wishlist,
      ownedPercentage: total ? ((owned / total) * 100).toFixed(1) : 0,
      readingPercentage: total ? ((reading / total) * 100).toFixed(1) : 0,
      wishlistPercentage: total ? ((wishlist / total) * 100).toFixed(1) : 0
    };
  }, [books]);

  return stats;
};
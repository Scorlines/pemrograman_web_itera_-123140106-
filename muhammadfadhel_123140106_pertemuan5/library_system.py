from abc import ABC, abstractmethod

class LibraryItem(ABC):
    """
    Abstract base class for all library items.
    Represents a generic item in the library with basic attributes.
    """
    def __init__(self, item_id, title):
        self._item_id = item_id  # Protected attribute
        self._title = title      # Protected attribute

    @property
    def item_id(self):
        """Property to get the item ID."""
        return self._item_id

    @property
    def title(self):
        """Property to get the title."""
        return self._title

    @abstractmethod
    def display_info(self):
        """
        Abstract method to display information about the item.
        Must be implemented by subclasses.
        """
        pass

class Book(LibraryItem):
    """
    Subclass representing a book.
    Inherits from LibraryItem and implements display_info.
    """
    def __init__(self, item_id, title, author, year):
        super().__init__(item_id, title)
        self.__author = author  # Private attribute
        self.__year = year      # Private attribute

    @property
    def author(self):
        """Property to get the author."""
        return self.__author

    @property
    def year(self):
        """Property to get the publication year."""
        return self.__year

    def display_info(self):
        """
        Displays information about the book.
        """
        print(f"ID Buku: {self.item_id}")
        print(f"Judul: {self.title}")
        print(f"Penulis: {self.author}")
        print(f"Tahun: {self.year}")
        print("-" * 30)

class Magazine(LibraryItem):
    """
    Subclass representing a magazine.
    Inherits from LibraryItem and implements display_info.
    """
    def __init__(self, item_id, title, issue, publisher):
        super().__init__(item_id, title)
        self.__issue = issue      # Private attribute
        self.__publisher = publisher  # Private attribute

    @property
    def issue(self):
        """Property to get the issue number."""
        return self.__issue

    @property
    def publisher(self):
        """Property to get the publisher."""
        return self.__publisher

    def display_info(self):
        """
        Displays information about the magazine.
        """
        print(f"ID Majalah: {self.item_id}")
        print(f"Judul: {self.title}")
        print(f"Edisi: {self.issue}")
        print(f"Penerbit: {self.publisher}")
        print("-" * 30)

class Library:
    """
    Class to manage the library collection.
    Handles adding, displaying, and searching items.
    """
    def __init__(self):
        self.__items = []  # Private list to store items

    def add_item(self, item):
        """
        Adds an item to the library collection.
        """
        if isinstance(item, LibraryItem):
            self.__items.append(item)
            print(f"Item '{item.title}' berhasil ditambahkan.")
        else:
            print("Tipe item tidak valid. Harus berupa LibraryItem.")

    def display_items(self):
        """
        Displays all items in the library.
        """
        if not self.__items:
            print("Tidak ada item di perpustakaan.")
            return
        print("Item Perpustakaan:")
        for item in self.__items:
            item.display_info()

    def search_by_title(self, title):
        """
        Searches for items by title (case-insensitive).
        """
        results = [item for item in self.__items if title.lower() in item.title.lower()]
        if results:
            print(f"Ditemukan {len(results)} item dengan judul mengandung '{title}':")
            for item in results:
                item.display_info()
        else:
            print(f"Tidak ada item ditemukan dengan judul mengandung '{title}'.")

    def search_by_id(self, item_id):
        """
        Searches for an item by ID.
        """
        for item in self.__items:
            if item.item_id == item_id:
                print("Item ditemukan:")
                item.display_info()
                return
        print(f"Tidak ada item ditemukan dengan ID '{item_id}'.")

def main():
    """
    Main function to run the library management system.
    Provides a simple menu for user interaction.
    """
    library = Library()

    # Sample data
    book1 = Book("B001", "Pemrograman Python", "John Doe", 2020)
    book2 = Book("B002", "Struktur Data", "Jane Smith", 2019)
    mag1 = Magazine("M001", "Teknologi Bulanan", "Edisi 45", "Penerbit Teknologi")
    mag2 = Magazine("M002", "Sains Hari Ini", "Edisi 12", "Penerbit Sains")

    library.add_item(book1)
    library.add_item(book2)
    library.add_item(mag1)
    library.add_item(mag2)

    while True:
        print("\nSistem Manajemen Perpustakaan")
        print("1. Tampilkan semua item")
        print("2. Cari berdasarkan judul")
        print("3. Cari berdasarkan ID")
        print("4. Tambah item baru")
        print("5. Keluar")
        choice = input("Masukkan pilihan Anda: ")

        if choice == "1":
            print()
            library.display_items()
        elif choice == "2":
            title = input("Masukkan judul untuk dicari: ")
            print()
            library.search_by_title(title)
        elif choice == "3":
            item_id = input("Masukkan ID untuk dicari: ")
            print()
            library.search_by_id(item_id)
        elif choice == "4":
            print("Pilih jenis item:")
            print("1. Buku")
            print("2. Majalah")
            item_type = input("Masukkan pilihan (1/2): ")
            if item_type == "1":
                item_id = input("Masukkan ID buku: ")
                title = input("Masukkan judul buku: ")
                author = input("Masukkan penulis buku: ")
                year = int(input("Masukkan tahun terbit: "))
                book = Book(item_id, title, author, year)
                library.add_item(book)
            elif item_type == "2":
                item_id = input("Masukkan ID majalah: ")
                title = input("Masukkan judul majalah: ")
                issue = input("Masukkan edisi majalah: ")
                publisher = input("Masukkan penerbit majalah: ")
                magazine = Magazine(item_id, title, issue, publisher)
                library.add_item(magazine)
            else:
                print("Pilihan tidak valid.")
        elif choice == "5":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
from tkinter import messagebox

from Model.BookModel import BookModel
from View import UpdateBookHandler, AddBookHandler
import tkinter as tk


class BookViewModel:
    def __init__(self, root, view):
        self.model = BookModel()
        self.view = view
        self.root = root

        self.id_entry = tk.Entry(self.root)
        self.id_entry.grid(row=0, column=1)

        self.get_all_books_button = tk.Button(self.root, text="Get all books", command=self.get_all_books)
        self.get_all_books_button.grid(row=0, column=0)

        self.get_book_by_id_button = tk.Button(self.root, text="Get book by ID", command=self.get_book_by_id)
        self.get_book_by_id_button.grid(row=1, column=1)

        self.add_book_button = tk.Button(self.root, text="Add Book", command=self.open_add_book_window)
        self.add_book_button.grid(row=1, column=0)

        self.delete_book_button = tk.Button(self.root, text="Delete book", command=self.delete_book)
        self.delete_book_button.grid(row=2, column=0)

        self.update_book_button = tk.Button(self.root, text="Update book", command=self.open_update_book_window)
        self.update_book_button.grid(row=2, column=1)

    def get_all_books(self):
        books = self.model.get_all_books()
        self.view.display_books(books)

    def get_book_by_id(self):
        selected_book_id = self.view.get_selected_book()
        if selected_book_id:
            book_id = selected_book_id
        else:
            book_id = self.id_entry.get()
        book = self.model.get_book_by_id(book_id)
        if book:
            self.view.display_books([book])
        else:
            messagebox.showinfo("Error", "There is no books with this ID")

    def delete_book(self):
        selected_book_id = self.view.get_selected_book()
        if selected_book_id:
            book_id = selected_book_id
        else:
            book_id = self.id_entry.get()
        status_code = self.model.delete_book(book_id)
        if status_code == 200:
            messagebox.showinfo("Done", "Book deleted successfully")
            self.view.clear_table()
            self.get_all_books()
            self.view.count_label.config(text=f"Items displayed: {len(self.view.tree.get_children())}")
        else:
            messagebox.showinfo("Error", "Failed to delete book")

    def open_add_book_window(self):
        AddBookHandler.AddBookWindow(self)

    def add_book(self, data):
        response = self.model.add_book(data)
        self.get_all_books()
        return response

    def open_update_book_window(self):
        selected_book_id = self.view.get_selected_book()
        if selected_book_id:
            book_id = selected_book_id
        else:
            book_id = self.id_entry.get()
        data = self.model.get_book_by_id(book_id)

        if data is not None:
            UpdateBookHandler.UpdateBookWindow(self, data)
        else:
            messagebox.showinfo("Error", "The book was not chosen")

    def update_book(self, book_id, data):
        status_code = self.model.update_book(book_id, data)
        self.get_all_books()
        return status_code

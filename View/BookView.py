from tkinter import ttk


class BookView:
    def __init__(self, root):
        self.root = root
        self.count_label = ttk.Label(self.root, text="Items displayed: 0")
        self.count_label.grid(row=4, column=0, columnspan=2)
        self.tree = ttk.Treeview(root, columns=(
            "ID", "Title", "Author", "Genre", "Year", "Cover", "Price", "Amount", "Status"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Genre", text="Genre")
        self.tree.heading("Year", text="Year")
        self.tree.heading("Cover", text="Cover")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Status", text="Status")
        self.tree.grid(row=3, column=0, columnspan=2)
        self.set_default_column_widths()

    def display_books(self, books):
        self.clear_table()
        for book in books:
            values = (book["id"], book["title"], book["author"], book["genre"], book["year"])
            if "cover" in book:
                values += (book["cover"],)
            if "price" in book:
                values += (book["price"],)
            if "amount" in book:
                values += (book["amount"],)
            if "status" in book:
                values += (book["status"],)
            self.tree.insert("", "end", values=values)

        self.count_label.config(text=f"Items displayed: {len(books)}")

    def get_selected_book(self):
        selection = self.tree.selection()
        if selection:
            selected_item_id = selection[0]
            item_data = self.tree.item(selected_item_id)
            selected_book_id = item_data['values'][0]
            return selected_book_id
        else:
            return None

    def clear_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def set_default_column_widths(self):
        for col in self.tree["columns"]:
            self.tree.column(col, width=100)

import tkinter as tk
from tkinter import messagebox
from pydantic import Field


class BookWindow(tk.Toplevel):
    def __init__(self, controller, title_text):
        super().__init__()
        self.controller = controller
        self.title(title_text)

        self.fields = ["title", "author", "genre", "year", "cover", "price", "amount", "status"]
        self.entries = {}

        for i, field in enumerate(self.fields):
            label = tk.Label(self, text=field)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="e")
            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="we")
            self.entries[field] = entry

        self.action_button = tk.Button(self, text=title_text, command=self.perform_action)
        self.action_button.grid(row=len(self.fields), columnspan=2, pady=10)

    def perform_action(self):
        data = {}
        for field, entry in self.entries.items():
            value = entry.get()
            if field == "title" or field == "author" or field == "genre" or field == "cover":
                data[field] = str(value)
            elif field == "year" or field == "amount":
                data[field] = int(value) if value.isdigit() else None
            elif field == "price":
                data[field] = float(value) if value.replace('.', '', 1).isdigit() else None
            elif field == "status":
                data[field] = value.lower() == "true"

        data["title"] = str(data["title"])
        data["author"] = str(data["author"])
        data["amount"] = int(data["amount"]) if data["amount"] is not None else Field(None, ge=0)

        if "genre" in data and data["genre"]:
            data["genre"] = str(data["genre"])
        if "year" in data and data["year"]:
            data["year"] = int(data["year"]) if data["year"] >= 1 else Field(None, ge=1)
        if "cover" in data and data["cover"]:
            data["cover"] = str(data["cover"])
        if "price" in data and data["price"]:
            data["price"] = float(data["price"]) if data["price"] >= 0 else Field(None, ge=0)
        if "status" in data:
            data["status"] = bool(data["status"])

        status_code = self.perform_specific_action(data)
        if status_code == 200:
            messagebox.showinfo("Done", f"Book {self.title()} successfully")
            self.destroy()
        else:
            messagebox.showinfo("Error", f"Failed to {self.title().lower()} book")

    def perform_specific_action(self, data):
        pass

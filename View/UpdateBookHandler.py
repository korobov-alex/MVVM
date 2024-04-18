from View import BookHandler


class UpdateBookWindow(BookHandler.BookWindow):
    def __init__(self, controller, data):
        super().__init__(controller, "Update Book")
        self.book_data = data

        for field, entry in self.entries.items():
            if field in self.book_data:
                entry.insert(0, str(self.book_data[field]))

    def perform_specific_action(self, data):
        return self.controller.update_book(self.book_data["id"], data)



from View import BookHandler


class AddBookWindow(BookHandler.BookWindow):
    def __init__(self, controller):
        super().__init__(controller, "Add Book")

    def perform_specific_action(self, data):
        return self.controller.add_book(data)

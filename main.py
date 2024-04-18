from View.BookView import BookView
from ViewModel.BookViewModel import BookViewModel
import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title("MVC (Lab2)")

    view = BookView(root)
    model_view = BookViewModel(root, view)

    root.mainloop()


if __name__ == "__main__":
    main()

# MVVM Book Management Application

## Overview

This project is a Python-based application that demonstrates the Model-View-ViewModel (MVVM) architectural pattern for creating a graphical user interface (GUI) using the Tkinter library. The application is designed to manage a collection of books, allowing users to perform various operations such as viewing all books, searching for a book by its ID, adding new books, updating existing books, and deleting books.

## Features

- **Book Management**: Users can view all books, search for a book by its ID, add new books, update existing books, and delete books.
- **MVVM Architecture**: The application is structured using the MVVM pattern, ensuring a clean separation of concerns between the Model (data), View (user interface), and ViewModel (logic that binds the Model and View).
- **Tkinter GUI**: The user interface is built using Tkinter, a standard Python library for creating desktop applications.
- **HTTP Requests**: The Model communicates with a backend server to perform CRUD operations on the book data, using the `requests` library for making HTTP requests.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (included with Python)
- Requests lib

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/korobov-alex/MVVM.git
   ```
2. Navigate to the project directory:
   ```
   cd repo
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

To run the application, execute the following command in the terminal:

```
python main.py
```

## Usage

After launching the application, you can interact with it through the GUI to manage your book collection.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.

## Acknowledgments

- The MVVM architectural pattern for its clear separation of concerns.
- The Tkinter library for providing a simple way to create GUI applications in Python.
- The `requests` library for handling HTTP requests to the backend server.

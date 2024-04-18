import requests


class BookModel:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000"

    def get_all_books(self):
        response = requests.get(self.base_url)
        return response.json()

    def get_book_by_id(self, book_id):
        response = requests.get(f"{self.base_url}/{book_id}")
        if response.status_code == 200:
            return response.json()

    def delete_book(self, book_id):
        response = requests.delete(f"{self.base_url}/{book_id}")
        return response.status_code

    def update_book(self, book_id, data):
        response = requests.put(f"{self.base_url}/{book_id}", json=data)
        return response.status_code

    def add_book(self, data):
        response = requests.post(self.base_url, json=data)
        return response.status_code




'''
class BookManager:
    def __init__(self, base_url):
        self.base_url = base_url

    def add_book(self, data):
        response = requests.post(self.base_url, json=data)
        return response.status_code

data = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Novel",
        "year": 1925,
        "cover": "https://example.com/covers/great-gatsby.jpg",
        "price": 1200,
        "amount": 122,
        "status": True
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Novel",
        "year": 1960,
        "cover": "https://example.com/covers/to-kill-mockingbird.jpg",
        "price": 1050,
        "amount": 122,
        "status": True
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian fiction",
        "year": 1949,
        "cover": "https://example.com/covers/1984.jpg",
        "price": 950,
        "amount": 122,
        "status": True
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Novel",
        "year": 1951,
        "cover": "https://example.com/covers/catcher-rye.jpg",
        "price": 1100,
        "amount": 122,
        "status": True
    },
    {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "genre": "Dystopian fiction",
        "year": 1932,
        "cover": "https://example.com/covers/brave-new-world.jpg",
        "price": 1000,
        "amount": 122,
        "status": True
    },
    {
        "title": "Moby-Dick; or, The Whale",
        "author": "Herman Melville",
        "genre": "Novel",
        "year": 1851,
        "cover": "https://example.com/covers/moby-dick.jpg",
        "price": 1300,
        "amount": 122,
        "status": True
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Novel",
        "year": 1813,
        "cover": "https://example.com/covers/pride-prejudice.jpg",
        "price": 1150,
        "amount": 122,
        "status": True
    },
    {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "genre": "High fantasy",
        "year": 1954,
        "cover": "https://example.com/covers/lord-rings.jpg",
        "price": 1500,
        "amount": 122,
        "status": True
    },
    {
        "title": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "genre": "Psychological fiction",
        "year": 1866,
        "cover": "https://example.com/covers/crime-punishment.jpg",
        "price": 1250,
        "amount": 122,
        "status": True
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "year": 1937,
        "cover": "https://example.com/covers/hobbit.jpg",
        "price": 950,
        "amount": 122,
        "status": True
    },
    {
        "title": "The Adventures of Huckleberry Finn",
        "author": "Mark Twain",
        "genre": "Adventure",
        "year": 1884,
        "cover": "https://example.com/covers/huckleberry-finn.jpg",
        "price": 1050,
        "amount": 122,
        "status": True
    },
    {
        "title": "The Picture of Dorian Gray",
        "author": "Oscar Wilde",
        "genre": "Gothic fiction",
        "year": 1890,
        "cover": "https://example.com/covers/dorian-gray.jpg",
        "price": 1150,
        "amount": 122,
        "status": True
    },
    {
        "title": "Wuthering Heights",
        "author": "Emily Brontë",
        "genre": "Gothic fiction",
        "year": 1847,
        "cover": "https://example.com/covers/wuthering-heights.jpg",
        "price": 1100,
        "amount": 122,
        "status": True
    },
    {
        "title": "The Brothers Karamazov",
        "author": "Fyodor Dostoevsky",
        "genre": "Philosophical fiction",
        "year": 1880,
        "cover": "https://example.com/covers/brothers-karamazov.jpg",
        "price": 1350,
        "amount": 122,
        "status": True
    },
    {
        "title": "Anna Karenina",
        "author": "Leo Tolstoy",
        "genre": "Realist novel",
        "year": 1877,
        "cover": "https://example.com/covers/anna-karenina.jpg",
        "price": 1200,
        "amount": 122,
        "status": True
    },
    {
        "title": "Frankenstein; or, The Modern Prometheus",
        "author": "Mary Shelley",
        "genre": "Gothic fiction",
        "year": 1818,
        "cover": "https://example.com/covers/frankenstein.jpg",
        "price": 1100,
        "amount": 122,
        "status": True
    },
    {
        "title": "Les Misérables",
        "author": "Victor Hugo",
        "genre": "Historical novel",
        "year": 1862,
        "cover": "https://example.com/covers/les-miserables.jpg",
        "price": 1250,
        "amount": 122,
        "status": True
    },
    {
        "title": "The Count of Monte Cristo",
        "author": "Alexandre Dumas",
        "genre": "Adventure novel",
        "year": 1844,
        "cover": "https://example.com/covers/count-monte-cristo.jpg",
        "price": 1300,
        "amount": 122,
        "status": True
    },
    {
        "title": "Don Quixote",
        "author": "Miguel de Cervantes",
        "genre": "Picaresque novel",
        "year": 1605,
        "cover": "https://example.com/covers/don-quixote.jpg",
        "price": 1400,
        "amount": 122,
        "status": True
    },
    {
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel García Márquez",
        "genre": "Magical realism",
        "year": 1967,
        "cover": "https://example.com/covers/one-hundred-years-solitude.jpg",
        "price": 1450,
        "amount": 122,
        "status": True
    }
]

book_manager = BookManager("http://127.0.0.1:8000")
for book_data in data:
    status_code = book_manager.add_book(book_data)
    print(f"Статус код для книги '{book_data['title']}': {status_code}")
'''
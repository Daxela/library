class Book:
    counter = 0

    def __init__(self, title, author, year, status):
        self.id = Book.counter
        Book.counter += 1
        self.title = title
        self.author = author
        self.year = year
        self.status = status

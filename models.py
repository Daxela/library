def check_status(status):
    if status not in {'в наличии', 'выдана'}:
        return "Некорректный статус книги"


class Book:

    with open('current_id.txt', 'r') as idFile:
        counter = int(idFile.read())

    def __init__(self, title: str = None, author: str = None, year: int = None, data: dict = None):

        if title and author and year:
            self.id = Book.counter
            Book.counter += 1
            self.title = title
            self.author = author
            self.year = year
            self.status = 'в наличии'

            with open('current_id.txt', 'w') as idFile:
                idFile.write(str(Book.counter))

        if data:
            self.id = data.get('id')
            self.title = data.get('title')
            self.author = data.get('author')
            self.year = data.get('year')
            self.status = data.get('status')

    def check(self):
        error = set()
        error.add(Book.check_id(self))
        error.add(Book.check_title(self))
        error.add(Book.check_year(self))
        error.add(Book.check_author(self))
        error.add(check_status(self.status))
        error.discard(None)
        return error

    def check_id(self):
        if not isinstance(self.id, int) or self.id < 0:
            return "Некорректный id книги"

    def check_title(self):
        if not isinstance(self.title, str):
            return "Некорректное название книги"

    def check_author(self):
        if not isinstance(self.author, str):
            return "Некорректно указан автор книги"

    def check_year(self):
        if not isinstance(self.year, int) or self.year < 1000 or self.year > 10000:
            return "Некорректный год издания книги"

    def receiving_issuing(self, status):
        check = check_status(status)
        if check:
            return False
        self.status = status
        return True

    def book_dict(self):
        return {'id': self.id, 'title': self.title, 'author': self.author, 'year': self.year, 'status': self.status}

    def demonstration(self):
        return f'Книга №{self.id}. {self.author} "{self.title}" {self.year} года издания - {self.status}'
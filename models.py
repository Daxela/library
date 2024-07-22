def check_status(status: str) -> str or None:
    if status not in {'в наличии', 'выдана'}:
        return "Некорректный статус книги"
    return None


class Book:
    with open('current_id.txt', 'r') as idFile:
        counter: int = int(idFile.read())

    def __init__(self, title: str = None, author: str = None, year: str or int = None, data: dict = None) -> None:

        self.id: str or int
        self.title: str
        self.author: str
        self.year: str or int
        self.status: str

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

    def check(self) -> set:
        error: set[str or None] = set()
        error.add(Book.check_id(self))
        error.add(Book.check_title(self))
        error.add(Book.check_year(self))
        error.add(Book.check_author(self))
        error.add(check_status(self.status))
        error.discard(None)
        return error

    def check_id(self) -> str or None:
        if not isinstance(self.id, int) or self.id < 0:
            return "Некорректный id книги"
        return None

    def check_title(self) -> str or None:
        if not isinstance(self.title, str):
            return "Некорректное название книги"
        return None

    def check_author(self) -> str or None:
        if not isinstance(self.author, str):
            return "Некорректно указан автор книги"
        return None

    def check_year(self) -> str or None:
        if not isinstance(self.year, int) or self.year < 1000 or self.year > 10000:
            return "Некорректный год издания книги"
        return None

    def receiving_issuing(self, status: str) -> bool:
        check: str or None = check_status(status)
        if check:
            return False
        self.status = status
        return True

    def book_dict(self) -> dict:
        return {'id': self.id, 'title': self.title, 'author': self.author, 'year': self.year, 'status': self.status}

    def demonstration(self) -> str:
        return f'Книга №{self.id}. {self.author} "{self.title}" {self.year} года издания - {self.status}'

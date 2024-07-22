import constants

try:
    f1 = open(constants.current_id)
    f1.close()
except FileNotFoundError:
    raise FileNotFoundError(f"Ошибка! Файл {constants.current_id} не найден!")


def check_status(status: str) -> str or None:
    if status not in {'в наличии', 'выдана'}:
        return "Некорректный статус книги"
    return None


class Book:
    with open(constants.current_id, 'r') as idFile:
        try:
            counter: int = int(idFile.read())
        except ValueError:
            raise ValueError(f"Ошибка! В файле {constants.current_id} ожидалось число!")

    def __init__(self, title: str = None, author: str = None, year: str or int = None, data: dict = None) -> None:

        self.id: str or int
        self.title: str
        self.author: str
        self.year: str or int
        self.status: str

        if title and author and year:
            Book.counter += 1
            self.id = Book.counter
            self.title = title
            self.author = author
            self.year = year
            self.status = 'в наличии'

            with open(constants.current_id, 'w') as idFile:
                idFile.write(str(Book.counter))

        if data:
            self.id = data.get('id')
            self.title = data.get('title')
            self.author = data.get('author')
            self.year = data.get('year')
            self.status = data.get('status')

    def check(self) -> set:
        error: set[str or None] = set()
        error.add(Book.check_year(self))
        error.add(check_status(self.status))
        error.discard(None)
        return error

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

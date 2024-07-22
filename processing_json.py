from models import Book


class Books:

    def __init__(self) -> None:
        self.books_list: list[Book]
        self.books_str: str
        self.books_list, self.books_str = read_json()

    def add_book(self, book: Book) -> None:
        self.books_list.append(book)
        data: dict or str = book.book_dict()
        data = str(data).replace('\'', '"')
        if len(self.books_str) > 2 and self.books_str[0] == '[':
            self.books_str = f"{self.books_str[:-1]}, {data}]"
        else:
            self.books_str = f"[{data}]"
        write_json(self.books_str)

    def search_books(self, book_title: str, book_author: str, book_year: int) -> int:
        found_books: int = 0
        for book in self.books_list:
            if book_title:
                if book.title != book_title:
                    continue
            if book_author:
                if book.author != book_author:
                    continue
            if book_year:
                if book.year != book_year:
                    continue
            found_books += 1
            print(book.demonstration())
        return found_books

    def search_id(self, book_id: int) -> bool and Book:
        flag: bool = False
        book: Book or None = None
        for book in self.books_list:
            if book.id == book_id:
                flag = True
                break
        return flag, book

    def delete_book(self, book_id: int) -> bool:
        flag: bool
        book: Book
        flag, book = Books.search_id(self, book_id)
        if not flag:
            return flag
        old_book: str = str(book.book_dict())
        self.books_str.replace(old_book, old_book + '||').replace(old_book, '').replace('||, ', '').replace(', ||', '')
        self.books_list.pop(self.books_list.index(book))
        write_json(self.books_str)
        return flag

    def receiving_issuing_book(self, book_id: int, status: str) -> bool or None:
        flag: bool
        book: Book
        flag, book = Books.search_id(self, book_id)
        if not flag:
            return flag
        index: int = self.books_list.index(book)
        old_book: str = str(book.book_dict()).replace('\'', '"')
        if not book.receiving_issuing(status):
            return None
        self.books_list[index] = book
        new_book: str = str(book.book_dict()).replace('\'', '"')
        write_json(self.books_str.replace(old_book, new_book))
        return flag


def write_json(json_obj: str) -> None:
    with open('books.json', 'wb') as jsonFile:
        jsonFile.write(bytes(json_obj, 'utf-8'))


def read_json() -> list and str:
    with open('books.json', 'rb') as jsonFile:
        json_obj: str = jsonFile.read().decode('utf-8')
        str_line: str = json_obj.replace('[', '').replace(']', '')
        number_lines: int = str_line.count('}')
        list_line: list = list()
        if number_lines:
            for number in range(number_lines):
                line: str = str_line[str_line.find('{') + 1:str_line.find('}')]
                dict_line: dict = dict()
                while line:
                    name: str = line[line.find('"') + 1:line.find(':') - 1]
                    line = line[line.find(':') + 2:]
                    if line[0] == '"':
                        line = line[1:]
                        dict_line[name] = line[:line.find('"')]
                        line = line[line.find('"') + 1:]
                    else:
                        if line.find(',') == -1:
                            dict_line[name] = int(line)
                            break
                        else:
                            dict_line[name] = int(line[:line.find(',')])
                list_line.append(Book(data=dict_line))
                str_line = str_line[str_line.find('}') + 1:]

        return list_line, json_obj

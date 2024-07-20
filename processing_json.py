from models import Book


class Books:

    def __init__(self):
        self.books_list, self.books_str = read_json()

    def add_book(self, book):
        self.books_list.append(book)
        data = book.book_dict()
        data = str(data).replace('\'', '"')
        if len(self.books_str) > 2 and self.books_str[0] == '[':
            self.books_str = f"{self.books_str[:-1]}, {data}]"
        else:
            self.books_str = f"[{data}]"
        write_json(self.books_str)

    def search_books(self, book_title, book_author, book_year):
        found_books = 0
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

    def search_id(self, book_id):
        flag = False
        for book in self.books_list:
            if book.id == book_id:
                flag = True
                break
        return flag, book

    def delete_book(self, book_id):
        flag, book = Books.search_id(self, book_id)
        if not flag:
            return flag
        old_book = str(book.book_dict())
        self.books_str.replace(old_book, old_book + '||').replace(old_book, '').replace('||, ', '').replace(', ||', '')
        self.books_list.pop(self.books_list.index(book))
        write_json(self.books_str)
        return flag

    def receiving_issuing_book(self, book_id, status):
        flag, book = Books.search_id(self, book_id)
        if not flag:
            return flag
        index = self.books_list.index(book)
        old_book = str(book.book_dict()).replace('\'', '"')
        if not book.receiving_issuing(status):
            return None
        self.books_list[index] = book
        new_book = str(book.book_dict()).replace('\'', '"')
        write_json(self.books_str.replace(old_book, new_book))
        return flag


# метод для добавления словаря в json файл
def write_json(json_obj):
    with open('books.json', 'wb') as jsonFile:
        jsonFile.write(bytes(json_obj, 'utf-8'))


# метод для преобразования json файла в список словарей (предусматривает только два типа данных значений словаря: строковый и целочисенный)
def read_json():
    with open('books.json', 'rb') as jsonFile:
        json_obj = jsonFile.read().decode('utf-8')
        str_line = json_obj.replace('[', '').replace(']', '')
        number_lines = str_line.count('}')
        list_line = list()
        if number_lines:
            for number in range(number_lines):
                line = str_line[str_line.find('{') + 1:str_line.find('}')]
                dict_line = dict()
                while line:
                    name = line[line.find('"') + 1:line.find(':') - 1]
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

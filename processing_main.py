from processing_json import Books
from models import Book

current_books = Books()


# def starting():
#     global current_books
#     current_books = Books()
#     print('Добро пожаловать в главное меню приложения "Библиотека"!\nЧто вы желаете сделать?')

def add_book():
    global current_books
    print('Для добавления новой книги введите информацию о ней.\nВведите название книги: ')
    current_book_title = input()
    print('Введите автора книги: ')
    current_book_author = input()
    print('Введите год издания книги (только число): ')
    current_book_year = input()
    if current_book_year.isdigit():
        current_book_year = int(current_book_year)
    current_book = Book(current_book_title, current_book_author, current_book_year)
    errors = current_book.check()
    if errors:
        print(f'Найденно {len(errors)} ошибок:')
        for error in errors:
            print(error)
    else:
        current_books.add_book(current_book)
        print('Книга добавлена! Спасибо за обращение!')


def delete_book():
    global current_books
    print('Для удаления книги введите ее уникальный идентификатор (id): ')
    current_book_id = input()
    if current_book_id.isdigit():
        current_book_id = int(current_book_id)
    if current_books.delete_book(current_book_id):
        print('Книга удалена! Спасибо за обращение!')
    else:
        print('Ошибка! Книга не может быть удалена! Проверьте введеный id и попробуйте снова.\nБудем ждать вашего обращения!')


def search_books():
    global current_books
    print('Для поиска книги введите информацию о ней. Если информация Вам не известна - пропустите шаг, нажав клавишу "Enter"\nВведите название книги или нажмите "Enter": ')
    current_book_title = input()
    print('Введите автора книги или нажмите "Enter": ')
    current_book_author = input()
    print('Введите год издания книги (только число) или нажмите "Enter": ')
    current_book_year = input()
    if current_book_year.isdigit():
        current_book_year = int(current_book_year)
    print('По вашему запросу найдены следующие книги:')
    count_books = current_books.search_books(current_book_title, current_book_author, current_book_year)
    print(f'Всего книг найдено - {count_books}. Спасибо за обращение!')


def demonstration_books():
    global current_books
    print(f'В библиотеке всего {len(current_books.books_list)} книг:')
    for book in current_books.books_list:
        print(book.demonstration())
    print('Спасибо за обращение!')


def receiving_issuing_book():
    global current_books
    print('Для изменения статуса книги введите необходимую информацию.\nВведите id книги: ')
    current_book_id = input()
    if current_book_id.isdigit():
        current_book_id = int(current_book_id)
    print('Введите новый статус книги: ')
    current_book_status = input()
    flag = current_books.receiving_issuing_book(current_book_id, current_book_status)
    if isinstance(flag, type(None)):
        print('Ошибка! Введен некорректный статус книги. Проверьте введеный статус и попробуйте снова.\nБудем ждать вашего обращения!')
    elif flag:
        print(f'Статус книги изменен на {current_book_status}! Спасибо за обращение!')
    else:
        print('Ошибка! Введен некорректный id книги. Проверьте введеный id и попробуйте снова.\nБудем ждать вашего обращения!')
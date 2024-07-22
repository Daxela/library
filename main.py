from processing_main import *


def main_menu(stage: bool) -> None:
    if stage:
        print("Добавление книги - 1, удаление книги - 2, поиск книги - 3, отображение всех книг - 4, изменение "
              "статуса книги - 5\nВведите код: ")
    else:
        print("Добавление книги - 1, удаление книги - 2, поиск книги - 3, отображение всех книг - 4, изменение "
              "статуса книги - 5, завершения программы - 6\nВведите код: ")
    command: str or int = input()
    if command.isdigit():
        command = int(command)
    match command:
        case 1:
            add_book()
        case 2:
            delete_book()
        case 3:
            search_books()
        case 4:
            demonstration_books()
        case 5:
            receiving_issuing_book()
        case 6:
            print("Программа завершенна. Спасибо за обращение, будем ждать Вас снова!")
            global final
            final = True
        case _:
            print("К сожалению, нет такой команды. Прочтите инструкцию и обратитесь снова. Будем ждать!")


if __name__ == '__main__':
    print('Добро пожаловать в главное меню приложения "Библиотека"!\nЧто вы желаете сделать?')
    k: bool = True
    final: bool = False
    while True:
        if final:
            break
        main_menu(k)
        k = False

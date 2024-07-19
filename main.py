def main_menu(stage: int) -> None:
    # В зависимости от того, какой раз мы используем программу меню немного изменяется
    if stage == 0:
        print("Добавление книги - 1, удаление книги - 2, поиск книги - 3, отображение всех книг - 4, изменение статуса книги - 5\nВведите код: ")
    else:
        print("Добавление книги - 1, удаление книги - 2, поиск книги - 3, отображение всех книг - 4, изменение статуса книги - 5, завершения программы - 6\nВведите код: ")
    # Вводим номер команды
    comanda = int(input())
    # Вызываем функции в соответствии с командой
    match comanda:
        case 1:
            print("Добавление книги")
        case 2:
            print("удаление книги")
        case 3:
            print("поиск книги")
        case 4:
            print("отображение всех книг")
        case 5:
            print("изменение статуса книги")
        case 6:
            print("Программа завершенна")
            # Используем глобальную переменную для завершения программы
            global final
            final = 1
        case _:
            print("Нет такой команды")


if __name__ == '__main__':
    print('Добро пожаловать в главное меню приложения "Библиотека"!\nЧто вы желаете сделать?')
    k = 0
    final = 0
    while True:
        if final == 1:
            break
        main_menu(k)
        k += 1

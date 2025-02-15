# library
Консольное приложение для управления библиотекой книг. Приложение позволяет добавлять, удалять, искать и отображать книги. Каждая книга содержит следующие поля: id (уникальный идентификатор), title (название книги), author (автор книги), year (год издания), status (статус книги: “в наличии”, “выдана”). Реализовано хранение данных в текстовом и json формате. Не использованы сторонние библиотеки.
### Как настроить проект
1. Скачайте и установите python 3.10 (или более новой версии).
2. Убедитесь, что скачали данный проект (library).
3. Проверьте файлы хранения данных. Файл books.json должен хранить перечень книг (если приложение уже использовалось) или быть пустым (если приложение еще не использовалось). Файл current_id.txt хранит в себе одно число - минимальный не использованный номер для идентификации книг (в самом начале это 0).
### Как запустить проект
1. Откройте приложение Командная строка. Перейдите в папку library, для этого напишите команду cd и путь к папке library.
2. Запустите приложение, для этого напишите команду python main.py.
3. Готово - приложение запущенно.
### Как взаимодействовать с приложением
Интерфейс приложения максимально удобен, поэтому после запуска приложения – приложение само объясняет вам как с ним взаимодействовать. Для ввода данных необходима клавиатура, набираете необходимый текст и нажимаете клавишу «Enter». Удачи!

### Документация
Документацию к коду проекта Вы можете найти в файлах проекта. Файл называется "Документация к коду проекта library.docx".
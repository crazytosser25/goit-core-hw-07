## goit-core-hw-07
# Homework module 7. Assistant bot

Бот запускається файлом bot.py. Для виводу, при наявності, використовується
colorama. За відсутності - вивід відбувається звичайним текстом. Данні
книги контактів зберігаються у файлі contacts.pkl. За відсутності файла 
створюється нова книга контактів і при закритті програми записується у новий файл.

    - help: Для отримання підказки по командах бота
    - add [ім'я] [телефон]: Додати або новий контакт з іменем та телефонним 
        номером, або телефонний номер к контакту який вже існує.
    - change [ім'я] [старий телефон] [новий телефон]: Змінити телефонний 
        номер для вказаного контакту.
    - phone [ім'я]: Показати телефонний номер для вказаного контакту.
    - all: Показати всі контакти в адресній книзі.
    - add-birthday [ім'я] [дата народження]: Додати дату народження для 
        вказаного контакту.
    - show-birthday [ім'я]: Показати дату народження для вказаного контакту.
    - birthdays: Показати дні народження, які відбудуться протягом наступного 
        тижня.
    - hello: Отримати вітання від бота.
    - close або exit: Закрити програму.
    
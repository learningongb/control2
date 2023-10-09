# Простая программа управления заметками

Заметки сохраняются в файле notes.json. Если файл не существует, он будет создан.  
Любые манипуляции с заметками сразу отражаются в файле.

## Команды управления
1. Вывести список заметок.  
Выводит дату, заголовок и идентификатор заметки. Идентификатор необходим в операциях изменения, удаления и просмотра записей.
2. Добавить заметку.  
Запрашивается заголовок и текст заметки. Идентификатор и текущая дата присваивается автоматически.
3. Вывести заметку.  
Выводит дату, заголовок, текст и идентификатор заметки по введенному идентификатору.
4. Изменить заметку.  
Позволяет изменить заголовок и/или текст заметки по идентификатору.
5. Удалить заметку.  
Удаляет заметку по идентификатору.
6. Вывести список заметок с фильтром.  
Позволяет вывести заметки за определенный период. Запрашиваются дата начала и дата окончания периода. Допускается любую из дат оставлять пустой.
0. Выход из программы.
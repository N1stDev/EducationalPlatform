import os.path

import settings
import users

_menu_states = ['main']
_menu_current_state = 'main'

def db_initialize():
    """
    В файле path.txt будет прописан путь до корневой директории с файлами баз данных
    Проверяем наличие файла Path.txt, а так же важных файлов, без которых программа не будет работать
    """

    if not os.path.isfile('path.txt'):
        f = open("path.txt", "w")
        print('Файл path.txt не был найден\nВведите путь до корневой папки с базой данных: ')
        settings.DB_PATH_MAIN = input()
        f.write(settings.DB_PATH_MAIN)
        f.close()
    else:
        print('Файл path.txt был найден')
        f = open("path.txt", "r")
        settings.DB_PATH_MAIN = f.read()
        f.close()

    print('Проверяем наличие ключевых файлов')
    critical_db_files = ['users.db', 'forum.db', 'files.db']
    critical_py_files = ['users.py', 'forum.py', 'files.py']

    for f in critical_py_files:
        if not os.path.isfile(f):
            print("Файлы программы повреждены. Завершаем программу")
            input()
            quit()

    for f in critical_db_files:
        if os.path.isfile(settings.DB_PATH_MAIN + '/' + f):
            critical_db_files.pop(critical_db_files.index(f))

    if not any(critical_db_files): print("Файлы баз данных найдены")
    else:
        print('Не найдены следующие файлы баз данных: ' + str(critical_db_files))
        print('Файлы будут созданы автоматически')

    users.users_initialize()
    if 'users.db' in critical_db_files:
        users.create_table()
    # if not 'forum.db' in critical_db_files:
    #     forum.create_table()
    # if not 'files.db' in critical_db_files:
    #     files.create_table()

def print_users_table():
    for u in users.get_all_users_table():
        print(u)

def print_current_menu(): #вывод текущего сеанса меню на экран
    if (_menu_current_state == 'main'):
        print('1. Вывести таблицу всех пользователей\n'
              '2. Добавить пользователя вручную\n'
              '3. Найти пользователя по логину\n'
              '4. Удалить пользователя по логину\n'
              'q. Завершить сеанс\n')
        i = input()
        if i == '1':
            print_users_table()
        if i == '2':
            first_name = input('Введите имя пользователя')
            last_name = input('Введите фамилию пользователя')
            login = input('Введите логин пользователя')
            password = input('Введите пароль пользователя')
            balance = input('Введите стартовый баланс пользователя')

            try: balance = int(balance)
            except: balance = 100

            u = users.User(first_name, last_name, login, password, balance)

            test = users.add_user(u)

            if (test):
                print('Пользователь успешно добавлен')
            elif (test):
                print('Произошла ошибка при добалении: скорее всего пользователь с таким логином уже существует')

        elif i == 'q':
            quit()

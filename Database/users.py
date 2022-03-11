import sqlite3
import os.path
import secrets

import settings

#Класс пользователя
class User:
    def __init__(self, first_name, last_name, login, password, balance=100):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password
        self.balance = balance

    def __str__(self):
        return str(self.get_list())

    def get_list(self):
        return [self.first_name, self.last_name, self.login, self.password, self.balance]

def users_initialize():
    global connection, c

    connection = sqlite3.connect(os.path.abspath('.') + '/' + settings.DB_PATH_MAIN + '/users.db')
    c = connection.cursor()

def create_table():
    c.execute("""CREATE TABLE users (
        first_name text,
        last_name text,
        login text,
        password text,
        balance integer
            )""")

def get_all_users_table():
    c.execute("SELECT * FROM users")
    return c.fetchall()

def get_user_by_login(login):
    c.execute("""
    SELECT * FROM users
    WHERE
    login = (?)
    """, [login])
    u = c.fetchone()

    if u != None:
        return User(u[0], u[1], u[2], u[3], int(u[4]))

def add_user(user):
    c.execute("SELECT * FROM users WHERE login = (?)", [user.login])
    dublicate = c.fetchall()
    if any(dublicate): return False
    c.execute("INSERT INTO users VALUES (?,?,?,?,?)", user.get_list())
    connection.commit()
    return True

def delete_user_by_login(login):
    c.execute("""
    DELETE FROM users 
    WHERE 
    login = (?)
    """, [login])
    connection.commit()


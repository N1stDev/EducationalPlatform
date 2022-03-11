import db_interface as dbi

dbi.db_initialize()
# dbi.users.add_user(dbi.users.User('Oleg', 'Zhmelev', 'losdayver', '123'))
#
# print(dbi.users.get_user_by_login('losdayver'))

#dbi.users.add_user(dbi.users.User('Petr', 'Petrov', 'pp', '123123123'))
print(dbi.users.get_user_by_login('ppp'))

while True:
    dbi.print_current_menu()

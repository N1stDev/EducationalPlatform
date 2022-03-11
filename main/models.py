from django.db import models


class Registration(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    login = models.CharField('Логин', max_length=50)
    password = models.CharField('Пароль', max_length=50)

    def __str__(self):
        return self.name + " " + self.surname

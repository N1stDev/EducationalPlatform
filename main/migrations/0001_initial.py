# Generated by Django 4.0.3 on 2022-03-11 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('login', models.CharField(max_length=50, verbose_name='Логин')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
            ],
        ),
    ]

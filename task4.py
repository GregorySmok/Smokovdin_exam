import csv
import string
import random


def create_login(s):
    '''Функция для создания логина
    Аргументы:
    s - принимает ФИО ученого'''
    fio = s.split()
    # возвращаем логин в нужном формате
    return f'{fio[0]}_{fio[1][0]}{fio[2][0]}'


def create_password():
    '''Функция для генерации случайного пароля'''
    # создаем строку из заглавных, строчных букв и цифр с помощью библиотеки string
    data = string.ascii_letters + string.digits
    # генерируем случайную последовательность длин 10 при помощи random.sample
    return ''.join(random.sample(data, k=10))


with open('scientist.txt', encoding='utf-8') as file:  # Откываем исходный файл
    reader = csv.reader(file, delimiter='#')
    data = list(reader)[1:]
    for el in data:
        # добавляем каждый строке логин и пароль
        el += [create_login(el[0]), create_password()]
with open('scientist_password.csv', 'w', newline='', encoding='utf-8') as file:  # открываем новый файл
    writer = csv.writer(file, delimiter='#')
    writer.writerow(['ScientistName', 'preparation', 'date', 'components',
                    'login', 'password'])  # вписываем новые названия столбцов
    writer.writerows(data)  # записываем все новые строки

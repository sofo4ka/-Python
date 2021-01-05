# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.

# def division_func(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print('Деление на ноль')
#
# while True:
#     try:
#         a = float(input('Введите первое число: '))
#         b = float(input('Введите второе число: '))
#         print(round(division_func(a, b), 2))
#         break
#     except ValueError:
#         print('Некорректный ввод')

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

def personal_data_processing(name, surname, birthyear, city, email, phone):
    return f' Имя: {name}, Фамилия: {surname}, год рождения: {birthyear}, город проживания: {city}, ' \
           f'email:{email}, телефон: {phone}'

print(personal_data_processing(name='Иван', surname='Иванов', birthyear=1999, city='Москва',
                               email='ivanov@mail.ru', phone='+74956783847'))


input_data = {'ID': 1, 'Имя': 'Иван', 'Фамилия': 'Иванов', 'год рождения': 1999, 'город проживания': 'Москва',
              'email': 'ivanov@mail.ru', 'телефон': '+74956783847'}

def personal_data_processing2(**kwargs):
    data_to_show = ['Имя', 'Фамилия', 'год рождения', 'город проживания', 'email', 'телефон']
    message = []
    for element in data_to_show:
        message.append(f'{element}: {kwargs[element]}')
    return message
print(personal_data_processing2(**input_data))

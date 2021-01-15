# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("testfile1.txt", "w", encoding="utf-8") as file_object:
    new_line = str()
    while True:
        new_line = input('Введите данные для ввода в файл по одной строке: \n')
        if len(new_line) == 0:
            break
        else:
            file_object.writelines(f'{new_line}\n')

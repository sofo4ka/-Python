# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
# элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

set_of_integer_numbers = [7, 5, 3, 3, 2]
try:
    users_input_number = int(input('Введите новый элемент: '))
except ValueError:
    print('Некорректный ввод')
number_of_entries = set_of_integer_numbers.count(users_input_number)
if number_of_entries > 0:
    index_of_entry = number_of_entries + set_of_integer_numbers.index(users_input_number)
    set_of_integer_numbers.insert(index_of_entry, users_input_number)
elif number_of_entries == 0 and set_of_integer_numbers[len(set_of_integer_numbers)-1] > users_input_number:
    set_of_integer_numbers.append(users_input_number)
else:
    for element in set_of_integer_numbers:
        if element < users_input_number:
            set_of_integer_numbers.insert(set_of_integer_numbers.index(element), users_input_number)
            break
print(set_of_integer_numbers)

#Более дешевый вариант by luchanos:
my_list = [9, 8, 7, 7, 6, 5, 3, 1]
new_number = int(input("Enter the new element: "))
i = 0
for n in my_list:
    if new_number <= n:
        i += 1
my_list.insert(i, new_number)
print(my_list)

my_list.index(7)
my_list.count(7)
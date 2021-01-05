# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.

def sum_calculation_of_numbers(list_of_numbers):
    summm = 0
    for element in list_of_numbers.split(' '):
        summm = summm + float(element)
    return summm


sum_of_numbers = 0
q = 0
while q == 0:
    try:
        sum_of_numbers = sum_of_numbers + sum_calculation_of_numbers(
            input('Введите строку чисел, разделенных пробелом: '))
        print(f'Сумма чисел равна: {sum_of_numbers}')
        while True:
            try:
                q = int(input('Введите 1 для выхода, 0 для продолжения ввода данных:'))
            except ValueError:
                print('Некорректный ввод')
            except TypeError:
                print('Некорректный ввод')
            finally:
                if q == 0 or q == 1:
                    break
    except ValueError:
        print('Некорректный ввод')


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class MyDivisionByNullError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    dividend = [34567, 456789, 0, 46, 687]
    divider = [56, 0, 878, 0, 'gggj']
    i = 0
    while i < min(len(dividend), len(divider)):
        try:
            if divider[i] == 0:
                raise MyDivisionByNullError("Деление на ноль недопустимо")
            print(round(dividend[i] / divider[i]))
        except Exception as err:
            print(err)
        i += 1

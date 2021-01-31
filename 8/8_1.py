# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры
# на реальных данных.

class Data:
    def __init__(self, data: str):
        self.data = data

    @classmethod
    def get_date(cls, data: str):
        """извлекает число, месяц, год и преобразовывет их тип к типу «Число»"""
        data_list = data.split('-')
        day = int(data_list[0])
        month = int(data_list[1])
        year = int(data_list[2])
        return [day, month, year]

    @staticmethod
    def data_validation(line):
        """проводит валидацию числа, месяца и года"""
        try:
            from datetime import datetime
            current_year = datetime.now().year
            data_list = line.split('-')
            day = int(data_list[0])
            month = int(data_list[1])
            year = int(data_list[2])
            if 0 < day < 32 and month in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12} and year <= current_year:
                if month in {4, 6, 9, 11} and day > 30:
                    print('В апреле, июне, сентябре и ноябре 30 дней')
                    raise ValueError
                elif month == 2:
                    if (year % 400 == 0 and day < 30) or (year % 400 != 0 and day < 29):
                        return line
                    else:
                        print('В феврале 28 дней, в високосный год - 29')
                else:
                    return line
            else:
                print('Некорректная дата')
        except Exception as err:
            print("Ошибка:", err)


today = Data(data='26-01-2021')
print(Data.get_date('26-01-2021'))
print(Data.get_date(today.data_validation('30-11-2021')))
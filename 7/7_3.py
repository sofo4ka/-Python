# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы
# методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных
# двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
# метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
# аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
# строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
# строку: *****\n*****\n*****.

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if int(self.quantity) > int(other.quantity):
            return Cell(self.quantity - other.quantity)
        else:
            print('Разность количества ячеек двух клеток меньше нуля')

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        try:
            return Cell(round(self.quantity // other.quantity))
        except Exception as err:
            print("Ошибка:", err)

    def make_order(self, quantity_in_row):
        try:
            number_of_rows = int(self.quantity / int(quantity_in_row))
            row = str()
            if self.quantity % quantity_in_row == 0:
                for i in range(number_of_rows - 1):
                    row += f"{'*' * quantity_in_row}\\n"
                row += f"{'*' * quantity_in_row}"
            else:
                for i in range(number_of_rows):
                    row += f"{'*' * quantity_in_row}\\n"
                row += f"{'*' * (self.quantity % quantity_in_row)}"
            return row
        except Exception as err:
            print("Ошибка:", err)


c1 = Cell(12)
c2 = Cell(15)
print((c1 + c2).quantity)
print((c2 - c1).quantity)
print((c1 * c2).quantity)
print((c2 / c1).quantity)
print(c1.make_order(5))
print(c2.make_order(5))
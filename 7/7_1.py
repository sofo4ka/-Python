# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.
from random import randint
class Matrix:
    def __init__(self, spisok_spiskov):
        self.spisok_spiskov = spisok_spiskov

    def __str__(self):
        for i in self.spisok_spiskov:
            for j in i:
                print(j, end=' ')
            print(' ')
        print(' ')

    def __add__(self, other):
        result_matrix = []
        for i in range(len(self.spisok_spiskov)):
            result_line = []
            for j in range(len(self.spisok_spiskov[0])):
                result_line.append(int(self.spisok_spiskov[i][j]) + int(other.spisok_spiskov[i][j]))
            result_matrix.append(result_line)
        return Matrix(result_matrix)

m = [[randint(-50, 50) for i in range(3)] for j in range(3)]
m2 = [[randint(-50, 50) for i in range(3)] for j in range(3)]
m3 = [[randint(-50, 50) for i in range(3)] for j in range(3)]
test_matrix = Matrix(m)
test_matrix2 = Matrix(m2)
test_matrix3 = Matrix(m3)
# test_matrix.__str__()
# test_matrix2.__str__()
# test_matrix3.__str__()

print(test_matrix + test_matrix2 + test_matrix3)
c = 1
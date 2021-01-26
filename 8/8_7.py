# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag
        self.complex = complex(real, imag)

    def __str__(self):
        return self.complex.__str__()

    def __add__(self, other):
        complex_sum_real = self.real + other.real
        complex_sum_imag = self.imag + other.imag
        return Complex(complex_sum_real, complex_sum_imag)

    def __mul__(self, other):
        complex_mul_real = self.real * other.real - self.imag * other.imag
        complex_mul_imag = self.real * other.imag + self.imag * other.real
        return Complex(complex_mul_real, complex_mul_imag)


if __name__ == '__main__':
    c1 = Complex(10, 5)
    c2 = Complex(7, 0)
    c3 = Complex(1, 3)
    print(c1 + c2 + c3)
    print(c1 * c2)
    print(c1 * c2 * c3)

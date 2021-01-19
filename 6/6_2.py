# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см
# толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation(self):
        """Расчет массы асфальта, необходимого для покрытия всего дорожного полотна. Формула:
        длина * ширина * (масса асфальта для покрытия 1 м2 дороги асфальтом, толщиной в 1 см) * толщина в см"""
        print('Масса асфальта в тоннах: ')
        return self._length * self._width * 25 * 5 / 1000


r = Road(length=5000, width=20)
print(r.mass_calculation())

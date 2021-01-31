# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import abstractmethod, ABC


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def fabric_consumption_calc(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super(Coat, self).__init__(name)
        self.size = size


    def fabric_consumption_calc(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, name, height):
        super(Suit, self).__init__(name)
        self.height = height

    def fabric_consumption_calc(self):
        return round(2 * self.height + 0.3, 2)


if __name__ == '__main__':
    c = Coat('красное пальто', size=42)
    s = Suit('чёрный костюм', 170)
    print(c.fabric_consumption_calc())
    print(s.fabric_consumption_calc())

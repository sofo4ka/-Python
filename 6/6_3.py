# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
        self._full_income_value = self._income.get('wage') + self._income.get('bonus')

    def get_full_name(self):
        """Метод получения полного имени сотрудника"""
        return f'Полное имя: {self.name} {self.surname}'

    def get_total_income(self):
        """Метод получения дохода с учетом премии"""
        return f'Доход с учетом премии: {self._full_income_value} руб.'


if __name__ == '__main__':
    income_ivanov = {'wage': 100000, 'bonus': 20000}
    p = Position(name='Иван', surname='Иванов', position='пилот', income=income_ivanov)
    print(p.get_full_name())
    print(p.get_total_income())

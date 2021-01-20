# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed}')

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn_direction(self):
        print('машина повернула')


class TownCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        if self.speed <= 60:
            print(f'Текущая скорость автомобиля: {self.speed}')
        else:
            print(f'Превышение установленной скорости движения транспортного средства, равной 60 км/ч!!!' \
                  f'Текущая скорость автомобиля: {self.speed}')


class SportCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)


class WorkCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        if self.speed <= 40:
            print(f'Текущая скорость автомобиля: {self.speed}')
        else:
            print(f'Превышение установленной скорости движения транспортного средства, равной 40 км/ч!!!' \
                  f'Текущая скорость автомобиля: {self.speed}')


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)


if __name__ == '__main__':
    t = TownCar(speed=48, color='green', name='УАЗ-3303', is_police=False)
    s = SportCar(speed=180, color='red', name='Ferrari 488', is_police=False)
    w = WorkCar(speed=50, color='black', name='ВАЗ-2109', is_police=False)
    p = PoliceCar(speed=80, color='white', name='UAZ Patriot', is_police=True)

    print(t.__dict__)
    print(s.__dict__)
    print(w.__dict__)
    print(p.__dict__)

    t.show_speed()
    s.go()
    w.show_speed()
    p.turn_direction()
    p.stop()

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
from abc import abstractmethod, ABC


class Office_equipment_warehouse:
    def __init__(self):
        self.office_equipment_warehouse_dict = {}

    def adding_to_warehouse(self, vendor_code: int, location: str, quantity: int):
        """Приём оргтехники на склад"""
        try:
            equipment_info = {'Местоположение': location, 'Количество на складе': quantity}
            self.office_equipment_warehouse_dict.setdefault(vendor_code, equipment_info)
        except Exception as err:
            print("Ошибка:", err)
        return self.office_equipment_warehouse_dict

    def change_location(self, vendor_code: int, new_location: str):
        """ Передача оргтехникив определенное подразделение компании."""
        try:
            if vendor_code in self.office_equipment_warehouse_dict.keys():
                equipment_info = self.office_equipment_warehouse_dict.get(vendor_code)
                if equipment_info.get('Количество на складе') > 0:
                    new_quantity = equipment_info.get('Количество на складе') - 1
                    equipment_info.update({'Количество на складе': new_quantity})

                    if 'Другие местоположения' not in equipment_info.keys():
                        equipment_info.setdefault('Другие местоположения', [new_location])
                    else:
                        if new_location not in equipment_info.get('Другие местоположения'):
                            location_data_to_write = equipment_info.get('Другие местоположения')
                            location_data_to_write.append(new_location)
                            equipment_info.update({'Другие местоположения': location_data_to_write})
                    self.office_equipment_warehouse_dict.update({vendor_code: equipment_info})
                    return self.office_equipment_warehouse_dict
                else:
                    return 'Нет свободных единиц на складе'
        except Exception as err:
            print("Ошибка:", err)


class Office_equipment(ABC):
    def __init__(self, name, vendor_code: int, manufacturer_code: int, year: int, size, weight, *args, **kwargs):
        self.name = name
        self.vendor_code = vendor_code
        self.manufacturer_code = manufacturer_code
        self.year = year
        self.size = size
        self.weight = weight

    @abstractmethod
    def do_your_thing(self):
        pass


class Printer(Office_equipment):
    def __init__(self, name, vendor_code: int, manufacturer_code: int, year: int, size, weight, printing_technology):
        super().__init__(name, vendor_code, manufacturer_code, year, size, weight)
        self.printing_technology = printing_technology

    def do_your_thing(self):
        print('Печатаем документ')


class Scanner(Office_equipment):
    def __init__(self, name, vendor_code: int, manufacturer_code: int, year: int, size, weight, optic_scan_resolution):
        super().__init__(name, vendor_code, manufacturer_code, year, size, weight)
        self.optic_scan_resolution = optic_scan_resolution

    def do_your_thing(self):
        print('Сканируем документ')


class Xerox(Office_equipment):
    def __init__(self, name, vendor_code: int, manufacturer_code: int, year: int, size, weight, print_type):
        super().__init__(name, vendor_code, manufacturer_code, year, size, weight)
        self.print_type = print_type

    def do_your_thing(self, quantity: int):
        for i in range(quantity):
            print('Ксерокопируем документ')


if __name__ == '__main__':
    sklad = Office_equipment_warehouse()
    printer1_dict = { 'name': 'HP LaserJet Pro M15w', 'vendor_code': 45678904, 'manufacturer_code': 34567820,
                      'year': 2020, 'size': '346 x 280 x 348 мм', 'weight': 3.8, 'printing_technology': 'laser' }
    printer1 = Printer(**printer1_dict)
    print(printer1.__dict__)
    printer1.do_your_thing()
    sklad.adding_to_warehouse(location='1А', quantity=2, vendor_code=printer1.vendor_code)
    scanner1_dict = { 'name': 'EPSON WorkForce DS-80W', 'vendor_code': 23456768, 'manufacturer_code': 56789340,
                      'year': 2019, 'size': '272 x 47 x 34мм', 'weight': 0.3, 'optic_scan_resolution': '600x600dpi' }
    scanner1 = Scanner(**scanner1_dict)
    print(scanner1.__dict__)
    scanner1.do_your_thing()
    sklad.adding_to_warehouse(location='1B', quantity=1, vendor_code=scanner1.vendor_code)
    xerox1_dict = { 'name': 'CANON imageRUNNER 2206iF', 'vendor_code': 34000000, 'manufacturer_code': 13456777,
                    'year': 2020, 'size': '622x606x607мм', 'weight': 36.1, 'print_type': 'b/w' }
    xerox1 = Xerox(**xerox1_dict)
    print(xerox1.__dict__)
    xerox1.do_your_thing(3)
    sklad.adding_to_warehouse(location='2А', quantity=3, vendor_code=xerox1.vendor_code)
    print(sklad.office_equipment_warehouse_dict)
    print(sklad.change_location(vendor_code=printer1.vendor_code, new_location='3 офис'))
    print(sklad.change_location(vendor_code=printer1.vendor_code, new_location='4 офис'))
    print(sklad.change_location(vendor_code=printer1.vendor_code, new_location='4 офис'))
    print(sklad.change_location(vendor_code=xerox1.vendor_code, new_location='4 офис'))

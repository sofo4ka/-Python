# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary_culc_func(hours_of_work, salary_per_hour, prize):
    return (hours_of_work * salary_per_hour) + prize


file_path, hours_of_work, salary_per_hour, prize = argv
print(argv)
print(salary_culc_func(int(hours_of_work), int(salary_per_hour), int(prize)))

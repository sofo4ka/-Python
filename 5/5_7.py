# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

firms = { }
average_profit_dict = { }
sum_of_profits = 0
cnt1 = 0
with open("testfile7.txt", "r", encoding="utf-8") as file_object:
    new_file = file_object.readlines()
    for line in new_file:
        cnt = 0
        for element in line.split(' '):
            cnt += 1
            if cnt == 1:
                firm_name = element
            elif cnt == 3:
                proceeds = int(element)
            elif cnt == 4:
                costs = int(element)
        profit = proceeds - costs
        firms.setdefault(firm_name, profit)
        if costs <= proceeds:
            sum_of_profits += profit
            cnt1 += 1
    average_profit_dict.setdefault('average_profit', sum_of_profits / cnt1)

final_list = [firms, average_profit_dict]
with open("testfile7_1.json", "w") as write_f:
    json.dump(final_list, write_f)

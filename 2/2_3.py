# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

year_list = [['зима', 1, 2, 12], ['весна', 3, 4, 5], ['лето', 6, 7, 8], ['осень', 9, 10, 11]]
year_dict = {'зима': [1, 2, 12],
             'весна': [3, 4, 5],
             'лето': [6, 7, 8],
             'осень': [9, 10, 11]}
while True:
    try:
        month = int(input('Введите месяц в виде целого числа от 1 до 12:'))
        if 1 <= month <= 12:
            break
    except ValueError:
        print('Некорректный ввод')
    else:
        print('Некорректный ввод')

for j in year_list:
    if month in j:
        print(j[0])

for i in year_dict.keys():
    if month in year_dict[i]:
        print(i)

#Более дешевый вариант by luchanos:
seasons_dict = {
        1: "winter",
        2: "winter",
        3: "spring",
        4: "spring",
        5: "spring",
        6: "summer",
        7: "summer",
        8: "summer",
        9: "autumn",
        10: "autumn",
        11: "autumn",
        12: "winter"}

seasons_list = ["winter",
                "winter",
                "spring",
                "spring",
                "spring",
                "summer",
                "summer",
                "summer",
                "autumn",
                "autumn",
                "autumn",
                "winter"]

try:
    month1 = int(input("Enter the month: "))
    print(f"FROM DICT: Month {month1} is {seasons_dict[month1]} month")
    print(f"FROM LIST: Month {month1} is {seasons_list[month1 - 1]} month")
except ValueError as err:
    print("Wrong value has been entered!", err)
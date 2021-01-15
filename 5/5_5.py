# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

def get_numbers():
    while True:
        try:
            input_data = input('Введите набор чисел через пробел: ')
            for element in input_data.split(' '):
                element = float(element)
            return input_data
        except Exception as err:
            print("Ошибка ввода")


with open("testfile5.txt", "w", encoding="utf-8") as file_object:
    file_object.writelines(get_numbers())

sum_of_numbers = 0

with open("testfile5.txt", "r", encoding="utf-8") as file_object1:
    output_data = file_object1.readline()
    for element in output_data.split(' '):
        sum_of_numbers += float(element)
        print(element)
    print(f'Сумма чисел в файле: {sum_of_numbers}')

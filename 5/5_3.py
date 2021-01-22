# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.

sum_of_salaries = 0
cnt_of_workers = 0
workers_with_low_salary = []

with open("testfile3.txt", "r", encoding="utf-8") as file_object:
    for line in file_object:
        new_line = line.split(', ')
        cnt_of_workers += 1
        sum_of_salaries += float(new_line[1])
        if float(new_line[1]) <= 20000:
            workers_with_low_salary.append(new_line[0])

print(f'Общее число сотрудников: {cnt_of_workers}')
print(f'Средняя зарплата: {round(sum_of_salaries/cnt_of_workers)}')
print('Cотрудники c окладом менее 20 тыс рублей: ')
for i in workers_with_low_salary:
    print(i)

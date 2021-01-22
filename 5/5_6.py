# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
# по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

school_subjects = {}

with open("testfile6.txt", "r", encoding="utf-8") as file_object:
    new_file = file_object.readlines()
    for line in new_file:
        sum_of_hours = 0
        cnt = 0
        for element in line.split(' '):
            cnt += 1
            if cnt == 1:
                subject_name = element[0:len(element)-1]
            else:
                try:
                    hours = element.split('(')
                    sum_of_hours += int(hours[0])
                except Exception as err:
                    pass
        school_subjects.setdefault(subject_name, sum_of_hours)

print(school_subjects)

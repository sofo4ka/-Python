# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

cnt = 0

with open("testfile2.txt", "r", encoding="utf-8") as file_object:
    for line in file_object:
        line_length = len(line)
        cnt += 1
        print(f'Длина {cnt} строки {line_length}')

print(f'В файле {cnt} строк')


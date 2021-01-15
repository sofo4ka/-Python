# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

new_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
full_data_to_write = []

with open("testfile4.txt", "r", encoding="utf-8") as file_object:
    for line in file_object:
        new_line = line.split(' — ')
        data_to_write = new_dict.get(new_line[0]) + ' - ' + new_line[1]
        full_data_to_write.append(data_to_write)


file_object_1 = open("testfile4_2.txt", "w", encoding="utf-8")
file_object_1.writelines(full_data_to_write)
file_object_1.close()

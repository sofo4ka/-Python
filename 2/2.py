# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

spisok = [2021, 'с', 'новым', 'годом', 20.21, None]
n = 0
try:
    n = int(input('Введите число элементов, которым вы хотите дополнить список:'))
except ValueError:
    print('Некорректный ввод')
for j in range(n):
    new_data = input('Введите элемент: ')
    try:
        spisok.append(float(new_data))
    except ValueError:
        if new_data == 'True':
            spisok.append(True)
        elif new_data == 'False':
            spisok.append(False)
        elif new_data == 'None':
            spisok.append(None)
        spisok.append(new_data)
print(spisok)

i = 0
if len(spisok) // 2 == 0:
    while i < len(spisok):
        spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
        i = i + 2
else:
    while i < len(spisok) - 1:
        spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
        i = i + 2
print(spisok)

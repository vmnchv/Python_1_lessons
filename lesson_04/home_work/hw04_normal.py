# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
# 1. Решение с помощью re

import re
line='mtMmEZUOmcq'
line_str = re.findall(r'[a-z]+', line)
print('Символы в нижнем регистре с использованием модуля re: \n',line_str)

# 2. Решение без re
# print(ord('A'), ord('Z'))
line='mtMmEZUOmcq'
symbol = list(map(lambda x: chr(x), list(range(65,91)))) # Преобразуем список из кодов ANSI в список букв A-Z
line_new = list(line)

for i , element in enumerate(line_new[:]):
    for element_2 in symbol:
        if element == element_2:
            line_new[i] = ' '
print('Символы в нижнем регистре : \n',line_new)
# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
import re
line_2='GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec'
print(line_2)
line_2_str = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line_2)
print('Список с использованием модуля re: \n',line_2_str)

#2 без re
# 2. Решение без re
line_2='GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec'
print(line_2)
symbol1 = list(map(lambda x: chr(x), list(range(65, 91)))) # Преобразуем список из кодов ANSI в список букв A-Z
symbol2 = list(map(lambda x: chr(x), list(range(97, 123)))) # Преобразуем список из кодов ANSI в список букв a-z
line_new = list(line_2)

lst = []
i = len(line_new) - 1
# Находим  символ в верхнем регистре после которого стоят еще два символа в верхнем регистре
while i >= 0:
    if line_new[i] in symbol2:
         lst.append(line_new[i])
    elif line_new[i] in symbol1 and i <= len(line_new) - 3 and line_new[i+1] in symbol1 and line_new[i+2] in symbol1:
        lst.append(line_new[i])
    else:
        lst.append(' ')
    i -= 1
lst.reverse() # Переворачиваем список

i = 0
lst2 = []
registr = True  # Начальное условие поиска сортировки символов в верхнем регистре
# Фильтрация списка.
while i <= len(lst)-1:
    if lst[i] in symbol2:
        registr = True
    if lst[i] in symbol1 and lst[i-1] in symbol2 and lst[i-2] in symbol2:
        lst2.append(lst[i])
        registr = False
    elif lst[i] in symbol1 and registr == False:
        lst2.append(lst[i])
    else:
        lst2.append(' ')
    i += 1
stroka=''.join(lst2).split(' ') # Преобразование в строку и разбиение по пробелам

line_str_3 = [i for i in stroka if i != ''] # Формирование выхрдного списка из строки
print('Список без использованием модуля re: \n',line_str_3)
print('------------------------------------------------------')


# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import random
MAX_CHISLO = 2500
spisok = [random.randint(0,9) for _ in range(MAX_CHISLO)]
spisok1 = ''.join(list(map(lambda x: str(x), spisok)))
print(spisok1)
# Запись в файл
path = 'spisok' + '.txt'
with open(path, 'w', encoding='UTF-8') as file:
    file.write(str(spisok))

# Чтение файла
with open(path, 'r', encoding='UTF-8') as file:
    stroka_1 = list(file.read())
print(stroka_1)


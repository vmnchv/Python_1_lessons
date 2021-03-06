#Murad Munchaev
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.


# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ['APPLE', 'MELON', 'Банан', 'Арбуз', 'Абрикос', 'Апельсин']
for num, frut in enumerate (fruits,1):
   print (str(num) + '.  {:>8}'.format(frut))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке и выведите результат.
spisok1 = ['Книга', 'Тетрадь', 'Ручка', 'Шар', 'Парта', 'Перо', 'Телефон', 3, -5, 1000]
spisok2 = ['Книга', 'Шар', 'Парта', 'Телефон', 'Карандаш', -5]
print('Первый список: {}'.format(spisok1))
print('Второй список: {}'.format(spisok2))

for el in spisok1[:]:
    for el2 in spisok2[:]:
        if el2 == el:
         spisok1.remove(el2)
print('Элементы из первого списка, которых нет во втором: {}'.format(spisok1))


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
# и выведите результат

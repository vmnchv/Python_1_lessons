#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      mnchv
#
# Created:     22.10.2018
# Copyright:   (c) mnchv 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""
fruits = ['Груша', 'Киви', 'Банан', 'Яблоко', 'Абрикос', 'Апельсин']
for num, frut in enumerate (fruits):
    print (str(num) + '.  {:>8}'.format(frut))
"""
num  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
new_num = []
#
print(num)
#
#
for el in reversed(num):
    count = num.index(el)
    if (el % 2) == 0:
          new_el= el/4
          new_num.insert(0, new_el)
          num.remove(el)
#
    else:
          el = el*2
          num[count] = el
#
print(num)
print(new_num)
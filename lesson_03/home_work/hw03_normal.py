__author__ = "Munchaev Murad"

from testfunc import test

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    res = []
    last=0
    next=1
    for i in range(m+1):
        # print ("i={}, last={}, next={}".format(i,last,next))
        if i >= n: res.append(next)
        last,next = next,next+last
    return res

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
# Комментарий: пузырьковая сортировка


def sort_to_max(origin_list):
    res=origin_list[:]
    for i in range(1,len(origin_list)):
        j=i
        while (res[j]<res[j-1]) and (j>0):
            res[j],res[j-1] = res[j-1],res[j]
            j-=1
    return res

# sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func,iter):
    res=[]
    for i in iter:
        if func(i):
            res.append(i)
    return res

def my_iter_filter(func,iter):
    for i in iter:
        if func(i):
            yield i

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
# Комментарий: используется свойство - диагонали параллелограмма делятся пополам в одной точке.
# Дополнительно проверяется равенство любых 2-х точек, что позволяет выявить вырожденный случай, когда
# все 4 точки равны. Для уменьшения числа операций можно рядом с a1==a3 сравнивать через or a2==a4.
def isparallelogramm(a1,a2,a3,a4):
    def centerpoint(a,b):
        return ((a[0]+b[0])/2,(a[1]+b[1])/2)
    if a1 == a3: return False
    return centerpoint(a1,a3) == centerpoint(a2,a4)


print("Задача 1. Ряд Фибоначчи.")
test("2-5",fibonacci(2,5),[2,3,5,8])
test("0-4",fibonacci(0,4),[1,1,2,3,5])
test("1-8",fibonacci(1,8),[1,2,3,5,8,13,21,34])

print("\nЗадача 2. Сортировка.")
test("1",sort_to_max([8,7,6,5,4,3,2,1]),[1,2,3,4,5,6,7,8])
test("2",sort_to_max([8,7,12,6,10,5,9,4,3,11,2,1]),[1,2,3,4,5,6,7,8,9,10,11,12])

print("\nЗадача 3. Filter")
test("my_filter 1",my_filter(lambda x:x>=0,[-1,2,4,-8,0,6]),[2,4,0,6])
test("my_filter 2",my_filter(lambda x:x>1,[-1,2,4,-8,0,6]),[2,4,6])
test("my_iter_filter 1",list(my_iter_filter(lambda x:x>=0,[-1,2,4,-8,0,6])),[2,4,0,6])
test("my_iter_filter 2",list(my_iter_filter(lambda x:x>1,[-1,2,4,-8,0,6])),[2,4,6])

print("\nЗадача 4. Параллелограмм.")
test("1",isparallelogramm((1,1),(1,1),(1,1),(1,1)),False)
test("1",isparallelogramm((1,1),(0,0),(1,1),(1,1)),False)
test("1",isparallelogramm((1,1),(1,1),(0,1),(1,1)),False)
test("1",isparallelogramm((0,0),(2,1),(7,1),(5,0)),True)
test("1",isparallelogramm((0,0),(2,8),(7,1),(5,0)),False)
test("1",isparallelogramm((0,0),(2,2),(4,0),(2,-2)),True)
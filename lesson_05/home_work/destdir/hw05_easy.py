# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
try:
    for i in range(1, 10):
        os.mkdir("dir_" + str(i))
except:
    print("Already exist")



a = input("enter something ")
print(a)

try:
    for i in range(1, 10):
        os.rmdir("dir_" + str(i))
except:
    print("Already removed")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os
list = os.listdir()
for j in list:
    print(j)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys
import os

destdir = os.path.abspath('destdir')
if not os.path.exists(destdir):
    os.makedirs(destdir)

# с использованием системного shell'а
os.system('copy %s %s' % (__file__,destdir))
"""
# другой вариант - с получением полного имени скрипта через sys.argv[0]
os.system('copy %s %s' % (sys.argv[0],destdir))

# без shell'а
dirname,filename = os.path.split(__file__)
content = open(__file__).read()
open(os.path.join(destdir,filename),'w').write(content)

"""
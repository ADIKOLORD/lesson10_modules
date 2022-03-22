"""
from random import choice
list_names = ['Adilet', 'Asel', 'Danislan', 'Ilyas', 'Bakyt', 'Askat']
com1 = []
com2 = []
while list_names != []:
    i = choice(list_names)
    if len(com1) <= int(len(list_names) / 2):
        com1.append(i)
        list_names.remove(i)
    else:
        com2.append(i)
        list_names.remove(i)
print(com1)
print(com2)
"""

# Problem 1

"""
import my_module
my_module
"""

# Problem 2
"""
from random import randint

names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
four_name = []
for i in range(4):
    r = randint(0, len(names) - 1)
    four_name.append(names[r])
    names.pop(r)
"""

# Problem 3
"""
import os
print(os.name)
"""

# Problem 4
"""
import os
from random import randint

for i in range(5):
    r = randint(1, 30)
    os.system(f'touch /home/adiko/Desktop{r}.txt')
"""

# Problem 5
"""
from random import choice, randint
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
com1 = []
com2 = []
com3 = []
com4 = []
count = 1
len_com = int(len(names) / 4)

while names != []:
    r = choice(names)
    if count <= len_com:
        com1.append(r)
        names.remove(r)
    elif count <= len_com * 2:
        com2.append(r)
        names.remove(r)
    elif count <= len_com * 3:
        com3.append(r)
        names.remove(r)
    else:
        com4.append(r)
        names.remove(r)
    count += 1
"""

# Problem 6
"""
import sys
print(eval(input()))
"""

# Problem 7
"""
import sys
first = input('>>> ')
second = input('>>> ')
if sys.getsizeof(first) > sys.getsizeof(second):
    print(f'Big size of {first} == {sys.getsizeof(first)}')
else:
    print(f'Big size of {second} == {sys.getsizeof(second)}')
"""

# Problem 8
"""
n = int(input('>>> '))
password = ''
for i in range(n):
    r = randint(0,9)
    password += str(r)
print(password)
"""

# Problem 9
"""
from random import randint
from time import sleep

print('Здравствуйте! Давайте сыграем игру "камень-ножница-бумага"')

input('Нажмите Enter если готовы >>> ')
com_count = 0
user_count = 0
while True:
    r = randint(0, 2)
    atributs = ['Камень', 'Бумага', 'Ножница']
    print('Выберите одного из трёх "камень-ножница-бумага"')
    input('Нажмите Enter если готовы >>> ')

    for i in range(3, 0, -1):
        print(f'Игра начнётся через {i}')
        sleep(1)

    print(f'Я выбрал {atributs[r]}')
    sleep(2)
    user = input('А вы какую выбрали? если\
     \n"Камень" нажмите "0"\
      \n"Бумага" нажмите "1"\
       \n"Ножница" нажмите "2"\n')

    if int(user) == 0 and r == 2:
        print('Поздравляю вы выиграли! :)')
        user_count += 1

    elif int(user) == 2 and r == 0:
        print('Оо я выиграл! :)')
        com_count += 1

    elif int(user) == r:
        print('Оо ничья  :)')

    elif int(user) < r:
        print('Оо я выиграл! :)')
        com_count += 1

    elif int(user) > r:
        print('Поздравляю вы выиграли! :)')
        user_count += 1

    else:
        print('Вы ввели неправильную цифру')

    clarify = input('Хотите заново? Д/Н >>> ')  # clarify - тактоо деген

    if clarify in 'ДдYyyesYesДада':
        continue
    else:
        print(f'Ваше очко: {user_count} \nМоё очко: {com_count}')
        break
"""

# Problem 10
"""
from random import randrange

r = randrange(6, 12, 2)
print(r)
n = randrange(5, 100, 5)
print(n)
"""

# Problem 11
"""
os.name - имя операционной системы. Доступные варианты: 'posix', 'nt', 'mac', 'os2', 'ce', 'java'.

os.environ - словарь переменных окружения. Изменяемый (можно добавлять и удалять переменные окружения).

os.getlogin() - имя пользователя, вошедшего в терминал (Unix).

os.getpid() - текущий id процесса.

os.uname() - информация об ОС. возвращает объект с атрибутами: sysname - имя операционной системы, nodename - имя машины в сети (определяется реализацией), release - релиз, version - версия, machine - идентификатор машины.

os.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True) - проверка доступа к объекту у текущего пользователя. Флаги: os.F_OK - объект существует, os.R_OK - доступен на чтение, os.W_OK - доступен на запись, os.X_OK - доступен на исполнение.

os.chdir(path) - смена текущей директории.

os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True) - смена прав доступа к объекту (mode - восьмеричное число).

os.chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True) - меняет id владельца и группы (Unix).

os.getcwd() - текущая рабочая директория.

os.link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True) - создаёт жёсткую ссылку.

os.listdir(path=".") - список файлов и директорий в папке.

os.mkdir(path, mode=0o777, *, dir_fd=None) - создаёт директорию. OSError, если директория существует.

os.makedirs(path, mode=0o777, exist_ok=False) - создаёт директорию, создавая при этом промежуточные директории.

os.remove(path, *, dir_fd=None) - удаляет путь к файлу.

os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None) - переименовывает файл или директорию из src в dst.

os.renames(old, new) - переименовывает old в new, создавая промежуточные директории.

os.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None) - переименовывает из src в dst с принудительной заменой.

os.rmdir(path, *, dir_fd=None) - удаляет пустую директорию.

os.removedirs(path) - удаляет директорию, затем пытается удалить родительские директории, и удаляет их рекурсивно, пока они пусты.

os.symlink(source, link_name, target_is_directory=False, *, dir_fd=None) - создаёт символическую ссылку на объект.

os.sync() - записывает все данные на диск (Unix).

os.truncate(path, length) - обрезает файл до длины length.

os.utime(path, times=None, *, ns=None, dir_fd=None, follow_symlinks=True) - модификация времени последнего доступа и изменения файла. Либо times - кортеж (время доступа в секундах, время изменения в секундах), либо ns - кортеж (время доступа в наносекундах, время изменения в наносекундах).

os.walk(top, topdown=True, onerror=None, followlinks=False) - генерация имён файлов в дереве каталогов, сверху вниз (если topdown равен True), либо снизу вверх (если False). Для каждого каталога функция walk возвращает кортеж (путь к каталогу, список каталогов, список файлов).

os.system(command) - исполняет системную команду, возвращает код её завершения (в случае успеха 0).

os.urandom(n) - n случайных байт. Возможно использование этой функции в криптографических целях.

os.path - модуль, реализующий некоторые полезные функции на работы с путями.
"""

# Problem 12
from datetime import datetime
today = datetime.today()
print(today.date())
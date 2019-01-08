# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


os.chdir(path) # cd
# ls - отображение полного пути текущей директории
def cd_change():
    import os
    b = input("Укажите путь к директории")
    try:
        os.chdir(r'{}'.format(b))
    except OSError:
        print("Вы неперешли в {} ".format(b))
    else:
        print("Вы перешли в {}  ".format(b))


def cp_copy():
    import shutil
    import os
    a = input("Укажите файл который нужно скопировать")
    try:
        b = str(os.path.abspath(os.curdir)) + str("/{}".format(a))
        shutil.copy(r'{}'.format(b), r'new_file.py')
    except OSError:
        print("Файл {} не создан ".format(a))
    else:
        print("Файл {} создан ".format(a))


def rm_remove():
    import os
    a = input("Укажите файл который удалить ")
    c = input("Если вы хотите удалить файл, нажмите 1")
    if int(c) == 1:
        try:
            b = str(os.path.abspath(os.curdir)) + str("/{}".format(a))
            os.remove(r'{}'.format(b))
        except OSError:
            print("Файл {} неможет быть удален ".format(a))
        else:
            print("Файл {} удален ".format(a))
    else:
        print("Файл {} остался в текущей директории".format(a))
def ls_full_path:
    print(os.path.dirname(os.path.abspath(__file__)))
ls_full_path()


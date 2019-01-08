# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
print('sys.argv = ', sys.argv)
input()


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")
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
def ls_full_path ():
    print(os.path.dirname(os.path.abspath(__file__)))

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "ls": ls_full_path,
    "rm": rm_remove,
    "cp": cp_copy,
    "cd": cd_change
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
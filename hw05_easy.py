# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.



def delete_dir():
    import os
    i = 1
    while True:
        a = "dir_" + str(i)


        if a != "dir_10":

            try:
                os.rmdir(a)
            except OSError:
                print("")
            else:
                print("Директория успешно удалена {} ".format(a))
        else:
            break
        i = i + 1

def create_dir():
    import os
    i = 1
    while True:
        a = "dir_" + str(i)


        if a != "dir_10":

            try:
                os.mkdir(a)
            except OSError:
                print("")
            else:
                print("Успешно создана  директория {}".format(a))
        else:
            break
        i = i + 1

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir():
    import os
    print(os.listdir())


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
#def copy_file():
def copy_file():
    import os
    import shutil
    a = os.path.realpath(__file__)
    print(a)
    shutil.copy(r'{}'.format(a), r'new_file.py')







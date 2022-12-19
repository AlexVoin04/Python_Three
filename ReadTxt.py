from prettytable import PrettyTable
import re


def rowAll():
    try:
        my_table = PrettyTable(["id", "last_name", "first_name", "middle_name", "age"])
        my_file = open("DataPeople.txt", encoding='utf8')
        s: list = my_file.readlines()
        a: int = 0

        while a < len(s):
            line: str = len(s[a])
            if a + 1 == len(s):
                id_user, surname, name, patronymic, age = map(str, s[a].split())
                my_table.add_row([id_user, surname, name, patronymic, age])
            else:
                remove_last: str = s[a][:line - 1]
                id_user, surname, name, patronymic, age = map(str, remove_last.split())
                my_table.add_row([id_user, surname, name, patronymic, age])
            a += 1
        print(my_table)
    except SyntaxError:
        print("Ошибка чтения файла!")
    except:
        print("Шото пошло не так")


def rowOutput(row):
    try:
        my_table = PrettyTable(["id", "last_name", "first_name", "middle_name", "age"])
        my_file = open("DataPeople.txt", encoding='utf8')
        s: list = my_file.readlines()
        a: int = 0
    

        while a < row:
            line: str = len(s[a])
            if a + 1 == len(s):
                id_user, surname, name, patronymic, age = map(str, s[a].split())
                my_table.add_row([id_user, surname, name, patronymic, age])
            else:
                remove_last: str = s[a][:line - 1]
                id_user, surname, name, patronymic, age = map(str, remove_last.split())
                my_table.add_row([id_user, surname, name, patronymic, age])
            a += 1
        print(my_table)
    except SyntaxError:
        print("Ошибка чтения файла!")
    except:
        print("Шото пошло не так")

def gat_table_result(row):
    try:
        my_table = PrettyTable(["id", "last_name", "first_name", "middle_name", "age"])
        my_file = open("DataPeople.txt", encoding='utf8')
        s: list = my_file.readlines()
        a: int = 0

        if (row == 'all'):
            sravn = len(s)
        else:
            sravn = row

        while a < sravn:
            line: str = len(s[a])
            if a + 1 == len(s):
                id_user, surname, name, patronymic, age = map(str, s[a].split())
                my_table.add_row([id_user, surname, name, patronymic, age])
            else:
                remove_last: str = s[a][:line - 1]
                id_user, surname, name, patronymic, age = map(str, remove_last.split())
                my_table.add_row([id_user, surname, name, patronymic, age])
            a += 1
        print(my_table)
    except SyntaxError:
        print("Ошибка чтения файла!")
    except:
        print("Что-то пошло не так ...")


if __name__ == '__main__':
    while True:
        try:
            strok = input("show data all для вывода всех записей, show data n, где n количество записей\n")
            try:
                result = re.search(r'show data (\d+)', strok)
                if result:
                    records = strok.split(' ')
                    gat_table_result(int(records[2]))
                else:
                    result = re.search(r'show data all', strok)
                    if result.group(0) == "show data all":
                        records = result.group(0).split(' ')
                        gat_table_result(records[2])
            except:
                print("Что-то пошло не так ...")
                
        except AttributeError:
            print("такой команды нет")
        except KeyboardInterrupt:
            print('Выход')
            exit()
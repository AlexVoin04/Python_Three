from prettytable import PrettyTable
import re


""" Получение данных от пользователя """
def getData():
    while True:
        try:
            check: str = input("Введите 'y' для добавления данных, 'n' для завершения, show data all для вывода всех записей и show data n, где n количество записей: ")
            #check: str = input()
            result_n = re.search(r'show data (\d+)', check)
            result_all = re.search(r'show data all', check)
            if check in ["y", "Y", "yes", "Yes", "YES"]:
                try:
                    print('Введите номер, ФИО и возраст:')
                    id_user, surname, name, patronymic, year = map(str, input().split())
                    print(f"Вы ввели: {id_user} {surname} {name} {patronymic} {year}")
                    assert year.isdigit(), id_user.isdigit()

                    # Запись данных в файл
                    my_file = open("DataPeople.txt", "a", encoding='utf8')
                    my_file.write(f"{id_user} {surname} {name} {patronymic} {year}\n")
                    print("Данные были записаны в файл\n")
                    
                except ValueError:
                    print('Не правильно внесены данные!')
                except KeyboardInterrupt:
                    print('Выход')
                except PermissionError:
                    print('У вас нет доступа к данному файлу!')
                except:
                    print('Ошибка!')
                finally:
                    my_file.close()  
            elif result_n:
                records = check.split(' ')
                gat_table_result(int(records[2]))
            elif result_all:
                if result_all.group(0) == "show data all":
                    records = result_all.group(0).split(' ')
                    gat_table_result(records[2])
            elif check in ["n", "N", "no", "No", "NO"]:
                print("Выход")
                break
            else:
                print('Нет такой команды')

        except KeyboardInterrupt:
            print('Выход')
            exit()
        except:
            print("Что-то пошло не так ...")

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
    getData()
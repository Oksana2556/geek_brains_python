from csv import DictWriter, DictReader
from os.path import exists

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

filename = 'phone.csv'
filename_from = 'phone_2.csv'

def get_data():
    flag = False
    while not flag:
        try: 
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Слишком короткое имя")
            last_name = input("Введите фамилию: ")
            if len(last_name) < 2:
                raise NameError("Слишком короткая фамилия")
            phone = input("Введите номер телефона: ")
            if len(phone) < 11:
                raise NameError("Неверный номер телефона")
            for i in phone:
                if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+']:
                    raise NameError("Неверный номер телефона")
        except NameError as err:
            print(err)

        else:
            flag = True

    return [first_name, last_name, phone]

def create_file(filename):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames = ['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)

def write_file(filename, lst):
    res = read_file(filename)
    obj = {'Имя': lst[0], 'Фамилия' : lst[1], 'Телефон' : lst[2]}
    res.append(obj)
    standart_write(filename, res)

def row_search(filename):
    last_name = input("Введите фамилию: ")
    res = read_file(filename)
    for row in res:
        if last_name == row['Фамилия']:
            return row
    return 0

def delete_row(filename):
    row_number = int(input("Введите номер строки: ")) - 1
    res = read_file(filename)
    res.pop(row_number)
    standart_write(filename, res)

def standart_write(filename, res):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames = ['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)

def change_row(filename):
    row_number = int(input("Введите номер строки: ")) - 1
    res = read_file(filename)
    data = get_data()
    res[row_number]['Имя'] = data[0]
    res[row_number]['Фамилия'] = data[1]
    res[row_number]['Телефон'] = data[2]
    standart_write(filename, res)

def copy_row_to_file(filename, filename_from):
    #filename_from = input("Введите имя файла: ")
    string_to_copy = identify_row(filename_from) #<class 'dict'>
    print(string_to_copy)
    res = read_file(filename)
    res.append(string_to_copy)
    standart_write(filename, res)

def identify_row(filename_from):
    row_number = int(input("Введите номер копируемой строки: ")) - 1
    res = read_file(filename_from)
    return res[row_number]


def main():
    while True:
        command = input("Введите команду:\n q - выход\n w - создание и запись\n r - чтение\n f - поиск по фамилии\n d - удаление строки\n ch - поменять строку\n cp - скопировать строку из другого файла\n")
        if command == "q":
            break
        elif command == "w":
            if not exists(filename):
                create_file(filename)
            write_file(filename, get_data())
        elif command == "r":
            if not exists(filename):
                print("Файл не существует, создайте его")
                continue
            print(read_file(filename))
        elif command == "f":
            if not exists(filename):
                print("Файл не существует, создайте его")
                continue
            res = row_search(filename)
            if res: 
                print(res)
            else:
                print("Запись не найдена")
        elif command == "d":
            if not exists(filename):
                print("Файл не существует, создайте его")
                continue
            delete_row(filename)
        elif command == "ch":
            if not exists(filename):
                print("Файл не существует, создайте его")
                continue
            change_row(filename)
        elif command == "cp":
            if not exists(filename) or not exists(filename_from):
                print("Файл не существует, создайте его")
                continue
            copy_row_to_file(filename, filename_from)


main()
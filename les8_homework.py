# Дополнить справочник возможностью копирования данных из одного файла в другой. 
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.


import os


def print_data():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        phonebook_str = file.read()
    print(phonebook_str)
    print()


def input_name():
    return input('Введите имя контакта: ')

def input_surname():
    return input('Введите фамилию контакта: ')

def input_patronymic():
    return input('Введите отчество контакта: ')

def input_phone():
    return input('Введите телефон контакта: ')

def input_address():
    return input('Введите адрес контакта: ').title()


def input_data():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    my_sep = ' '
    return f'{surname} {my_sep} {name} {my_sep} {patronymic} {my_sep} {phone} {address}'


def add_contact():
    new_contact_str = input_data()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(new_contact_str)


def search_contact():
    print('Варианты поиска: \n'
        '1. Поиск по фамилии\n'
        '2. Поиск по имени\n'
        '3. Поиск по отчеству\n'
        '4. Поиск по телефону\n'
        '5. Поиск по адресу\n')
    command = input('Выберете вариант поиска: ')

    while command not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод. Повторите запрос')
        command = input('Выберете ариант поиска: ')

    i_search = int(command) - 1
    search = input('Введите данные для поиска: ').lower()
    print()

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')

    check_cont = False
    for contact_str in contacts_list:
        lst_contact = contact_str.lower().replace('\n', ' ').split()
        if search in lst_contact[i_search]:
            print(contact_str)
            print()
            check_cont = True
        if not check_cont:
            print('Такого контакта нет')

# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

# Копируем строку выбранную пользователем из справочника и записываем в новый файл
def contact_copy():
    command = ''
    while command != '5':
        print('Меню копирования: \n'
            '1. Копировать контакт 1\n'
            '2. Копировать контакт 2\n'
            '3. Копировать контакт 3\n'
            '4. Копировать контакт 4\n'
            '5. Выход\n')
        command = input('Выберете пункт меню: ')

        while command not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод. Повторите запрос')
            command = input('Выберете пункт меню: ')
        print()

        match command:
            case '1':
                copy_contact_1()
            case '2':
                copy_contact_2()
            case '3':
                copy_contact_3()
            case '4':
                copy_contact_4()
            case '5':
                print('Выход в главное меню')
        print()


def copy_contact_1():
    with open('phonebook.txt', 'r', encoding='utf-8') as input_file, open('copy_phonebook.txt', 'w', encoding='utf-8') as output_file:
        lines = input_file.readlines()
        filtered_lines = [line for line in lines if 'Иванов' in line]
        output_file.writelines(filtered_lines)

def copy_contact_2():
    with open('phonebook.txt', 'r', encoding='utf-8') as input_file, open('copy_phonebook.txt', 'w', encoding='utf-8') as output_file:
        lines = input_file.readlines()
        filtered_lines = [line for line in lines if 'Петров' in line]
        output_file.writelines(filtered_lines)

def copy_contact_3():
    with open('phonebook.txt', 'r', encoding='utf-8') as input_file, open('copy_phonebook.txt', 'w', encoding='utf-8') as output_file:
        lines = input_file.readlines()
        filtered_lines = [line for line in lines if 'Сидоров' in line]
        output_file.writelines(filtered_lines)

def copy_contact_4():
    with open('phonebook.txt', 'r', encoding='utf-8') as input_file, open('copy_phonebook.txt', 'w', encoding='utf-8') as output_file:
        lines = input_file.readlines()
        filtered_lines = [line for line in lines if 'Александров' in line]
        output_file.writelines(filtered_lines)


def interface():
    with open('phonebook.txt', 'a', encoding='utf-8'):
        pass
    command = ''
    os.system('cls')
    while command != '5':
        print('Меню пользователя: \n'
            '1. Вывод данных на экран\n'
            '2. Добавить контакт\n'
            '3. Поиск контакта\n'
            '4. Копирование контакта в новый файл\n'
            '5. Выход\n')
        command = input('Выберете пункт меню: ')

        while command not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод. Повторите запрос')
            command = input('Выберете пункт меню: ')
        print()

        match command:
            case '1':
                print_data()
            case '2':
                add_contact()
            case '3':
                search_contact()
            case '4':
                contact_copy()
            case '5':
                print('Завершение программы')
        print()


if __name__ == '__main__':
    interface()
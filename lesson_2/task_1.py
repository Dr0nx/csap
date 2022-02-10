"""
Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции
создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета
в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также
оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""

from chardet import detect
import re
import csv


def get_data():
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    info_txt = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    regex = (rf'{main_data[0][0]}(.+)'
             rf'|{main_data[0][1]}(.+)'
             rf'|{main_data[0][2]}(.+)'
             rf'|{main_data[0][3]}(.+)')

    for txt in info_txt:
        with open(txt, 'rb') as f:
            raw_data = f.read()
        encoding = detect(raw_data)['encoding']

        result = []
        with open(txt, 'r', encoding=encoding) as f:
            for line in f:
                match = re.search(regex, line)
                if match:
                    matched = match.string.split(':')
                    result.append([matched[0], matched[1]])

            trans_m = [[result[i][j] for i in range(len(result))] for j in range(len(result[0]))]
            trans_m[1][2], trans_m[1][1] = trans_m[1][1], trans_m[1][2]
            trans_m[1][1], trans_m[1][0] = trans_m[1][0], trans_m[1][1]
            main_data.append([x.strip() for x in trans_m[1]])

    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    for i in range(1, len(main_data[1])):
        os_prod_list.append(main_data[i][0])
        os_name_list.append(main_data[i][1])
        os_code_list.append(main_data[i][2])
        os_type_list.append(main_data[i][3])
    print(f'В каждой строке соответствующий список (os_prod_list, os_name_list, os_code_list, os_type_list): \n\n'
          f'{os_prod_list}\n{os_name_list}\n{os_code_list}\n{os_type_list}\n')

    return main_data


def write_to_csv():
    main_data = get_data()
    with open('file.csv', 'w', encoding='utf-8') as csv_file:
        f_write = csv.writer(csv_file)
        for line in main_data:
            f_write.writerow(line)


if __name__ == "__main__":
    write_to_csv()

    print('Главный список file.csv:\n')
    with open('file.csv') as f:
        print(f.read())

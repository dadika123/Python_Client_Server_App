import csv
import re


def get_data():
    files_list = ['info_1.txt', 'info_2.txt', 'info_3.txt', ]
    rows_name = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [rows_name, os_prod_list, os_name_list, os_code_list, os_type_list]
    for file in files_list:
        with open(file) as f:
            for row in f:
                for row_name in rows_name:
                    target = re.match(rf'({row_name}):\s*(.*)', row)
                    if target:
                        if target[1] == rows_name[0]:
                            os_prod_list.append(target[2])
                        elif target[1] == rows_name[1]:
                            os_name_list.append(target[2])
                        elif target[1] == rows_name[2]:
                            os_code_list.append(target[2])
                        elif target[1] == rows_name[3]:
                            os_type_list.append(target[2])
    return main_data


def write_to_csv(name, data):
    with open(name, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(data[0])
        writer.writerows(zip(*data[1:]))


def main():
    csv_filename = 'main_data.csv'
    write_to_csv(csv_filename, get_data())


if __name__ == '__main__':
    main()

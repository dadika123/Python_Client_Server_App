import re


def get_data():
    files_list = ['info_1.txt', 'info_2.txt', 'info_3.txt', ]
    rows_name = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    for file in files_list:
        with open(file) as f:
            for row in f:
                for row_name in rows_name:
                    target = re.match(rf'{row_name}:\s*(.*)', row)
                    if target:
                        print(target[0])


def write_to_csv():
    pass


def main():
    get_data()


if __name__ == '__main__':
    main()

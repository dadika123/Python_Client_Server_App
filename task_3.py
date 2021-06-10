import yaml


def write_data_to_yaml(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


def read_data_from_yaml(file_name):
    with open(file_name, encoding='utf-8')as f:
        f_content = yaml.load(f, Loader=yaml.FullLoader)
    print(f_content)


def main():
    file = 'file.yaml'
    data = {
        'brands': ['ASUS', 'DELL', 'LENOVO', 'APPLE'],
        'models prices': {
            'GX531GM': '\u20bd135000',
            'G14VHS': '\u20bd162000',
            'G15GSL': '\u20bd127500'}
    }

    write_data_to_yaml(data, file)
    read_data_from_yaml(file)


if __name__ == '__main__':
    main()

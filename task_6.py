import locale


def main():
    install_coding = locale.getpreferredencoding()
    print(install_coding)
    with open('test_file.txt', encoding='utf-8') as f_n:
        for el_str in f_n:
            print(el_str)


if __name__ == '__main__':
    main()

def main():
    letter_1, letter_2, letter_3 = 'разработка', 'сокет', 'декоратор'
    print(type(letter_1), type(letter_2), type(letter_3))
    letter_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
    letter_2 = '\u0441\u043e\u043a\u0435\u0442'
    letter_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
    print(type(letter_1), type(letter_2), type(letter_3))
    print(letter_1, letter_2, letter_3)


if __name__ == '__main__':
    main()
    
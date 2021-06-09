"""
    Из слов "attribute", "класс", "функция" и "type" можно записать в байтовом
    виде только "attribute" и "type", так как остальные слова состоят из
    символов не входящих в таблицу ASCII.
"""


def main():
    words = ['attribute', 'класс', 'функция', 'type']
    for word in words:
        try:
            bytes(word, 'ascii', errors='strict')
        except UnicodeEncodeError:
            print(
                f'Слово "{word}" не записано в байтовом виде т.к. содержит не только ASCII символы')
        else:
            print(f'Слово "{word}" может быть записано в байтовом виде')


if __name__ == '__main__':
    main()

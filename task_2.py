def main():
    words = ['class', 'method', 'function', ]
    for word in words:
        word_b = bytes(word, encoding='utf-8', errors='replace')
        print("{:>10} {:>10} {:>10}".format(
            str(type(word_b)), word, str(len(word_b))))


if __name__ == '__main__':
    main()

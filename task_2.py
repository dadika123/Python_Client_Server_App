def main():
    words = ['class', 'method', 'function', ]
    for word in words:
        word_b = bytes(word, encoding='utf-8', errors='replace')
        print(f"{type(word)} {word_b} {len(word_b)}")


if __name__ == '__main__':
    main()

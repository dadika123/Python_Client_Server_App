letter_1, letter_2, letter_3, letter_4 = 'разработка', 'администрирование', 'protocol', 'standart'
letter_1_enc = letter_1.encode('utf-8')
letter_2_enc = letter_2.encode('utf-8')
letter_3_enc = letter_3.encode('utf-8')
letter_4_enc = letter_4.encode('utf-8')
print(letter_1_enc, letter_2_enc, letter_3_enc, letter_4_enc)
print(type(letter_1_enc), type(letter_2_enc),
      type(letter_3_enc), type(letter_4_enc))
letter_1_dec = letter_1_enc.decode('utf-8')
letter_2_dec = letter_2_enc.decode('utf-8')
letter_3_dec = letter_3_enc.decode('utf-8')
letter_4_dec = letter_4_enc.decode('utf-8')
print(letter_1_dec, letter_2_dec, letter_3_dec, letter_4_dec)
print(type(letter_1_dec), type(letter_2_dec),
      type(letter_3_dec), type(letter_4_dec))

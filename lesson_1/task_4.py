""" Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode). """

some_strings = ['разработка', 'администрирование', 'protocol', 'standard']

print(f'Преобразовываю слова из строкового представления\n{some_strings}')
enc_str_bytes = [str.encode(x, encoding='utf-8') for x in some_strings]
print(f'в байтовое\n{enc_str_bytes}')
print(f'и обратно из байтового в строковое')
dec_str_bytes = [bytes.decode(x, encoding='utf-8') for x in enc_str_bytes]
print(dec_str_bytes)

""" Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
«декоратор». Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед нами файл в
неизвестной кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке
он был создан. """

from chardet import detect

test_file = 'test_file.txt'
with open(test_file, 'w') as f:
    f.write('сетевое программирование\nсокет\nдекоратор')

with open(test_file, 'rb') as f:
    raw_data = f.read()
encoding = detect(raw_data)['encoding']
print('encoding:', encoding, '\n')

with open(test_file, encoding=encoding) as f:
    for line in f:
        print(line, end='')

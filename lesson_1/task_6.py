""" Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
«декоратор». Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед нами файл в
неизвестной кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке
он был создан. """

from chardet import detect
from os.path import isfile

text = ['сетевое программирование', '\n', 'сокет', '\n', 'декоратор']
test_file = 'test_file.txt'
if not isfile(test_file):
    with open(test_file, 'w') as f:
        f.writelines(text)
else:
    with open(test_file, 'r') as f:
        for line in f:
            print(line)
            result = detect(b'line')
            # line = line.decode(result['encoding']).encode('utf-8')
            # print(line.decode('utf-8'))

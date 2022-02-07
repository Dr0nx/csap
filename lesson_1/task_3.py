""" Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе. Важно:
решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем. """

# ...
# File "/Users/dr0n/Documents/csap/lesson_1/task_3.py", line 7
#     some_bytes = [b'attribute', b'класс', b'функция', b'type']
#                                         ^
# SyntaxError: bytes can only contain ASCII literal characters
# (SyntaxError: байты могут содержать только литеральные символы ASCII (<= 127 байт))
# байты в таком виде b'класс', b'функция' вызывают исключение

# Одно решение с генерацией исключения SyntaxError
some_words = ['attribute', 'класс', 'функция', 'type']
some_bytes = []
non_some_bytes = []

for word in some_words:
    try:
        some_bytes.append(eval(f'b"{word}"'))
    except SyntaxError:
        non_some_bytes.append(word)

print(f'Слова в байтовом формате: {some_bytes}')
print(f'Слова, которые невозможно записать в байтовом формате: {non_some_bytes}')
print('\n')

# Использование кодовых точек исправляет эту проблему.
some_bytes = [
    b'\u0061\u0074\u0074\u0072\u0069\u0062\u0075\u0074\u0065',
    b'\u043a\u043b\u0430\u0441\u0441',
    b'\u0444\u0443\u043d\u043a\u0446\u0438\u044f',
    b'\u0074\u0079\u0070\u0065',
]
print('\n'.join([f'Слово "{x}" можно записать в байтовом формате.' for x in some_bytes]))

print('\n')

# Использую произвольную строку в строковом и байтовом представлении
some_strings = input('Введите строку: ')
some_bytes = some_strings.encode('unicode_escape')
print(some_strings, some_bytes)

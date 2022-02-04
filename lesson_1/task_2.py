"""
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""

some_bytes = [b'class', b'function', b'method']
for byte in some_bytes:
    print('Тип:', eval('type(byte)'), '-', 'Содержимое:', eval('byte'), '-', 'Длинна переменной:', eval('len(byte)'))

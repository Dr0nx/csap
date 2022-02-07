""" Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на
кириллице. """

from platform import system
from subprocess import Popen, PIPE
from chardet import detect

param = '-n' if system().lower() == 'windows' else '-c'
for host in 'yandex.ru', 'youtube.com':
    args = ['ping', param, '1', host]
    result = Popen(args, stdout=PIPE)
    for line in result.stdout:
        result = detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'), end='')

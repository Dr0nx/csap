""" Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на
кириллице. """
from platform import system
from subprocess import Popen, PIPE
# from

print('Начало')
param = '-n' if system().lower() == 'windows' else '-c'
for host in 'yandex.ru', 'youtube.com':
    args = ['ping', param, '1', host]
    result = Popen(args, stdout=PIPE)
    for line in result.stdout:
        print(line.decode('cp1251').encode('utf8'))
        # print(line.decode('utf-8').encode('cp1251'))
        # line = line.decode('utf-8').encode('windows-1251')
        # print(line)

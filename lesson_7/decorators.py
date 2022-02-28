import sys
import logging


# Метод определения модуля, источника запуска.
# Метод find () возвращает индекс первого вхождения искомой подстроки,
# если он найден в данной строке.
# Если его не найдено, - возвращает -1.

LOGGER = logging.getLogger('server') if sys.argv[0].find('client.py') == -1 else logging.getLogger('client')


def log(func_to_log):
    def log_saver(*args, **kwargs):
        result = func_to_log(*args, **kwargs)
        LOGGER.debug(f'Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}.'
                     f' Вызов из модуля {func_to_log.__module__}.'
                     f' @@@Вызов из модуля {sys._getframe().f_back.f_code.co_filename.split("/")[-1]}.')
        return result

    return log_saver

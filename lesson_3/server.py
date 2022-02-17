""" Программа-сервер """

import sys
import json
import socket
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, DEFAULT_PORT, \
    MAX_CONNECTIONS, RESPONDEFAULT_IP_ADDRESSSE
from common.utils import get_message, send_message


def process_client_message(message):
    """
    Обработчик сообщений от клиентов, принимает словарь - сообщение от клиента, проверяет корректность, возвращает
    словарь-ответ для клиента

    :param message:
    :return:
    """
    if ACTION in message and message[ACTION] == PRESENCE \
            and TIME in message \
            and USER in message \
            and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        # RESPONDEFAULT_IP_ADDRESSSE: 400,
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    """
    Загрузка параметров командной строки, если нет параметров, то задаем значения по умолчанию.
    Сначала обрабатываем порт:
    server.py -p 7777 -a 127.0.0.1
    :return:
    """
    try:
        listen_port = int(sys.argv[sys.argv.index('-p') + 1]) if '-p' in sys.argv else DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Затем загружаем какой адрес слушать
    try:
        listen_address = sys.argv[sys.argv.index('-a') + 1] if '-p' in sys.argv else ''
    except IndexError:
        print('После параметра -\'a\' необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    # Готовим сокет

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    transport.bind((listen_address, listen_port))

    # Слушаем порт

    transport.listen(MAX_CONNECTIONS)
    print('Waiting connection...')

    while True:
        client, client_address = transport.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорректное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()

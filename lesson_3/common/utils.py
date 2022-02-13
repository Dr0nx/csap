""" Утилиты """

import json
from common.variables import *


def get_message(client):
    """
    Утилита приема и декодирования сообщения принимает байты, выдает словарь, если принято что-то другое и выдает
    ошибку значения.
    :param client:
    :return:
    """

    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        if not isinstance(json_response, str):
            raise ValueError
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    """
    Утилита кодирования и отправки сообщения, приминает словарь и отправляет его.
    :param sock:
    :param message:
    :return:
    """
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)

import unittest
import sys
import os

sys.path.append(os.path.join(os.getcwd(), '..'))
from server import process_client_message
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE


class TestClassServer(unittest.TestCase):
    err_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }
    ok_dict = {RESPONSE: 200}

    def test_no_action(self):
        # Ошибка если нет действия
        self.assertEqual(process_client_message(
            {TIME: '1.2', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_wrong_action(self):
        # Ошибка если неизвестное действие
        self.assertEqual(process_client_message(
            {ACTION: 'Wrong', TIME: '1.2', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_no_time(self):
        # Ошибка, если запрос не содержит штампа времени
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_no_user(self):
        # Ошибка - нет пользователя
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: '1.2'}), self.err_dict)

    def test_unknown_user(self):
        # Ошибка - не Guest
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.2, USER: {ACCOUNT_NAME: '_Guest_'}}), self.err_dict)

    def test_ok_check(self):
        # Корректный запрос
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.2, USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dict)


if __name__ == '__main__':
    unittest.main()

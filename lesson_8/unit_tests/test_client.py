import unittest
import sys
import os

sys.path.append(os.path.join(os.getcwd(), '..'))
from client import create_presence, process_ans
from common.variables import TIME, ACTION, PRESENCE, ACCOUNT_NAME, USER, RESPONSE, ERROR


class TestClassClient(unittest.TestCase):

    def test_create_presence(self):
        # Тестирование create_presence()
        test = create_presence()
        test[TIME] = 1.2
        self.assertEqual(test, {
            ACTION: PRESENCE,
            TIME: 1.2,
            USER: {
                ACCOUNT_NAME: 'Guest'
            }
        })

    def test_create_presence_incorrect_parameters(self):
        # Тестирование обработки ввода некорректных данных
        test = create_presence()
        # test[TIME] = 1.2
        self.assertNotEqual(test, {
            ACTION: PRESENCE,
            TIME: 1.2, USER: {
                ACCOUNT_NAME: 'Fail',
            }
        })

    def test_process_ans_200(self):
        # Тестирование ответа сервера 200
        self.assertEqual(process_ans({RESPONSE: 200}), '200: OK')

    def test_process_ans_400(self):
        """
        Тестирование ответа сервера 400, неверный ответ сервера
        """
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'error 400'}), '400: error 400')

    def test_process_ans_400_no_response(self):
        # Тестирование исключения ValueError, когда нет RESPONSE
        self.assertRaises(ValueError, process_ans, '400: error 400')


if __name__ == '__main__':
    unittest.main()


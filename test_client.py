import unittest
import clientserver


class Testclientserver(unittest.TestCase):
    def setUp(self):
        self.s = clientserver.get_server_socket('localhost', 7777)
        self.c = clientserver.get_client_socket('localhost', 7777)
        self.sender = self.s.accept()[0]
        clientserver.send_data(self.c, {'test': 'test'})
    def tearDown(self):
        self.c.close()
        self.s.close()
    def test_get_data(self):
        self.assertEqual(clientserver.get_data(self.sender), {'test': 'test'})
    def test_send_data(self):
        with self.assertRaises(TypeError):
            clientserver.send_data()

if __name__ == '__main__':
    unittest.main()
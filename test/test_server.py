
import chat.clientserver as clientserver
import socket
import unittest
import sys



class TestServer(unittest.TestCase):
    def setUp(self):
        self.s = clientserver.get_server_socket('localhost', 7777)

    def tearDown(self):
        self.s.close()

    def test_server_socket_is_socket(self):
        self.assertIsInstance(self.s, socket.socket)

    def test_server_socket_addr(self):
        self.assertEqual(self.s.getsockname(), ('127.0.0.1', 7777))


if __name__ == '__main__':
    unittest.main()

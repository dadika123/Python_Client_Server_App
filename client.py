import argparse
import pickle
import time
from socket import AF_INET, SOCK_STREAM, socket

s = socket(AF_INET, SOCK_STREAM)
parser = argparse.ArgumentParser(description='Messenger startup settings')
parser.add_argument('--addr', default='localhost', help='address')
parser.add_argument('--port', default=7777, help='port')
args = parser.parse_args()
arg_port = int(args.port)
arg_addr = args.addr


def init_socket():
    s.connect((arg_addr, arg_port))


def send_msg():
    msg = {
        "action": "authenticate",
        "time": time.time(),
        "user": {
            "account_name":  "chuzhikov_danil",
            "password":      "czkvktzV279797"
        }
    }
    s.send(pickle.dumps(msg))
    data = s.recv(1024)
    print('Сообщение от сервера:', pickle.loads(data), 'длинной ', len(data)),
    s.close()


if __name__ == '__main__':
    socket = init_socket()
    msg = send_msg()

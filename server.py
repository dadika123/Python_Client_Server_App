from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, socket
import pickle
import argparse

s = socket(AF_INET, SOCK_STREAM)

parser = argparse.ArgumentParser(description='Messenger startup settings')
parser.add_argument('--addr', default='0.0.0.0', help='address')
parser.add_argument('--port', default=7777, help='port')
args = parser.parse_args()
arg_port = int(args.port)
arg_addr = args.addr


def init_socket():
    s.bind((arg_addr, arg_port))
    s.listen(6)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)


def main():
    while True:
        client, addr = s.accept()
        print('Получен запрос на соединение от %s' % str(addr))
        data = client.recv(1024)
        response = {
            'response': 200,
            'alert': 'Вы успешно вошли в систему'
        }
        client.send(pickle.dumps(response))

        client.close()


if __name__ == '__main__':
    socket = init_socket()
    try:
        main()
    except Exception as text:
        print('Ошибка! Сервер не запустился')

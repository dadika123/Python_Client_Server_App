import argparse
import socket
import json
import logging
import os.path

ADDRESS = 'localhost'
PORT = 7777
CONNECTIONS = 10


def log(func):
    def wrapped(*args, **kwargs):
        logger = logging.getLogger('chat.decorator')
        logger.info(f'Вызвана функция: {func.__name__}, с аргументами: {args, kwargs}')
        return func(*args, **kwargs)
    return wrapped


@log
def get_server_socket(addr, port):
    s = socket.socket()
    s.bind((addr, port))
    s.listen(CONNECTIONS)
    return s


@log
def get_client_socket(addr, port):
    s = socket.socket()
    s.connect((addr, port))
    return s


@log
def send_data(recipient, data):
    recipient.send(json.dumps(data).encode('utf-8'))


@log
def get_data(sender):
    return json.loads(sender.recv(1024).decode("utf-8"))


def create_parser():
    parser = argparse.ArgumentParser(
        description='JSON instant messaging'
    )

    parser_group = parser.add_argument_group(title='Parameters')
    parser_group.add_argument(
        '-a', '--addr', default=ADDRESS, help='IP address')
    parser_group.add_argument('-p', '--port', type=int,
                              default=PORT, help='TCP port')

    return parser

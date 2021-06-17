import logging

import chat.clientserver as clientserver
import chat.jim as jim
import log.client_log_config


logger = logging.getLogger('chat.client')

if __name__ == '__main__':
    logger.debug('Клиент запущен')
    client_name = input('Введите имя: ')
    parser = clientserver.create_parser()
    namespace = parser.parse_args()
    sock = clientserver.get_client_socket(namespace.addr, namespace.port)
    server_addr = sock.getpeername()
    print(f'Connected to server: {server_addr[0]}:{server_addr[1]}')
    logger.info(f'Connected to server: {server_addr[0]}:{server_addr[1]}')
    jim.PRESENCE['user']['account_name'] = client_name
    clientserver.send_data(sock, jim.PRESENCE)

    while True:
        try:
            data = clientserver.get_data(sock)
        except ConnectionResetError:
            logger.info(ConnectionResetError)

        if data['response'] != '200':
            break

        msg = input('Введите сообщение ("exit" для выхода): ')
        jim.MESSAGE['message'] = msg

        try:
            clientserver.send_data(sock, jim.MESSAGE)
            logger.info(
                f'Сообщение размером:{len(jim.MESSAGE)} направлено пользователю - {server_addr}')
        except ConnectionResetError:
            logger.error(ConnectionResetError)

    logger.info('Приложение завершено!')
    sock.close()

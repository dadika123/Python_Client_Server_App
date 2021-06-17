import logging

import chat.clientserver as clientserver
import chat.jim as jim
import log.server_log_config


client_name = ''
logger = logging.getLogger('chat.server')


if __name__ == '__main__':
    logger.debug('Сервер запущен!')
    parser = clientserver.create_parser()
    namespace = parser.parse_args()
    sock = clientserver.get_server_socket(namespace.addr, namespace.port)

    server_addr = sock.getsockname()
    logger.info(f'Сервер запущен в {server_addr[0]}:{server_addr[1]}')
    print(f'Сервер запущен в {server_addr[0]}:{server_addr[1]}')

    client, address = sock.accept()
    logger.info(f'Подключился клиент: {address[0]}:{address[1]}')
    print(f'Подключился клиент: {address[0]}:{address[1]}')

    while True:
        data = clientserver.get_data(client)

        if client_name == '':
            if data['action'] == 'presence' and data['user']['account_name'] != '':
                client_name = data['user']['account_name']
                jim.RESPONSE['response'], jim.RESPONSE['alert'] = jim.SERVER_RESP[0]
                print(
                    f'{data["time"]} - {data["user"]["account_name"]}: {data["user"]["status"]}')
            else:
                jim.RESPONSE['response'], jim.RESPONSE['alert'] = jim.SERVER_RESP[1]

        if client_name != '' and data['action'] == 'msg':
            print(f'{data["time"]} - {client_name}: {data["message"]}')
            jim.RESPONSE['response'], jim.RESPONSE['alert'] = jim.SERVER_RESP[0]

            if data["message"] == 'exit':
                jim.RESPONSE['response'], jim.RESPONSE['alert'] = jim.SERVER_RESP[2]

        clientserver.send_data(client, jim.RESPONSE)

        if jim.RESPONSE['response'] != '200':
            client.close()
            break

    sock.close()

import clientserver
import jim

if __name__ == '__main__':
    client_name = input('Введите имя: ')

    parser = clientserver.create_parser()
    namespace = parser.parse_args()

    sock = clientserver.get_client_socket(namespace.addr, namespace.port)

    server_addr = sock.getpeername()
    print(f'Connected to server: {server_addr[0]}:{server_addr[1]}')

    jim.PRESENCE['user']['account_name'] = client_name
    clientserver.send_data(sock, jim.PRESENCE)

    while True:
        data = clientserver.get_data(sock)

        if data['response'] != '200':
            break

        msg = input('Введите сообщение ("exit" для выхода): ')
        jim.MESSAGE['message'] = msg
        clientserver.send_data(sock, jim.MESSAGE)

    sock.close()

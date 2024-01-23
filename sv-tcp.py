import socket

def start_server():
    # Configurações do servidor
    host = 'localhost'
    port = 8080

    # Criação do socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Associa o socket ao endereço e porta
    server_socket.bind((host, port))

    # Habilita o servidor para aceitar conexões
    server_socket.listen()

    print(f"Servidor aguardando conexão em {host}:{port}")

    while True:
        # Aceita a conexão do cliente
        client_socket, client_address = server_socket.accept()
        print(f"Conexão estabelecida com {client_address}")

        # Envia mensagem de confirmação para o cliente
        confirmation_message = "Conexão estabelecida com sucesso!"
        client_socket.send(confirmation_message.encode())

        # Fecha a conexão com o cliente
        client_socket.close()

if __name__ == "__main__":
    start_server()
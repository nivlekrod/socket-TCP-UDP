import socket

def start_server():
    # Configurações do servidor
    host = 'localhost'  # Pode usar também '127.0.0.1'
    port = 8080

    # Criação do socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Associa o socket ao endereço e porta
    server_socket.bind((host, port))

    print(f"Servidor aguardando conexão em {host}:{port}")

    while True:
        # Recebe dados do cliente
        data, client_address = server_socket.recvfrom(1024)
        print(f"Recebido: {data.decode()} de {client_address}")

        # Envia mensagem de confirmação para o cliente
        confirmation_message = "Conexão estabelecida com sucesso!"
        server_socket.sendto(confirmation_message.encode(), client_address)

if __name__ == "__main__":
    start_server()

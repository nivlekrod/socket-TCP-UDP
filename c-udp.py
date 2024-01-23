import socket

def start_client():
    # Configurações do cliente
    host = 'localhost'  # Pode usar também '127.0.0.1'
    port = 8080

    # Criação do socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Mensagem a ser enviada
    message = "Olá, servidor!"

    # Envia mensagem para o servidor
    client_socket.sendto(message.encode(), (host, port))

    # Recebe mensagem de confirmação do servidor
    confirmation_data, server_address = client_socket.recvfrom(1024)
    print(f"Recebido do servidor: {confirmation_data.decode()}")

    # Fecha o socket do cliente
    client_socket.close()

if __name__ == "__main__":
    start_client()
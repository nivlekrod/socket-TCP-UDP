import socket

def start_client():
    # Configurações do cliente
    host = 'localhost'
    port = 8080

    # Criação do socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta ao servidor
    client_socket.connect((host, port))
    print(f"Conectado ao servidor em {host}:{port}")

    # Recebe mensagem de confirmação do servidor
    confirmation_data = client_socket.recv(1024)
    print(f"Recebido do servidor: {confirmation_data.decode()}")

    # Fecha o socket do cliente
    client_socket.close()

if __name__ == "__main__":
    start_client()
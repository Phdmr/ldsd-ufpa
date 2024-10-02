# servidor_tcp.py
import socket
import threading


def handle_client(client_socket, addr):
    """Função para tratar cada cliente em uma thread separada"""
    print(f"Conexão estabelecida com: {addr}")
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Recebido de {addr}: {data.decode()}")
            client_socket.send(b"Mensagem recebida.")
        except:
            break
    client_socket.close()
    print(f"Conexão fechada com: {addr}")


def tcp_server():
    """Função principal do servidor TCP que aceita múltiplos clientes"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))
    server_socket.listen(5)  # Permite até 5 conexões em espera
    print("Servidor TCP rodando na porta 8080...")

    while True:
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(
            target=handle_client, args=(client_socket, addr)
        )
        client_thread.start()


if __name__ == "__main__":
    tcp_server()

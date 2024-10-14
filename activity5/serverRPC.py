from xmlrpc.server import SimpleXMLRPCServer


# Funções que serão chamadas remotamente
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida"
    return x / y


# Função para lidar com a desconexão
def disconnect(client_ip):
    print(f"Cliente {client_ip} se desconectou.")
    return True


# Cria o servidor RPC na porta 8000
server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor RPC disponível na porta 8000...")

# Registra as funções para serem acessíveis remotamente
server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")
server.register_function(disconnect, "disconnect")

# Inicia o servidor, que ficará aguardando chamadas RPC
server.serve_forever()

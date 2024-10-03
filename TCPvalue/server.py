import socket
BUFFER_SIZE = 4096
host = '10.210.0.40'  
port = 8900

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))
server_socket.listen(1)
print(f"Server in ascolto su {host}:{port}")

while True:
    client_socket, addr = server_socket.accept()
    #print(f"Connessione da: {addr}")
    message = client_socket.recv(BUFFER_SIZE).decode('utf-8')
    print(f"CLIENT: {message}")
    par1, par2 = message.split(',')
    response = f"Ho letto: PARAMENTRO_1={par1.strip()}, PARAMETRO_2={par2.strip()}"
    client_socket.send(response.encode('utf-8'))
    client_socket.close()
    print(f"Connessione con: {addr} terminata")

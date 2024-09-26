import socket

server_address = ('192.168.1.54', 12345)
BUFFER_SIZE = 4092 #in byte
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


for i in range(10):
    message = f"Ciao {i+1}".encode()  # Trasforma la stringa in byte
    udp_client_socket.sendto(message, server_address)
    data, address = udp_client_socket.recvfrom(BUFFER_SIZE)
    print(f"Risposta dal server: {data.decode()}")
udp_client_socket.close()

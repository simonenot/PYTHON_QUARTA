import socket

server_address = ('192.168.1.54', 12345)
BUFFER_SIZE = 4092

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#Specifica che il socket utilizzerà l’indirizzo IPv4 e Indica che il socket utilizzerà il protocollo UDP
udp_server_socket.bind(server_address)

print("Server in ascolto...")

while True:
    data, client_address = udp_server_socket.recvfrom(BUFFER_SIZE)
    print(f"Messaggio ricevuto: {data.decode()} da {client_address}") #rispondo quando ricevo i mess
    response = "Messaggio ricevuto".encode()
    udp_server_socket.sendto(response, client_address)

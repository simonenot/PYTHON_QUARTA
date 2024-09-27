import socket

server_address = ("172.20.10.4", 12345)
BUFFER_SIZE = 4092  # Massima dimensione trasmissibile

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind(server_address)  # Associa il socket all'indirizzo e alla porta

print("Server in ascolto...")

while True:
    data, address = udp_server_socket.recvfrom(BUFFER_SIZE)  # Mette in ascolto il server
    message = data.decode('utf-8')
    print(f"CLIENT: {message}")
    
    if message == "break":
        print("Chiusura del server.")
        break

    response = input("Risposta: ")
    udp_server_socket.sendto(response.encode('utf-8'), address)

udp_server_socket.close()

import socket

server_address = ("10.210.0.40", 12345)
BUFFER_SIZE = 4092  # Massima dimensione trasmissibile

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Inserisci  messaggio: ")
    udp_client_socket.sendto(message.encode('utf-8'), server_address)
    
    if message == "break":
        print("Chiusura del client.")
        break

    data, address = udp_client_socket.recvfrom(BUFFER_SIZE)
    response = data.decode('utf-8')
    print(f"Risposta dal server: {response}")

udp_client_socket.close()

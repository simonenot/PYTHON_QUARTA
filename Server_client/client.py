import socket

server_address= ('192.168.1.126',12345) #587 porta criptata
BUFFER_SIZE = 4092 #byte

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message="Ciao sono il client".encode()  #trasforma la stringa dal formato encode a byte
udp_client_socket.sendto(message, server_address)
data, address= udp_client_socket.recvfrom(BUFFER_SIZE)
print(data.decode())

udp_client_socket.close()   

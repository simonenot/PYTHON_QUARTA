import socket as s
import threading as t

SERVER_ADDRESS = ("192.168.126.1", 8900)
BUFFER_SIZE = 4096

def main():
    server_UDP = s.socket(s.AF_INET, s.SOCK_DGRAM)
    server_UDP.bind(SERVER_ADDRESS)
    _, client_address = server_UDP.recvfrom(BUFFER_SIZE)
    print(f"connessione a {client_address}")
    server_UDP.sendto("Server online".encode(), client_address)
    # Crea i thread per inviare e ricevere messaggi
    thread_invio = t.Thread(target=invio, args=(server_UDP, client_address))
    thread_ricezione = t.Thread(target=ricezione, args=(server_UDP,))
    
    thread_invio.start()
    thread_ricezione.start()


# Funzione per inviare messaggi
def invio(server_UDP, client_address):
    while True:
        data = input("")
        server_UDP.sendto(data.encode('utf-8'), client_address)

# Funzione per ricevere messaggi
def ricezione(server_UDP):
    while True:
        data, address = server_UDP.recvfrom(BUFFER_SIZE)
        print(f"Client: {data.decode('utf-8')}")

if __name__ == "__main__":
    main()
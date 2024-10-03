import socket as s
import threading as t

SERVER_ADDRESS = ("192.168.126.1", 8900)
BUFFER_SIZE = 4096

def main():
    client_UDP = s.socket(s.AF_INET, s.SOCK_DGRAM)
    client_UDP.sendto("connessione".encode("utf-8"), SERVER_ADDRESS)
    thread_invio = t.Thread(target=invio, args=(client_UDP,))
    thread_ricezione = t.Thread(target=ricezione, args=(client_UDP,))
    
    thread_invio.start()
    thread_ricezione.start()

# Funzione per inviare messaggi
def invio(client_UDP):
    while True:
        data = input("")
        client_UDP.sendto(data.encode('utf-8'), SERVER_ADDRESS)

# Funzione per ricevere messaggi
def ricezione(client_UDP):
    while True:
        data, address = client_UDP.recvfrom(BUFFER_SIZE)
        print(f"Server: {data.decode('utf-8')}")

if __name__ == "__main__":
    main()
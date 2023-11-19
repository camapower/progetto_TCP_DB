import socket

def main():
    # Definizione dell'indirizzo del server e della porta
    server_address = ("localhost", 10000)

    # Creazione del socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connessione al server
    client_socket.connect(server_address)

    # Ciclo per gestire la richiesta della password e iniziare l'interazione con il server
    while True:
        password_request = client_socket.recv(1024).decode().strip()
        print(password_request)
        
        password_input = input().strip()
        client_socket.sendall(password_input.encode())
        
        response = client_socket.recv(1024).decode().strip()
        print(response)
        
        if response == "Connessione accettata!":
            break

    # Ricezione del menu dal server e gestione delle richieste dell'utente
    while True:
        menu = client_socket.recv(1024).decode().strip()
        print(menu)
        
        choice = input("Inserisci il numero corrispondente all'operazione desiderata: ").strip()
        client_socket.sendall(choice.encode())
        
        if choice == "8":
            break

        # Ricezione e stampa della risposta del server
        server_response = client_socket.recv(1024).decode().strip()
        print(server_response)

    client_socket.close()

if __name__ == "__main__":
    main()

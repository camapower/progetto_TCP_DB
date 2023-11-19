import socket
import threading
import mysql.connector

# Definizione della password
password = "camassa1234"

# Funzione per gestire la connessione con un client
def handle_client(client_socket, client_address):
    print("Connessione accettata da", client_address)
    
    # Variabile per il conteggio degli errori di password
    error_password = 0
    
    while True:
        client_socket.sendall("Inserisci la password: ".encode())
        password_input = client_socket.recv(1024).decode().strip()
        
        if password_input == password:
            client_socket.sendall("Connessione accettata!".encode())
            break
        else:
            error_password += 1
            
            if error_password == 3:
                client_socket.sendall("Connessione rifiutata!".encode())
                client_socket.close()
                print("Connessione rifiutata a", client_address)
                return
            else:
                client_socket.sendall("Password errata, riprova ".encode())
    
    # Menu di scelta per il client
    menu = """Cosa vuoi fare?
    - 1 - Leggere liberamente all'interno del database
    - 2 - Creare una tabella
    - 3 - Aggiorna un dato di una tabella
    - 4 - eliminare una tabella
    - 5 - inserire dei dati all'interno della tabella
    - 6 - elimina un database
    - 7 - crea un database
    - 8 - esci """
    client_socket.sendall(menu.encode())
    
    while True:
        # Ricezione della risposta del client e gestione delle richieste
        response = client_socket.recv(1024).decode().strip()
        print("Il client vuole eseguire la scelta", response)
        
        if response == "8":
            break
        elif response== "1":
            import mysql.connector
            import socket as sock
            #import mariadb

            # mysql.connector.connect --> mariadb.connect
            def db_get():
                conn = mysql.connector.connect(
                    host="localhost", #127.0.0.1
                    user="root",
                    password="",
                    database="5b_tpsit",
                    port=3306, 
                    )

                cur = conn.cursor()

                # si chiama una funzione di libreria passando i parametri di ricerca dell'utente. esempio controlla_caratteri(nome)
                query = input("inserisci la query: ")
                cur.execute(query)
                dati = cur.fetchall()
                print(dati)
                return dati

            #creazione server socket
            if __name__ == '__main__':
                db_get()
                break
            
        if response== "2":
            # Python implementation to create a table in MySQL
            import mysql.connector
            import socket as sock

            # connecting to the mysql server
            
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="5b_tpsit",
                port=3306
            )

                # cursor object c
            c = db.cursor()
            database="5b_tpsit"
            nome_table=input("inserisci il nome della tabella: ")                       #inserire gli attr in riga 124
            txt="""`id` INT NOT NULL AUTO_INCREMENT,
            `nome` VARCHAR(45) NULL,
            `cognome` VARCHAR(45) NULL,                                
            `eta` INT NOT NULL,
            `pos_lavorativa` VARCHAR(45) NULL, 
            `data_ass` DATE NOT NULL,
            `residenza` VARCHAR(45) NULL, 
            PRIMARY KEY (`id`))"""
            
        
            table = f"""CREATE TABLE {database}.{nome_table} (
            {txt}"""
            
            c.execute(table)
            
            c = db.cursor()
            
            # fetch  details in the database
            c.execute(f"desc {nome_table}")
            
            # print the table details
            for i in c:
                print(i)
            
            
            # finally closing the database connection
            db.close()
            break
        
        if response == "3":
                    # Python implementation to update data of a table in MySQL
            import mysql.connector

            # connecting to the mysql server

            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="5b_tpsit",
                port=3306
            )

            # cursor object c
            c = db.cursor()
            nome_table=input("inserisci il nome della tabella: ")   
            nome_column=input("inserisci il nome della colonna: ")   
            value=input("seleziona il valore: ")
            attributo=input("inserisci l'attributo da confrontare:")
            valuecr=input("inserisci valore da confrontare:")
            # update statement 

            query = (f"""UPDATE {nome_table}\
                SET {nome_column} = "{value}" WHERE {attributo} = "{valuecr}" """)

            # execute the update query to modify
        
            c.execute(query)
            db.commit()
            print("update eseguito con successo")

            # finally closing the database connection
            db.close()
            break

        
        if response== "4":
            import mysql.connector
            import socket as sock
            #import mariadb

            # mysql.connector.connect --> mariadb.connect
            def db_get():
                conn = mysql.connector.connect(
                    host="localhost", #127.0.0.1
                    user="root",
                    password="",
                    database="5b_tpsit",
                    port=3306
                    )

                cur = conn.cursor()
                nome_table=input("inserisci il nome della tabella da eliminare: ")
                # si chiama una funzione di libreria passando i parametri di ricerca dell'utente. esempio controlla_caratteri(nome)
                query = (f"DROP TABLE {nome_table} ")
                cur.execute(query)
                conn.commit()
                print(f"tabella {nome_table} eliminata")

            #creazione server socket
            if __name__ == '__main__':
                db_get()
                break
        
        
        if response== "5":
            # Python implementation to insert data into a table in MySQL
            import mysql.connector

            # connecting to the mysql server

            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="5b_tpsit",
                port=3306
            )

            # cursor object c
            c = db.cursor()

            # inserire qui i valori
            insert = """INSERT INTO dipendenti_andrea_camassa (
            nome,
            cognome,
            eta,
            pos_lavorativa,
            data_ass,
            residenza) 
            VALUES (%s, %s, %s, %s, %s, %s)"""

            # si mettono i dati degli inserimenti all'interno della lista
            data = [('Federico', 'Marini', 29, 'Web Developer', '2023-04-09', 'Lucca'),
                ('Ludovica', 'Rinaldi', 35, 'Infermiera', '2023-06-15', 'Pescara'),
                ('Gianluca', 'Villa', 41, 'Ingegnere del Software', '2023-01-28', 'Vicenza'),
                ('Marta', 'Marchi', 27, 'Grafico', '2023-08-11', 'Aosta'),
                ('Niccolò', 'Rizzi', 31, 'Commercialista', '2023-03-20', 'Nuoro')]

            # execute the insert commands for all rows and commit to the database
            c.executemany(insert, data)
            db.commit()
            print("inserimento eseguito con successo")
            # finally closing the database connection
            db.close()
            break

        if response== "6":
            import mysql.connector
            import socket as sock
            #import mariadb

            # mysql.connector.connect --> mariadb.connect
            def db_get():
                conn = mysql.connector.connect(
                    host="localhost", #127.0.0.1
                    user="root",
                    password="",
                    port=3306
                    )

                cur = conn.cursor()
                nome_table=input("inserisci il nome del database da eliminare: ")
                # si chiama una funzione di libreria passando i parametri di ricerca dell'utente. esempio controlla_caratteri(nome)
                query = (f"DROP DATABASE {nome_table} ")
                cur.execute(query)
                conn.commit()
                print(f"database {nome_table} eliminato")

            #creazione server socket
            if __name__ == '__main__':
                db_get()
                break
        
                
                
        if response == "7":
            import mysql.connector
            import socket as sock
            #import mariadb

            # mysql.connector.connect --> mariadb.connect
            def db_get():
                conn = mysql.connector.connect(
                    host="localhost", #127.0.0.1
                    user="root",
                    password="",
                    port=3306
                    )

                cur = conn.cursor()
                nome_db=input("inserisci il nome del database da creare: ")
                # si chiama una funzione di libreria passando i parametri di ricerca dell'utente. esempio controlla_caratteri(nome)
                query = (f"CREATE DATABASE {nome_db} ")
                cur.execute(query)
                conn.commit()
                print(f"database {nome_db} creato")

            #creazione server socket
            if __name__ == '__main__':
                db_get()
                break


        else:
            client_socket.sendall("Scelta non valida, riprova.".encode())

    client_socket.close()
    print("Connessione chiusa con", client_address)

# Funzione per il server multithread
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 10000)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print("Server in attesa di connessioni...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()

README:
PASSAGGIO 1:
IMPORTARE IL DATABASE SU XAMPP;
PASSAGGIO 2: 
CONNETTERE CLIENT E SERVER

password: camassa1234

NOTA BENE ---> QUESTO PROGETTO NON E' STATO OTTIMIZZATO AL MASSIMO PER TUTTI I PUNTI... INFATTI PER I PUNTI 2 e 5 
BISOGNERA' MODIFICARE NEL CODICE LA VARIABILE txt e insert CON I VALORI DESIDERATI AL SUO INTERNO

es punto 2:
txt="""`id` INT NOT NULL AUTO_INCREMENT,
            `nome` VARCHAR(45) NULL,
            `cognome` VARCHAR(45) NULL,                                
            `eta` INT NOT NULL,
            `pos_lavorativa` VARCHAR(45) NULL, 
            `data_ass` DATE NOT NULL,
            `residenza` VARCHAR(45) NULL, 
            PRIMARY KEY (`id`))"""
es punto 5:
 insert = """INSERT INTO dipendenti_andrea_camassa (
            nome,
            cognome,
            eta,
            pos_lavorativa,
            data_ass,
            residenza) 
            VALUES (%s, %s, %s, %s, %s, %s)"""

DA NOTARE CHE NEL PUNTO 5 BISOGNERA' METTERE UN NUMERO DI %s UGUALE AL NUMERO DEGLI ATTRIBUTI DELLA TABELLA DESIDERATA

ALTRO PROBLEMA DELLA CONNESSIONE E' CHE PURTROPPO SI CHIUDE DOPO OGNI SCELTA (MI SCUSO PER NON ESSERE RIUSCITO A RENDERE
LA CONNESSIONE MIGLIORE).

PASSAGGIO 3:

DIVERTITI UTILIZZANDO QUESTO ESERCIZIO ANCORA MOLTO ACERBO

GRAZIE DELL'ATTENAZIONE --> ANDREA CAMASSA
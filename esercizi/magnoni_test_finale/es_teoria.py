#DOMANDA 1
# abbiamo due distinti tipi di ereditarietà:
# eredità lineare in cui la classe figlia eredità direttamente i metodi del padre e
# viene instanziata direttamente nel "main":

from abc import abstractmethod
import json


class Fabbrica:
    def __init__(self) -> None:
        pass

    @abstractmethod    
    def produci(self):
        pass

class Fabbrica_scarpe(Fabbrica):
    def __init__(self) -> None:
        super().__init__()

    def produci(self):
        print("produco delle scarpe")


# nell'ereditarietà parallela invece abbiamo che la classe figlia viene instanziata
# all'interno della classe madre e può essere fatto un numero "illimitato di volte"

## definizione classe Fabbrica 
class Fabbrica:
    def __init__(self) -> None: 
        pass # il costruttore non fa nulla
    
    def produci(self):
        pass #funzione che non fa nulla, ma che poi viene sovrascritta nelle classi figlie


    def aggiungi_prodotti(self):
        while "yes" == input("aggiungere fabbrica? yes-no: "):
            obj = None
            product = input("cosa produci? chiodi o scarpe?")
            if product == "chiodi":
                obj = Chiodi()
                obj.produci()
            elif product == "scarpe":
                obj = Scarpe()
                obj.produci()
            else: 
                print("non possiamo produrre questo prodotto")



class Chiodi(Fabbrica):
    def __init__(self) -> None:
        super().__init__() # l'init di Chiodi richiama l'init di super dove super 
                           # è una referenza alla classe padre (Fabbrica) ed è completamente
                           # equivalente a Fabbrica.__init__()
    
    def produci(self): #sovrascrittura del metodo della classe padre
        print("ho prodotto dei chiodi")
    
class Scarpe(Fabbrica):
    def __init__(self) -> None:
        super().__init__()

    def produci(self):
        print("ho prodotto delle scarpe")


fabbrica = Fabbrica()
fabbrica.aggiungi_prodotti()

# DOMANDA 2:
# polimorfismo




#ereditarietà & incapsulamento

class Persona:
    def __init__(self,nome,cognome,codice_fiscale) -> None:
        self.nome = nome
        self.cognome = cognome
        self.__codiceFiscale__ = codice_fiscale
        #il codice fiscale è un elemento "privato della persona" per cui non accessibile direttamente
        # e quindi non modificabile 
        # possiamo inserire un metodo per renderlo modificabile

    def set_codice_fiscale(self, codice_fiscale):
        #potremmo mettere di richiedere una password
        # e solo se la password è giusta si può cambiare il codice
        # if password == self.password:
        self.__codiceFiscale__ = codice_fiscale

class Studente(Persona):
    def __init__(self, nome, cognome, codice_fiscale, scuola) -> None:
        super().__init__(nome, cognome, codice_fiscale)
        
        self.scuola = scuola

        #la classe studente eredita tutti i metodi e le proprietà della classe padre,
        # ma non ha accesso ai suo elementi privati

# DOMANDA 3:
# il try except serve per gestire gli errori all'interno di python e poter meglio studiare
# la natura
x = None
try:
  print(x) #try exectutin this instructions
except NameError: #if the error that you get is a NameError then:
  print("Variable x is not defined")
except: #if the error doesn't match to any of the errors above 
  print("Something else went wrong")

# DOMANDA 4:
# le lambda expression permettono di incapsulare una funzione in una variabile che poi possiamo usare a piacimento
op = lambda a : a**2
op2 = lambda a : a*2

def esegui_op(op, n):
    return op(n)

esegui_op(op,3)
# oltre a garantire una certa leggibilità del codice le lambda expressions permettono una certa sicurezza nel codice
# dato che l'operazione svolta all'interno di queste è totalmente incapsulata nelle stesse e quindi non leggibile 
# dall'esterno


# DOMANDA 5
# possiamo convertire i tipi attraverso un casting per cui per esempio possiamo convertire
# un numero in una stringa "castando str"

stringa = str(5)
# e possiamo poi riconvertirlo in numero castando a sua volta
numero = int(stringa)

# esiste anche un tipo di cast per le classi in cui si converte una classe padre
# in una classe figlia 
#self.classe_padre = classe_figlia

# infine possiamo convertire le strutture dati come liste e dizionarie in formati 
# come il json e il pickle per rendere appunto i dati più facili da trasmettere
# (se inviamo ad un codice javascript usiamo il json se python il pickle)

# DOMANDA 6
# le condizioni (if/elif/else) servono per creare dei branching all'interno del codice
# in base a determinate situazioni nel codice
# i loop (while e for) hanno due funzioni divere: il primo itera più volte una porzione
# di codide finchè una certa condizione non viene soddisfatta, il secondo itera su tutti
# gli elementi di una lista
# le classi sono delle strutture dati con in più la possibilità di possedere dei metodi 
# ovvero delle funzioni in gradi di manipolare i dati contenuti nella classe


# esempi: vedi esercizi pratici





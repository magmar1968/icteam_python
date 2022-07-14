## cos'è l'ereditarietà e scrivi un esempio

# l'ereditarietà è una proprietà del linguaggio ad oggetti che permmette di creare
# delle strutture gerarchi tra gli oggetti permettendo tra le altre cose di ereditare
# appunto le proprietà della classe del livello sovrastante

class Person:
    def __init__(self,yage,yname,ysurname):
        self.age = yage
        self.name = yname
        self.surname = ysurname


class Student(Person):
    def __init__(self, yage, yname, ysurname, yschool):
        super().__init__(yage, yname, ysurname)
        self.school = yschool


## cos'è il polimorfismo e scrivi un codice di esempio

# il polimorfismo è il principio per cui possiamo sfruttare le proprietà di un oggetto
# indipendentemente dal tipo specifico.
# legato all'ereditarietà per esempio permette di effetturare l'override di una funzione
# definita in una qualche classe madre

class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def make_sound():
        pass


class Cat(Animal):
    def __init__(self, age, name):
        super().__init__(age, name)
    
    def make_sound():
        print("meo")

class Dog(Animal):
    def __init__(self, age, name):
        super().__init__(age, name)
    
    def make_sound():
        print("wof")


## cos'è l'incapsulamento

# l'incapsulamento è ciò che permette all'interno di python di creare del codice accessbile
# solamente in lettura o proprio inaccessibile dall'esterno della classe stessa

## definisci cos'è una classe 

# una classe è un'astrazione di un concetto in codice andando quindi a definire il
# concetto attraverso le sue proprietà. Per esempio una persona viene rappresentata
# nel codice attraverso le sue caratteristiche (età, nome, lavoro, ...) e cosa questi
# possa fare all'interno del codice (cambiare nome, cambiare lavoro ecc.)

## definisci cosa sia una condizione e da cosa sia composta

#una condizione è un "branch nel codice" ovvero una sezione che in base allo stato
# di verità di una certa proprietà esegue una certa parte del codice rispetto ad un'altra

doggo = Dog(5,"fuffy")

if(doggo.name == "fuffy"):
    print( "wow.... original")
else:
    print(f"hi {doggo.name}")


## descrivi cos'è un ciclo e scrivine uno funzionante

# un ciclo è una porzione di codice che viene ripetuta fino a quando una certa condizione
# smette di essere rispettata
risposta = ""
while(risposta != "linux"):
    risposta = input("qual è il miglior OS?")



## scrivi un codice in cui applichi init e spiegalo


class Tree:
    def __init__(self, specie, age) -> None:
        self.specie = specie
        self.age = age

#init viene chiamato appena l'oggeto viene istanziato ed agisce come una sorta di 
# costruttore per il nostro oggetto andando a definire le proprietà della classe.
# il self corrisponde ad una referenza alla classe stessa.
# la presenza dei trattini bassi indica che l'init è eseguibile unicamente all'interno
# della classe stessa

         



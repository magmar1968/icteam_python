import os

class Animal:
    def __init__(self,yfamily,yspecie,yage,ycode,yname= None):
        self.__family = yfamily
        self.__specie = yspecie
        self.__age    = yage
        self.__code   = ycode 
        self.__name   = yname

    def print_stats(self):
        print( "codice:  " + str(self.__code))
        print( "famiglia:" + str(self.__family))
        print( "specie:  " + str(self.__specie))
        print( "eta':    " + str(self.__age))
        print( "nome:    " + str(self.__name))

    

class Zoo:
    def __init__(self, name):
        self.name = name
        self.mammal_enclosure  = []
        self.reptile_enclosure = []
        self.fish_pond         = []
        self.bird_encluser     = []


    def add_animal(self,animal):
        if(animal.family == "mammiferi"):
            self.mammal_enclosure.append(animal)
        elif(animal.family == "rettili"):
            self.reptile_enclosure.append(animal)
        elif(animal.family == "pesci"):
            self.fish_pond.append(animal)
        elif(animal.family == "uccelli"):
            self.bird_encluser.append(animal)
        else:
            print("alien not accepted in our zoo")
    
    def print_enclosures(self):
        print("mammiferi:")
        for animal in self.mammal_enclosure:
            animal.print_stats()
        print("rettili: ")
        for animal in self.reptile_enclosure:
            animal.print_stats()
        print("pesci: ")
        for animal in self.fish_pond:
            animal.print_stats()
        print("uccelli: ")
        for animal in self.bird_encluser:
            animal.print_stats()

        
class User:
    def __init__(self):
        self.__user__ = None
        self.__password__ = None

    def set_user(self,yuser):
        self.__user__ = yuser

    def set_password(self, ypassword):
        self.__password__ = ypassword



###voglio un maiiiiinnnnn



print("    BENVENUTO AL NOSTRO PORTALE PER IL TUO ZOO VIRTUALE   ")
print("           premi un qualsiasi tasto per contunuare        ")
input()
os.system("clear")
print(" sembra che tu non abbia ancora un account prego inserire username e password")
username = input(" username: ")
password = input( " password: ")

utente = User()
utente.set_user(username)
utente.set_password(password)

print("grazie mille! Procedi alla creazione del tuo zoo digitale ")
print("           premi un qualsiasi tasto per contunuare        ")
input()
os.system("clear")

zoo = Zoo("best zoo ever")

inp = ""

while(inp != "quit"):
    family = input("famiglia: ")
    specie = input("specie:   ")
    code   = input("codice:   ")
    age    = input("eta':     ")
    name   = input("nome:     ")
    check_continue   = input("continuare? yes-no ")

    zoo.add_animal(Animal(family,specie,age,code,name))

    if check_continue == "yes" or check_continue == "y":
        continue
    else: break



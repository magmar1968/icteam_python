from calendar import c
from http import client
from secrets import choice
from matplotlib.style import available
from classes_def import * 
import random
import os
#riempiano il concessionario manualmente... non il massimo

car_list = []

colors = ["blue" , "yellow", "red", "black", "orange"]

##### inseriamo un po' di fiat
for i in range(0,50):
    brand = "FIAT"
    code  = "FI_" + str(i)
    color = colors[random.randint(0, len(colors)-1)]
    price = random.randint(8000,20000)
    luxury = False
    car_list.append(Car_on_sold(code,brand,color,luxury,price))


for i in range(0,20):
    brand = "Ferrari"
    code  = "FER_" + str(i)
    color = "red" #i mean what are talking about
    price = random.randint(100000,300000)  
    luxury = True
    car_list.append(Car_on_sold(code,brand,color,luxury,price))

for i in range(0,100):
    brand = "Wolkswagen"
    code  = "WOG_" + str(i)
    color = colors[random.randint(0, len(colors)-1)]
    price = random.randint(15000, 100000)
    if( price > 50000):
        luxury = True
    else: luxury = False
    car_list.append(Car_on_sold(code,brand,color,luxury,price))

### ok let's put everything into the concessionario

concessionario = Car_dealer(car_list,0)

#UI

print("          BENVENUTO NELLA NOSTRO CONCESSIONARIO DIGITALE        ")
print("                                                                ") # si potrebbe fare un \n ma così è più facile da visualizzare
print("              premi qualsiasi tasto per continuare              ")
appo = input()

os.system('clear')

print("gentile cliente la preghiamo di inserire i suoi dati personali  ")
print("così da poter personalizzare il sistema e falicitare l'acquisto.")
nome =    input("nome   :  ")
cognome = input("cognome:  ")
eta =     input("eta'   :  ")
budget =  input("budget :  ")
rich =    input("ricco(1 yes 0 no):") #giusto un tantinello ingenuo
client = Client(eta,nome,cognome,budget,rich)
print("              premi qualsiasi tasto per continuare              ")
input()

print("gentile cliente usi i seguenti comandi per navigare tra le auto")
print("e effettuare la sua scelta\n")

help =  "comandi disponibili:\n \
    help: scrive a schermo tutti i comandi disponibili\n \
    list: scrive a schermo le caratteristiche delle macchine a lei disponibili\n \
    buy:  questo comando le serve per compare un auto le verrà chiesto il codice di\n\
          quest'ultima\n\
    offerta: controlla che l'auto di interesse possa essere sconta e se lo sconto sia\n\
             accessibile basandosi sulle sue caratteristiche\n\
    quit: esci dal programma e chiudi la scheda\n\n\
            prema un tasto qualsiasi per continuare"
    
print(help)
input()
os.system("clear")
choice = ""
while("quit" != choice):
    choice = input(":")
    if choice == "help":
        print(help)
        input()
    elif choice == "list":
        concessionario.print_avaible_cars(client=client)
    elif choice == "buy":
        code = input("please insert car code: ")
        concessionario.buy_car(code=code,client=client)
    elif choice == "offerta":
        code = input("please insert car code: ")
        concessionario.check_if_descountable(code,client=client)
    elif choice == "quit":
        print("arrivederci e alla prossima")

    
    else:
        print("ERROR: unrecognized input")





























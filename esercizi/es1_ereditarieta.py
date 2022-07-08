class Person:
    lista_input = []


my_person = Person()
nome    = ""
cognome = ""
occup   = ""
age         = 0

nome        = input("inserisci il nome della persona:    ")
cognome     = input("inserisci il cognome della persona: ")
age         = input("inserisci l'età della persona:      ")
occup       = input("inserire professione:               ")

status = True

if type(nome) == str:
    my_person.lista_input.append(nome)
if type(cognome) == str:
    my_person.lista_input.append(cognome)
if type(occup) == str:
    my_person.lista_input.append(occup)
if type(age) == int(age):
    my_person.lista_input.append(age)







print(my_person.lista_input)

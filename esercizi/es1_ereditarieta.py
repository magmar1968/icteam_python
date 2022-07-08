class Person:
    lista_input = []


my_person = Person()
nome    = ""
cognome = ""
professione = ""
age     = 0

nome        = input("inserisci il nome della persona:    ")
cognome     = input("inserisci il cognome della persona: ")
age         = input("inserisci l'età della persona:      ")
professione = input("inserire professione:               ")

if type(nome) == str:
    my_person.lista_input.append(nome)
if type(cognome) == str:
    my_person.lista_input.append(cognome)
if type(professione) == str:
    my_person.lista_input.append(professione)

my_person.lista_input.append(age)


print(my_person.lista_input)

def check_yes_no(answ):
    while (answ != "yes" and answ != "no"):
        print("please insert yes or no")
        answ = input(": ")
    
    
    return answ


sum = lambda a,b: a + b
sub = lambda a,b: a - b
mol = lambda a,b: a * b
div = lambda a,b: a / b

def solve_op(op,num1,num2):
    return op(num1,num2)

finished = False
while finished == False:

    print("perfavore inserisci il tipo di operazione tra quelle disponibili:")
    print(" - sottrazione                                                   ")
    print(" - divisione                                                     ")
    print(" - somma                                                         ")
    print(" - moltiplicazione                                               ")

    operation = input(":  ")
    op = None
    if (operation == "sottrazione" ):
        op = sub
    elif (operation == "divisione"):
        op = div
    elif (operation == "somma"):
        op = sum
    elif (operation == "moltiplicazione"):
        op = mol
    else :
        print("ERROR: l'operazione selezionata non esite. Controlla di aver ")
        print("       scritto correttamente il nome.")
        continue

    print("inserire i due numeri: ")
    a = float(input(": "))
    b = float(input(": "))

    ris = solve_op(op=op,num1=a,num2=b)

    print(f"il risultato è: {ris} ")

    print("continuare? yes-no")
    answ = check_yes_no( input(": "))
    if answ == "no":
        finished = True
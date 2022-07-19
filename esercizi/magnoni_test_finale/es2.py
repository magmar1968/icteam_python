def check_yes_no(answ):
    while (answ != "yes" and answ != "no"):
        print("please insert yes or no")
        answ = input(": ")
    
    
    return answ



class AziendaMadre:
    def __init__(self,nomeazienda, percent_tasse,fatturato) -> None:
        self.nome = nomeazienda
        self._tasse = percent_tasse
        self.__fatturato = fatturato

    def paga_tasse(self):
        tasse = self.__fatturato*self._tasse
        return tasse

    def paga_tasse_sussidiarie(self):
        sussidiarie = []

        finished = False
        while finished == False:

            nome = input("inserisci il nome della sussidiaria: ")
            fatturato = float(input("inserisci il fatturato della sussidiaria: "))
            sussidiarie.append(Sussidiaria(nome,self._tasse,fatturato))

            if(len(sussidiarie) >= 2 ):
                answ = check_yes_no(input("would you like to continue? yes-no: "))

                if(answ == "no"):
                    finished = True

            tasse_da_pagare = 0.
        for sussidiaria in sussidiarie:
            tasse_da_pagare += sussidiaria.paga_tasse()

        print(f"dobbiamo al fisco {tasse_da_pagare}")



        
class Sussidiaria(AziendaMadre):
    def __init__(self, nomeazienda, percent_tasse, fatturato) -> None:
        super().__init__(nomeazienda, percent_tasse, fatturato)

    def paga_tasse(self):
        return super().paga_tasse()



azienda = AziendaMadre("nike", 0.20, 3000000)
azienda.paga_tasse_sussidiarie()
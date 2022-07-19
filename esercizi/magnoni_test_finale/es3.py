from abc import abstractclassmethod
import json
import pickle

def check_yes_no(answ):
    while (answ != "yes" and answ != "no"):
        print("please insert yes or no")
        answ = input(": ")
    
    
    return answ


class Converter:
    def __init__(self,num1,num2,num3) -> None:
        self._mylist = [num1,num2,num3]

    @abstractclassmethod
    def convert(self):
        pass



class Converter_json(Converter):
    def __init__(self, num1, num2, num3) -> None:
        super().__init__(num1, num2, num3)


    def convert(self):
        return json.dumps(self._mylist)

class Converter_pickle(Converter):
    def __init__(self, num1, num2, num3) -> None:
        super().__init__(num1, num2, num3)

    def converter(self):
        return pickle.dumps(self._mylist)


converted_list = None
finished = False
while finished == False:
    print(" inserisci gli elementi della lista")    
    el1 = input(" : ")
    el2 = input(" : ")
    el3 = input(" : ")

    print(" in which format would you like to convert the list? ")
    print(" - json                                              ")
    print(" - pickle                                            ")
    answ = input(" : ")
    while answ != "json" and answ != "pickle":
        answ = input("please write json or pickle")


    if answ == "json":
        print("ready for friday 13? ")
        converter = Converter_json(el1,el2,el3)
        converted_list = converter.convert()

    else: 
        print( "i'm a pickle morty!")
        converter = Converter_pickle(el1,el2,el3)
        converted_list = converter.convert()
    
    print(converted_list)

    answ = check_yes_no( input("would you like to reconvert the list? yes-no: "))

    if answ == "no":
        finished = True
    
    






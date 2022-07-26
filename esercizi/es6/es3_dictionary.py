from ast import Pass


class MyDict():
    def __init__(self) -> None:
        self._myDict = {}
        self.__dictFiller = MyDict_filler
        self.__dictPrinter = MyDict_printer

    def fill(self,key,elements):
        self.__dictFiller.fill(key,elements)

    def print(self):
        self.__dictPrinter.print()
    

class MyDict_filler(MyDict):
    def __init__(self) -> None:
        pass

    def fill(self,key,elements):
        self._myDict[key].append(elements)

class MyDict_printer(MyDict):
    def __init__(self) -> None:
        Pass
    
    def print(self):
        print(self._myDict)
        
finished = False
myDict = MyDict()
while finished is not True:
    key = input("insert the key: ")
    elements = []
    another = True
    while another is not False:
        elements.append(input("insert the element: "))
        if input("Would you like to insert another element? (y-n): ") == "y":
            continue
        else:
            another = False
    
    myDict.fill(key,elements)
    if input("would you like to continue?(y-n): ") == "y":
        continue
    else:
        finished = True


myDict.print()






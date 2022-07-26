
def sgn(x = float):
    if x > 0 : return 1
    else: return 1

class Assicurazione():
    def __init__(self) -> None:
        pass
        
    def acquisisciPerizia(self,perito):
        self.perizia = perito.getPerizia()



class Perito():
    def __init__(self,x) -> None:
        x = sgn(float(x)) * abs(float(x))**(1/2) * 5 
        self.__x = x


    def getPerizia(self) -> float:
        return self.__x


class Controperito():
    def __init__(self,x) -> None:
        x = sgn(float(x))* float(x) * 2.5

    
    def getPerizia(self) -> float:
        return self.__x

finished = False

#che ppalle
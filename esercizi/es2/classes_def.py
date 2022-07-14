class Car():
    def __init__(self, _code=str, _brand = str, _color = str, _luxury=bool):
        self.code   = _code
        self.brand  = _brand
        self.color  = _color
        self.luxury = _luxury
        


class Car_on_sold(Car):
    def __init__(self,_code = str, _brand=str, _color = str, _luxury=bool, _price = float,
                 _discount = 0.10, _sold = False):
        super().__init__(_code,_brand,_color,_luxury)
        self.sold     = _sold
        self.price    = _price
        self.discount = _discount


class Car_dealer():
    def __init__(self, _total_car,_profit = 0):
        self.total_car   = _total_car
        self.profit      = _profit


        self.sold_cars   = []
        self.tosell_cars = []
        for car in self.total_car:
            if(car.sold == False):
                self.tosell_cars.append(car)
            else:
                self.sold_cars.append(car)
    
    def print_car_detail(self,car):
        
        print("code:   " + str(car.code)  )
        print("brand:  " + str(car.brand) )
        print("color:  " + str(car.color) )
        print("luxury: " + str(car.luxury))
        print("price:  " + str(car.price) )
        if( car.luxury == False):
            print("discounted price:" + str(car.price - car.price * car.discount))
        if(car.sold == True):            
            print("status: sold")
        else:
            print("status: available")

        print("\n")  

    def print_all(self):
        for car in self.total_car:
            self.print_car_detail(car) 
            
    def print_avaible_cars(self):
        for car in self.tosell_cars:
            self.print_car_detail(car.code)
         
    def print_avaible_cars(self, client):
        for car in self.total_car:

            if(car.price <= float(client.budget)):
                self.print_car_detail(car)

    def buy_car(self,code,client):
        for car in self.tosell_cars:
            if str(car.code) == str(code):
                if ( int(client.age) < 25 and client is not client.rich):
                    price = car.price - car.price* car.discount 
                else:
                   price =  car.price
                
                if(price >= float(client.budget)):
                    print("ERROR: il costo della macchina è superiore alle vostre disponibilità.")
                    print("       acquisto annulato")
                    return -1

                else:
                    car.sold = True
                    self.sold_cars.append(car)
                    self.tosell_cars.remove(car) #non funzica
                    self.profit += price
                    print( "acquisto eseguito con successo!")
                 
                return 0

        print("ERROR: codice non trovato acquisto annullato")
        return -1

    def check_if_descountable(self,code,client):
        for car in self.tosell_cars:
            if str(car.code) == str(code):
                if ( int(client.age) < 25 and client is not client.rich):
                    price = car.price - car.price* car.discount
                    print("l'auto e la sua persona rispettano i requisiti per lo sconto")
                    print("il costo complessivo è quindi: " + str(price))
                else:
                    print("siamo spiacenti, ma i requisiti per accedere allo sconto non")
                    print("sono rispettati")

##################################################################
####                CLIENT CLASS DEFINITIONS                  ####


class Person():
    def __init__(self, _age = int, _name = str, _surname = str):
        self.age  = _age
        self.name = _name
        self.surname = _surname


class Client(Person):
    def __init__(self, _age = int, _name = str, _surname = str, _budget = float, _rich = bool):
        super().__init__(_age, _name, _surname)
        self.rich = _rich
        self.budget = _budget

from getpass import getpass

from sympy import false, true




class Server:  
    def __init__(self,ip,passwordadmin) -> None:
        self.ip = ip
        self.__passwordadmin = passwordadmin
        self.__users = []
        self.__user = None
    

    def login(self):
        ID = input(        " please inser your ID: ")
        password = getpass(" please insert your password: ")

        for user in self.__users:
            if user.ID == ID:
                if(user.check_password(password)):
                    print("password accepted. Welcome to your account.")
                    self.__user = user
                    return
        
        else: print("password or ID are wrong unable to continue")

    def logout(self):
        self.__user = None
        print("succesfully logout")

    def sudo_su(self):
        if self.__user == None:
            print("ERROR: impossible to become superuser if you fist don't log as a normal user")
            return False
        
        else: 
            if self.check_passwordadmin(getpass("please insert the admin password: ")):
                print("succesfully promoted at super user")
                return True
            else:
                print("ERROR: wrong password. Unable to continue as superUser")



    def check_passwordadmin(self,passwordadmin):
        if self.__passwordadmin == passwordadmin:
            return True
        else :
            return False


class User:
    def __init__(self,ID,name,surname,adress,password) -> None:
        self.__data = {"name":name, "surname":surname,"adress":adress,"password":password}
        self._ID = ID
        self.__superuser = False



    def print_stats(self):
        print(f"name:    {self._name}   ")
        print(f"surname: {self._surname}")
        print(f"adress:  {self._adress} ")
    
    def check_password(self,password):
        if self.__data["password"] == password:
            return True
        else:
            return False
    
    def change_stats(self,password):
        if self.check_password(password):
            print("password accepted")
            self.__change_name(input("insert new name: "))
            self.__change_surname(input("insert new surname: "))
            self.__change_adress(input("insert new adress: "))
        else:
            print("ERROR: password rejected. Unable to continue")

    def __change_name(self,name):
        self.__data["name"] = name
    def __change_surname(self,surname):
        self.__data["surname"] = surname
    def __change_adress(self,adress):
        self.__data["adress"] = adress    
    def __change_password(self,password):
        self.__data["password"] = password


    @property
    def ID(self):
        return self._ID

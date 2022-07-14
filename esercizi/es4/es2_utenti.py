class Server:
    __users = []
    
    def __init__(self) -> None:
        pass


    def add_user_ext(self, user):
        #if user in self.__users:
        if self.check_username(user.username):
            print("L'utente esiste già. Prego inserire un nuovo utente")
        else: 
            self.__users.append(user)
            print("user succesfully created")

    def add_user_int(self):
        username = input("enter the username: ")
        while(self.check_username(username=username)):
            username = input("Username already exist please insert a different one: ")

        password = input("insert password: ")
        name     = input("inser name:      ")
        surname  = input("insert surname:  ")

        self.add_user_ext(User(username,password,name,surname))


    def get_user(self,username):
        for user in self.__users:
            if(user.username == username):
                return user
        else:
            print("ERROR: username not found")

    def check_username(self, username):
        for user in self.__users:
            if (user.username == username):
                return True
        else:
            return False


class UserData:
    def __init__(self,username, password, name, surname) -> None:
        self.username = username
        self.__password__ = password
        self.__name__     = name
        self.__surname__  = surname



    def __print_data(self) -> None:
        print("username: " + self.__username )
        print("name:     " + self.__name__     )
        print("surname:  " + self.__surname__  )
    
    def __check_password(self,password) -> bool:
        return (self.__password__ == password)
    
    # setters 
    def __set_name(self, name) -> None:
        self.__name__ = name
    def __set_surname(self,surname) -> None:
        self.__surname__ = surname



class User(UserData):
    def __init__(self, username, password, name, surname) -> None:
        super().__init__(username, password, name, surname)

    
    def print_data(self):
        password = input("to print your data you must insert your password: ")
        if(self.check_password(password=password)):
            super().__print_data()
        else:
            print("ERROR: wrong password operation aborted")
        

    def change_data(self):
        password = input("to change your data you must insert your password: ")
        if( UserData.__check_password(password=password)):
            super().__set_name(input("insert the new name: "))
            super().__set_surname(input("insert the new surname: "))
        else:
            print("ERROR: wrong password operation aborted")

server = Server()

# server.add_user_int()

user = User("magmar69","ciao", "lorenzo", "magnoni")
server.add_user_ext(user=user)

user.change_data()
user.get_user("magmar69")
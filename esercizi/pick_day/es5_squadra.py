class Player:
    def __init__(self,code,name,surname,role) -> None:
        self.code = code
        self.name = name
        self.surname = surname
        self.role = role
    
    def print(self):
        print("name:   " + str(self.name)    )
        print("surname:" + str(self.surname) )
        print("role:   " + str(self.role)    )



class Squadra:
    def __init__(self, team_name) -> None:
        self.team_name = team_name
        self.players = []
        self.rosa    = []
    

    def fill_tema(self):
        print("please fill the team with all the players")

    def add_player(self,player):
        self.players.append(player)

    def add_player_to_rosa(self,player):
        self.players.append(player)
        self.rosa.append(player)
    
    def move_player_to_rosa(self,code):
        pass


from prettytable import PrettyTable

class Personnage:
    def __init__(    self, 
                     name="user", 
                     force=0, 
                     sante= 0, 
                     defense= 0):
        self.name    = name 
        self.force   = force
        self.sante   = sante
        self.defense = defense 
        self.sac     = {
            'weapon' : [],
            'potion' : [],
            'objet'  : []
        }

    def affiche_etat(self):
        table = PrettyTable()
        table.field_names = ["name", 
                             "sante", 
                             "force",
                             "defense"]
        table.add_row(      [f"{self.name}",
                             f"{self.sante}",
                             f"{self.force}",
                             f"{self.defense}"]
                      )
        print("\n",table,"\n")
        
        
    def attaquer(self,player):
        print(f"\n {self.name}!! Attaque !! {player.name}\n")
        if player.defense > 0 :
            player.defense -= self.force 
            if player.defense <= 0 :
                player.sante -= abs(player.defense)
                player.defense = 0 
        else :
            player.sante -= self.force 
    
    def prendre_arme(self,weapon):
        if weapon.type == "DEF":
            self.defense += weapon.power
            return 
        self.force += weapon.power
         
    def subit_attaque(self,player):
        impact = self.se_defend(player)
        self.sante -= impact 
        if self.sante <= 0:
            self.meurt()
    
    def mourir(self):
        self.sante = 0 
        print(f" Player {self.name} est mort !!!!!! ")